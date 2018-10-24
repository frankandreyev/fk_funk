# switchMetoCat
# Input :
# threshold -> max threshold, if the number of values is greater than the threshold, then the numeric value stays numeric
# data -> pandas dataframe
# Output : returns the column names under the threshold in cat and the column names over the threshold in num

def split_switchMetoCat (threshold, data) :
    cat = list()
    num = list()
    for col in data.columns :
        if( (data[col].dtype == 'float') | (data[col].dtype == 'int')) :
            if(data[col].nunique() <= threshold) : cat.append(col)
            else : num.append(col)
    return cat, num
