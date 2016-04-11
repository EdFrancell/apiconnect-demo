import requests, json

requests.packages.urllib3.disable_warnings()


headers = {
    'x-ibm-client-id': "default",
    'x-ibm-client-secret': "SECRET",
    'content-type': "application/json",
    'accept': "application/json"
    }

host = 'http://rio.mybluemix.net'

#host =  'https://localhost:4004'

result = requests.get(host + "/api/temperatures", headers=headers, verify=False).text

print result

result = requests.get(host + "/api/humidities", headers=headers, verify=False).text

print result