import os
from dotenv import load_dotenv
import requests
from datetime import date, datetime 
from twilio.rest import Client

#Loads key.env file for API keys
load_dotenv()
x = 0 
time = 0 
departureWeather =0
arrival_weather = 0
message = 0
phone_number = ''


#Following function returns basic flight statistics with real-time location and aircraft image.
def flight_data(querystring = {"withAircraftImage":"true","withLocation":"true"},flight=1,year=2,month=3,day=4):
    try: # They are all the inputs need. 
      flight = str(flight)
      year = int(year) 
      month = int(month)
      day = int(day)
      print(flight,year,month,day)
    except:
      print("Invalid arguments: ")
    
    try:
      date1 = str(date(year, month, day))
              
    except:
      print("Date Error")
      return "Unable to process request. Either a servers are down or date cannont be read."
      
      
      #Standard API code for it to work
    api = "https://aerodatabox.p.rapidapi.com/flights/number/"
    url = api + flight +"/"+date1
      
  
    headers = {
      "X-RapidAPI-Key": os.getenv('flightAPI'),
        "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
      }
        #Standard API code for it to work

    global x,time,departureWeather,arrival_weather,message
    print("HI")

    try: 
      
      response = requests.request("GET", url, headers=headers, params=querystring)
      print(f'response is {response}')
    
      airline = response.json()[0]["airline"]["name"]
      
  
      departure = response.json()[0]["departure"]["airport"]["name"]
      #departureWeather = departure_weather(departure)

  
      arrival = response.json()[0]["arrival"]["airport"]["name"]
      #arrivalWeather = arrival_weather(arrival)

      time = response.json()[0]["departure"]["scheduledTimeLocal"]

      image = response.json()[0]["aircraft"]["image"]["url"]

    except:
      print(response.json()["message"])
      return response.json()["message"]
    
    print("Here")

    try: # does not work need to debug this. 
    
      real_time_geo = response.json()[0]["location"]
      print(f'real_time_geo is {real_time_geo}')
  
      list_location = list(real_time_geo.values())
      print(f'list_location is {list_location}')

      lat = list_location[4]
  
      lon = list_location[5]
      print(lat,lon)
      lat_lon = [lat,lon]
      #map(lat_lon[0],lat_lon[1])
    except:
      print("Real time location for this flight is not available")
      x = "Real time location for this flight is not available"
      print(response.json())
      message = f'This is a {airline} flight, Flying from {departure} to {arrival}. Time: {time}."Real time location for this flight is not available"'
      
      return message

    
  #download image
    r = requests.get(image)
    with open('flight.jpg','wb') as f:
     f.write(r.content)
    
  
    print("This is a "+ airline +" flight.")
  
    print("Flying from  " + departure )
  
    print("To  " + arrival)
  
    print(time)
    try:
      print(lat_lon)
    except:
      print("")
    
    message = f'This is a {airline} flight, Flying from {departure} to {arrival}. Time: {time}'
    x = response.json()
    return message



# Following fuction returns an image of map with APIs taking latitude and longitude of the aircraft.
def map():
  global x
  if (x == "Real time location for this flight is not available"):
    return "Real time location for this flight is not available; Unable to Map location"

  if (x != 0):
    try:
      list_location = list(x[0]["location"].values())

      lat = str(list_location[4])
      lon = str(list_location[5])
    
  

      endpoint = 'https://maps.googleapis.com/maps/api/staticmap?center='
      map_size = '&zoom=7&size=400x400&markers=color:red%7Clabel:O%7C'
      marker = '&markers=size:mid%7Ccolor:0xFF0000%7C&key='
      #All API keys are stored in a seperate file called key.env and the following line is extracting that respective map key for this function to work
      API =  os.getenv('maps')
    
      image_url = endpoint + lat+','+lon + map_size + lat+','+lon + marker + API

      r = requests.get(image_url)
      with open('flight_map.jpg','wb') as f:
        f.write(r.content)
      print("It worked")
      return "Flight has been found and tracked."

    except:
      print('Doesnt work')
      return "Error"

  else:
      return  "Real time location for this flight is not available; Unable to Map location"





#Link example for MAP >>>>>>>>    https://maps.googleapis.com/maps/api/staticmap?center=52.47159, -1.76778&zoom=6&size=400x400&markers=color:blue%7Clabel:S%7C52.47159, -1.76778&markers=size:mid%7Ccolor:0xFFFF00%7Clabel:C%7CTok,AK%22&key=AIzaSyBJM6palbsErzflk8nXqV4wWQdH_Zdg5_E'
'''
https://maps.googleapis.com/maps/api/staticmap?
center=52.47159, -1.76778
&zoom=6&size=400x400
&markers=color:blue%7Clabel:S%7C52.47159, -1.76778
&markers=size:mid%7Ccolor:0xFFFF00%7Clabel:C%7CTok,AK%22
&key=AIzaSyBJM6palbsErzflk8nXqV4wWQdH_Zdg5_E'
'''


