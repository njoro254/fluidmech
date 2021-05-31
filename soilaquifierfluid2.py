import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np



fig = plt.figure()
plt.figure(figsize=(9,9))



x=[0, 9.0, 90, 4.8, 2.4, 0]
y=[0, 0, 6.0, 6.0, 9.0, 0]






gridsize=[6, 12, 24, 48, 72, 96]
changeingridsize=[1.5,0.75,0.375,0.1875,0.125,0.09375]
prevequipotentialfergridsize=[6.75, 6.75, 6.75, 6.75, 6.75, 6.75]

#for all grid sizes
#3,0.05=(6.75-6)/x tangent of 30km section versus 67.5km point
#headchange=((changeingridsize)*0.5)/30 

headchange=[0.025,0.0125,0.00625,0.003125,0.002083, 0.0015625]
err=np.log(headchange)



#grid head=2500-125
#=2375m

#Hfine-Hgrid=2.418-2.375
#=0.043

#for all values except 72 log error=0
#for 72 total head=43*no of equipotentials
#=0.086





 




#for 2418
#equipotential sizes,by2,head error
#1.5,3,0
#0.75,1.5,0 
#0.375,0.75,0
#0.1875,0.375,0
#0.125,0.35,0.0086
#0.09375,0.1875,0


#for Q, if no change in head the k.h=0



#flow lines interpolation/spline at specific points

#meshgrid wih range of values with background trapezium

m=list(np.arange(0,9,0.09375)) #for 96
l1=m
m,l1=np.meshgrid(m,l1)

n=list(np.arange(0,9,0.125)) #for 72
l2=n
[n,l2]=np.meshgrid(n,l2)
	

o=list(np.arange(0,9,0.1875))#for 48
l3=o
[o,l3]=np.meshgrid(o,l3)

p=list(np.arange(0,9,0.375)) #for 24
l4=p
[p,l4]=np.meshgrid(p,l4)
	
q=list(np.arange(0,9,0.75)) #for 12
l5=q
[q,l5]=np.meshgrid(q,l5)

r= list(np.arange(0,9,1.5)) #for 6
l6=r
[r,l6]=np.meshgrid(p,l6)
	


ax1=fig.add_subplot(111, aspect='equal')
#ax1=fig.add_subplot(r,l6, color='royalblue')
ax1.plot(r,l6)
# color='royalblue')


#gridsize=size(F)

f=ax1.add_patch(patches.Polygon(xy=list(zip(x,y)),fill=False))
#plt.show()


#contour


ax=fig.add_subplot(111, aspect='equal')
x1 = np.linspace(0, 15, 90)
x2 = np.linspace(0, 7.5, 90)
x3 = np.linspace(0, 37.5, 90)
x4 = np.linspace(0, 18.75, 90)
x5 = np.linspace(0, 12.5, 90)
x6 = np.linspace(0, 0.9375, 90)
y1 = np.linspace(0, 15, 90)
y2 = np.linspace(0, 7.5, 90)
y3 = np.linspace(0, 3.75, 90)
y4 = np.linspace(0, 1.875, 90)
y5 = np.linspace(0, 1.25, 90)
y6 = np.linspace(0, 0.9375, 90)

ax.plot(x1,y1)
ax.plot(x2,y2)
ax.plot(x3,y3)
ax.plot(x4,y4)
ax.plot(x5,y5)
ax.plot(x6,y6)
#plt.show()


#1.5,3,0
#0.75,1.5,0 
#0.375,0.75,0
#0.1875,0.375,0
#0.125,0.35,0.0086
#0.09375,0.1875,0

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.contour(X, Y, Z, colors='black');



