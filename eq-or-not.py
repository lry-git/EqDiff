#!/usr/bin/env python

import os
import csv
# 路径供用户修改
eq_suffix='_equal_pairs.csv'
ineq_suffix='_inequal_pairs.csv'
diff_res_path='output/Linux_compare-2.csv'

project_file=os.path.split(diff_res_path)
project_name=project_file.rsplit('.',1)[0]

with open(diff_res_path, 'r') as csv_file:
    csv_r = csv.reader(csv_file)
    next(csv_r)  # skip the header    
    
    for row in csv_r:
        label = int(row[3]) 
        if label:
                           
        print("line id: %d"%line_id)  
        errors.write("row: %s\n"%str(row))        
        # function='unknown'
        # defuses.append(DefUse(name, total_path, 
        defuse1=getDefUse(row,which,label)
        defuse2=getDefUse(row[1:],which,label)