import numpy as np
import pandas as pd

filename = "datasets/all_seasons.csv"

df = pd.read_csv(filename)

# 1, 6, 7, 8, 10, 

# 10



mask = df.iloc[:,10] != 'Undrafted'

filtered = df[mask].copy()

filtered['draft_round'] = pd.to_numeric(filtered['draft_round'])

filtered['draft_number'] = pd.to_numeric(filtered['draft_number'])


filtered['ovrdraftpick'] = filtered['draft_round'] * filtered['draft_number']


filtered.drop(['draft_round','draft_number', 'useless', 'player_weight', 'college', 'country','team_abbreviation'], axis=1, inplace=True)

filtered['draft_year'] = pd.to_numeric(filtered['draft_year'])

filtered['season'] = filtered['season'].str[:4]

filtered['season'] = pd.to_numeric(filtered['season'])

rookieseasons = filtered[(filtered['draft_year'] == filtered['season']) | (filtered['draft_year'] == filtered['season'] + 1)]

rookieseasons.to_csv("newseasons.csv", index = False)



