from collections import OrderedDict

def replace_all(text,dic):
    for i, j in dic.items():
        text=text.replace(i,j)
    return text

od=OrderedDict([("%s"%i,"_") for i in '\/:*?"<>|'])
s1=replace_all('(已被eyespot刪除) <PigIsBignana> 1-2-2.txt',od)

print(s1)

______________________________________________________________________
results
  (已被eyespot刪除) _PigIsBignana_ 1-2-2.txt
