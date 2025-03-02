import folium
import pandas

#Definir las variables

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
el = list(data["ELEV"])

#funcion para color segun la altura

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif elevation < 2000:
        return "orange"
    else:
        return "red"
    
#Crear el mapa

map = folium.Map(location=[4.701657, -74.072470], zoom_start=4, tiles="OpenStreetMap")

#Agregar marcadores de volcanes

fg = folium.FeatureGroup(name="Volcanoes")

for lat, lon, el in zip(lat, lon, el):
    fg.add_child(folium.CircleMarker(location = [lat, lon], 
                                     radius = 7.5,
                                     fill_color = color_producer(el),
                                     color = 'grey',
                                     fill_opacity = 0.5,
                                     popup = "elevation: " + str(el) + "m"))
    
#Agregar un layer de population

with open("world.json", "r", encoding="utf-8-sig") as f:
    geojson_data = f.read()

fgv = folium.FeatureGroup(name="Population")

fgv.add_child(folium.GeoJson(data = geojson_data,
                            style_function=lambda x: {'fillColor':'green' 
                                                      if x['properties']['POP2005'] < 10000000 
                                                      else 'orange' 
                                                      if 10000000 <= x['properties']['POP2005'] < 20000000 
                                                      else 'red'}))

#llamar a la funcion para agregar los marcadores

map.add_child(fgv)
map.add_child(fg)
map.add_child(folium.LayerControl())

#Guardar el mapa en un archivo .html

map.save("mapa.html")