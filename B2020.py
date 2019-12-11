# program to calculate the gain or loss on bitcoin transactions
# one line of text as header followed by columns of data
# Data file   date, +/-coin number, cost$
#             20190402,0.050,205

import csv
import sys
import os
from datetime import date
from decimal import *


datafile = "test.txt"
writefile = "test.csv"

Precision = 8      # number of decimal places in the data
 
tcost = 0          # running totals for partial sale
tnum = 0
tprofit = 0

def SortData():
# separate data into 2 strings
# one with sales and one with buys

    Buy = ""
    Sell = ""
    BuyCnt = 0
    SellCnt = 0
    with open('work.tmp', newline='') as f1:
        reader = csv.reader(f1)
        for line in reader:
            a1 = line[1]
            if a1[0] == '-':
                SellCnt += 1
                Sell = Sell + str(SellCnt) + ',' + line[0] + ',' + line[1] + ',' + line[2] + '\n'
            else:
                BuyCnt += 1		
                Buy = Buy + str(BuyCnt) + ',' + line[0] + ',' + line[1] + ',' + line[2] + '\n'	

# sort the Buy and Sell strings into descending order by index numbers
# assume the datafile is in chronologic order and you want to use FIFO accounting
# the data would be rearanged from a chronologic order

    sortflag = 1
    while sortflag > 0:
        sortflag = 0
        cnt = 0
        d1 = ""
        c1 = ""
        Temp = ""
        lastflag=0
        passNum = 0
        for c in range(len(Buy)):
            a1 = Buy[c]
            if a1 == '\n':
                d1 = d1 + a1
                cnt = 0
                passNum += 1
                if passNum == 1:
                    c2 = c1
                    d2 = d1
                if passNum > 1:		
                    c3 = c1			
                    d3 = d1
                    A = int(c2)				
                    B = int(c3)		
                    if (A > B):
                        Temp = Temp + c2 + d2
                        c2 = c3
                        d2 = d3
                        lastflag=1
                    if (A < B):
                        Temp = Temp + c3 + d3	
                        sortflag = 1					
                        lastflag=2
                    			
                d1 = ""
                c1 = ""			
                continue		       
            if a1 == ',':
                cnt = cnt + 1
            if cnt == 0:
                c1 = c1 + a1
            if cnt > 0:
                d1  = d1 + a1
        if lastflag == 1:
            Temp = Temp + c3 + d3  	
        if lastflag == 2:
            Temp = Temp + c2 + d2		
        Buy = Temp           	
	
# filter out the index numbers before writing the new work file
    with open('work.tmp','w') as f2:
        Temp = ""
        for c in range(len(Buy)):
            a1 = Buy[c]
            if a1 == '\n':
                d1 = d1 + a1
                Temp = Temp + d1
                d1 = ""
                cnt = 0
            if ((a1 == ',') and (cnt == 0)):
                cnt += 1
                continue
            if cnt > 0:
                d1 = d1 + a1
        f2.write(Temp)

    sortflag = 1
    while sortflag > 0:
        sortflag = 0
        cnt = 0
        d1 = ""
        c1 = ""
        Temp = ""
        lastflag=0
        passNum = 0
        for c in range(len(Sell)):
            a1 = Sell[c]
            if a1 == '\n':
                d1 = d1 + a1
                cnt = 0
                passNum += 1
                if passNum == 1:
                    c2 = c1
                    d2 = d1
                if passNum > 1:		
                    c3 = c1			
                    d3 = d1
                    A = int(c2)				
                    B = int(c3)		
                    if (A > B):
                        Temp = Temp + c2 + d2
                        c2 = c3
                        d2 = d3
                        lastflag=1
                    if (A < B):
                        Temp = Temp + c3 + d3
                        sortflag = 1					
                        lastflag=2
                    			
                d1 = ""
                c1 = ""			
                continue		       
            if a1 == ',':
                cnt = cnt + 1
            if cnt == 0:
                c1 = c1 + a1
            if cnt > 0:
                d1  = d1 + a1
        if lastflag == 1:
            Temp = Temp + c3 + d3  	
        if lastflag == 2:
            Temp = Temp + c2 + d2		
        Sell = Temp           	

