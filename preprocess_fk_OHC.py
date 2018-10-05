# Description : One hot encoding on feature_name

# INPUT :
# df : (pandas.dataframe) The dataframe we're working on
# feature_name : (string) The name of the feature to be OHCed
# dummy_na : (boolean) Activate dummy on NA values

# OUTPUT : 
# Returns df with the k-1 dummies and with feature_name dropped

def preprocess_fk_OHC (df, feature_name, dummy_na = False) :
    import pandas as pd
    dum_df = pd.get_dummies(df[feature_name], prefix = feature_name, drop_first = True, dummy_na = dummy_na)
    return pd.concat([df,dum_df], axis = 1).drop(feature_name, axis = 1)
