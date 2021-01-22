import plotly.figure_factory as pff
import statistics 
import random 
import pandas as pd
import csv
import plotly.graph_objects as go
df = pd.read_csv("C:/Users/HOME/3D Objects/C-110/data.csv")
data = df["temp"].tolist()
mean = statistics.mean(data)
standarddev = statistics.stdev(data)
#print(mean)
#print(standarddev)
#to find out mean and standard devation of 100data points
dataset = []
for i in range(0,100):
    randindex = random.randint(0,len(data))
    value = data[randindex]
    dataset.append(value)
samplingmean = statistics.mean(dataset)
standarddeviation = statistics.stdev(dataset)
#print(mean)
#print(standarddeviation)
#function to get a mean of given data samples
def randomsetmean(counter):
    dataset = []
    for i in range(0,counter):
        randindex = random.randint(0,len(data)-1)
        value = data[randindex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
def showfig(meanlist):
    df = meanlist
    mean = statistics.mean(df)
    fig = pff.create_distplot([df],["temp"],show_hist = False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()
def setup():
    meanlist = []
    for i in range(0,1000):
        setmean = randomsetmean(100)
        meanlist.append(setmean)
    showfig(meanlist)
    mean = statistics.mean(meanlist)
    print("mean of sampling distribution:", mean)
setup()        
def standarddeviation():
    meanlist = []
    for i in range(1,1000):
        setofmean = randomsetmean(100)
        meanlist.append(setofmean)
    standarddeviation = statistics.stdev(meanlist)
    print("standard deviation of sampling distribution:", standarddeviation)
standarddeviation()        
     