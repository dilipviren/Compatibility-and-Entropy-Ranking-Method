from transformation import step_1, step_3, step_2, comp_weights, entropy_weights
import pandas as pd


def csw(file_name, type_attr, e_lower=None, e_upper=None, best_value=True,
        headers=None, objects_as_columns=True, object_tobe_ranked=''):

    df = pd.read_csv(file_name, header=headers)
    print('The Raw data: ')
    print(df, '\n')
    # Applying the Normalization Steps :
    if not objects_as_columns:
        df = df.transpose()
    h = []
    for i in range(len(df)):
        x = df.iloc[i]
        attr_type = type_attr[i]

        e = step_1(x, attr_type, e_lower, e_upper)
        normalized_v = step_2(e, best_value=best_value)

        normalized_p = step_3(normalized_v)
        h.append(normalized_p)

    mat = pd.DataFrame(h)

    print('The table of normalized values: \n', mat)
    print()

    # Generating the Compatibility and Entropy weights
    comp_matrix = comp_weights(mat)
    entropy_matrix = entropy_weights(mat)

    length = len(mat.columns)

    mat['comp'] = comp_matrix
    mat['entropy'] = entropy_matrix

    mat['net_weights'] = mat['comp']/2 + mat['entropy']/2

    global final_weights
    final_weights = mat['net_weights']

    print('The net weights are:\n', mat['net_weights'])

    print()

    # print(sum(mat['net_weights']))
    # Generating the net weights
    for d in range(length):
        de = str(d)
        final = 'final'+de
        mat[final] = mat[d]*mat['net_weights']

    # Generating the final scores
    final_scores = []
    for col in (mat.columns[-length:]):
        final_score = sum(mat[col])
        final_scores.append(final_score)

    # print('Final Scores:{}'.format(final_scores))
    # print()

    names = []
    for d in range(1, length+1):
        names.append(object_tobe_ranked+str(d))

    # creating the scores table
    results = pd.DataFrame(final_scores, index=names)
    print('The final scores are:\n', results)
    print()

    # Displaying the objects with ranks
    results['rank'] = results.rank(ascending=False)
    print('The ranked results are:\n', results)
    print()














