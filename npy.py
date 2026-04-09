import numpy as np

def npy2to3(data):
    
    if isinstance(data, bytes):
        return data.decode('utf-8')
    arr = np.array(data)
    
    if arr.dtype.kind == 'S': 
        return arr.astype(str)
        
    return arr