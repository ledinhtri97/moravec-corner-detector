import numpy as np

def neighbors(arr,x,y,n=3):
	''' Given a 2D-array, returns an nxn array whose "center" element is arr[x,y]'''
	arr=np.roll(np.roll(arr,shift=-x+1,axis=0),shift=-y+1,axis=1)
	return arr[:n,:n]

im = [[0, 0, 0, 0, 0],
	[0, 1, 0, 0, 0],
	[0, 1, 1, 0, 0],
	[0, 1, 1, 1, 0],
	[0, 0, 0, 0, 0]]

im = np.asarray(im)

# print(im)

shifts = [[1, 0], [1, 1], [0, 1], [-1, 1]]

point = (1, 1)

window = neighbors(im, 2, 2)

E = []

for shift in shifts:
	wdShift = neighbors(im, point[0] + shift[1], point[1] + shift[0])
	subWd = np.power(wdShift - window, 2)
	E.append(np.sum(subWd));
		
print(E)
		