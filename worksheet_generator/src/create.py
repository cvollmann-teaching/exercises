#!/usr/bin/env python3
"""
1. summary
    one function for one component (table, tasks,...) of the sheet
2. extended summary
3. routine listings
4. see also
5. notes
6. references
7. examples
"""

from . import file_utils

def conf(sheet_dict: dict) -> dict:
    """
    adds missing but required items to the sheet dictionary

    Parameters
    ----------
    sheet_dict : dict
                 as given in the parsed json config

    Returns
    -------
    a deep copy of it
    """
    from .conf import default_sheet_dict
    from copy import deepcopy

    valid_sheet_dict = deepcopy(sheet_dict)

    for key, val in default_sheet_dict.items():
        valid_sheet_dict.setdefault(key, val)
        if isinstance(val, dict):
            for key_2, val_2 in val.items():
                valid_sheet_dict[key].setdefault(key_2, val_2)
                if isinstance(val_2, dict):
                    for key_3, val_3 in val_2.items():
                        valid_sheet_dict[key][key_2].setdefault(key_3, val_3)

    return valid_sheet_dict


def newcommands(newcommands_dict: dict, filename: str) -> None:
    """

    Parameters
    ----------
    newcommands_dict
    filename

    Returns
    -------

    """
    if newcommands_dict:
        with open(filename, "w") as newcommands_tex:
            for command_name, command_definition in newcommands_dict.items():
                newcommands_tex.write("\\newcommand{{"
                                      "\\{command_name}"
                                      "}}{{"
                                      "{command_definition}"
                                      "}}\n".format(
                    command_name=command_name, command_definition=command_definition
                ))
    return


def pdf(tex_filename_to_compile: str, working_directory: str, quiet = True) -> None:
    """

    Parameters
    ----------
    tex_filename_to_compile
    working_directory
    """
    import os

    log = "> /dev/null 2>&1 " if quiet else ""

    command = "cd " + working_directory \
              + " && " \
              + "pdflatex -interaction=nonstopmode -output-directory=build/ "+log \
              + tex_filename_to_compile
    os.system(command)
    return


def table(exercises_dict: dict, dest_abs_filename: str, table_switch: bool) -> None:
    """

    Parameters
    ----------
    exercises_dict : dict
    dest_abs_filename : str
    table_switch : bool/ empty or nonempty data type
    """
    from tabulate import tabulate
    with open(dest_abs_filename, "w") as tableTex:
        if bool(table_switch) and bool(exercises_dict):
            exercises_number = len(exercises_dict)
            headers = ["Task:"] + list(range(1, exercises_number + 1)) + ["Total", "Grade"]
            row2 = ["Points:"] + [""] * (exercises_number + 2)

            exercise_points = []
            for single_exercise_dict in exercises_dict.values():
                # if Points not given, it is set to default value (i.e., 0)
                p = single_exercise_dict.get("Points", 0)
                if type(p) == str and p.isdigit():
                    exercise_points += [int(p)]
                elif type(p) == int:
                    exercise_points += [p]
            row3 = ["Total:"] + exercise_points + [sum(exercise_points), "--"]
            table = [row2, row3]
            tableTex.write("{"
                           + tabulate(table, headers=headers, tablefmt="latex")
                           + "}")
    return

