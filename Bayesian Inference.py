"""
@author: Sandeep
"""
import sys

possibleValues = [] 
n=int(input())
for i in range(0, n): 
    ele = str(input())
    possibleValues.append(ele.split(","))
    x=int(len(possibleValues[i]))
    for j in range(0, x):
        if possibleValues[i][j][0]==" ":
            possibleValues[i][j]=possibleValues[i][j][1:len(possibleValues[i][j])]

dependency = []
for i in range(0, n): 
    dependency.append(input().strip().split()) 
    
parent = []
for j in range(n):
    a = [j]
    for i in range(n):
        if dependency[i][j]=='1':
            a.append(i)
    parent.append(a)


data = []    
m = int(input())
for i in range(0, m): 
    ele = str(input())
    data.append(ele.split(","))
    x=int(len(data[i]))
    for j in range(0, x):
        if data[i][j][0]==" ":
            data[i][j]=data[i][j][1:len(data[i][j])]


lst = [];
for item in data:
    item = tuple(item)
    lst.append(item)
lst = set(lst)
def cnt_f(n):
    n = list(n);
    n.append(data.count(n));
    return n;
lst = sorted(list(map(cnt_f,lst)))

#print(lst);

def evaluate(cond):
    ss = 0;
    for i in range(len(lst)):
        sat = True
        for j in range(len(cond)):
            sat = sat and (lst[i][cond[j][0]] == cond[j][1])
        if(sat):
            ss += lst[i][-1];
    return ss

def generate(ans,parents,p_no,temp):
    if(p_no == len(parents)):
        ans.append(temp)
    else:    
        for i in range(len(possibleValues[parents[p_no]])):
            temp1 = temp+ [[parents[p_no],possibleValues[parents[p_no]][i]]]
            generate(ans,parents,p_no+1,temp1)

for i in range(n):
    generated_seq =[]
    temp = []
    generate(generated_seq,parent[i],0,[])
    for j in range(len(generated_seq)):
        if evaluate(generated_seq[j][1:])!=0:
            print(str(round(evaluate(generated_seq[j])/evaluate(generated_seq[j][1:]),4)),end =" ");
        else :
            print('0',end =" ");
        if j<len(generated_seq)-1:
            print(' ',end =" ");
    if i<n-1:
        print('');       
    