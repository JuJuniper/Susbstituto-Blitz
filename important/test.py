from pprint import pprint
import back_end.apiLOL as Api

def limparTerminal():
    print("\n\n\n\n\n\n\n\n\n")

def ppELO(jsELO):

    for i in jsELO:
        if (i['queueType'] == 'RANKED_TFT_PAIRS'): continue

        print(i['queueType'], i['tier'], i['rank'], i['leaguePoints'], 'pdl')
        print(i["wins"], '/', i['losses'])

def ppUser(jsUser):

    print(jsUser['name'])
    print(jsUser['summonerLevel'])

def changeIdByName(cl):
     for i in cl: i[0] = Api.champNameByID(i[0])

def printUser(User):

    _id = Api.IDbySummoner(User)

    jsELO = Api.JsonEloByID(_id)
    jsSum = Api.JsonSummonerByID(_id)

    maestrias = Api.topMaestry(3, _id)
    changeIdByName(maestrias)

    limparTerminal()
    
    ppUser(jsSum)
    ppELO(jsELO)
    print(maestrias)

def TESTE__UltimaPartida(User):
    
    limparTerminal()

    _id = Api.IDbySummoner(User)
    _puuid = Api.PuuIDbyEsID(_id)
    pprint(Api.JsonHistoricoByPuuID(_puuid))


#TESTE__UltimaPartida("InFaMeZ")
#_id = Api.IDbySummoner("InFaMeZ")
#_puuid = Api.PuuIDbyEsID(_id)

_json = Api.JsonPartidaByMatchID("BR1_2539465626")
printUser("InFaMeZ")
#pprint(_json["info"]["participants"][1])
#with open('partida.txt', 'w') as f:
    #f.write(str(Api.JsonPartidaByMatchID("BR1_2539465626")))