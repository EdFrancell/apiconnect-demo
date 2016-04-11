import requests, json, random, datetime

requests.packages.urllib3.disable_warnings()

host = 'http://rio.mybluemix.net'

host = 'https://localhost:4004'

headers = {
    'x-ibm-client-id': "default",
    'x-ibm-client-secret': "SECRET",
    'content-type': "application/json",
    'accept': "application/json"
    }

currentValue = str(random.uniform(1.5, 40.9))[:4]
payload = {"currentValue": currentValue,"id": 501, "timestamp" : datetime.datetime.now().isoformat()}
r = requests.post(host + "/api/temperatures", headers=headers, verify=False, data = json.dumps(payload))
print r.text

#for i in range(1,101):
#	currentValue = str(random.uniform(1.5, 40.9))[:4]
#	payload = {"currentValue": currentValue,"id": i, "timestamp" : datetime.datetime.now().isoformat()}
#	r = requests.post(host + "/api/temperatures", headers=headers, verify=False, data = json.dumps(payload))
#	print r.text

#for i in range(1,101):
#	currentValue = str(random.uniform(1.5, 80.0))[:4]
#	payload = {"currentValue": currentValue,"id": i, "timestamp" : datetime.datetime.now().isoformat()}
#	r = requests.post(host + "/api/humidities", headers=headers, verify=False, data = json.dumps(payload))
#	print r.text