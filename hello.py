import leaguepedia_parser
import json
import urllib.request

lp = leaguepedia_parser.LeaguepediaParser()

# Gets you tournaments in the region, by default only returns primary tournaments
tournaments = lp.get_tournaments('Europe', year=2020,tournament_level='Secondary')

# Gets you all games for a tournament. Get the name from get_tournaments()
for i in tournaments:
    if i['name'] == 'LFL Division 2 2020':
        games = lp.get_games(i['name'])

print(games)

index = 0
urlDIV2 = []
for i in games:
    urlDIV2.append(i['match_history_url'])
    index += 1

print(index,urlDIV2)

s = []
for i in urlDIV2:
    s.append(i.split('match-details/'))

print(s)

url = []
for i in s:
    url.append('https://acs.leagueoflegends.com/v1/stats/game/' + i[1])

print(url)

headers = {}
headers['cookie'] = "_gcl_au=1.1.2106265452.1579169629; _ga=GA1.2.1669728078.1579169630; _hjid=ccd9b883-792f-4aff-a0f8-0c8f711e7b25; ajs_group_id=null; _tlp=2820:16705877; s_fid=058B095915A9A931-3F4CE3FE9F899602; notice_preferences=3:; notice_gdpr_prefs=0,1,2,3:; cmapi_gtm_bl=; cmapi_cookie_privacy=permit 1,2,3,4; new_visitor=false; rp2=1582554081607-Repeat; ajs_user_id=null; ping_session_id=d51f4f11-2f7b-444c-bd14-93dbeeb069b8; _gid=GA1.2.906518356.1585303136; PVPNET_TOKEN_EUW=eyJkYXRlX3RpbWUiOjE1ODUzMDMxNDA5ODQsImdhc19hY2NvdW50X2lkIjozNjE3MTI0MCwicHZwbmV0X2FjY291bnRfaWQiOjM2MTcxMjQwLCJzdW1tb25lcl9uYW1lIjoiYXJuYWh1ZCIsInZvdWNoaW5nX2tleV9pZCI6IjkwMzQ3NTJiMmI0NTYwNDRhZTg3ZjI1OTgyZGFkMDdkIiwic2lnbmF0dXJlIjoiV093c2tDRU1tT3FNKzFOMlh5U05mb2ROUHpJU0VwbE9uYmYwY3BTMDB1NklzYnhYalErZWtpdjlveEFIVFFCNTJVd3pOclc4TDFnOVhpMExqWURpT2N6MWZ6V1g4Rll4aE5yeXdsaWtZcm51Vy9BSjlMbkIwSGFNSytYVllkdTJteTg2bDFyMU4xL0hnWlB2cWI5YndhNHdnM1Q2OXJ2cjk1MFFuQm1KQ1A4PSJ9; PVPNET_ACCT_EUW=arnahud; PVPNET_ID_EUW=36171240; PVPNET_REGION=euw; PVPNET_LANG=fr_FR; id_token=eyJraWQiOiJzMSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIxOTFiZjkyOC0zMzBhLTU3MjAtYjMzYy1mZTQ5OGNmODdlOTYiLCJjb3VudHJ5IjoiZnJhIiwicGxheWVyX3Bsb2NhbGUiOiJlbi1VUyIsImFtciI6WyJjb29raWUiXSwiaXNzIjoiaHR0cHM6XC9cL2F1dGgucmlvdGdhbWVzLmNvbSIsImxvbCI6W3siY3VpZCI6MzYxNzEyNDAsImNwaWQiOiJFVVcxIiwidWlkIjozNjE3MTI0MCwidW5hbWUiOiJhcm5hdWQzMDEyIiwicHRyaWQiOm51bGwsInBpZCI6IkVVVzEiLCJzdGF0ZSI6IkVOQUJMRUQifV0sImxvY2FsZSI6ImZyX0ZSIiwiYXVkIjoicnNvLXdlYi1jbGllbnQtcHJvZCIsImFjciI6IjAiLCJwbGF5ZXJfbG9jYWxlIjoiZW4tVVMiLCJleHAiOjE1ODUzODk1MzksImlhdCI6MTU4NTMwMzEzOSwiYWNjdCI6eyJnYW1lX25hbWUiOiJhcm5haHVkIiwidGFnX2xpbmUiOiJFVVcifSwianRpIjoiWGllVkY2cmZSNWMiLCJsb2dpbl9jb3VudHJ5Ijoia29yIn0.Xgn17hWMwj5AW6saTL6ayD91ulTuFDsTmMwL1BhXLQGwSCKdJmnUDRW4S6UPLV0HM1bjJR_nCPt1jIjjTFIj9_1K41kWES92fgGiIyPN0iFHUhIuMuaC-3884GBEdatEzjIJaXEITyT7YGn4k9QDp_iL16SobiQXFOKFiBm7x-I; id_hint=sub%3D191bf928-330a-5720-b33c-fe498cf87e96%26lang%3Dfr%26game_name%3Darnahud%26tag_line%3DEUW%26id%3D36171240%26summoner%3Darnahud%26region%3DEUW1%26tag%3Deuw; __cfduid=da678c9c05c0a89c271415567126e7c781585303142; notice_behavior=implied,eu; _sctr=1|1585263600000; _tlc=t.co%2FQDlftBwhJU%3Famp%3D1:1585317227:euw.leagueoflegends.com%2Fen-gb%2F:leagueoflegends.com; _tlv=11.1579169631.1584537018.1585317227.17.1.1; _gat=1"