# filter out the index numbers before writing the new work file
    with open('work.tmp','a') as f2:
        Temp = ""
        for c in range(len(Sell)):
            a1 = Sell[c]
            if a1 == '\n':
                d1 = d1 + a1
                Temp = Temp + d1
                d1 = ""
                cnt = 0
            if ((a1 == ',') and (cnt == 0)):
                cnt += 1
                continue
            if cnt > 0:
                d1 = d1 + a1
        f2.write(Temp)

	
	
	
print("\n\nBasis-Profit Calculator")
print("Ed Jordan, 14 Feb 2018")

sortFlag = ""
a = ""
a2 = ""
b = len(sys.argv)
if b > 1:
    for c in range(b): 
        a2 = sys.argv[c]
        print(a2)
        if a2[0] != '-':
            a = a2
			
        if ((a2 == '-h') or (a2 == '--help') or (a2 == '-H')):
            print("Data should have one line of buys before the first sale.  It can have a line of headers at the top.")
            print("Data file needs 3 columns.  These are separated by commas or tabs.")
            print("Program uses last-in to first-out, LIFO, basis accounting\n")
            print("Data should be in chronological order with buys first before sales.")
            print("An 'index out of range' error probably is related to the data file format. ")
            print("Parameters:\n -h or --help or -H: help\n first parameter: datafile name\nFirstIn-FirstOut: -F")
            print("python B2018.py datafile.txt -F")
            print("See the README file.")
            sys.exit(1)

        if ((a2 == '-F') or (a2 == '-f')):
            sortFlag = "F"
			
if a != '': 
    dfile = ''
    for s in range(0,len(a)):
        if a[s] == '.':
            break
        dfile = dfile + a[s]

    datafile = dfile + '.txt'
    writefile = dfile + '.csv'
    print(datafile)

with open(datafile,'r') as f1:
    with open('work.tmp','w') as f2:
        for line in f1:
            msg = ""
            flag = 0
            for s in range(0,len(line)):
                a = line[s]
                if line[0] == '\n':
                    break               
                if a == chr(9):
                    a = ','
                    msg = msg + a
                elif ((a == ',') and (flag == 1)):
                    continue
                elif a == '$':
                    flag = 1
                    continue
                elif ((a == ',') and (flag == 1)):
                    continue
                elif a == ' ':
                    continue
                else:
                    msg = msg + a
             
            f2.write(msg)    
            f2.close

	
if sortFlag == 'F':
    print("Option -F")
    SortData()   


	
def GetDecimal(n3):        # each piece of data should have the correct number of decimals
    cnt = 0
    for s in range(0,len(n3)):
        a = n3[s]
        cnt = cnt + 1
        if a == '.':
            cnt = 0
       
    return cnt
	
	
def AdjFlag(n1,n2,Prec):
    flag=0		
    
# 3 outcomes for addition of sold coins with bought coins
# negative - more sold than bought
# positive - fewer sold than bought
# zero - equal number sold and bought  $flag 0, 1, or 2

    a = "0."
    for s in range(0,Prec):
        a = a + "0"
		
    a = a + "5"
    a = Decimal(a)	
    pr1 = float(n1)
    pr2 = float(n2)    
	
    if pr1 < a:           # decimal point + 1 ?
        pr1 = 0
    if pr2 < a:
        pr2 = 0
    
    pr3 = pr1 - pr2

    if pr3 == 0:
        flag = 0
    if pr3 > 0:
        flag = 2
    if pr3 < 0:
        flag = 1

# if the flag is zero.  The amounts of the coins are equal
# the price of the bought coins == the basis of the sold coins
# both the bought coin row and the sold coin row can be deleted
# from the data file

    return flag

def findRecordIndex():
    inx = 1					# starting record
    try:
        with open('work.tmp', newline='') as f1:
            reader = csv.reader(f1)
            cnt = 0
            for line in reader:
                cnt=cnt+1
                n1 = line[1]
                if n1[0] == '-':
                    inx = cnt
                    break
            f1.close
        inx = inx -1
    except IndexError:
        inx = 0
    return inx

