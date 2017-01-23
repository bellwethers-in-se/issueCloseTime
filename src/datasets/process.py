import os
import sys
from glob import glob
from pdb import set_trace

root = os.path.join(os.getcwd().split('src')[0], 'src')
if root not in sys.path:
    sys.path.append(root)


def make_new_groups():
    dir = os.path.abspath(os.path.join(root, "datasets"))
    inner_dirs = ['1', '7', '14', '30', '90', '365']
    for datapath in os.listdir(dir):
        formatted_path = os.path.join(dir, datapath)
        if os.path.isdir(formatted_path):
            set_trace()


if __name__ == "__main__":
    make_new_groups()
