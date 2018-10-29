# feature : string feature
# threshold : percentage of non outlier

def outliers_value (feature, threshold = 99) :
    tmp = full_df.groupby(feature)[feature].agg('count')
    out = tmp.cumsum().apply(lambda x : (x/tmp.sum())*100)
    return out[out < threshold]
barplot_var = ['assists','boosts','headshotKills','vehicleDestroys','teamKills','roadKills','weaponsAcquired']
hist_var = ['heals','killPoints','kills','killStreaks',
            'longestKill','rideDistance','revives','swimDistance',
            'walkDistance','winPoints']
other_var = ['killPlace','numGroups']

# Example :
#for i in barplot_var :
#    print(outliers_value(i))
