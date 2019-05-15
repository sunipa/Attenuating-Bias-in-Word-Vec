import numpy as np

list1 = open('maleNames.txt','r');
list2 = open('femaleNames.txt','r');

list1 = list1.readlines(); 
list2 = list2.readlines()

X = np.loadtxt('Enter model name here')
wl = open('Enter corresponding word list name here','r')
wl = wl.readlines()



def processList(l):
	for i in range(len(l)):
		l[i] = l[i].strip().lower()
	return l
def meanList(l):
	vec= [0] * 300
	for i in range(len(l)):
		vec = vec + X[wl.index(l[i])]
	return vec/float(len(l))

wl = processList(wl)
Two_means = meanList(processList(list1)) - meanList(processList(list2))
Two_meansDir = Two_means/np.linalg.norm(Two_means)