#Following function returns departure weather. It takes a city as parameter from the flight function and returns weather
def departure_weather(city="london"):

  #Standard API code for it to work
  weather_api = "https://weatherapi-com.p.rapidapi.com/current.json"
  
  querystring = {"q":city}

  headers = {
	"X-RapidAPI-Key": os.getenv('weatherAPI'),
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
  #Standard API code for it to work
  response = requests.request("GET", weather_api, headers=headers, params=querystring)
  weather_C= response.json()["current"]["temp_c"]

  sky_state = response.json()["current"]["condition"]["text"]
  try:
    visibility = response.json()["current"]["condition"]["vis_miles"]
  except:
    print("")

  print("Current temperature in " + city +" is " +str(round(weather_C))+"°C")
  print("Sky is "+sky_state)
  try:
    print(visibility)
  except:
    print("")
  return f"Current temperature in {city} is {str(weather_C)}°C"



#Following function returns arrival weather. It takes a city as parameter from the flight function and returns weather
def arrival_weather(city="london"):
  
  #Standard API code for it to work
  weather_api = "https://weatherapi-com.p.rapidapi.com/current.json"
  
  querystring = {"q":city}

  headers = {
	"X-RapidAPI-Key": os.getenv('weatherAPI'),
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
  #Standard API code for it to work
  try:
    response = requests.request("GET", weather_api, headers=headers, params=querystring)

    weather_C= response.json()["current"]["temp_c"]

    sky_state = response.json()["current"]["condition"]["text"]
  
    visibility = response.json()["current"]["condition"]["vis_miles"]
  except:
    print("")

  print("Current temperature in " + city +" is " +str(round(weather_C))+"°C")
  print("Sky is "+sky_state)
  try:
    print(visibility)
  except:
    print("")
  
  return response.json()

  



#Following function validates IATA airport code and returns false if code is wrong. If it is correct it passes these codes to be used in the next function.
def airport_code(airport = 'bhx',airport2 = 'lhr'):
  airport = str(input("3 digits airport code. Example: Bhx for Brirmingham > "))
  airport2 = str(input('3 digits airport code. Example:  LHR for London > '))
  
  if len(airport) == 3 and len(airport2) == 3:
    return airport, airport2
    
  else:
    return print(False)


#Following function takes IATA airport code afrom the previous function and returns estimated travel time between two given airports.
def airportDistance(airport='BHX',airport2='LHR'):
  
  try:
    #Standard API code for it to work
    url = 'https://aerodatabox.p.rapidapi.com/airports/iata/'

    urlFinal = url + airport + "/distance-time/"+ airport2

    headers = {
	    "X-RapidAPI-Key": "dc8191f566mshf8f3507be42b2cep1020d8jsnf07d622bc030",
	    "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
    }
    #Standard API code for it to work
    response = requests.request("GET", urlFinal, headers=headers)
    print(response.json())

    approx = response.json()["approxFlightTime"]

    return print('Estimated flight time from ' +airport + ' to ' + airport2 +' is ' +approx)
  except:
    return "Unable to process request either servers are down or airport code is incorrect."


#Following function checks a UK number's format and returns the correct format of the number to be used in the next functio to send a message.
def number_check(number='+447196325410'):
  number = str(number)
  global phone_number

  print(f"I'm here; Nymbe = {number}")
  if number.startswith('+') == True:
    phone_number = number
    return number
  elif number.startswith('07') == True:
    list_num = list(number)
    num = ''.join(list_num[1:11])
    number = str("+44"+num)
    phone_number = number
    print(f"HIs {phone_number}, {number}")


    return number
  else:
    list_num = list(number)
    num = ''.join(list_num[2:14])
    number = str("+"+num)
    phone_number = number
    return number
    
#Following function sends a message to the correct format number passed by previous function.
def Message(time="00:00",flight_insight=x):
  global phone_number
  print(f"I'm here now; Nymbe = {phone_number}")

   #Standard API code for it to work
  account_sid = os.getenv('account_SID') 
  auth_token = os.getenv('Auth')  
  client = Client(account_sid, auth_token) 
  #Standard API code for it to work
  try:
  
    airline = str(x[0]["airline"]["name"])
    departure = str(x[0]["departure"]["airport"]["name"])
    arrival = str(x[0]["arrival"]["airport"]["name"])
    time = str(x[0]["departure"]["scheduledTimeLocal"])

  
  #Standard API code for it to work
    message = client.messages.create( 
                                from_='+16208378159',  
                                body= "This is a "+ airline +" flight✈️." + " Flying from  " +   departure +"🛫." +" To  " + arrival + "🛩️." + " ⏳Departue time is " + time,      
                                to= phone_number,
                            ) 
   
    print(message.sid)
    return f'Message send to {phone_number}; SSID is {message.sid}'
  except:
    return f"Message cannot be sent to {phone_number}"
  #Standard API code for it to work

  
 

'''
# flight_data({"withAircraftImage":"true","withLocation":"true"},'SK7674',2022,11,19)
x = [{'greatCircleDistance': {'meter': 9217813.25, 'km': 9217.813, 'mile': 5727.684, 'nm': 4977.221, 'feet': 30242169.44}, 'departure': {'airport': {'icao': 'EHAM', 'iata': 'AMS', 'name': 'Amsterdam, Amsterdam Schiphol', 'shortName': 'Schiphol', 'municipalityName': 'Amsterdam', 'location': {'lat': 52.3086, 'lon': 4.763889}, 'countryCode': 'NL'}, 'scheduledTimeLocal': '2022-11-18 20:55+01:00', 'actualTimeLocal': '2022-11-18 21:32+01:00', 'scheduledTimeUtc': '2022-11-18 19:55Z', 'actualTimeUtc': '2022-11-18 20:32Z', 'terminal': '2', 'checkInDesk': '9-16', 'gate': 'F4', 'quality': ['Basic', 'Live']}, 'arrival': {'airport': {'icao': 'VTBS', 'iata': 'BKK', 'name': 'Bangkok, Suvarnabhumi', 'shortName': 'Suvarnabhumi', 'municipalityName': 'Bangkok', 'location': {'lat': 13.681099, 'lon': 100.747}, 'countryCode': 'TH'}, 'scheduledTimeLocal': '2022-11-19 13:50+07:00', 'actualTimeLocal': '2022-11-19 14:08+07:00', 'scheduledTimeUtc': '2022-11-19 06:50Z', 'actualTimeUtc': '2022-11-19 07:08Z', 'quality': ['Basic', 'Live']}, 'lastUpdatedUtc': '2022-11-19 07:05Z', 'number': 'KL 803', 'callSign': 'KLM803', 'status': 'Approaching', 'codeshareStatus': 'IsOperator', 'isCargo': False, 'aircraft': {'reg': 'PH-BVG', 'modeS': '484CBB', 'model': 'Boeing 777', 'image': {'url': 'https://farm3.staticflickr.com/2881/32846366523_9fe723b535_z.jpg', 'webUrl': 'https://www.flickr.com/photos/20476255@N00/32846366523/', 'author': 'Riik@mctr', 'title': 'KL/KLM Royal Dutch Airlines Boeing 777 PH-BVD', 'description': 'Manchester Airport (EGCC)', 'license': 'AttributionShareAlikeCC', 'htmlAttributions': ['Original of "<span property=\'dc:title\' itemprop=\'name\'>KL/KLM Royal Dutch Airlines Boeing 777 PH-BVD</span>" by  <a rel=\'dc:creator nofollow\' property=\'cc:attributionName\' href=\'https://www.flickr.com/photos/20476255@N00/32846366523/\' target=\'_blank\'><span itemprop=\'producer\'>Riik@mctr</span></a>.', 'Shared and hosted by <span itemprop=\'publisher\'>Flickr</span> under <a target="_blank" rel="license cc:license nofollow" href="https://creativecommons.org/licenses/by-sa/2.0/">CC BY-SA</a>']}}, 'airline': {'name': 'KLM'}}, {'greatCircleDistance': {'meter': 2190054.26, 'km': 2190.054, 'mile': 1360.837, 'nm': 1182.535, 'feet': 7185217.38}, 'departure': {'airport': {'icao': 'VTBS', 'iata': 'BKK', 'name': 'Bangkok, Suvarnabhumi', 'shortName': 'Suvarnabhumi', 'municipalityName': 'Bangkok', 'location': {'lat': 13.681099, 'lon': 100.747}, 'countryCode': 'TH'}, 'scheduledTimeLocal': '2022-11-19 15:15+07:00', 'actualTimeLocal': '2022-11-19 16:38+07:00', 'runwayTimeLocal': '2022-11-19 16:38+07:00', 'scheduledTimeUtc': '2022-11-19 08:15Z', 'actualTimeUtc': '2022-11-19 09:38Z', 'runwayTimeUtc': '2022-11-19 09:38Z', 'runway': '01R', 'quality': ['Basic', 'Live']}, 'arrival': {'airport': {'icao': 'RPLL', 'iata': 'MNL', 'name': 'Manila, Ninoy Aquino', 'shortName': 'Ninoy Aquino', 'municipalityName': 'Manila', 'location': {'lat': 14.5086, 'lon': 121.02}, 'countryCode': 'PH'}, 'scheduledTimeLocal': '2022-11-19 19:30+08:00', 'actualTimeLocal': '2022-11-19 20:23+08:00', 'runwayTimeLocal': '2022-11-19 20:23+08:00', 'scheduledTimeUtc': '2022-11-19 11:30Z', 'actualTimeUtc': '2022-11-19 12:23Z', 'runwayTimeUtc': '2022-11-19 12:23Z', 'terminal': '3', 'runway': '06', 'quality': ['Basic', 'Live']}, 'lastUpdatedUtc': '2022-11-19 12:33Z', 'number': 'KL 803', 'callSign': 'KLM803', 'status': 'Arrived', 'codeshareStatus': 'IsOperator', 'isCargo': False, 'aircraft': {'reg': 'PH-BVG', 'modeS': '484CBB', 'model': 'Boeing 777', 'image': {'url': 'https://farm3.staticflickr.com/2881/32846366523_9fe723b535_z.jpg', 'webUrl': 'https://www.flickr.com/photos/20476255@N00/32846366523/', 'author': 'Riik@mctr', 'title': 'KL/KLM Royal Dutch Airlines Boeing 777 PH-BVD', 'description': 'Manchester Airport (EGCC)', 'license': 'AttributionShareAlikeCC', 'htmlAttributions': ['Original of "<span property=\'dc:title\' itemprop=\'name\'>KL/KLM Royal Dutch Airlines Boeing 777 PH-BVD</span>" by  <a rel=\'dc:creator nofollow\' property=\'cc:attributionName\' href=\'https://www.flickr.com/photos/20476255@N00/32846366523/\' target=\'_blank\'><span itemprop=\'producer\'>Riik@mctr</span></a>.', 'Shared and hosted by <span itemprop=\'publisher\'>Flickr</span> under <a target="_blank" rel="license cc:license nofollow" href="https://creativecommons.org/licenses/by-sa/2.0/">CC BY-SA</a>']}}, 'airline': {'name': 'KLM'}}, {'greatCircleDistance': {'meter': 9217813.25, 'km': 9217.813, 'mile': 5727.684, 'nm': 4977.221, 'feet': 30242169.44}, 'departure': {'airport': {'icao': 'EHAM', 'iata': 'AMS', 'name': 'Amsterdam, Amsterdam Schiphol', 'shortName': 'Schiphol', 'municipalityName': 'Amsterdam', 'location': {'lat': 52.3086, 'lon': 4.763889}, 'countryCode': 'NL'}, 'scheduledTimeLocal': '2022-11-19 20:55+01:00', 'actualTimeLocal': '2022-11-19 21:31+01:00', 'runwayTimeLocal': '2022-11-19 21:50+01:00', 'scheduledTimeUtc': '2022-11-19 19:55Z', 'actualTimeUtc': '2022-11-19 20:31Z', 'runwayTimeUtc': '2022-11-19 20:50Z', 'terminal': '2', 'checkInDesk': '9-16', 'gate': 'F7', 'runway': '36L', 'quality': ['Basic', 'Live']}, 'arrival': {'airport': {'icao': 'VTBS', 'iata': 'BKK', 'name': 'Bangkok, Suvarnabhumi', 'shortName': 'Suvarnabhumi', 'municipalityName': 'Bangkok', 'location': {'lat': 13.681099, 'lon': 100.747}, 'countryCode': 'TH'}, 'scheduledTimeLocal': '2022-11-20 13:50+07:00', 'scheduledTimeUtc': '2022-11-20 06:50Z', 'quality': ['Basic']}, 'lastUpdatedUtc': '2022-11-19 20:59Z', 'number': 'KL 803', 'callSign': 'KLM803', 'status': 'Departed', 'codeshareStatus': 'IsOperator', 'isCargo': False, 'aircraft': {'reg': 'PH-BVD', 'modeS': '484561', 'model': 'Boeing 777', 'image': {'url': 'https://farm2.staticflickr.com/1717/25058600220_58ca28e307_z.jpg', 'webUrl': 'https://www.flickr.com/photos/34153108@N06/25058600220/', 'author': 'GerardvdSchaaf', 'title': 'PH-BVD', 'description': 'Schiphol, Februari 2016', 'license': 'AttributionCC', 'htmlAttributions': ['Original of "<span property=\'dc:title\' itemprop=\'name\'>PH-BVD</span>" by  <a rel=\'dc:creator nofollow\' property=\'cc:attributionName\' href=\'https://www.flickr.com/photos/34153108@N06/25058600220/\' target=\'_blank\'><span itemprop=\'producer\'>GerardvdSchaaf</span></a>.', 'Shared and hosted by <span itemprop=\'publisher\'>Flickr</span> under <a target="_blank" rel="license cc:license nofollow" href="https://creativecommons.org/licenses/by/2.0/">CC BY</a>']}}, 'airline': {'name': 'KLM'}}]
print(x)


print(map())
  
'''
airportDistance()