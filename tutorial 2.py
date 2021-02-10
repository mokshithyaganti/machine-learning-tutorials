import numpy as np
import matplotlib.pyplot as plt
x= np.array([1,2,3])
z=np.array([1.2,1.9,3.2])
import matplotlib.pyplot as plt
x= np.array([1,2,3])
z=np.array([1.2,1.9,3.2])
def values(x,z):
	A=x.sum()
	B=z.sum()
	C=(x*x).sum()
	D=(z*z).sum()
	E=len(x)
	w0=(C*B-A*D)/(C*E-A*A)
	w1=(B-(E*w0))/A
	return w1,w0
slope,intercept=values(x,z)
final_values=[slope*i+ intercept for i in x]

plt.scatter(x,z)
plt.plot(x,z,'y*')
plt.plot(x,final_values,'c')
plt.show()
