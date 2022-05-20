import os
import re
import math
import shutil

files = os.listdir(".")

re_f = re.compile(r"(\d+)\.?[\s_](.+).(ipynb)")


def init_folder(id):
    N = 200
    sid = math.floor((id-1)/N)
    eid = math.ceil((id-1)/N)
    if eid == sid:
        eid += 1
    return f"{sid*N+1:04}-{eid*N:04}"


def get_new_filename(f, create_dirs=False):
    id, title, ext = re_f.findall(f)[0]
    d = init_folder(int(id))

    if not os.path.exists(d) and create_dirs:
        os.makedirs(d)

    id_ = f"{int(id):04}"
    title_ = title.lower().replace(" ", "_")

    f_ = os.path.join(d, f"{id_}_{title_}.{ext}")
    count = 0
    while os.path.exists(f_):
        count += 1
        f_ = os.path.join(d, f"{id_}_{title_}_{count}.{ext}")
    return f_


for f in files:
    if re_f.search(f):
        f_ = get_new_filename(f, create_dirs=True)
        if not os.path.exists(f_):
            print(f"{f:70} > {f_}")
            os.rename(f, f_)
        else:
            print(f"{f:70} > {f_}: Exception: path exists")

header = [
        "# Leet Code Solutions",
        "I started doing leet code properly on *03.10.2021.*",
        "Here I will document all the problems that I have solved using *jupyter-notebooks*."
    ]

body = []

import re
count = 0
for r, dirs, files in os.walk("./"):
    if not r.startswith("./.") and r != "./":
        line = f"## {r} \n"
        body.append(line)
        line = f"*{len(files)} problems* \n"
        body.append(line)
        count += len(files)
        for f in files:
            v = re.split(r"_|\.", f)
            v_ = " ".join(v[1:-1])
            line = f"* {v[0]} [{v_}]({f}) \n"
            body.append(line)


with open("Readme.md", "w+") as fh:
    for l in header:
        fh.write(l + "\n")
    line = f"* A total of **{count} problems** \n"
    fh.write(line + "")
    for l in body:
        fh.write(l + "")
