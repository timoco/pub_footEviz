import requests

# curl --request GET 
# 	--url 'https://free-api-live-football-data.p.rapidapi.com/football-players-search?search=m' 
# 	--header 'x-rapidapi-host: free-api-live-football-data.p.rapidapi.com' 
# 	--header 'x-rapidapi-key: 3ce4317182msh1ec30ae960bb2a9p1bd7f7jsnf6c1a283ec9b'
def get_live_matches():
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures?live=all"
    headers = {
        "X-RapidAPI-Key": FOOTIE_DATA_API_KEY,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()['response']
    return data
