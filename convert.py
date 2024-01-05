"""
Convert the old map quiz files into more modern javascript/HTML
And add a few features.
"""

import re
import os
import shutil

def convert_mapping(map_html):
    """Convert the <area> tags in the <map> tags into dictionary format"""
    def insert_shape(m):
        """Define whether the shape is a polygon or rectangle based on the number of coordinates"""
        if m.group(0).count(",") > 3:
            return m.group(0) + '", shape: "poly'
        else:
            return m.group(0) + '", shape: "rect'

    map_str = re.sub('<area shape="(?:poly|rect)" coords=', "coords: ", map_html.strip())
    map_str = re.sub("""(coords: "[^"]+") href="javascript:mapclick\(('[^']+').+""", 
                    r"        \2: {id: %d, \1},", map_str)
    map_str = re.sub("""coords: "([^"]+)""", insert_shape, map_str)
    map_str = "\n".join([x % (i+1)  for i, x in enumerate(map_str.split("\n"))])

    return map_str

def convert_file(quiz_name, old_fp, new_fp, template_fn):
    """Convert a single html file"""
    # extract the mapping string from the old html file and convert it into dictionary format:
    with open(old_fp, mode="r", encoding="utf-8") as file:
        html = file.read()
        mapping = "\n".join(re.findall("<area.+", html))
        map_str = convert_mapping(mapping)

    # open the template and replace the placeholders with the data:
    with open(template_fn, mode="r", encoding="utf-8") as file:
        template = file.read()
    new = re.sub("QUIZ_NAME", quiz_name, template)
    new = re.sub("FEATURES", map_str, new)

    # store the converted file:
    with open(new_fp, mode="w", encoding="utf-8") as file:
        file.write(new)

def convert_folder(in_folder, out_folder, template_fn):
    """Convert all html files in a folder and copy the image files"""
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
    for fn in os.listdir(in_folder):
        if fn.endswith("html"):
            old_fp = os.path.join(in_folder, fn)
            new_fp = os.path.join(out_folder, fn)
            quiz_name = fn[:-5]
            convert_file(quiz_name, old_fp, new_fp, template_fn)
            old_img_fp = re.sub("\.html", ".jpg", old_fp)
            new_img_fp = re.sub("\.html", ".jpg", new_fp)
            shutil.copyfile(old_img_fp, new_img_fp)



if __name__ == "__main__":

    quiz_name = "tarim"

    old_fp = f"old_versions/{quiz_name}.html"
    new_fp = f"new_versions/{quiz_name}.html"
    template_fn = "template.html"
    convert_file(quiz_name, old_fp, new_fp, template_fn)

    convert_folder("old_versions", "new_versions_auto", template_fn)