obj = []
for i in url:
    req = urllib.request.Request(i, headers = headers)
    html = urllib.request.urlopen(req).read().decode()
    # parse json object
    obj.append(json.loads(html))

#correction des datas : correction des noms des joueurs
for i in obj:
    for j in i['participantIdentities']:
        if j['player']['summonerName'] == 'TPAA Louis':
            j['player']['summonerName'] = 'TPAA NoTiixX'
        if j['player']['summonerName'] == 'Chapovich' or j['player']['summonerName'] == 'Lunary Chapi':
            j['player']['summonerName'] = 'LUNARY CHAP'
        if j['player']['summonerName'] == 'UFZ Akabane1':
            j['player']['summonerName'] = 'UFZ Akabane'
        if j['player']['summonerName'] == 'Lunary Jbzz':
            j['player']['summonerName'] = 'LUNARY Jbzz'
        if j['player']['summonerName'] == 'LUNARY TIOO' or j['player']['summonerName'] == 'Nulary Tioo':
            j['player']['summonerName'] = 'LUNARY Tioo'
        if j['player']['summonerName'] == 'LUNARY SHARKY' or j['player']['summonerName'] == 'LUNARY SHARKK':
            j['player']['summonerName'] = 'LUNARY Sharkk'
        if j['player']['summonerName'] == 'UFZ Nuclear':
            j['player']['summonerName'] = 'UFZ Nuclearint'
        if j['player']['summonerName'] == 'TH SenZu':
            j['player']['summonerName'] = 'TH Senzu'
        if j['player']['summonerName'] == 'GO Zenöz':
            j['player']['summonerName'] = 'GO Zenoz'
        if j['player']['summonerName'] == 'MZG Melon ':
            j['player']['summonerName'] = 'MZG Melon'
        if j['player']['summonerName'] == 'Lunary Exakick':
            j['player']['summonerName'] = 'LUNARY Exakick'
        if j['player']['summonerName'] == 'UFZ Adam':
            j['player']['summonerName'] = 'KC Adam'
        if j['player']['summonerName'] == 'UFZ Akabane':
            j['player']['summonerName'] = 'KC Akabane'
        if j['player']['summonerName'] == 'UFZ Nuclearint':
            j['player']['summonerName'] = 'KC Nuclearint'
        if j['player']['summonerName'] == 'UFZ Jujutw0':
            j['player']['summonerName'] = 'KC Jujutw0'
        if j['player']['summonerName'] == 'UFZ Helaz':
            j['player']['summonerName'] = 'KC Helaz'

for i in obj:
    gold100 = 0;
    gold200 = 0;
    for j in i['participants']:
        if j['teamId'] == 100:
            gold100 += j['stats']['goldSpent']
        else:
            gold200 += j['stats']['goldSpent']
    for j in i['participants']:
        if j['teamId'] == 100:
            j['stats']['goldSpentPercentage'] = j['stats']['goldSpent'] / gold100
        else:
            j['stats']['goldSpentPercentage'] = j['stats']['goldSpent'] / gold200

for i in obj:
    print(i)

#J'ai tous les JSON des matchs
#Je veux sortir pour chaque joueurs, deaths et totalDamageDealtToChampions
print(obj[0]['participantIdentities'])

playerPseudo = []
for i in obj:
    for j in i['participantIdentities']:
        playerPseudo.append(j['player']['summonerName'])

playerPseudo = dict.fromkeys(playerPseudo)
print(len(playerPseudo),playerPseudo)

for i in playerPseudo:
    playerPseudo[i] = {'team': '','nbGames': 0,'gameDuration': 0, 'deaths': 0, 'totalDamageDealtToChampions': 0, 'goldSpentPercentage': 0}

for i in playerPseudo:
    if i.split(' ',1)[0] == 'GO':
        playerPseudo[i]['team'] = 'GO'
    if i.split(' ',1)[0] == 'BTL':
        playerPseudo[i]['team'] = 'BTL'
    if i.split(' ',1)[0] == 'MZG':
        playerPseudo[i]['team'] = 'MZG'
    if i.split(' ',1)[0] == 'FCN':
        playerPseudo[i]['team'] = 'FCN'
    if i.split(' ',1)[0] == 'TPAA':
        playerPseudo[i]['team'] = 'TPAA'
    if i.split(' ',1)[0] == 'LUNARY':
        playerPseudo[i]['team'] = 'LUNARY'
    if i.split(' ',1)[0] == 'ZPR':
        playerPseudo[i]['team'] = 'ZPR'
    if i.split(' ',1)[0] == 'KC':
        playerPseudo[i]['team'] = 'KC'
    if i.split(' ',1)[0] == 'TH':
        playerPseudo[i]['team'] = 'TH'
    if i.split(' ',1)[0] == 'OPL':
        playerPseudo[i]['team'] = 'OPL'

for i in obj:
    for j in i['participantIdentities']:
        for k in playerPseudo:
            if k == j['player']['summonerName']:
                id = j['participantId']
                for l in i['participants']:
                    if l['participantId'] == id:
                        playerPseudo[k]['nbGames'] += 1
                        playerPseudo[k]['gameDuration'] += i['gameDuration'] / 60
                        playerPseudo[k]['deaths'] += l['stats']['deaths']
                        playerPseudo[k]['totalDamageDealtToChampions'] += l['stats']['totalDamageDealtToChampions']
                        playerPseudo[k]['goldSpentPercentage'] += l['stats']['goldSpentPercentage']

print(playerPseudo)

exportJSON = json.dumps(playerPseudo)

f = open("Div2_Players_stats.json", "w")
f.write(exportJSON)
f.close()


