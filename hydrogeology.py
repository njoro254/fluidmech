import scipy.integrate as sc
import math

#Q*(integral(r^2*S/4Tt)infinity[e-u/u du])/(4*math.pi*T)

m1,m2=72,240
S,T=10**-5,10**-2
s=0.15*(sc.quad(lambda u: math.exp(-u)/u, (112.5*S)/(4*T*72), math.inf)[0])/(4*math.pi*T)


#theis solution

from numpy import *
import matplotlib.pyplot as plt


sTx72= array([0.14175, 1.14271, 8.67903,59.346])
sTx240= array([0.15612,  1.28642, 10.1158, 73.6861])
sTy72= array([0.141755,  0.141755,  0.001967,  0.000224])
sTy240= array([0.15612, 0.018361,  0.002110, 0.000238])
sS72= array([8.67904,  11.4271,  14.1756,  16.9241])
sS240= array([10.1159, 12.8642, 15.6127, 18.3612])
x1=array([4,3,2,1])
x2=array([4,3,2,1])
x3=array([5,6,7,8])

fig = plt.figure()
#ax1 = fig.add_subplot(311)
#ax1.plot(x1, sTx72);
#ax2 = ax1.twinx()
#ax2.plot(x1, sTx240, 'r');
#ax1.set_ylabel('drawdown metres');
#ax1.set_xlabel('Transmissivity X');


#ay1 = fig.add_subplot(312)
#ay1.plot(x2, sTy72);
#ay2 = ay1.twinx()
#ay2.plot(x2, sTy240, 'r');
#ay1.set_ylabel('drawdown metres');
#ay1.set_xlabel('Transmissivity Y');

#az1 = fig.add_subplot(313)
#az1.plot(x3, sS72);
#az2 = az1.twinx()
#az2.plot(x3, sS240, 'r');
#az1.set_ylabel('drawdown metres');
#az1.set_xlabel('Storativity');
#plt.show()


errTx72= array([97.2201, 77.5939, -70.177, -1063.6])
errTx240= array([98.553, 88.089, 6.3351, -582.27])
errTy72= array([97.2201,  99.668, 99.9614, 99.9956])
errTy240= array([98.5537, 99.8299,  99.9804, 99.9977])
errS72= array([-70.177,  -124.061,  -177.953,  -231.845])
errS240= array([6.335,  -19.112,  -44.562,  -70.0111])



ax1 = fig.add_subplot(311)
ax1.plot(x1, errTx72);
ax2 = ax1.twinx()
ax2.plot(x1, errTx240, 'r');
ax1.set_ylabel('error');
ax1.set_xlabel('Transmissivity X');

ay1 = fig.add_subplot(312)
ay1.plot(x2, errTy72);
ay2 = ay1.twinx()
ay2.plot(x2, errTy240, 'r');
ay1.set_ylabel('error');
ay1.set_xlabel('Transmissivity Y');

az1 = fig.add_subplot(313)
az1.plot(x3, errS72);
az2 = az1.twinx()
az2.plot(x3, errS240, 'r');
az1.set_ylabel('error');
az1.set_xlabel('Storativity');
plt.show()
