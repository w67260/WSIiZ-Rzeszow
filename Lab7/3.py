import numpy as np
tab=np.zeros((3,3))
#print(tab)

#tab[1:,:2]=1
#tab[:,2]=1
#tab[:2,:]=1
#tab[:2,0]=1
tab[:2,[0,2]]=1
print(tab)