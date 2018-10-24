# switchMetoCat
# Input :
# threshold -> max threshold, if the number of values is greater than the threshold, then the numeric value stays numeric
# num_data -> contains a dataframe with numeric variables only
# Output : returns the column names under the threshold in cat and the column names over the threshold in num

def split_switchMetoCat(threshold = 10, data) :
    cat = list()
    num = list()
    for col in data.columns :
        if( (data[col].dtype == 'float') | (data[col].dtype == 'int')) : num.append(col)
        else : cat.append(col)
    return cat, num
