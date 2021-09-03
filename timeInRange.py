# -*- coding: utf-8 -*-
"""
@author: Chris
"""
import pandas as pd
import datetime

pumpNumbers = ["2", "7", "10", "14", "16", "21", "24", "28"]

#imports formatted data
def getData(pumpNum):
    baseDirectory = "C:\\Users\\Chris\\OneDrive\\Masters\\Project\\Code\\data\\"
    pumpNumbers = ["2", "7", "10", "14", "16", "21", "24", "28"]
    if pumpNum not in pumpNumbers:
        print("error, invalid pump number")
    return pd.read_excel(baseDirectory + pumpNum + "RoundedGlucose.xlsx")



allPumps = {}

for pump in pumpNumbers:
    #target data, variableData
    glucoseData = getData(pump)
    print(pump + " GlucoseData:")
    print(glucoseData)
    
    valueSum = 0
    less3_9 = 0
    greater10 = 0
    inTarget = 0
    for i in range(len(glucoseData)):
        value = glucoseData["Glucose Value (mmol/L)"][i]
        valueSum += value
        if value < 3.9:
            less3_9 += 1
        elif value > 10:
            greater10 += 1
        else:
            inTarget += 1
        
    
    percentageLess = round((100 / len(glucoseData)) * less3_9, 2)
    percentageGreater = round((100 / len(glucoseData)) * greater10, 2)
    percentageTarget = round((100 / len(glucoseData)) * inTarget, 2)
    average = round(valueSum / len(glucoseData), 2)
    
    allPumps[pump] = [average, percentageLess, percentageGreater, percentageTarget]
    
    print(percentageLess)
    print(percentageGreater)
    print(percentageTarget)

print(allPumps)

df = pd.DataFrame.from_dict(allPumps, orient = "index", 
                            columns = ["Average (mmol/l)", "Time Glucose < 3.9 mmol/l", 
                                       "Time glucose > 10 mmol/l", "Time in Target [3.9 - 10] mmol/l"])
print(df)

df.to_csv("C:\\Users\\Chris\\OneDrive\\Masters\\Project\\Code\\data\\timeInRangeValues.csv", index = True)