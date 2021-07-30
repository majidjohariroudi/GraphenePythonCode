#majid johari roudi
#8 amordad 1400
import matplotlib.pyplot as plt
import math
n ,m = 10 , 8
a = math.cos(math.pi/3) ; b = math.sin(math.pi/3)
x = [] ; y = [] 
for j in range(m):
	for i in range(n):
		x.append(3 * i * a)
		y.append(i* b + 2 * j *b)
		x.append(3 * i * a + a)
		y.append(2 * j * b + ( i + 1 ) * b)
plt.scatter(x,y,s=20,marker='o',color='g')
plt.savefig('graphene.pdf')
plt.show()