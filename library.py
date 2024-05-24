import numpy as np


def compute_t_terms(xi,yi):
    """This function yields a time sampling for the dots cloud of which coordinates are (xi,yi) couples."""
    N = len(xi)
    ti = np.zeros_like(xi)
    ti[0] = 0
    for i in range(1,N):
        d = np.sqrt((xi[i]-xi[i-1])**2+(yi[i]-yi[i-1])**2)
        ti[i] = ti[i-1] + d
    return ti

def lagrange_interpolation(xi,yi,ti,t):
    """This function computes the Lagrange polynomials value in t and returns the coordinates of the 
    interpolating corresponding polynomial."""
    N = len(xi)
    x,y = 0,0
    for i in range(N):
        Li = 1
        for j in range(N):
            if j != i:
                Li *= (t-ti[j])/(ti[i]-ti[j])
        x += Li*xi[i]
        y += Li*yi[i]
    return x,y