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
            fout=open(path,'a') #a=append  w=write
            fout.write(datestr) #在最前排寫入當日股票日期
            for b1 in block:
                b1clr=b1.translate({ord(c): None for c in '"'})
                pattern = '%s%s'
                padding = ' ' * (20 - calc_len(b1clr))
                fout.write(pattern % (padding,b1clr))
            fout.write('\n') #換行
            fout.close()     
            #return block
            #print(block)
            #print(fstock)
      
    
sort_out('20190314')
#print(a)

#________________________________________________________________________

widths = [
        (126,    1), (159,    0), (687,     1), (710,   0), (711,   1),
        (727,    0), (733,    1), (879,     0), (1154,  1), (1161,  0),
        (4347,   1), (4447,   2), (7467,    1), (7521,  0), (8369,  1),
        (8426,   0), (9000,   1), (9002,    2), (11021, 1), (12350, 2),
        (12351,  1), (12438,  2), (12442,   0), (19893, 2), (19967, 1),
        (55203,  2), (63743,  1), (64106,   2), (65039, 1), (65059, 0),
        (65131,  2), (65279,  1), (65376,   2), (65500, 1), (65510, 2),
        (120831, 1), (262141, 2), (1114109, 1),
]


def calc_len(string):
    def chr_width(o):
        global widths
        if o == 0xe or o == 0xf:
            return 0
        for num, wid in widths:
            if o <= num:
                return wid
        return 1
    return sum(chr_width(ord(c)) for c in string)

#________________________________________________________________________
#result:

![image] (https://github.com/s4017050400/CrawlerTutorial/blob/master/TWSE/%E7%88%AC%E8%9F%B21.PNG)
