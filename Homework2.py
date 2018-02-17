# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 22:14:55 2018

@author: hp-pc
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

def index(string:str,word:str,x:int):
    if word not in string[x:]:
        return -1
    i=string[x:].find(word)
    return i+x

def findword(filename:str, word:str):
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print("Warning: File %s not found"%(filename))
        print(-1)

    lines = file.readlines()
    myString = ""
    locations = []
    for eachLine in lines:
        myString = myString + eachLine;
    
    x=0
    while len(myString[x:]) >= len(word):
        x=index(myString,word,x)
        x=x+1
        if x==0:
            break
        else:
            locations.append(x)
    
    print(locations)
    
def Datasorter(filename:str):
    
    Categories=[]
    with open(filename) as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            Categories.append(row['Category'])
            
        CategorySet=set(Categories)
        CategoryList=list(CategorySet)
        CategoryList.sort()
        ValueListofList=[[] for x in range(len(CategoryList))]
        csvfile.seek(0)
        for row in reader:
            for i in range(len(CategoryList)):
                if row['Category']==CategoryList[i]:
                    ValueListofList[i].append(row['Value'])
        
    ListofListofValues=[[] for x in range(len(CategoryList))]
    for i in range(len(CategoryList)):
        SetofValues=set(ValueListofList[i])
        ListofValues=list(SetofValues)
        ListofValues.sort()
        ListofListofValues[i]=ListofValues

    maxlen = max([len(member) for member in ListofListofValues])
    [member.extend([""] * (maxlen - len(member))) for member in ListofListofValues]
    #print(ListofListofValues)
    TListofListofValues=np.array(ListofListofValues).T.tolist()               
                    
    with open("sorteddata.csv","w",newline='') as csvfile:
        writer=csv.writer(csvfile,dialect='excel')
        writer.writerow(CategoryList)
        writer.writerows(TListofListofValues)
    
def gpsdataplot(filename:str):
    data=np.loadtxt(filename,delimiter=',',skiprows=1,usecols=[2,3,4,5,6,7],dtype=(float))
    powerDB=data[:,5]
    endF=data[:,4]
    p_av=np.mean(powerDB)
    p_med=np.median(powerDB)
    p_min=np.min(powerDB)
    p_max=np.max(powerDB)
    
    i=[index for index, value in enumerate(powerDB) if value == p_med]
    j=[index for index, value in enumerate(powerDB) if value == p_min]
    k=[index for index, value in enumerate(powerDB) if value == p_max]
    
    endf_i=endF[i]
    endf_j=endF[j]
    endf_k=endF[k]
    
    finallist=[p_av,p_med,p_min,p_max]
    
    finallist.append(endf_i.tolist())
    finallist.append(endf_j.tolist())
    finallist.append(endf_k.tolist())
    
    fig=plt.figure(1)
    ax=fig.add_subplot(111)
    ax.set_xlabel("ending frequency sweep")
    ax.set_ylabel("received signal strength")
    ax.set_title("Antenna data at <location>")
    axes = plt.gca()
    axes.set_xlim([min(endF),max(endF)])
    axes.set_ylim([min(powerDB),max(powerDB)])
    ax.plot(endF,powerDB,'bo',linewidth=1.0,linestyle='-')
    ax.annotate('MaxPowerDB', xy=(min(endF[k]), max(powerDB)), xytext=(min(endF[k])+10, max(powerDB)+10),
            arrowprops=dict(facecolor='black', shrink=0.05))
    plt.show()
    
    return finallist