import re
import requests
import datetime

sites_state = "/home/hntd/flowRate/usgs/id-sites.txt"
wdurl       = "https://waterdata.usgs.gov/usa/nwis/uv?site_no="
local_api   = "http://127.0.0.1:3333/api/update/"
logfile     = '/home/hntd/flowRate/usgs/usgs-update.log'
sites       = open (sites_state,"r")
count       = 0

def scrape(log,count):
  global flow_rate
  url = wdurl+site
  page = requests.get(url)
  html = page.text
  log.write("USGS request number: "+str(count)+" "+"Status code: "+str(page.status_code)+'\r\n')
  text = re.search("(value:.*)",str(html))
  if text:
    flow_rate = text.group(1).rsplit("value: ")[1]
  flow_rate = flow_rate.rsplit(" &")[0]
  flow_rate= str(flow_rate).replace(" ","_")

def api_put(site,local_api):
  local_api = local_api+site
  data = {"site": site, "flowrate": flow_rate}
  r = requests.put(local_api, verify=False, json=data)
  log.write("API UPDATE STATUS CODE: "+str(r.status_code)+'\r\n')

for site in sites:
  count = count + 1
  site = site.strip('\n')
  log = open(logfile,'a')
  scrape(log,count)
  api_put(site,local_api)
log.close()
