import math
import numpy as np


def step_1(x, type_attr, e_lower=None, e_upper=None):
    E = []
    if type_attr == 'Monotone1':
        for a in x:
            delta = max(x) - a
            E.append(delta)

    if type_attr == 'Monotone2':
        for a in x:
            delta = a - min(x)
            E.append(delta)

    if type_attr == 'Interval':
        for a in x:

            if e_lower <= a <= e_upper:
                delta = a - a
                E.append(delta)

            elif a < e_lower:
                delta = e_lower - a
                E.append(delta)

            elif a > e_upper:
                delta = a - e_upper
                E.append(delta)

            else:
                raise ValueError

    return E


def step_2(y, best_value=True):

    V = []
    if best_value:
        for a in y:
            v = max(y) - a
            V.append(v)
    else:
        for a in y:
            v = a - min(y)
            V.append(v)

    return V


def step_3(z):

    P = []

    for a in z:
        p = a/sum(z)
        P.append(p)

    return P


def comp_weights(x):
    # Calculating the compatibility weights
    comp_deg = []

    for a in range(len(x)):
        row_i = [g for g in x.iloc[a]]
        length = len(x.columns)
        comp_i = []

        for j in range(len(x)):
            if j == a:
                continue
            else:
                row_j = [f for f in x.iloc[j]]
                comp_ij = sum([row_i[k]*row_j[k] for k in range(length)])/\
                          (math.sqrt(sum([c**2 for c in row_i])) * math.sqrt(sum([b**2 for b in row_j])))
                comp_i.append(comp_ij)

        comp_deg.append(sum(comp_i))

    comp_weight = [r/sum(comp_deg) for r in comp_deg]

    print('The compatibility weights are: ', comp_weight)
    print()

    return comp_weight


def entropy_weights(x):
    # Calculating the entropy weights
    en_weights = []
    en_weight = []

    for a in range(len(x)):
        row_i = [g for g in x.iloc[a]]
        p_row = [(p*(np.log(p))) if p != 0 else 0 for p in row_i]
        h_i = -1*sum(p_row)/np.log(len(row_i))
        en_weights.append(1-h_i)

    for i in en_weights:
        en_weight.append(i/sum(en_weights))

    print('The entropy weights are: ', en_weight)
    print()

    return en_weight





