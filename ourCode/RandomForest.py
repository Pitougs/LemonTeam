# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:47:44 2017

@author: Zeyu YANG
"""

path.append('../public_data')
path.append('../ourCode')
path.append('ourCode/')

from sklearn.ensemble import RandomForestRegressor

def loadData(fileName):
        
    numFeat = len(open(fileName).readline().split('\t')) 
    dataMat = []
    fr = open(fileName)
    
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat) :
            lineArr.append(curLine[i])        
        dataMat.append(lineArr)
    return dataMat

    
def loadSolution(fileName):
    
    numFeat = len(open(fileName).readline().split('\t')) 
    fr = open(fileName)
    dataMat = []
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        for i in range(numFeat) :
            dataMat.append(curLine[i])
    
    return dataMat

    
        
if __name__ == '__main__':
    
    data = loadData('movierec_train.data')
    target = loadSolution('movierec_train.solution')
    test = loadData('movierec_test.data')
    
    pred = []
    
    rf = RandomForestRegressor()
    rf.fit(data, target)
    
    predict = rf.predict(test)
    pred.extend(predict)

    for i in range (49) :
        rf = RandomForestRegressor()
        rf.fit(data, target)
        predict = rf.predict(test)
        pred = np.add(pred,predict)
        
    print pred/50
    
