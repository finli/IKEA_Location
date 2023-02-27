#import geopandas as gpd
import pandas as pd
import numpy as np
import requests
import urllib.parse
import time

IKEA = pd.read_csv("IKEA warehouse locations.csv", sep = ";",
                    dtype={'Latitude':float,'Longitude':float, "Zip": str})

IKEA = IKEA.dropna(axis=1, how='all')
IKEA = IKEA.dropna(axis=0, how='all')
#print(IKEA.dtypes)

IKEA['Latitude'], IKEA['Longitude']= IKEA.get('Latitude', np.nan), IKEA.get('Longitude', np.nan)

def addressToLatLong(search_str:str, verify_str:str):
    """
    Given address information, searches open street map for Latitude and Longitude.
    Parameters:
    search_str (str): A string containing combined address pieces
    verify_str (str): A string with different address pieces used to ensure correct
        address has been found

    Returns: Latitude (float), Longitude (float)
    If no response or incorrect response is found, returns np.nan.
    """
    #nominatim requires infrequent use
    print(search_str)
    print(verify_str)

    time.sleep(15)
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(search_str) +'?format=json'
    response = requests.get(url).json()
    print(response)
    #return NaN if response is empty
    if not response:
        return np.nan, np.nan

    correct_response_exists = False
    for r in response:
        #find the response with the correct verify_str
        if verify_str.casefold() in r.get("display_name").casefold():
            correct_response = r
            correct_response_exists = True

    if not correct_response_exists:
        return np.nan, np.nan

    return correct_response["lat"], correct_response["lon"]

"""
Loop through dataframe IKEA. If lat and long haven't been found, search for them.
Write results after every query to reduce numbers of queries (required by nominatim.)

Sometimes different address pieces will produce results.
The first to try is "IKEA", ["City"], ["Zip"], ["Country"],
"""

for i in IKEA.index:

    #first, check and see if long/lat has already been found, skip those
    if np.isnan(IKEA.at[i, "Latitude"]):

        address = ", ".join((IKEA.at[i, "Name"], IKEA.at[i, "Country"], str(IKEA.at[i, "Zip"])))
        #address = ", ".join(("IKEA", str(IKEA.at[i, "Street"]), IKEA.at[i, "Country"]))
        IKEA.at[i, "Latitude"], IKEA.at[i, "Longitude"] = addressToLatLong(address, IKEA.at[i, "City"])
        #address = ", ".join((IKEA.at[i, "Country"], IKEA.at[i, "Street"]))
        #IKEA.at[i, "Latitude"], IKEA.at[i, "Longitude"] = addressToLatLong(address, IKEA.at[i, "City"])
        IKEA.to_csv("IKEA_warehouse_latlong.csv", index=False, na_rep='NaN')
        print(IKEA.at[i, "Latitude"], IKEA.at[i, "Longitude"])
print(IKEA)

#must use zip because the list comprehension turns into a list of tuple
#IKEA["lat"], IKEA["long"] = zip(* [AddressToLatLong(x) for x in zip(IKEA["Street"], ", ".join(("IKEA", IKEA["City"], IKEA["Zip"], IKEA["Country"]))) ] )