def findListA(inx):
    dataLista = ""
    f1 = open('work.tmp', 'r')
    cnt = 1
    c1 = ""
    for line in f1:   
        c1 = c1 + str(line)    
        cnt = cnt + 1 
        if cnt == inx:
            f1.close
            break
    
    dataLista = c1
    return dataLista

def findListB(inx):
    dataListb =""
    inx = inx +2
    f1 = open('work.tmp', 'r')
    cnt = 0
    c1 = ""
    for line in f1:
        cnt = cnt +1      
        if cnt >= inx:
            c1 = c1 + str(line)     
            
    f1.close
    dataListb = c1
    return dataListb

def saveData(html):
    csv.register_dialect('escaped', delimiter = ' ', escapechar="\\",  quoting=csv.QUOTE_NONE)
    with open(writefile, 'a', newline='') as f1:
        linewriter = csv.writer(f1, dialect='escaped')
        linewriter.writerow(html)
        f1.close
    return

def writeData(dataLista, html, dataListb):
    f1 = open('work.tmp','w')
    f1.write(dataLista)
    f1.write(html)
    f1.write(dataListb)
    f1.close
    return

def makePositive(x):     # string x is returned positive
    c = x
    a = ""
    for b in range(len(c)):
        if c[b] != '-':
            a = a + c[b]
    return a

def adjLength(x,y):      # limit string to 2 decimal digits for currency.
                         # y is the number of digits after the decimal point
    cnt=0
    a = ""
    e = ""
    c = ""
    d = 0
    flag = 0    # flag for the decimal point
    flag2 = 0   # flag for a leading zero in e
    for b in range(len(x)):
        f = x[b]
        if flag == 1:
            cnt = cnt + 1
            if cnt > y:
                d = int(f)
                break
            e = e+f
        if f == '.':
            flag = 1
        if flag == 0:
            c = c + f
					
    if d > 4:     
        flag=0
        cnt = 0

        for b in range(len(e)):
            if e[b] != "0":
                flag = 1
            if e[b] == "0":
                if flag == 0:
                    flag2 = flag2+1   # count leading zeros
            else:
                cnt = cnt+1           # digits after leading 0

#  int drops all leading zeros
# if e is all 9s  - they become zeros and c is incremented
# if e is all 0s  - it becomes 1 and we drop one leading 0
# if e after the leading zeros is all 9s we also drop 1 0

        pr = ""
        pr1= ""
        if cnt > 0:
            for b in range(cnt):
                pr = pr + "9"
                pr1 = pr1 + "0"
            
            pr = int(pr)
            e = int(e)
            
            if e == pr:
                if cnt < y:
                    e = "1"+pr1
                    flag2 = flag2 -1
                if cnt == y:
                    e = pr1
                    c = int(c)
                    c = c + 1
                    c = str(c)
            else:
                e = e + 1
                e = str(e)
                for b in range(flag2):
                    e = '0'+e

        if cnt == 0:
            e = 1
            flag2 = flag2-1
            e = str(e)
            if flag2 > 0:            # add leading zeros
                e = str(e)
                for b in range(flag2):
                    e = "0"+e

    a = c +"."+e        
    n = y - len(e)
	
    if n > 0:
        for b in range(n):
            a = a + "0"		# add trailing zeros
            
    return a    
    
def adjValue(x):   # adj value of digital x  and make string
    if x == 0:
        a = "0.00"
    else:
        a = str(x) 

    return a             

# Save work.tmp first to the spreadsheet.  This followed by the program output	
msg = ""
saveData(msg)

with open('work.tmp','r') as f1:
    for line in f1:
        msg = ''
        for a in range(0,len(line)):
            if line[a] != '\n':
                msg = msg + line[a]

        saveData(msg)  
	
# write first row of the spreadsheet
msg = ""
saveData(msg)
msg = "saleDate,number,cost,unitPrice,proceeds,buyDate,profit,gain"
saveData(msg)

