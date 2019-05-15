import numpy as np

def projection(u,v): #u is any vector in the embedding, v is the bias direction
	u = u - np.dot(u,v[0])*v[0] - np.dot(u,v[1])*v[1]
	return u	
