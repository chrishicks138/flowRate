import threading
from queue import Queue
import time
import re
import requests
import datetime

lock = threading.Lock()

def scrape(wdurl,site):
  data = []
  global flow
  global date
  global timezone
  url = wdurl+site
  print("Downloading: "+url)
  page = requests.get(url)
  html = page.text
  text = re.search("(USGS\t.*)",str(html))
  if text:
    flow_rate = text.group(1).rsplit("\t")
  for item in flow_rate:
    data.append(item)
  date     = str(data[2])
  timezone = str(data[3])
  flow     = str(data[4])

def api_put(site,local_api):
  local_api = local_api+site
  data = {"site": site, "flowrate": flow, "date": date, "timezone": timezone}
  r = requests.put(local_api, verify=False, json=data)

def do_work(item):
  sites = open(item,"r")
  local_api = "http://localhost:3333/api/update/"
  wdurl = "https://waterservices.usgs.gov/nwis/iv/?format=rdb,1.0&sites="
  for site in sites:
    site = site.strip('\n')
    scrape(wdurl,site)
    api_put(site,local_api)
  with lock:
    print(threading.current_thread().name,item)

def worker():
  while True:
    item = q.get()
    do_work(item)
    q.task_done()
# Create the queue and thread pool.
q = Queue()
sites_state = ["./flowRate/usgs/id-sites.txt","./flowRate/usgs/co-sites.txt"]
for state in sites_state:
  t = threading.Thread(target=worker)
  t.daemon = True # thread dies when main thread (only non-daemon thread) exits.
  t.start()
# stuff work items on the queue (in this case, just a number).
start = time.perf_counter()
for state in sites_state:
  q.put(state)
q.join() # block until all tasks are done
# "Work" took .1 seconds per task. 20 tasks serially would be 2 seconds. With 4 threads should be about .5
# seconds (contrived because non-CPU intensive "work")
print('time:',time.perf_counter() - start)

'''
local = "http://localhost:3333/api/13206000"
localpage = requests.get(local)
htmll = localpage.text
whdata = {"value1": htmll, "value2": " ", "value3": " "}
whurl = "https://maker.ifttt.com/trigger/flow/with/key/jejMA-IrKcQ28zqrLehtC-K586j5giZWtgL2ZpQiFW3"
d = requests.post(whurl, verify=True, json=whdata)
'''
