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
        print(f"{f:70} > {f_}")
        os.rename(f, f_)