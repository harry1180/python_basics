import os,glob,time
import re
from bs4 import BeautifulSoup
currentDirABSPath=os.path.split(os.path.abspath(__file__))[0]
startTime=time.time();

import xlwt
from pandas import DataFrame
#def xcelwriters(SoureFolder="Sanity_checks_op",targetFileExt=".txt"):
def xcelwriters():
    #for filename in glob.glob('*.txt'):
    files=glob.glob('*.txt')
    aaa=[]
    count=0
    #a=open(filename,'r')
    for i in files:
        with open(i) as f:
            for line in f:
                count=count+1
                #print (count)
                split=line.split()
                #print(line.split())
                lines=line.split()
                book=xlwt.Workbook(encoding="utf-8")
                k=10
                sheet1 = book.add_sheet("Sheet %d"%k)
                df = DataFrame({'Sample column': lines})
                df.to_excel('test.xlsx', sheet_name='sheet1', index=False)
                #ff=aaa.append(lines)
                #print (ff)
                print (lines)
                print ('this is a seperator')
                """for i,e in enumerate(lines):
                    sheet1.write(i,e,lines)
                    #print('this is i %d'%i,e,lines)
                    book.save("trails%d.xls"%k)
                    #book.save("trails.xlsx")"""

                    

"""aaa.append(i.split("\n"))
        k=3
        for n in aaa:
            book=xlwt.Workbook(encoding="utf-8")
            print (n)
            sheet1 = book.add_sheet("Sheet %d"%k)
            df = DataFrame({'Stimulus Time': n})
            df.to_excel('test.xlsx', sheet_name='sheet1', index=False)
            #sheet1='sheet1'+'k'
            #sheet1.write(k,1,n)
            k=k+1
            #print(k)
    book.save("trails%d.xls"%i)"""
""" book=xlwt.Workbook(encoding="utf-8")
            sheet1 = book.add_sheet("Sheet %d"%k)
            k=k+1
            kk=0
            sheet1.write(k,0, aaa[kk])
            kk=kk+1
            sheet1='sheet1'+'k'
            book.save("trails%d.xls"%k)
           #print (i)
        #print (a)
        
        #print (filename)
        #for i in filename:
            #a=open(i,'r')
            #print (a)"""
xcelwriters()
#extractQueries()
#endTime=time.time()
#execTime=endTime-startTime
#print("\tExecution Time : %f secs"%execTime);

