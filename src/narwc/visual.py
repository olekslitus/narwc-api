"""..."""

import folium
import webbrowser

output_file = "map2.html"

map = folium.Map(location=[45.372, -121.6972], zoom_start=12, tiles="openstreetmap.hot")

tooltip = "Click me!"

folium.Marker(
    [45.3288, -121.6625], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip
).add_to(map)
folium.Marker(
    [45.3311, -121.7113], popup="<b>Timberline Lodge</b>", tooltip=tooltip
).add_to(map)

map.save(output_file)

webbrowser.open(output_file)
