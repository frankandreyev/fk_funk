# Input :
# data -> "pandas" dataframe
# Output :
# cat <- names of the categorical columns
# num <- names of the numeric type columns

def split_catfloat(data) :
    cat = list()
    num = list()
    for col in data.columns :
        if( (data[col].dtype == 'float') | (data[col].dtype == 'int')) : num.append(col)
        else : cat.append(col)
    return cat, num
