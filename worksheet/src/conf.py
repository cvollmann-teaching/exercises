#: default settings for non-existing but necessary entries
# BETTER DO NOT CHANGE THIS DICT
default_sheet_dict = {
    "exercises_database": "./db",  # like "Open" button
    "build_directory": "./build",  # like "Save as" button
    "template": {
        "filename": "./templates/sheet.tex",
        "symlink": False,
        "newcommands": {
            "LectureName": "",
            "Lecturer": "",
            "Tutor": "",
            "Semester": "",
            "SheetTitle": "",
            "Date": "",
            "Place": ""
        }
    },
    "versions": {  # the keys dictated from the bools def. in the tex-templ
        "inclass":
            {"solution": "false", "inclass": "true"},
        "plain":
            {"solution": "false", "inclass": "false"},
        "solution":
            {"solution": "true", "inclass": "false"}
    },
    "table": False,
    "default_exercise_setting":
        {
            "nbconvert": False,
            "Points": "",
            "Header": "true",
            "tags": "",
            "tasknum": "",
            "table": False
        },
    "tasks": {}
}
