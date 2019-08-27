import re
import requests
import time

#log = open("./flw.log",'w+')
file = open("./id-sites.txt","r")
wdurl = "https://waterdata.usgs.gov/usa/nwis/uv?site_no="
count = 0
while True:
  count =+ 1
  for line in file:
    line = line.strip('\n')
    url = wdurl+line

    page = requests.get(url) # request page.
    html = page.text # convert data to text.
    print(str(page.status_code)+'\r\n')
    text = re.search("(value:.*)",str(html)) # find first match of word "value", which is next to the data we need.
    if text:
      river_flow_rate = text.group(1).rsplit("value: ")[1] # split text right of searched text, which is the data we need.
    river_flow_rate_file_name = river_flow_rate.rsplit(" &")[0] # split string so we get river flow value and date
    river_flow_rate_file_name = str(river_flow_rate_file_name).replace(" ","_") # replace spaces with underscores


    url1 = 'http://127.0.0.1:3333/api/river_flow_rates/'+line
    data = {"site": line, "flowrate": river_flow_rate_file_name}
    r = requests.post(url1, verify=False, json=data)
    print(count)
    print(str(r.status_code)+'\r\n')
  time.sleep(3)
