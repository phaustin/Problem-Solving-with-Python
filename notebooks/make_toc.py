from pathlib import Path
import re
import pprint
import yaml
from collections import defaultdict
import json
from jupytext.cli import jupytext

text="""# header

```{tableofcontents}
```

"""

pp = pprint.PrettyPrinter(indent=4)

section_match = re.compile(".*\d\d\.(\d\d).*")

all_files = list(Path().glob("**/*ipynb"))
all_files = [item for item in all_files if item.as_posix().find("_build") < 0]

def numsort(the_path):
    the_dir = Path(the_path).parent
    chapter_number = the_dir.name.split('-')[0]
    the_match =section_match.match(the_path.name)
    if the_match:
        section_number=the_match.group(1)
    else:
        raise ValueError(f"could not match {the_path}")
    return int(chapter_number),int(section_number)

yaml_skeleton = Path("_toc.yml")
#toc_structure = yaml.safe_load(yaml_skeleton.read_text(encoding="utf8"))
all_files.sort(key=numsort)
all_files = [item.as_posix() for item in all_files]

all_tups = [item.split('/') for item in all_files]
pp.pprint(all_tups)
with open('structure.json','r') as struc:
    structure_list = json.load(struc)

structure_dict = dict()
# {'file': '07-Functions-and-Modules/index', 'sections': [{'file': '07-Fu
for item in structure_list:
    dict_key = item['file'].split('/')[0]
    structure_dict[dict_key]=item

key_list = list(structure_dict.keys())

def dir_sort(the_key):
    chap_num = the_key.split('-')[0]
    return int(chap_num)

def file_sort(filename):
    strname = filename['file']
    chapter_number = strname.split('-')[0]
    the_match =section_match.match(strname)
    if the_match:
        section_number=the_match.group(1)
    else:
        raise ValueError(f"could not match {filename}")
    return int(section_number)


key_list.sort(key = dir_sort)
    
dir_list = [Path(item).parent for item in all_files]
all_dirs = set(dir_list)


dirwrite=True
if dirwrite:
    for a_dir in all_dirs:
        new_file = a_dir / 'index.md'
        with open(new_file,'w') as outfile:
            outfile.write(text)

# new_list = list()
# for the_dir in key_list:
#     item = structure_dict[the_dir]
#     file_list=[]
#     sec_files = Path(the_dir).glob("**/*.ipynb")
#     for a_file in sec_files:
#         file_list.append({"file":a_file.as_posix()})
#     file_list.sort(key=file_sort)
#     item['sections'] = file_list
#     new_list.append(item)

# with open('data.yml', 'w', encoding = "utf8") as outfile:
#     yaml.dump(new_list, outfile, default_flow_style=False)
    
# for a_file in all_files:
#     print(a_file)
#     jupytext([a_file, "--to","md:myst"])
    
    
