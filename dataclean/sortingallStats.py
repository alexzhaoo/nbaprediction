import pandas as pd
import numpy as np

filename = 'datasets/allStats.csv'

file = pd.read_csv(filename)


file.drop(['TEAM_ABBREVIATION', 'TEAM_ID', 'PLAYER_ID', 'SEASON_ID', 'LEAGUE_ID', 'FullName' , 'PLAYER_AGE' ], axis=1, inplace=True)


file.to_csv("allStatsFiltered.csv", index = False)

