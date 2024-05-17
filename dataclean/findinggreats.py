import numpy as np
import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import requests
import time


filename = "datasets/alltimegreats.csv"
filename2 = "datasets/newseasons.csv"

filename3 = "datasets/final_data.csv"
filename4 = "datasets/alltimegreats.csv"


namedf = pd.read_csv(filename3)


namedf['name'] = namedf['first'] + ' ' + namedf['last']

def checkAllstar(df,namedf,filename3):

    df3 = pd.read_csv(filename3)
    
    # result = pd.concat([df3.iloc[:, 0], namedf['name']], axis=1)

    mask = df['FullName'].isin(namedf['name'])

    df['isallstar'] = mask.astype(int)

    return df


def removingDuplicates(filename,filename2):
    df = pd.read_csv(filename)

    df2 = pd.read_csv(filename2)

    df.drop_duplicates(subset=df.columns[0], keep='first', inplace=True)

    mask = df.iloc[:, 0].isin(df2.iloc[:, 0])

    filtered = df[~mask]

    return filtered


newdf = removingDuplicates(filename,filename2)


def getIDs():
    allnbaplayers = players.get_players()

    ids = []
    playernames = []

    for player in allnbaplayers:
        ids.append(player['id'])
        playernames.append(player['full_name'])

    return ids , playernames



def getStats(idlist):
    stats = []
    for id in idlist:
        max_retries = 3
        retry_interval = 5  
        for attempt in range(max_retries):
            try:
                career = playercareerstats.PlayerCareerStats(player_id=id)
                df = career.get_data_frames()[0]
                firstTwo = df.head(2)
                stats.append(firstTwo)
                break  
            except requests.exceptions.ReadTimeout:
                if attempt < max_retries - 1:
                    print("Timeout occurred. Retrying after {} seconds...".format(retry_interval))
                    time.sleep(retry_interval)
                else:
                    print("Max retries exceeded for player ID {}. Skipping...".format(id))
                    break
    combineddf = pd.concat(stats, ignore_index=True, sort=False)
    combineddf = combineddf.dropna(axis=1, how='all')
    return combineddf


idlist , playerlist = getIDs()

playernames = pd.DataFrame(playerlist, columns=['FullName'])
playernames['PLAYER_ID'] = idlist

finaldf = getStats(idlist)

finaldf = pd.merge(finaldf, playernames, on='PLAYER_ID')

finaldf = checkAllstar(finaldf,namedf,filename4 )

filtered = finaldf.copy()
 

filtered['SEASON_ID'] = filtered['SEASON_ID'].str[:4]  

filtered['SEASON_ID'] = pd.to_numeric(filtered['SEASON_ID'])  



filtered = filtered[filtered['SEASON_ID'] >= 1981]  




filtered.to_csv("allStats.csv",index = False)


















