import json
import os
from copy import deepcopy
import glob
from pathlib import Path

# the directory path to work with
collection = "./db/elomath"  # os.fsencode(directory_in_str)


def script_to_tex_inputlisting(exercise_directory: str) -> None:
    for progExerciseFilenameAbsolute in glob.glob(exercise_directory + "/*_solution.py"):
        with open(progExerciseFilenameAbsolute[0:-3] + ".tex", "w") as progSolutionTex:
            progSolutionTex.write("\lstinputlisting[numbers=none]{"
                                  + os.path.basename(progExerciseFilenameAbsolute)
                                  + "}")
    return


def ipynb_to_py(exercise_directory: str) -> None:
    for ipynb_task_filename in glob.glob(exercise_directory + "/*_solution.ipynb")[0:3]:
        task_name = os.path.basename(ipynb_task_filename)[0:-6]
        os.system("cd " + exercise_directory
                  + " && jupyter nbconvert --no-prompt --to script " + task_name + ".ipynb 2> /dev/null"
                  + " && sed -i '/^$/d' " + task_name + ".py")
    return

# PUT FILES INTO DIRECTORIES
def move_files_to_dir(collection):
    for file in os.listdir(collection):
        tex_filename = os.fsdecode(file)
        if tex_filename.endswith(".tex") and not tex_filename.endswith(("_solution.tex")):
            tex_filename = os.path.splitext(tex_filename)[0]
            print("\n--------\n" + collection + "/" + tex_filename + "\n--------")
            os.system("mkdir -p " + collection + "/" + tex_filename + "/build")
            for exercise_file in glob.glob(collection + "/" + tex_filename + "*"):
                print("mv " + exercise_file + " " + collection + "/" + tex_filename + "/")
                os.system("mv " + exercise_file + " " + collection + "/" + tex_filename + "/")


# RENAME WITHIN DIR
def correctly_name_within_dir(collection):
    # TOO DANGEROUS
    pass
    # for dir_name in os.listdir(collection):
    #     dir_name = collection + "/" + os.fsdecode(dir_name) + "/"
    #     if os.path.isdir(dir_name) and "build" not in dir_name:
    #         print("\n--------\n" + dir_name + "\n--------")
    #         os.system("mv " + dir_name + "*solution.tex " + dir_name + "solution.tex")
    #         os.system("mv " + dir_name + "*.json " + dir_name + "meta.json")
    #         os.system("mv " + dir_name + "*.pdf " + dir_name + "build/print.pdf")
    #         os.system("mv " + dir_name + "*_exam.py " + dir_name + "task.py")
    #         os.system("mv " + dir_name + "*solution.py " + dir_name + "solution.py")
    #
    #         tex = glob.glob(dir_name + "*.tex")
    #         if tex.count(dir_name + "solution.tex"):
    #             tex.remove(dir_name + "solution.tex")
    #             os.system("mv " + tex[0] + " " + dir_name + "task.tex")
    #
    #         # create meta json
    #         json = glob.glob(dir_name + "*.json")
    #         if not json:
    #             modify_meta_json(dir_name + "meta.json", ident=os.path.basename(dir_name))
    #         else:
    #             os.system("mv " + json[0] + " " + dir_name + "meta.json")


def modify_meta_json(document, create_template=True, **kwargs):
    """

    Parameters
    ----------
    document : str
         path to the document (= dir with specification of an exercise)
    create_template
    kwargs

    Returns
    -------

    """
    json_template = {
        "id": "",
        "title": "",
        "subtitle": "",
        "tags": "",
        "related_ids": "",
        "solutionLength": ""
    }
    document = os.path.abspath(document)
    document = os.path.normpath(document)
    meta_file = document + "/meta.json"
    meta_file = os.path.normpath(meta_file)
    if os.path.isfile(meta_file) and os.stat(meta_file).st_size > 0:
        # if meta exists and is not empty we read and then insert the (key,value) pairs
        with open(meta_file, "r") as json_file:
            dict_file = json.load(json_file)
        with open(meta_file, "w") as json_file:
            for key, value in kwargs.items():
                dict_file[key] = value
            json.dump(dict_file, json_file, indent=4, sort_keys=False)
    elif create_template:
        # otherwise we create a new from template and add the pairs
        with open(meta_file, "w") as json_file:
            dict_file = deepcopy(json_template)
            for key, value in kwargs.items():
                dict_file[key] = value
            json.dump(dict_file, json_file, indent=4, sort_keys=False)
    return


