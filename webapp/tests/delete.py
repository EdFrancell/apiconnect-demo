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

result = requests.delete(host + "/api/temperatures/100", headers=headers, verify=False).text
result = requests.delete(host + "/api/temperatures/101", headers=headers, verify=False).text
result = requests.delete(host + "/api/temperatures/102", headers=headers, verify=False).text