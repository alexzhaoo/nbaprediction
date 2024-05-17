import pandas as pd
import numpy as np

filename = 'allStats.csv'

file = pd.read_csv(filename)


file.drop(['TEAM_ABBREVIATION', 'TEAM_ID', 'PLAYER_ID', 'SEASON_ID', 'LEAGUE_ID' ], axis=1, inplace=True)

file['PTS'] = file['PTS'] / file['GP']

