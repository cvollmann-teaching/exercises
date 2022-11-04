#!/usr/bin/env python3
import os
import sys
import shutil
import src.create as create
import src.file_utils as file_utils
import src.conf as settings


def main():
    """
    generate sheets from a given exercise pool and template
    a sheet is a composition of specified db and comes in three versions
       - plain: just the task
       - inlcass: the task with some empty squared space for the solution
       - solution: the task and the solution to it
    """

    collections_dict = file_utils.parse_json(sys.argv[1], exit_if_empty=True)

    for k, (sheet_title, sheet_dict) in enumerate(collections_dict.items()):
        print("\n Sheet", str(k) + ":", sheet_title, "\n")

        sheet_dict = create.conf(sheet_dict)

        exercises_database = sheet_dict["exercises_database"]
        # absolute path to make sure that the imports of db in the latex document
        # task.tex properly work independent of the location of the build Directory!
        exercises_database = os.path.abspath(exercises_database)
        if not os.path.isdir(exercises_database):
            print(
                "ERROR: exercise database directory <{exercises_database}> "
                "does not exist\n\t<".format(exercises_database=exercises_database)
            )
            sys.exit()

        sheet_build_directory = sheet_dict["build_directory"] + "/" + sheet_title
        os.makedirs(sheet_build_directory + "/build", exist_ok=True)
        os.makedirs(sheet_build_directory, exist_ok=True)

        file_utils.copy_or_symlink(sheet_dict["template"]["filename"],
                               sheet_build_directory + "/main.tex",
                               symlink=sheet_dict["template"]["symlink"]
                               )

        file_utils.copy_or_symlink(os.path.dirname(__file__)+"/latex_src/exercisecommand.sty",
                               sheet_build_directory + "/exercisecommand.sty"
                               )

        create.newcommands(sheet_dict["template"]["newcommands"],
                           sheet_build_directory + "/newcommands.tex"
                           )

        create.table(sheet_dict.get("exercises"),
                     sheet_build_directory + "/table.tex",
                     sheet_dict.get("table", settings.default_sheet_dict["table"])
                     )

        #  we create task-VERSION.tex and SHEETTITLE-VERSION.pdf for every VERSION
        versions = sheet_dict["versions"].items()
        for version_key, version_bools in versions:
            print("create version <{version}>".format(version=version_key))
            create.exercises(exercises_database,
                             sheet_dict.get("exercises"),
                             sheet_build_directory,
                             (version_key, version_bools),
                             settings.default_sheet_dict)
            # copy because template requires task.tex
            src = sheet_build_directory + "/exercises-" + version_key + ".tex"
            dst = sheet_build_directory + "/exercises.tex"
            shutil.copy(src, dst)
            create.pdf("main.tex", sheet_build_directory, quiet=True)
            # save main.pdf from being overwritten
            src = sheet_build_directory + "/build/main.pdf"
            dst = sheet_build_directory + "/" + sheet_title + "-" + version_key + ".pdf"
            shutil.copy(src, dst)
    return


if __name__ == "__main__":
    main()
