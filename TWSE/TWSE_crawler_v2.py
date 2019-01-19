#把所有資料分別存在各自的TXT檔中


import requests
from io import StringIO
import pandas as pd
import numpy as np

def fetch(datestr):
    response = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALL')
    return response

def sort_out(datestr):
    #datestr='20181116'
    resp = fetch(datestr)
    
    
    for i in resp.text.split('\n'):
        block=i.split('",')
        if len(block) == 17 and i[0] != '=':
            del block[16] #del '\r'
            fstock=(block[0]+block[1]).translate({ord(c): None for c in '"'}) #1101台泥
            path= r'C:/Users/s4017/Desktop/a/'+ str(fstock) + '.txt' #prefix the string with r (to produce a raw string)
            fout=open(path,'w')
            fout.write(datestr) #在最前排寫入當日股票日期
            for b1 in block:
                b1clr=b1.translate({ord(c): None for c in '"'})
                pattern = '%s%s'
                padding = ' ' * (20 - calc_len(b1clr))
                fout.write(pattern % (padding,b1clr))
            fout.close()     
            #return block
            #print(block)
            #print(fstock)
      
    
sort_out('20190118')
#print(a)


________________________________________________________________________
result:

