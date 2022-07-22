import os
import shutil
import filecmp
import difflib
from .config import *

def copy_file(srcfile,dstpath):                       # 复制函数
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(srcfile)             # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)                       # 创建路径
        shutil.copy(srcfile, os.path.join(dstpath,fname))          # 复制文件
        print ("copy %s -> %s"%(srcfile, os.path.join(dstpath,fname)))

def get_files(path):
    for filepath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            # yield os.path.join(filepath,filename)
            yield (filepath, filename)

def seekFile(root_path,name):
    for tp in get_files(root_path):
        if tp[1]==name:
            return tp[0]+'/'+tp[1]
    return None

def getFileName(path):
    strs=path.rsplit('/',1)
    if(len(strs)>1):
        file_name=strs[1]       
    else:
        file_name=path
    return file_name

def getFileKey(path):
    file_name=getFileName(path)
    strs=file_name.split('.')
    if not strs[0]:
        return '.'+strs[1]
    else:
        return strs[0]

# 为True表示两文件相同
def cmpFiles(file_name1,file_name2):
    # 如果两边路径的头文件都存在，进行比较
    try:
        return filecmp.cmp(file_name1, file_name2)
    # 如果两边路径头文件不都存在，抛异常
    except IOError as e:
        print("Error: File not found or failed to read",e)
        exit()

def readContent(file_path):
    with open(file_path) as f:
        content = f.read().splitlines(keepends=True)
    return content

def diffFiles(file_path1,file_path2):
    split1=os.path.split(file_path1)
    split2=os.path.split(file_path2)
    comp_sub_dir=os.path.split(split1[0])[1]
    name1=split1[1]
    name2=split2[1]
    html_name='diff_'+name1+'_'+name2+'.html'
    out_comp_path=os.path.join(out_dir,comp_sub_dir)
    html_path=os.path.join(out_comp_path,html_name)
    if not os.path.exists(out_comp_path):
        os.makedirs(out_comp_path) 
    content1=readContent(file_path1)
    content2=readContent(file_path2)
    html_diff = difflib.HtmlDiff()
    htmlcontent = html_diff.make_file(content1, content2)
    with open(html_path, 'w') as f:
        f.write(htmlcontent)
    return os.path.join(comp_sub_dir,name1), os.path.join(comp_sub_dir,name2), os.path.abspath(html_path)    

