from comp_en_func import *
from transformation import *
import math
import numpy


class CompatibilityEntropyRanking:
    def __init__(self, file_name, type_attr, e_lower=None, e_upper=None, best_value=True,
                 headers=None, objects_as_columns=True, object_tobe_ranked=''):
        self.file_name = file_name
        self.type_attr = type_attr
        self.e_lower = e_lower
        self.e_upper = e_upper
        self.best_value = best_value
        self.headers = headers
        self.objects_as_columns = objects_as_columns
        self.objects2 = object_tobe_ranked
        self.mat1 = None
        self.comp_w = None
        self.ent = None

    def normalization(self):
        df = pd.read_csv(self.file_name, header=self.headers)
        print('The Raw data: ')
        print(df, '\n')
        # Applying the Normalization Steps :
        if not self.objects_as_columns:
            df = df.transpose()
        h = []
        for i in range(len(df)):
            x = df.iloc[i]
            attr_type = self.type_attr[i]

            e = step_1(x, attr_type, self.e_lower, self.e_upper)
            normalized_v = step_2(e, best_value=self.best_value)

            normalized_p = step_3(normalized_v)
            h.append(normalized_p)

        mat = pd.DataFrame(h)
        self.mat1 = mat
        print('The table of normalized values: \n', mat)
        print()

    def compatibility(self):
        self.comp_w = comp_weights(self.mat1)
        return self.comp_w

    def entropy(self):
        self.ent = entropy_weights(self.mat1)
        return self.ent

    def evaluate(self):
        mat = self.mat1
        length = len(mat.columns)

        mat['comp'] = self.comp_w
        mat['entropy'] = self.ent

        mat['net_weights'] = mat['comp'] / 2 + mat['entropy'] / 2

        final_weights = mat['net_weights']

        print('The net weights are:\n', mat['net_weights'])

        print()

        # print(sum(mat['net_weights']))
        # Generating the net weights
        for d in range(length):
            de = str(d)
            final = 'final' + de
            mat[final] = mat[d] * mat['net_weights']

        # Generating the final scores
        final_scores = []
        for col in (mat.columns[-length:]):
            final_score = sum(mat[col])
            final_scores.append(final_score)

        # print('Final Scores:{}'.format(final_scores))
        # print()

        names = []
        for d in range(1, length + 1):
            names.append(self.objects2 + str(d))

        # creating the scores table
        results = pd.DataFrame(final_scores, index=names)
        print('The final scores are:\n', results)
        print()

        # Displaying the objects with ranks
        results['rank'] = results.rank(ascending=False)
        print('The ranked results are:\n', results)
        print()
