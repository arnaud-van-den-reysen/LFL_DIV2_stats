import leaguepedia_parser
import json
import urllib.parse
import urllib.request

lp = leaguepedia_parser.LeaguepediaParser()

# Gets you tournaments in the region, by default only returns primary tournaments
tournaments = lp.get_tournaments('Europe', year=2020,tournament_level='Secondary')

# Gets you all games for a tournament. Get the name from get_tournaments()
for i in tournaments:
    if i['name'] == 'LFL Division 2 2020':
        games = lp.get_games(i['name'])

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
headers['cookie'] = "new_visitor=false; _ga=GA1.2.1031275918.1523789907; ajs_group_id=null; s_fid=084E61FD2F17B1A9-1289DE22C7C4D704; C3UID-694=13974767501535292492; C3UID=13974767501535292492; __qca=P0-1655653013-1549286329912; _tlp=2820:16705877; __cfduid=da3ac128a3b3a4bb9b8a6efd6a9eec2921555402977; _scid=92ea0b26-1de4-472c-b7d4-b545cb5180b9; notice_preferences=2:; notice_gdpr_prefs=0,1,2:; _hjid=91d2d6ca-565f-4a84-b767-d17d36043bc0; rp2=1575806458255-Repeat; ajs_user_id=null; _gcl_au=1.1.1748260163.1576528939; PVPNET_TOKEN_EUW=eyJkYXRlX3RpbWUiOjE1NzY1Mjg5NDk2NjksImdhc19hY2NvdW50X2lkIjozNjE3MTI0MCwicHZwbmV0X2FjY291bnRfaWQiOjM2MTcxMjQwLCJzdW1tb25lcl9uYW1lIjoiYXJuYWh1ZCIsInZvdWNoaW5nX2tleV9pZCI6IjkwMzQ3NTJiMmI0NTYwNDRhZTg3ZjI1OTgyZGFkMDdkIiwic2lnbmF0dXJlIjoicE5RWWVua0IyZEdUZW12N0JIc2xaTEcvQVVZb0VGdkJWaXNOUys5K0JJUk5iVWVrK3NOR2RaZ1hlYmhNald5OTAxU2x5UXZYb0xwYVlnV1d0Vk9sM3NvYmt1dDlteFpjYWJuSk02M0N3RXVWdmw2TlRGWjMwd1d1L2hBSlhSNGxiZlBVa3MwMzZlYzBnazVQNExKVXh2L2paVnh6TkM4Y2RrWjFEeEliOTNjPSJ9; PVPNET_ACCT_EUW=arnahud; PVPNET_ID_EUW=36171240; PVPNET_REGION=euw; PVPNET_LANG=fr_FR; id_token=eyJraWQiOiJzMSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIxOTFiZjkyOC0zMzBhLTU3MjAtYjMzYy1mZTQ5OGNmODdlOTYiLCJjb3VudHJ5IjoiZnJhIiwiYW1yIjpbImNvb2tpZSJdLCJpc3MiOiJodHRwczpcL1wvYXV0aC5yaW90Z2FtZXMuY29tIiwibG9sIjpbeyJjdWlkIjozNjE3MTI0MCwiY3BpZCI6IkVVVzEiLCJ1aWQiOjM2MTcxMjQwLCJ1bmFtZSI6ImFybmF1ZDMwMTIiLCJwdHJpZCI6bnVsbCwicGlkIjoiRVVXMSIsInN0YXRlIjoiRU5BQkxFRCJ9XSwibG9jYWxlIjoiZnJfRlIiLCJhdWQiOiJyc28td2ViLWNsaWVudC1wcm9kIiwiYWNyIjoiMCIsImV4cCI6MTU3NjYxNTM0OCwiaWF0IjoxNTc2NTI4OTQ4LCJhY2N0Ijp7ImdhbWVfbmFtZSI6ImFybmFodWQiLCJ0YWdfbGluZSI6IkVVVyJ9LCJqdGkiOiJkTzExOEVpVGpQRSIsImxvZ2luX2NvdW50cnkiOiJmcmEifQ.GVGM4Ss5cc4lQKXaZnkXYXjbp5F4iSWYd6HPkqCqT4l0va7EF0INbHNLONmOKnS4c9-htLnMCpl1I9LmlexRIM58CodTO7OGz5tqP8kirtJ7KCeqAIbrsvWrDN3jQA5bHyoWiX3IPB3E8C76AOZ5BaAN-AE0sYSy5TpDjHo_hOw; id_hint=sub%3D191bf928-330a-5720-b33c-fe498cf87e96%26lang%3Dfr%26game_name%3Darnahud%26tag_line%3DEUW%26id%3D36171240%26summoner%3Darnahud%26region%3DEUW1%26tag%3Deuw; _tlc=:1576531469:euw.leagueoflegends.com%2Ffr%2F:leagueoflegends.com; _tlv=92.1550590967.1567793215.1576531488.242.1.2; ping_session_id=3adfe217-a333-4dab-996e-3c8a2d1a61c4; _gid=GA1.2.803505458.1577904415; _gat=1"

obj = []
for i in url:
    req = urllib.request.Request(i, headers = headers)
    html = urllib.request.urlopen(req).read().decode()
    print(html)
    # parse json object
    obj.append(json.loads(html))

print(obj[0]['teams'][0])





