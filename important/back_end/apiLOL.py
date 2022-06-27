import os
from dotenv import load_dotenv
import urllib.request
import urllib.parse
import json

load_dotenv()
key = "?api_key=" + str(os.getenv("RIOT_API_KEY"))
#key = "?api_key=RGAPI-e274cd7b-3d0d-4449-b114-faddfefb2b27"
base_request = "https://br1.api.riotgames.com"

def IDbySummoner(Summoner):

    Summoner = urllib.parse.quote(Summoner)

    final_resquest = base_request+"/lol/summoner/v4/summoners/by-name/"+Summoner+key
    JsonObj = urllib.request.urlopen(final_resquest)
    data = json.load(JsonObj)
    
    return data['id']

def PuuIDbyEsID(esID):

    endPoint = base_request+"/lol/summoner/v4/summoners/"+esID+key
    JsonObj = urllib.request.urlopen(endPoint)
    data = json.load(JsonObj)

    return data['puuid']

def JsonSummonerByID(esID):

    endPoint = base_request+'/lol/summoner/v4/summoners/'+esID+key
    jsonObj = urllib.request.urlopen(endPoint)
    return json.load(jsonObj)

def JsonEloByID(esID):

    endPoint = base_request+'/lol/league/v4/entries/by-summoner/'+esID+key
    jsonObj = urllib.request.urlopen(endPoint)
    return json.load(jsonObj)

def JsonHistoricoByPuuID(puuID):
    
    Ebase_request = "https://americas.api.riotgames.com"
    endPoint = Ebase_request+"/lol/match/v5/matches/by-puuid/"+puuID+"/ids"+key
    jsonObj = urllib.request.urlopen(endPoint)
    return json.load(jsonObj)

def JsonPartidaByMatchID(mId):
    
    Ebase_request = "https://americas.api.riotgames.com"
    endPoint = Ebase_request+"/lol/match/v5/matches/"+mId+key
    jsonObj = urllib.request.urlopen(endPoint)
    return json.load(jsonObj)

def JsonLiga(tier, divisao, queue):

    endPoint = base_request+'/lol/league/v4/entries/'+queue+'/'+divisao+'/'+tier+key
    jsonObj = urllib.request.urlopen(endPoint)
    return json.load(jsonObj)

def topMaestry(top, esID):

    endPoint = base_request+'/lol/champion-mastery/v4/champion-masteries/by-summoner/'+esID+key
    JsonObj = urllib.request.urlopen(endPoint)
    data = json.load(JsonObj)

    maestrias = []

    for i in range(top):
        temp = [data[i]['championId'], data[i]['championLevel'], data[i]['championPoints']]
        maestrias.append(temp)

    return maestrias
    
def LevelBy_ID(esID):

    final_resquest = base_request+"/lol/summoner/v4/summoners/"+esID+key
    JsonObj = urllib.request.urlopen(final_resquest)
    data = json.load(JsonObj)
    
    return int(data['summonerLevel'])

def getVersion():

    endPoint = 'https://ddragon.leagueoflegends.com/api/versions.json'
    JsonObj = urllib.request.urlopen(endPoint)
    data = json.load(JsonObj)

    return data[0]

def URL_ProfileIcon(esID):

    base_PI_URL = "http://ddragon.leagueoflegends.com/cdn/"+getVersion()+"/img/profileicon/"
    endPoint = base_request+"/lol/summoner/v4/summoners/"+esID+key
    
    JsonObj = urllib.request.urlopen(endPoint)
    data = json.load(JsonObj)
    profileIconId = str(data['profileIconId'])

    return base_PI_URL+profileIconId+".png"

def URL_ChampIcon(champ):

    return "http://ddragon.leagueoflegends.com/cdn/"+getVersion()+"/img/champion/"+champ+".png"
        
def champNameByID(championId):
    
    request = 'http://ddragon.leagueoflegends.com/cdn/12.2.1/data/en_US/champion.json'
    JsonObj = urllib.request.urlopen(request)
    data = json.load(JsonObj)
    champs = data['data']

    for champ in champs:
        if (int(champs[champ]['key']) == int(championId)):
            return champs[champ]['name']