def walk_and_apply(collection, apply=None, *args, **kwargs):
    """
    iterate through collection directory and deliver the absolute path
    each document (=exercise directory) to the apply function

    Parameters
    ----------
    collection : str
    apply : callable

    Returns
    -------

    """
    documents = glob.glob(collection + "/**/*/", recursive=True)
    for document in documents:
        if "/build" not in document:
            document = os.path.abspath(document)
            apply(document, *args, **kwargs)
    return


# GET DICT OF ALL EXERCISES
def get_all_tasks(directory, verbose=0):
    task_dict_default = {}
    tasks_dict = {}
    for dirpath, dirnames, filenames in os.walk(directory):
        path_name = os.fsdecode(dirpath) + "/"
        path_name = os.path.relpath(path_name, directory)
        if "build" not in path_name and path_name != ".":
            if verbose:
                print(path_name)
            tasks_dict[path_name] = task_dict_default
    return tasks_dict


# GET DICT OF ALL EXERCISES
def get_all_task_names(directory, verbose=0):
    task_names = []
    for dirpath, dirnames, filenames in os.walk(directory):
        path_name = os.fsdecode(dirpath) + "/"
        path_name = os.path.relpath(path_name, directory)
        if "build" not in path_name and path_name != ".":
            if verbose:
                print(path_name)
            task_names += [path_name]
    return task_names


def get_all_task_names_glob(directory, verbose=0):
    task_names = []
    documents = glob.glob(collection + "/**/*/", recursive=True)
    for document in documents:
        if "build" not in document:
            task_names += [os.path.relpath(document, directory)]
    return task_names


def get_all_task_names_pathlib(directory, verbose=0):
    task_names = []
    for document in Path(directory).rglob("**/"):
        if "build" not in document.name:
            task_names += [os.path.relpath(document, directory)]
    task_names.remove(".")
    return task_names


def convert_list_to_dict(all_task_names):
    return {task: {} for task in all_task_names}


def merge_meta(collection, task_names, verbose=0):
    merged_meta = dict()
    for task in task_names:
        meta_filename = collection + "/" + task + "/meta.json"
        with open(meta_filename, 'r') as infile:
            merged_meta[task] = json.load(infile)

    return merged_meta


def tex_to_json():
    # # read task from latex and insert string as value for key "task"
    #            try:
    #                with open(tex_filename+".tex", "r") as f:
    #                    print("Read task from ", tex_filename+".tex")
    #                    dict_file["task"] = f.read()
    #                    print(dict_file)
    #            except OSError:
    #                print("ERROR ", tex_filename+".tex NOT THERE")
    #            # if latex solution exists: read solution from latex
    #            # and insert string as value for key "solution"
    #            try:
    #                with open(tex_filename+"_solution.tex", "r") as f:
    #                    dict_file["solution"] = f.read()
    #            except OSError:
    #                print("!!!! " + tex_filename +"_solution.tex not found")
    #                continue
    #            # dump this into the json file
    #            json_file = open(tex_filename + ".json", "w")
    #            json.dump(dict_file, json_file, indent = 4, sort_keys = False)
    #            json_file.close()
    return


if __name__ == "__main__":

    all_list = get_all_task_names(collection)
    all_dict = convert_list_to_dict(all_list)
    # walk_and_apply(collection, modify_meta_json, collection, id="")

    for document in glob.glob("/home/vollmann/Seafile/2_TEACHING/old_exercises/svd/*.tex"):
        if "_solution" not in document:
            document = os.path.basename(document)[0:-4]
            document = collection + "/" + document
            if os.path.isdir(document):
                print(document)
                tag = "Linear Algebra, Singular Values"
                modify_meta_json(document, create_template=False, tags=tag)
                if "prog" in document:
                    print("+++++++++++++prog+++++++++\n", document)
                    modify_meta_json(document, create_template=False, tags=tag+", Python")

