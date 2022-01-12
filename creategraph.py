import requests
r =requests.get('http://ha123blix.eu.pythonanywhere.com/api1/history')
print(r.text)
