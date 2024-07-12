import numpy as np

def calculate(list):
    a = np.array(list)
    b = a.reshape((3,3))
    mean = [np.mean(b,axis = 0).tolist(), np.mean(b,axis = 1).tolist(), np.mean(a).tolist()]
    variance = [np.var(b,axis = 0).tolist(), np.var(b, axis = 1).tolist(), np.var(a).tolist()]
    std = [b.std(axis = 0).tolist(), b.std(axis = 1).tolist(), a.std().tolist()]
    max_val = [np.max(b, axis = 0).tolist(), np.max(b, axis = 1).tolist(), np.max(a).tolist()]
    min_val = [np.min(b, axis = 0).tolist(), np.min(b, axis = 1).tolist(), np.min(a).tolist()]
    sum_val = [np.sum(b, axis = 0).tolist(), np.sum(b, axis = 1).tolist(), np.sum(a).tolist()]

    calculations = {
        'mean' : mean,
        'variance' : variance,
        'standard deviation' : std,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }

    return calculations