import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import requests

from io import StringIO




print('paste values or pass empty field to request from web server: http://ha123blix.eu.pythonanywhere.com/')
val = ""
#val = input('paste here:')

if val == "":
  r =requests.get('http://ha123blix.eu.pythonanywhere.com/api1/history')
  val = r.text


val = val.replace(' ', '\n')

data = np.genfromtxt(StringIO(val), delimiter=";", skip_header=1, skip_footer=0, names=['x', 'y', 'z'])

print (data)

x_=[]
i = 0;
for k in data:
  x_.append(i)
  i = i +1

temp_1 = 0

# filter

for index, temp in enumerate(data['x']):
  
  if(temp == 85):
    data['x'][index] = temp_1;
  else:
    temp_1 = temp
    
  if(temp <= -10):
    data['x'][index] =-10;

for index, y in enumerate(data['y']):
  rep = 5
  if(index >=rep ):
    sum=0
    for k in range(rep):
      sum =sum + data['y'][index-k]
    data['y'][index] = sum/rep

for index, z in enumerate(data['z']):
  rep = 5
  if(index >=rep ):
    sum=0
    for k in range(rep):
      sum =sum + data['z'][index-k]
    data['z'][index] = sum/rep



plt.rcParams["figure.figsize"] = (24, 6)
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title("Zeitreihe")    
ax1.set_xlabel('time')
ax1.set_ylabel('value')

ax1.plot(x_, data['x']*10, color='r', label='the data')
ax1.plot(x_, data['y'], color='g', label='the data' )
ax1.plot(x_, data['z'], color='b', label='the data' )
plt.savefig("history/graph.png")
