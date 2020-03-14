#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib
# matplotlib.use('Agg')
get_ipython().run_line_magic('matplotlib', 'notebook')
import numpy as np
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
canvas1.pack()

def getExcel ():
    global data
    global xyz,lat,vel 
    import_file_path = filedialog.askopenfilename()
    data = pd.read_excel (import_file_path)
    xyz = pd.DataFrame(data, columns= ['X pos (m)','Y pos (m)','Z pos (m)'])
    vel = pd.DataFrame(data, columns= ['X vel (m/s)','Y vel (m/s)','Z vel (m/s)'])
    lat = pd.DataFrame(data, columns= ['Latitude (deg)','Longitude (deg)'])
    
    
browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_Excel)

root.mainloop()
xyz=xyz.reset_index().values
vel=vel.reset_index().values
lat=lat.reset_index().values

x=[]
y=[]
z=[]
xvel=[]
yvel=[]
zvel=[]
latitude=[]
longitude=[]
for i in range(len(xyz)):
    x.append(xyz[i][1])
    y.append(xyz[i][2])
    z.append(xyz[i][3])
    xvel.append(vel[i][1])
    yvel.append(vel[i][2])
    zvel.append(vel[i][3])
    latitude.append(lat[i][1])
    longitude.append(lat[i][2])
t=np.linspace(1,len(xyz),len(xyz))
    
plt.figure()
plt.subplot(311)
plt.plot(t,x)
plt.xlabel('Time')
plt.ylabel('X-Coordinates')

plt.subplot(312)
plt.plot(t,y)
plt.xlabel('Time')
plt.ylabel('Y-Coordinates')

plt.subplot(313)
plt.plot(t,z)
plt.xlabel('Time')
plt.ylabel('Z-Coordinates')
plt.show()

plt.figure()
plt.subplot(311)
plt.plot(t,xvel)
plt.xlabel('Time')
plt.ylabel('X-Velocity')

plt.subplot(312)
plt.plot(t,yvel)
plt.xlabel('Time')
plt.ylabel('Y-Velocity')

plt.subplot(313)
plt.plot(t,zvel)
plt.xlabel('Time')
plt.ylabel('Z-Velocity')
plt.show()

plt.figure()
plt.plot(latitude,longitude)
plt.show()


# In[ ]:




