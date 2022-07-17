from comp_en_func import csw

attr_list = ['Monotone2', 'Monotone2', 'Monotone2', 'Monotone2', 'Monotone1', 'Monotone1']

test2 = csw('test_data2.csv', type_attr=attr_list,
            headers=None, object_tobe_ranked='plan', objects_as_columns=False)
