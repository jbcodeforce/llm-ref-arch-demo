import pandas as pd
import sqlite3, io

'''
Take a excel file and extract the TA recommendation from the description column.
'''

def processDescription(description):
    description = description.replace("\n\n", "\n")
    description = description.replace("Description:", "\n### Description\n\n")
    description = description.replace("Alert Criteria", "### Alert Criteria\n\n")
    description = description.replace("Recommended Action", "### Recommended Action\n\n")
    description = description.replace("_x000D_", "\n")
 
    description = description.replace("Additional Resources", "### Additional Resources\n\n")
    return description

filename="./docs/all.xlsx"
# dfs is a dictionary of dataframes
dfs = pd.read_excel(filename, sheet_name=None)



output = "./docs/ta-recommendations.md"

f = open(output, "w")
for key in dfs.keys():
    df = dfs[key]
   
    title = df.columns[0]
    description = dfs[key].iloc[1,0]
    f.write("\n## " + title + "\n\n" + processDescription(description) + "\n")

f.close()