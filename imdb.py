import http.client
import json
import requests
import time

conn = http.client.HTTPSConnection("imdb.iamidiotareyoutoo.com")

conn.request("GET", "/search?q=witch")

res = conn.getresponse()
data = res.read()

response = json.loads(data.decode("utf-8"))
for i in response["description"]:
    poster_url = i["#IMG_POSTER"]
    print("Downloading... ",poster_url)
    r = requests.get(poster_url, allow_redirects=True)
    open(i["#IMDB_ID"]+'.jpg', 'wb').write(r.content)
    time.sleep(0.5)