# d1 is the date of the purchase
# d2 is the date of the sale
# gain is the long or short term nature of the sale
# p1 is the price of the purchased coins
# p2 is the price of the sale of coins and it is negative
# p3 is the price per coin in dollars purchased
# p4 is the price per coin in dollars sold
# n1 is the number of coins bought
# n2 is the number of coins sold.


inx = 1
while inx > 0:
    
    d1=""
    d2=""
    n1=""
    n2=""
    p1=""
    p2=""
    p3=""
    p4=""

    cnt2 = 0
    flag = 0
    dataListA = ""
    dataListB = ""

    inx = findRecordIndex() 
    if inx < 1:
        break
    
    with open('work.tmp', newline='') as f1:
        reader = csv.reader(f1)
        cnt=0
        
        for line in reader:
            cnt=cnt+1
            if cnt == inx:
                d1 = line[0]
                n1 = line[1]
                p1 = line[2]
            if cnt == inx+1:
                d2 = line[0]
                n2 = line[1]
                p2 = line[2]
                break
        f1.close
		
    Precision = GetDecimal(n1)           # set decimal number based on data 
    p1 = makePositive(p1)
    p2 = makePositive(p2)  
    n1 = makePositive(n1)
    n2 = makePositive(n2)
	
    yr1 = d1[0]+d1[1]+d1[2]+d1[3] 
    yr2 = d2[0]+d2[1]+d2[2]+d2[3]       
    if d1[4] == 0:
        mo1 = d1[5]        
    else:
        mo1 = d1[4] + d1[5]
    if d1[6] == 0:
        da1 = d1[7]
    else:
        da1 = d1[6] + d1[7]      
    if d2[4] == 0:
        mo2 = d2[5]        
    else:
        mo2 = d2[4] + d2[5]
    if d2[6] == 0:
        da2 = d2[7]
    else:
        da2 = d2[6] + d2[7]

    yr1 = int(yr1)
    mo1 = int(mo1)
    da1 = int(da1)
    yr2 = int(yr2)
    mo2 = int(mo2)
    da2 = int(da2)        

    date1 = date(yr1,mo1,da1)
    date2 = date(yr2,mo2,da2)
    date3 = abs(date2-date1)
    date3 = date3.days
    if date3 > 365:
        gain = "L"
    else:
        gain = "S"

# the basis for the sale is the share of the coins purchased
# is #sold/#bought x price of the whole purchase	
    
    p1 = Decimal(p1)          # cost of purchase
    p2 = Decimal(p2)          # proceeds of sale  
    n2 = Decimal(n2)          # number sold
    n1 = Decimal(n1)          # number bought
    p3 = Decimal(p1/n1)       # price per coin bought
    p4 = Decimal(p2/n2)       # price per coin sold
    p4 = float(p4)
    p4 = Decimal(p4)
    p3 = float(p3)
    p3 = Decimal(p3)
	
    basis = p3*n2        
    pr9 = basis
    profit = p2 - basis
	
    basis = adjValue(basis)
    basis = adjLength(basis,2)
    basis = Decimal(basis)
    profit = adjValue(profit)
    profit = adjLength(profit,2)
    profit = Decimal(profit)
    pr8 = profit
   
		
