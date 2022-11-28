import urllib.request  # allow me use an GET request from a website
import urllib.parse  # allow me to parse the data retrieved from website
import json as JSON  # this allow me to use JS and manipulate data retrieved
from urllib.request import Request, urlopen


#API website - https://apipheny.io/free-api/

def Website_Call(url="https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist,sexist,explicit&format=txt&type=single"):
  request = urllib.request.urlopen(url)
  respdata = str(request.read())  # this allows python to understand the data received
  respdata = respdata.strip("b")  # this formats the data so data is understandable
  respdata = respdata.strip("'")  # this formats the data so data is understandable
  print(respdata)
  if url == "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist,sexist,explicit&format=txt&type=single":
    return respdata

  try: 
    json = JSON.loads(respdata) # convert webrequest data into json dictionary if Json is given
    return json["joke"]
  except:
    return "Unable to process JSON - Sorry Try Again"




from urllib import request
from urllib.request import Request, urlopen
 
url = "https://howmanyfps.com/games/call-of-duty-warzone"
request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
webpage = urlopen(request_site).read()
print(webpage)