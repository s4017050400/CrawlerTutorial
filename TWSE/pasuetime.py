#loop for date
from datetime import date
from datetime import timedelta


def datebyyear(year):
    #today=date.today() #which is like datetime.date(2018,10,3)
    start = date(2004,2,11) #TWSE 股市開始給抓的日子
    one_day=timedelta(days=1) #one day which can be plused
    result = [] #where for loop date store in 

    for i in range(0,20*year): #1+365天
        date1=start+i*one_day
        standard=date1.isoformat().replace('-','')#.translate({ord(c):None for c in '-'})#date.isoformat() is 2018-10-03
        #sort_out(standard)
        result.append(standard)
    return result
        #print(standard)



import time

def loopstockdata(year):
    #date = datebyyear(year)
    #print(date)
    for date in datebyyear(year):
        if int(date) % 5 == 0:
            time.sleep(0.5)
        sort_out(date)
