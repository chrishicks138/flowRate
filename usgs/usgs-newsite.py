import requests

file = open("./flowRate/usgs/co-sites.txt","r")

for line in file:
  line = line.strip('\n')
  url = 'http://127.0.0.1:3333/api/river_flow_rates'
  data = {"site": line, "flowrate": "777", "date": "7-7-7", "timezone": "777"}
  r = requests.post(url, verify=False, json=data)
  print(str(r.status_code)+'\r\n')
