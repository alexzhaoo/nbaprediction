import numpy as np
import pandas as pd

filename = "datasets/all_seasons.csv"
filename2 = "datasets/final_data.csv"
filename3 = "datasets/alltimegreats.csv"

df = pd.read_csv(filename)

# 1, 6, 7, 8, 10, 

# 10

namedf = pd.read_csv(filename2)


namedf['name'] = namedf['first'] + ' ' + namedf['last']

def checkAllstar(df,namedf,filename3):

    df3 = pd.read_csv(filename3)
    
    # result = pd.concat([df3.iloc[:, 0], namedf['name']], axis=1)

    mask = df.iloc[:, 0].isin(namedf['name'])

    df['isallstar'] = mask.astype(int)

    return df


mask = df.iloc[:,10] != 'Undrafted'

filtered = df[mask].copy()

filtered['draft_round'] = pd.to_numeric(filtered['draft_round'])

filtered['draft_number'] = pd.to_numeric(filtered['draft_number'])


filtered['ovrdraftpick'] = filtered['draft_round'] * filtered['draft_number']


filtered.drop(['draft_round','draft_number', 'useless', 'player_weight', 'college', 'country','team_abbreviation'], axis=1, inplace=True)

filtered['draft_year'] = pd.to_numeric(filtered['draft_year'])

filtered['season'] = filtered['season'].str[:4]

filtered['season'] = pd.to_numeric(filtered['season'])

rookieseasons = filtered.copy()


rookieseasons = rookieseasons[
    (rookieseasons['draft_year'].astype(float) + 1 == rookieseasons['season'].astype(float)) |
    (rookieseasons['draft_year'].astype(float) == rookieseasons['season'].astype(float))
]


rookieseasons.drop(['player_height', 'draft_year', 'ovrdraftpick', 'season'], axis=1, inplace=True)


finaldf = checkAllstar(rookieseasons, namedf, filename3)

finaldf.to_csv("newseasons.csv", index = False)



