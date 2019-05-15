import numpy as np

def projection(u,v): #u is any vector in the embedding, v is the bias direction
	u = u - np.dot(u,v)*v
	return u	
