import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError('List must contain nine numbers.')
  else:
    calculations = {'mean': None, 
                    'variance': None, 
                    'standard deviation': None,
                    'max': None,
                    'min': None,
                    'sum': None}

    v = np.array(list).reshape(3,3)

    temp = []
    temp.append(v.mean(axis=0).tolist())
    temp.append(v.mean(axis=1).tolist())
    temp.append(v.flatten().mean())
    calculations['mean'] = temp

    temp = []
    temp.append(v.var(axis=0).tolist())
    temp.append(v.var(axis=1).tolist())
    temp.append(v.flatten().var())
    calculations['variance'] = temp

    temp = []
    temp.append(v.std(axis=0).tolist())
    temp.append(v.std(axis=1).tolist())
    temp.append(v.flatten().std())
    calculations['standard deviation'] = temp

    temp = []
    temp.append(v.max(axis=0).tolist())
    temp.append(v.max(axis=1).tolist())
    temp.append(v.flatten().max())
    calculations['max'] = temp

    temp = []
    temp.append(v.min(axis=0).tolist())
    temp.append(v.min(axis=1).tolist())
    temp.append(v.flatten().min())
    calculations['min'] = temp

    temp = []
    temp.append(v.sum(axis=0).tolist())
    temp.append(v.sum(axis=1).tolist())
    temp.append(v.flatten().sum())
    calculations['sum'] = temp

    return calculations