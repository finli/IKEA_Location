# IKEA_Location
I did a small project to practice using https://nominatim.openstreetmap.org and GeoPandas.
Since I am located in Sweden, I thought it would be fun to plot the location of
every IKEA warehouse.

# Data Collection
I found this wikipedia article that lists all of the countries with IKEA stores. I then looked at the official IKEA webpage for each country to get the address of each store. I manually
added these to my file. I used my python script find_lat_long.py to look for the latitude and longitude of each store based on its address. This worked well for many countries. When the languages were significantly different from English, this did not work well. In that case, I had to manually find the latitude and longitude from Google Maps.

China was an especially difficult country. Google maps is not often used there and the information on Google was unreliable. Additionally, there were many stores listed as IKEAs on google maps, such as “IKEA leisure hotel”, “IKEA Northeast Speciality Food Supermarket”, “IKEA supermarket”, “Esteem Ikea Home Textile Discount Factory”, “Ikea Convenience Store”, “IKEA heating”, and “IKEA wine and cigarette.” I am not sure if the name IKEA isn’t protected in China, so many stores were using it, or if they were spurious listings on Google Maps.



Findings: There is only one IKEA in South America (in Chile). There are 3 in Africa (all in Egypt). There were 13 IKEAs in Russia, but they all closed last year because of Russia’s attack on Ukraine.
