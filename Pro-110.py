import csv
import pandas as pd
import plotly.express as px
import plotly.figure_factory as pf
import statistics as st
import plotly.graph_objects as pg
import random as r

file = input("File name : ")
column = input("Column name : ")
f = pd.read_csv(file)
df = f[column].tolist()
print(df)

mean = st.mean(df)
print(mean)
deviation = st.stdev(df)
print(deviation)

f1 = f["Unit Price"].tolist()


def randomSet(counter):
  dataSet = []
  for i in range(0,counter):
    randomN = r.randint(1,len(f1) - 1)
    value = f1[randomN]
    dataSet.append(value)
  mean = st.mean(dataSet)
  return mean

def showFig(meanList):
  f1 = meanList
  mean = st.mean(f1)
  deviation = st.stdev(f1)
  print(mean)
  print(deviation)
  fig = pf.create_distplot([f1],["temp"],show_hist = False)
  fig.add_trace(pg.Scatter(x = [mean,mean],y = [0,1],mode = "lines",name= "mean"))
  fig.show()

def main():
  meanList = []
  for i in range(0,1000):
    rmean = randomSet(100)
    meanList.append(rmean)
  showFig(meanList)

main()
