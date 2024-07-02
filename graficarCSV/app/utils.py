def getInfoPlayersGameGraph(playerDict):
    infoPlayerDict = {
        'levelPlayer':int(playerDict['Level']),
        'killsPlayer':int(playerDict['Kills']),
        'deathsPlayer': int(playerDict['Deaths']),
        'assistsPlayer': int(playerDict['Assists']),
    }
    labels = infoPlayerDict.keys()
    values= infoPlayerDict.values()
    return labels, values

def getDictPlayer (data, playerName):
    result = list(filter(lambda item: item['Player']==playerName,data))
    return result