# the price obtained for the coins sold minus the basis = gain/loss  p2 = proceeds of sale
# remaining coins unsold are n1 - n2  
# the price per coin purchased does not change.  p3 and p4 don't change

    profit = adjValue(profit)
    profit = adjLength(profit,2)
    newNumCoins = n1-n2
    newBasis = newNumCoins*p3
    newBasis = adjValue(newBasis)
    newNumCoins = str(newNumCoins)
    basis = adjValue(basis)

    newBasis = adjLength(newBasis,2)

    profit = adjLength(profit,2)
    newNumCoins = adjLength(newNumCoins,Precision)
    
    flag = AdjFlag(n1,n2, Precision)

  
    dataListA = findListA(inx)
    dataListB = findListB(inx)

    if flag == 0:                       # equal number sold and bought
        if tnum > 0:
            tnum = tnum + n2
            tprofit = tprofit + pr8
            tcost = tcost + pr9
            p5 = adjValue(tnum)
            p6 = adjValue(tcost)
            p7 = adjValue(tprofit)
            p5 = adjLength(p5,Precision)
            p6 = adjLength(p6,2)
            p7 = adjLength(p7,2)
            
        n2 = str(n2)
        p3 = adjValue(p3)
        p3 = adjLength(p3,2)
        n2 = adjLength(n2,Precision)
        p1 = adjValue(p1)
        p2 = adjValue(p2)
        p1 = adjLength(p1,2)
        p2 = adjLength(p2,2)
        p4 = adjValue(p4)
        p4 = adjLength(p4,2)
        msg = d2+",-"+n2+","+basis+","
        msg = msg+p4+","+p2+","+d1+","+profit+","+gain
        if tnum > 0:
            msg = msg + ","+p5+","+p6+","+p7
            tnum = 0
            tprofit = 0
            tcost =  0
            
        saveData(msg)
        msg = '\n'
        writeData(dataListA,msg,dataListB)

    if flag == 2:                             # fewer number sold than bought
        if tnum > 0:
            tnum = tnum + n2
            tprofit = tprofit + pr8
            tcost = tcost + pr9
            p5 = adjValue(tnum)
            p6 = adjValue(tcost)
            p7 = adjValue(tprofit)
            p5 = adjLength(p5,Precision)
            p6 = adjLength(p6,2)
            p7 = adjLength(p7,2)
        
        
        n2 = str(n2)
        profit = str(profit)
        n2 = adjLength(n2,Precision)
        p2 = adjValue(p2)
        p2 = adjLength(p2,2)
        p4 = adjValue(p4)
        p4 = adjLength(p4,2)
        msg = d2+",-"+n2+","+basis+","+p4+","+p2+","+d1+","+profit+","+gain
        if tnum > 0:
            msg = msg + ","+p5+","+p6+","+p7
            tnum = 0
            tprofit = 0
            tcost =  0
            
        saveData(msg)
        msg = d1+','+newNumCoins+','+newBasis+'\n'

        writeData(dataListA,msg,dataListB)
  
    if flag == 1:                           # greater number sold than bought - carry some over unsold coins to the next sale
                                            # n1 becomes the number sold and the proceeds are n1*p4  for sale proceeds
		                                    # p1 is the basis of the sold coins 
                                            # want to add totals for coin number, cost, profit  9 Dec 2019
        nn1 = n2 - n1
        tnum = tnum + n1
        newBasis = nn1*p4
        np2 = n1*p4
        nn1 = str(nn1)
        nn1 = makePositive(nn1)
        nn1 = adjLength(nn1,Precision)
        profit = np2-p1        
        tprofit = tprofit + profit
        tcost = tcost + p1
        np2 = adjValue(np2)
        np2 = adjLength(np2,2)
        p1 = adjValue(p1)
        p1 = adjLength(p1,2)
        n1 = str(n1)  
        n1 = adjLength(n1,Precision)      
        p2 = str(p2)
        p4 = adjValue(p4)
        p4 = adjLength(p4,2)
        profit2=adjValue(profit)
        profit2=adjLength(profit2,2)
        newBasis = adjValue(newBasis)
        newBasis=adjLength(newBasis,2)
        p5 = adjValue(tnum)
        p5 = adjLength(p5,Precision)
        p6 = adjValue(tcost)
        p6 = adjLength(p6,2)
        p7 = adjValue(tprofit)
        p7 = adjLength(p7,2)
        
        msg = d2+",-"+n1+","+p1+","+p4+","+np2+","+d1+","
        msg = msg +profit2+","+gain+","+p5+","+p6+","+p7
        saveData(msg)
        
        msg = d2+',-'+nn1+',-'+newBasis+'\n'
        writeData(dataListA,msg,dataListB)
		

		
#  add the work.tmp residual file to the spreadsheet
#  then delete the work.tmp file
msg = ""
saveData(msg)
msg = 'Residual,Unsold,Items'
saveData(msg)

with open('work.tmp','r') as f1:
    for line in f1:
        msg = ''
        for a in range(0,len(line)):
            if line[a] != '\n':
                msg = msg + line[a]

        saveData(msg)  
       
		
os.remove('work.tmp')

print('done')
sys.exit(0)