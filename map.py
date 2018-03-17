import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Mapbox Bright")

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


fg=folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat,lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln],popup=str(el)+" m",radius=6,color="grey",fill_opacity=0.7, fill_color=color_producer(el)))


#fg.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig'), style_function=lambda x:{'fill_color':'yellow' if x['properties']['POP2005'] < 10000000}))

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
map.save("Map5.html")