def exercises(exercise_database: str, exercises_dict: dict,
              sheet_output_directory : str, version: tuple, default_fallback_dict) -> None:
    """

    Parameters
    ----------
    exercise_database
    exercises_dict
    dest_directory
    versions

    Returns
    -------

    """
    import glob
    import os

    version_key, version_bools = version

    with open(sheet_output_directory + "/exercises-" + version_key + ".tex", "w") as exercisesTex:

        # if exercises_dict is empty (not indicated) we leave the exercises.tex empty
        if bool(exercises_dict):
            for exercise_name, exercise_dict in exercises_dict.items():
                exercise_directory = exercise_database + "/" + exercise_name
                if not os.path.isdir(exercise_directory) or os.listdir(exercise_directory) == []:
                    # exercise ignored if dedicated directory is not found
                    print(
                        "WARNING (from <{who}>):\n The exercise directory <{exercise_name}> "
                        "does not exist at all or is empty! "
                        "We ignore this exercise.\n".format(who=exercises.__name__,
                                                        exercise_name=exercise_name)
                    )
                    # don't write a latex command \exercises and continue with next exercise
                    continue

                if not os.path.exists(exercise_directory + "/task.tex"):
                    print(
                        "WARNING (from <{who}>)::\n The task.tex file not found in "
                        "<{exercise_name}>. We ignore this exercise.\n".format(who=exercises.__name__,
                                                                       exercise_name=exercise_name)
                    )
                    continue

                # SOLUTION.tex
                version_bool_solution = exercise_dict.get("solution", version_bools.get("solution"))
                if version_bool_solution:
                    solution_files = glob.glob(exercise_directory + "/solution.*")
                    if solution_files:
                        solution_suffix = glob.glob(exercise_directory + "/solution.*")[0].split(".")[-1]
                        if solution_suffix == "ipynb":
                            # if the solution is a notebook then we might want to
                            # nbconvert this notebook to a script and move script
                            # to exercise_directory/build/
                            if exercise_dict.get("nbconvert", default_fallback_dict["default_exercise_setting"]["nbconvert"]):
                                os.system("cd " + exercise_directory
                                          + " && jupyter nbconvert --no-prompt --to script solution.ipynb 2> /dev/null"
                                          + " && sed -i '/^$/d' solution.py"
                                          + " && mv solution.py build/"
                                          )
                            # then we create a solution.tex in /build
                            # which inputs script.py as listing
                            solution_directory = exercise_directory + "/build"
                            with open(solution_directory + "/solution.tex", "w") as progSolutionTex:
                                # note that the root file is the .ipynb so that the .py file lies in /build
                                progSolutionTex.write("\lstinputlisting[numbers=none]{solution.py}")

                        elif solution_suffix in "py":
                            # then we create a solution.tex in / which inputs script as listing
                            solution_directory = exercise_directory + "/build"
                            with open(solution_directory + "/solution.tex", "w") as progSolutionTex:
                                # note that the root file is the .py so that it DOES NOT
                                # lie in /build but in ../
                                progSolutionTex.write("\lstinputlisting[numbers=none]{../solution.py}")
                        else:
                            # then our original solution is a tex file found in the exercise dir as solution.tex
                            solution_directory = exercise_directory

                    else:
                        # if solution of this exercise is asked for, but we cannot find any solution then
                        # we do not try to input a solution in latex to prevent compile errors
                        version_bool_solution = "false"  # the latex false boolean
                        solution_directory = ""  # can be any str

                # META.json (for tags)
                # get tags from parsed json config
                #  - first fallback: sidecar file meta.json
                #  - second fallback: default dict
                meta_json = exercise_directory+"/meta.json"
                metajson_exists = os.path.exists(meta_json)
                if metajson_exists:
                    meta = file_utils.parse_json(meta_json)
                else:
                    "INFO: <{metajson}> does not exist".format(metajson=meta_json)
                    meta = {}
                fallback_tags = meta.get("tags", default_fallback_dict["default_exercise_setting"]["tags"])
                tags = exercise_dict.get("tags", fallback_tags)

                # WRITE LATEX exercise
                # serve \exercise command interface as defined in the template file
                exercise_directory = os.path.relpath(exercise_directory, sheet_output_directory)
                if solution_directory:
                     solution_directory = os.path.relpath(solution_directory, sheet_output_directory)
                exercise_latex_command = "\\exercises{" + exercise_directory + "/}{" \
                                     + solution_directory + "/}{" \
                                     + tags + "}{" \
                                     + str(exercise_dict.get("Points", default_fallback_dict["default_exercise_setting"]["Points"])) + "}{" \
                                     + exercise_dict.get("Header", default_fallback_dict["default_exercise_setting"]["Header"]) + "}{" \
                                     + version_bool_solution + "}{" \
                                     + exercise_dict.get("inclass", version_bools["inclass"]) + "}\n"
                # print(exerciseCommand)
                exercisesTex.write(exercise_latex_command)

    return

