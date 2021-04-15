import json
import pathlib


def dict_to_config(dictionary, file="config.json", verbose=False, **kwargs):
    json_txt = json.dumps(dictionary, **kwargs)
    if verbose:
        print(json_txt)
    pathlib.Path(file).write_text(json_txt)


dict_to_config({'a': 1, "b": 2}, verbose=True, indent=2)


"""
using **kwargs we can call the function with many arguments without adding them as parameters
"""