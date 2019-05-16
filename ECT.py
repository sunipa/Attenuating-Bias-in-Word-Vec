import numpy as np
from scipy.spatial.distance import cosine,euclidean
from scipy.stats import spearmanr


def processList(l):
	for i in range(len(l)):
		l[i] = l[i].strip().lower()
	return l

def meanList(l):
	vec= [0] * 300
	for i in range(len(l)):
		vec = vec + X[wl.index(l[i])]
	return vec/float(len(l))

def cosine1(x, y):
	return np.dot(x,y.T)

def ect(mean1, mean2, wordlist):
	sim1=[0]*len(wordlist);sim2=[0]*len(wordlist)
	for i in range(0,len(wordlist)):
	
		sim1[i]=1-cosine(v1,A[wl.index(wordlist[i])]); sim2[i]=1-cosine(v2,A[wl.index(wordlist[i])])


	return spearmanr(sim1, sim2))
	
f1=open('gender1.txt','r')
x=f1.readlines()



##### Testing with professions #####

import json

A =  np.loadtxt('Enter numpy matrix with vectors (biased or debiased)')

#### Normalization (optional) ####
#for i in range(0,len(A)):
#	A[i] = A[i]/np.linalg.norm(A[i])

f1 = open('Enter corresponding word list','r')
wl = f1.readlines()

wl = processList(wl)

f1=open('maleNames.txt','r') #if you have debiased using names, put in gendered word list (man, he, father...) here
x=f1.readlines()
m1 = meanList(processList(x))

f1=open('femaleNames.txt','r') #if you have debiased using names, put in gendered word list (woman, she, mother...) here
x=f1.readlines()
m2 = meanList(processList(x))

with open('professions.json') as fj :
	data = json.load(fj)
wordset =  set()
for i in range(len(data)):
	data[i] = data[i][0]
	if data[i] in wl:
		wordset.add(data[i])

wordset = list(wordset)

def ect(mean1, mean2, wordlist):
	sim1=[0]*len(wordlist);sim2=[0]*len(wordlist)
	for i in range(0,len(wordlist)):
	
		sim1[i]=1-cosine(mean1,A[wl.index(wordlist[i])]); sim2[i]=1-cosine(mean2,A[wl.index(wordlist[i])])


	return spearmanr(sim1, sim2))

print (ect(m1,m2,wordset))
