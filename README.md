# Multi-attribute decision making by combining probabilty distributions based on compatibilty and entropy
Function that demonstrates ranking algorithm based on compatibility and entropy weights.

It ranks any number of decision objects based on some decision attributes. The decision attributes may be of monotone, interval or extreme point type.

This function takes any dataframe, along with information on the types of the various decision attributes in the data, and displays scores for each of the decision object. These scores denote the 'ideal-ness' of each decision object. The higher the score, the more the given data supports the selection of the decision object in question.

Original Paper discussing ranking algorithm: https://link.springer.com/article/10.1007/s10489-020-01738-9

# 'comp_en_class' contains class:

>CompatibilityEntropyRanking(file_name, type_attr, e_lower=None, e_upper=None, best_value=True, headers=None, objects_as_columns=True, object_tobe_ranked='')
                                                         
## Parameters:                                                            
>1. file_name: path of .csv file containing dataset with decision objects and attributes.  
>2. type_attr: iterable (list or tuple) containing the type of each decision attribute as a string. example: ('Monotone1', 'Monotone2',
                                                                                                     'Interval1', 'Interval2',
                                                                                                     'Extreme1', 'Extreme2')      
>3. e_lower: lower limit of interval, if a given attribute has interval type  
>4. e_upper: upper limit of interval, if a given attribute has interval type  
>5. best_value: bool, whether a given attribute has best value at the max point or interval  
>6. header:   
>7. objects_as_columns: bool, whether the decision objects comprise the columns of the input data  
>8. objects_tobe_ranked: the names of the decision objects (plan, scheme, etc.)  

### Types of decision attributes:   
   >1) Monotone type 1 (or type 2) where the attribute is more optimal when the value is largest (or smallest),  
   >2) Interval type 1 (or type 2) where the attribute has the best (or worst) impact when it lies in a certain interval,  
   >3) Extreme point type 1 (or type 2) where the attribute has best (or worst) impact at a partiular value, which is not a maximum or minimum value  

## Methods: 







