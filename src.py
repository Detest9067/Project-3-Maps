import requests
import json
import pymongo
from pymongo import MongoClient
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import pandas as pd


def get_f1_races(year):
    url = f"https://f1-live-motorsport-data.p.rapidapi.com/races/{year}"

    headers = {
        "X-RapidAPI-Key": f"{os.getenv('RAPIDAPI_KEY')}",
        "X-RapidAPI-Host": "f1-live-motorsport-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    response_json = json.loads(response.text)

    return response_json


def filter_tax_data(tax_file, country_file, output_file):
    df = pd.read_csv(tax_file)
    f1 = pd.read_csv(country_file)
    distinct_countries = pd.DataFrame({'country': f1['country'].unique()})
    filtered_tax_df = df[df['Country'].isin(distinct_countries['country'])]
    filtered_tax_df.to_csv(output_file, index=False)



def get_location_data(url, headers, collection_name):
    response = requests.get(url, headers=headers)
    data = response.json()

    with open(f"data/{collection_name}.json", "w") as f:
        json.dump(data, f)

    client = MongoClient("localhost:27017")
    db = client['ironhack']
    collection = db[collection_name]

    location = collection.find({})

    geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    location_list = list(location)
    for doc in location_list:
        for result in doc["results"]:
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        result["geocodes"]["main"]["latitude"],
                        result["geocodes"]["main"]["longitude"]
                    ]
                },
            }
            geojson["features"].append(feature)
    return geojson



def create_map(geojson_list, query_list):
    latitude = sum(feature["geometry"]["coordinates"][0] for geojson in geojson_list for feature in geojson["features"]) / len([feature for geojson in geojson_list for feature in geojson["features"]])
    longitude = sum(feature["geometry"]["coordinates"][1] for geojson in geojson_list for feature in geojson["features"]) / len([feature for geojson in geojson_list for feature in geojson["features"]])
    map = folium.Map(location=[latitude, longitude], zoom_start=13)


    for i, (geojson, query) in enumerate(zip(geojson_list, query_list)):
        folium.GeoJson(geojson).add_to(map)
        for feature in geojson["features"]:
            lat = feature["geometry"]["coordinates"][0]
            lng = feature["geometry"]["coordinates"][1]
            if 'starbucks' in query.lower():
                icon= Icon(color='green', prefix='fa', icon='coffee', icon_color='black')
            elif 'school' in query.lower():
                icon= Icon(color='red', prefix='fa', icon='graduation-cap', icon_color='black')
            elif 'sports' in query.lower():
                icon= Icon(color='blue', prefix='fa', icon='basketball', icon_color='black')
            elif 'airport' in query.lower():
                icon= Icon(color='orange', prefix='fa', icon='plane', icon_color='black')
            else:
                icon= Icon(color='red', prefix='fa', icon='graduation-cap', icon_color='black')
            Marker(location=[lat, lng], icon=icon).add_to(map)
    lat = 1.35
    lng = 103.71
    icon = Icon(color='gray', prefix='fa', icon='map-marker', icon_color='black')
    Marker(location=[lat, lng], icon=icon).add_to(map)

    map.save("maps/all_locations_map.html")

import folium

import folium

def add_marker_to_map(latitude, longitude, map_obj):
    # add a marker to the pre-existing map
    folium.Marker(location=[latitude, longitude]).add_to(map_obj)

