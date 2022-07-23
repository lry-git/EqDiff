本项目可以辅助等价性分析判断，用于产生同一个文件夹中所有文件的组合，以及组合配对的两个文件间的Difference，最后由人工根据Diff文件中的信息，为每一对组合打上标签，label=1表示equal，label=0表示inequal。

# environment

Ubuntu 18+

Python 3

# diff

用户修改了diff.py中的comp_path变量后(例如comp_path = 'input/Linux_compare-2')，运行diff.py，就会在output文件夹下看到需要分析的项目对应的project_name.csv文件，该文件格式如下：

| file1  | file2  | diff_path               | label |
| ------ | ------ | ----------------------- | ----- |
| foo1.c | foo2.c | diff_foo1.c_foo2.c.html | 待定  |

 用户可以将diff_path下的HTML文件打开，可以看到图形化的diff信息，还可以有简单的交互，方便用户确定等价性，最后填写label信息，label=1表示equal，label=0表示inequal

# classifier

用户填好project_name.csv中的label后，修改classifier.py中的label_res_path变量，运行classifier.py，即可在output文件夹下看到相应的equal.csv和inequal.csv