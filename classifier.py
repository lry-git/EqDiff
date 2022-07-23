#!/usr/bin/env python3

import os
import csv
from pack.config import *

eq_suffix = '_equal_pairs.csv'
ineq_suffix = '_inequal_pairs.csv'
label_res_path = 'output/Linux_compare-2.csv'  # 路径由用户自行修改

project_file = os.path.split(label_res_path)
project_name = project_file.rsplit('.', 1)[0]
eq_file_path = os.path.join(out_dir, project_name+eq_suffix)
ineq_file_path = os.path.join(out_dir, project_name+ineq_suffix)
with open(eq_file_path, 'w') as eq_file, open(ineq_file_path, 'w') as ineq_file:
    eq_w = csv.writer(eq_file)
    ineq_w = csv.writer(ineq_file)
    with open(label_res_path, 'r') as label_file:
        csv_r = csv.reader(label_file)
        next(csv_r)  # skip the header
        for row in csv_r:
            if len(row)==0:
                continue
            assert len(row)>3,'there is no label'
            label = int(row[3])
            if label:
                eq_w.writerow(row[:2])
            else:
                ineq_w.writerow(row[:2])
