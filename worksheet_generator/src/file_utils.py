import os
import json
import sys



def parse_json(json_filename, exit_if_empty=False) -> dict:
    """
    read first command line argument and consider as filename

    Returns
    -------
    config_dict : dict
        parsed json config file as dict data type
    """

    if not os.path.isfile(json_filename):
        print("ERROR: file \"" + json_filename + "\" does not exist")
        if exit_if_empty:
            sys.exit()

    with open(json_filename, "r") as f:
        json_as_dict = json.load(f)
    return json_as_dict


def relative_symlink(source, link):
    # for relpath to work we have to remove the filename from the link path
    relative_source = os.path.relpath(source, os.path.dirname(link))
    os.symlink(relative_source, link)
    return None

def copy_or_symlink(source_filename: str, dest_filename: str, create_empty_file=False,
                    symlink=False) -> None:
    """

    Parameters
    ----------
    source_filename
    dest_filename
    create_empty_file

    Returns
    -------

    """
    import os, sys, shutil
    if os.path.isfile(source_filename):
        if symlink:
            try:
                os.remove(dest_filename)
            except OSError:
                pass
            relative_symlink(source_filename, dest_filename)
        else:
            shutil.copy(source_filename, dest_filename)
    elif not source_filename and create_empty_file:
        print(
            "WARNING (" + copy_or_symlink.__name__ + "): "
               "no source filename indicated  for " + dest_filename +
            " (empty string as value). We create empty file")
        open(dest_filename, "a").close()
    else:
        print("ERROR (" + copy_or_symlink.__name__ + "): "
                        "the following file does not exist: \n\t" + source_filename)
        sys.exit()
    return


