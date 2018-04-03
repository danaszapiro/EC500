import json
import os
from pymongo import MongoClient

# function to connect to Mongodb and initialize database
def Initialize():
    fname = open("airports.json", 'r')
    data = json.load(fname.read())
    client = MongoClient('localhost:27017')
    db = client.Airports
    db.Airports.insert_many(data)
    
# function to add new airports to database    
def Insert(code, lat, lon, name, city, state, country, woeid, tz, phone, email, url, runwayLen, elev, icao, directFlights, carriers):
    try:
        
    client = MongoClient()
    db = client.Airports
    airport = {
    			"code": code,
             "lat": lat,
             "lon": lon,
             "name": name,
             "city": city,
             "state": state,
             "country": country,
             "woeid": woeid,
             "tz": tz,
             "phone": phone,
             "email": email,
             "url": url,
             "runway_length": runwayLen,
             "elev": elev,
             "icao": icao,
             "direct_flights": directFlights,
             "carriers": carriers
             }
    
    db.Airports.insert(airport)
    
    except Exception, e:
        print str(e)
    
# function to update specific field in an airport in the database        
 def Update(query, field, value):
        try:
            
        client = MongoClient()
        db = client.Airports
        updateValue = {field:value}
        db.Airports.update_one(query, updateValue)
        
        except Exception, e:
            print str(e)
    
 def Search(query, projection):
    try:
        
    client = MongoClient()
    db = client.airports
    result = db.Airports.find({query: projection})

    print("The results for your search are: \n")
    for item in result:
        print(result)
        
    except Exception, e:
        print str(e)
        
 def main(): 
     if __name__ == "__main__":
        os.system("mongod")
        Initialize()
        while(1):
            selection = raw_input("Choose an action to perform on airport database:\n -To insert new airport type 1\n -For searching type 2\n -To update type 3\n")

            if selection == 1:
                    print("Please enter the following fields: \n")
                code = raw_input("Airport code: ")
                lat = raw_input("Latitude coordinate: ")
                lon = raw_input("Longitude coordinate: ")
                name = raw_input("Airport name: ")
                city = raw_input("City: ")
                state = raw_input("State: ")
                country = raw_input("Country: ")
                woeid = raw_input("woeid: ")
                tz = raw_input("tz: ")
                phone = raw_input("Phone number: ")
                email = raw_input("Email address: ")
                url = raw_input("url: ")
                runway = raw_input("runway length: ")
                elevation = raw_input("elevation: ")
                icao = raw_input("icao: ")
                directFlights = raw_input("direct flights: ")
                carriers = raw_input("carriers: ")
                Add(code, lat, lon, name, city, state, country, woeid, tz, phone, email, url, runway, elevation, icao, directFlights, carriers)
                Find(field, val)
            elif selection == 2:
                query = raw_input("Please enter the field you are looking for: ")
                projection = raw_input("Please enter a keyword: ")
                Search(query, projection)
            elif selection == 3:
                query = raw_input("Please enter the code for the airport to update: ")
                field = raw_input("Please enter a field to update: ")
                val = raw_input("Please enter the updated value for the field: ") 
                Update(query, field, val)
            else:
                print("ERROR! Invalid input")