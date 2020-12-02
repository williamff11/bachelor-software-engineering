import urllib3

url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/1980/1999/BRA.csv"

# Usando urllib3
http = urllib3.PoolManager()
response = http.request('GET', url)
csv = response.data
