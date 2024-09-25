import requests

def get_weather(city, api_key, units):
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
    request = requests.get(url)
    content = request.json()
    print(content)

get_weather("Kannur","121553b8a009fac52d44f9dfd8b06364","standard")