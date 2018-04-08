'''
在“0987654321”之间添加“+”“-”“*”“/”和“=”使等式成立。
这 5 个符号必须都用到且只能用一次。
优先循序为先乘除后加减。
“+”可以做加号，也可以作为正号，“-”可以做减号，也可以作为负号。
列出所有可能的答案。
数字的顺序不能改变。
'''
import itertools
import numpy as np
str1 = '0987654321'
str2 = '+-*/='
str1_list = list(str1)
str2_list = list(str2)
np_arr = np.array(str1_list)
result = list(itertools.permutations(range(len(str1_list)), len(str2_list)))
for i in result:
	if i[2] ==0 or i[3]==0 or i[4] == 0:
		continue
	else:
	    newlist = np.insert(np_arr,i,str2_list).tolist()
	    if (i[0] ==0 or i[1]==0) and newlist[2] == '9':
	    	newlist.pop(1)
	    if newlist[0] == '0' and newlist[1] == '9':
	    	newlist.pop(0)
	    str3 = ''.join(newlist)
	    idx = str3.find('=')
	    left = str3[:idx]
	    right = str3[idx+1:]
	    # print(left,right)
	    if eval(left) == eval(right):
	    	print(str3)