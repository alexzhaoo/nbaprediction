import numpy as np
import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats



filename = "datasets/alltimegreats.csv"
filename2 = "datasets/newseasons.csv"

def comparingFiles(filename,filename2):
    df = pd.read_csv(filename)

    df2 = pd.read_csv(filename2)

    df.drop_duplicates(subset=df.columns[0], keep='first', inplace=True)

    mask = df.iloc[:, 0].isin(df2.iloc[:, 0])

    filtered = df[~mask]

    return filtered


newdf = comparingFiles(filename,filename2)

def getIDs(newdf):
    allnbaplayers = players.get_players()

    ids = []

    for ind in newdf.index:
        name = newdf['Players'][ind]

        bigfund = next((player for player in allnbaplayers if player["full_name"] == name), None)
        
        if bigfund:
            ids.append(bigfund['id'])
    return ids


idlist = getIDs(newdf)

def getStats(idlist):
    stats = []
    for id in idlist:
        career = playercareerstats.PlayerCareerStats(player_id = id)

        df = career.get_data_frames()[0]

        firstTwo = df.head(2)

        stats.append(firstTwo)


    combineddf  = pd.concat(stats,ignore_index= True, sort = False)

    combineddf = combineddf.dropna(axis=1, how='all')

    return combineddf


finaldf = getStats(idlist)

finaldf.to_csv("alltimegreatFirstTwoSeasons.csv",index = False)




















