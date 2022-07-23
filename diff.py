#!/usr/bin/env python3
import os
import sys
import csv
import itertools

sys.path.append('.')
from pack.config import *
from pack.file_sys import *

def diff(csv_w, filepath, combs):
    for comb in combs:
        diff_res = diffFiles(os.path.join(
            filepath, comb[0]), os.path.join(filepath, comb[1]))
        csv_w.writerow(diff_res)
            
if __name__ == "__main__":       
    comp_path = 'input/Linux_compare-2'  # 路径由用户自行修改
    project_name = os.path.split(comp_path)[1].strip('/\\')
    with open(os.path.join(out_dir, project_name+'.csv'), 'w') as csv_file:
        csv_w = csv.writer(csv_file)
        csv_w.writerow(['file1', 'file2', 'diff_path', 'label'])
        for filepath, dirnames, filenames in os.walk(comp_path):
            if len(filenames) > 0 and len(dirnames) == 0:
                diff(csv_w, filepath, itertools.combinations(filenames, 2))
                             
