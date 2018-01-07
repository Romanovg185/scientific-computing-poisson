import numpy as np

N = 5
h = 1/N

## Making the matrix
def tridiag(N, a=-1, b=2, c=-1):
	al = [a for _ in range(N-1)]
	bl = [b for _ in range(N)]
	cl = [c for _ in range(N-1)]

	return np.diag(al, -1) + np.diag(bl, 0) + np.diag(cl, 1)

def make_matrix(dim):
    M = 1/(h**2)*np.kron(tridiag(N-1), np.eye(N-1)) + 1/(h**2)*np.kron(np.eye(N-1), tridiag(N-1))
    O = 1/(h**2)*np.kron(M, np.eye(N-1)) + 1/(h**2)*np.kron(np.eye(N-1), M)
    if dim == 2:
        return M
    else:
        return O

## Making the right-hand vector
def apply_function_on_meshgrid_2D():
    x = [(i+1)/N for i in range(N-1)]
    xes, ys = np.meshgrid(x,x)
    f = (xes**2 + ys**2)*np.sin(xes*ys)
    return f.flatten()

def apply_function_on_meshgrid_3D():
    x = [(i+1)/N for i in range(N-1)]
    zs, ys, xes = np.meshgrid(x,x,x, indexing='ij')
    f = (xes**2 + ys**2 + zs**2) * np.sin(xes*ys*zs)
    return f.flatten()

def make_righthand_vector(dim):
    if dim == 2:
        return apply_function_on_meshgrid_2D()
    else:
        return apply_function_on_meshgrid_3D()
