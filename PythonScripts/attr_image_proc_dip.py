# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 23:43:25 2021

@author: Ariel
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 04:43:12 2021

@author: Ariel
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 18:01:21 2021

@author: Ariel
"""

import os
import matplotlib.pyplot as plt
import matplotlib.image as img 
import matplotlib.colors as mcol
import numpy as  np
from PIL import Image
import random
#%%
filename='m58_attr_sm'
y_mod=134000
z_mod=1700
seis=img.imread('Images\%s.png' % filename)

seis=seis[63:652,228:1184,:] #Dip final

dims=seis.shape
#ypix_conv=dims[1]/81600
#ypix_conv=dims[1]/52601 #factor to convert distance in meters to pixels based on image size

y_pix=np.linspace(0,74500,dims[1])
z_pix=np.linspace(0,z_mod,dims[0])
yloc=np.zeros((dims[0],dims[1]))
zloc=np.zeros((dims[0],dims[1]))
seis_clean=seis
#col_filter=np.float32([0.0, 0.0, 0.0])
#for j in range(0,dims[1]):
#    for k in range(0,dims[0]):
#        chk=seis[k,j,:]
#        if (chk==col_filter).all()==True:
#            seis_clean[k,j,:]=[0, 0, 0]
#%% Converting RGB to int
seis_int=seis_clean[:,:,0]
for j in range(0,dims[1]):
    for k in range(0,dims[0]):
        seis_int[k,j]=0.299*seis_clean[k,j,0]+0.587*seis_clean[k,j,1]+0.114*seis_clean[k,j,2]
                        
        
#%% QC 

fig1,(ax1,ax3)=plt.subplots(2,sharex=True)        
ax1.imshow(seis)
ax3.imshow(seis_int,cmap='gray',vmin=0,vmax=1)
plt.xlabel('Pixels')
ax1.set_aspect(aspect=0.5)
ax3.set_aspect(aspect=0.5)
fig1=plt.gcf()
plt.show()
print(seis.shape)
#%% Data preparation
dims=seis_clean.shape
y_pix=np.linspace(40220,114720,dims[1])
z_pix=np.linspace(0,z_mod,dims[0])
yloc=np.zeros((dims[0],dims[1]))
zloc=np.zeros((dims[0],dims[1]))
 

for j in range(0,dims[1]):
    zloc[:,j]=0-z_pix
for k in range(0,dims[0]):  
    yloc[k,:]=y_pix
plt.contourf(yloc,zloc,seis_int,cmap='gray',vmin=0,vmax=1)
plt.show()
# # dipline
xx=40800*np.ones((dims[0]*dims[1]))
#data_out=np.stack((xx,np.flipud(yloc.flatten()),zloc.flatten(),seis_int.flatten()),axis=1)
data_out=np.stack((xx,yloc.flatten(),zloc.flatten(),seis_int.flatten()),axis=1)

#Save data
np.savetxt('%s_xyz3.txt'% filename,
           data_out,delimiter=',',
           fmt='%10.3f')

#%% Final Clean up 

#Random sampling
data_in=open('%s_xyz3.txt'% filename,'r').readlines()


with open('Attributes\%s_xyz_clean3.txt' % filename, 'w') as outfile:
    for line in data_in:
        check=line.strip().split(',')[3]
        check2=line.strip().split(',')[2]
        if check!='     0.000' and check2!='     0.000':
            outfile.write(line)
outfile.close()

data_clean=open('Attributes\%s_xyz_clean3.txt'% filename,'r').readlines()
full=len(data_clean)
samp_size=int(0.25*full) # set sample size of pixels
data_ran_samp=random.sample(data_clean,samp_size)
with open('Attr_ran10\%s_xyz_clean_ran3.txt' % filename, 'w') as outfile:
    outfile.write('#X,Y,Z,attr \n')
    for line in data_ran_samp:
        outfile.write(line)
outfile.close()
#%%
filename='m58_attr_sm'
data = np.genfromtxt('Attr_ran10\%s_xyz_clean_ran3.txt' % filename, delimiter=',')
num=data.shape[0]
xc=72.5*np.ones([1700,1])
zc=np.linspace(0,-1700,1700)
fig2,ax=plt.subplots(figsize=(7,2))
pts=plt.scatter(data[0::,1]/1000,data[0::,2],c=data[0::,3],s=1,cmap='ocean')
plt.plot(xc,zc,'--',linewidth=0.75,color='gray') #intersection of line 22
#ax.set_xlim(0,134)
ax.set_ylim(-1000,-200)
plt.title('m58- {} points'.format(num))
plt.xlabel('Distance [km]')
plt.ylabel('Depth [m]')
#cbar=fig2.colorbar(pts,orientation="horizontal", pad=0.2)
#cbar.ax.set_xlabel('Normalized amplitude', rotation=0)
plt.show()
fig2.savefig('Dipline_%s2.jpg'%filename,dpi=450,bbox_inches='tight')


