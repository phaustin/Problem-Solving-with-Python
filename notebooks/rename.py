import re
from yaml import safe_load, dump

from pathlib import Path

# all_files = Path().glob("**/*")
# for item in all_files:
#     the_str = str(item)
#     if the_str.find("_build") > -1 or \
#        the_str.find(".ipynb") > -1:
#        continue
#     new_string1 = re.sub(r'^\d\d-','',item.name)
#     new_string2 = re.sub(r'^\d\d_','',new_string1)
#     new_string = re.sub(r'^\d\d-','',new_string2)
#     new_name = item.parent / new_string
#     item.rename(new_name)
#     if item.is_dir() and item.name != new_string:
#         print("found folder")
#         print(item.name,new_string)
#     elif item.is_file() and item.name != new_string:
#         print("found file")
#         print(item.name,new_string)
#     else:
#         print("nothing")
#         print(item.name,new_string)


import yaml


def clean_name(the_string):
    new_string1 = re.sub(r"/\d\d-", "/", the_string)
    new_string2 = re.sub(r"/\d\d_", "/", new_string1)
    new_string = re.sub(r"/\d\d-", "/", new_string2)
    new_string3 = re.sub(r"\d\d-", "", new_string)
    new_string4 = re.sub(r"\d\d_", "", new_string3)
    new_string5 = re.sub(r"\d\d-", "", new_string4)
    return new_string5


def dict_generator(indict, pre=None):
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        if "file" in indict:
            new_name = clean_name(indict["file"])
            indict["file"] = new_name
            print(f"bingo1 {indict['file']}")
        for key, value in indict.items():
            if isinstance(value, dict):
                if "file" in value:
                    print(f"bingo2 {value['file']}")
                for d in dict_generator(value, pre + [key]):
                    yield d
            elif isinstance(value, list) or isinstance(value, tuple):
                for v in value:
                    for d in dict_generator(v, pre + [key]):
                        yield d
            else:
                yield pre + [key, value]
    else:
        yield pre + [indict]


with open("_toc.yml", "r") as stream:
    try:
        the_list = yaml.safe_load(stream)
        for item in the_list:
            print(f"\n\n++seperate++\n\n")
            out = dict_generator(item)
            for item in out:
                print(item)
    except yaml.YAMLError as exc:
        print(exc)

with open("new_toc.yml", "w") as stream:
    yaml.dump(the_list, stream)
