import pandas as pd
from pandas.core.dtypes.missing import na_value_for_dtype
from pandas.core.frame import DataFrame
from pandas.core.indexes.base import Index, ensure_index


# File_Name, Sheet_Name
data = pd.read_excel('multi-column-sort.xlsx', sheet_name='Sheet1')

# Blank dictionary
dfcreator = {}

#loop based on first column items
for i in range(data[data.columns[0]].shape[0]):
    #create blank list
    dfcreator[i] = []
    #convert series to list
    for j in data.iloc[i, 1:].to_list():
        #ignore null and not available
        if pd.isna(j):
            continue
        elif pd.isnull(j):
            continue
        else:
            dfcreator[i].append(j)
#Sort arrays inside dictionary
for i in dfcreator:
    dfcreator[i].sort()
#convert dictionary to dataframe, orient=index to avoid Not Equal array size error
df = pd.DataFrame.from_dict(dfcreator, orient='index')
#export Dataframe to excel
with pd.ExcelWriter('sorted_file.xlsx', engine='xlsxwriter', engine_kwargs={'options': {'strings_to_numbers': True}}) as writer:
    df.to_excel(writer, index=False, header=False)
