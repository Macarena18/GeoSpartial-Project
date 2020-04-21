import requests
import os
from dotenv import load_dotenv

#Funcion para obtener coordenadas de una direccion con Geocode
def geocode(address): #Use geocode api to do forward geocoding. https://geocode.xyz/api
    res = requests.get(f"https://geocode.xyz/{address}",params={"json":1})
    data = res.json()
    apiKey = os.getenv("GOOGLE_APIKEY")
    print("WE HAVE APIKEY") if apiKey else print("NO APIKEY FOUND")
    # Return as GeoJSON -> https://geojson.org/
    return { "coordinates": [float(data["longt"]), float(data["latt"])]}

# Obtener info sobre places con Googleplaces(Search)
def getFromApi(path,queryParams=dict(),apiKey=""):
    url=f"https://maps.googleapis.com/maps/api{path}"
    headers = {"Authorization":f"token {apiKey}"} if apiKey else {}
    res = requests.get(url, params=queryParams, headers=headers)
    print(res.status_code)
    return res.json()

#Funcion  para obtener info sobre places con FourSquare
def getFromFoursquare(coordinates,distance,name,category):
    url = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
    client_id=os.getenv("FOURSQUARE_APIKEY_ID"),
    client_secret=os.getenv("FOURSQUARE_APIKEY_SECRET"),
    v='20200417',
    ll= coordinates,
    radius= distance,
    query= name,
    categoryId= category,
    )
    resp = requests.get(url=url, params=params)
    return resp.json()