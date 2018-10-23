'''
Created on Oct 22, 2018

@author: orcasweb
'''
import folium

neighborhoods = ['Palermo', 'Ricoleta', 'Santelmo', 'Puerto Madero', 'Belgrano', 'La Boca']
palermo = neighborhoods[0]
la_boca = neighborhoods[-1]
print(neighborhoods)

coordinates = [-34.6037, -58.3816]
ba_latitude = coordinates[0]
ba_longitude = coordinates[1]

buenos_map = folium.Map([ba_latitude, ba_longitude])
buenos_marker = folium.Marker([ba_latitude, ba_longitude])
buenos_marker.add_to(buenos_map)
buenos_markers = [buenos_marker]
neighborhoods = ['Palermo', 'Ricoleta', 'Santelmo', 'Puerto Madero', 'Belgrano', 'La Boca']
marker_one = folium.Marker([-34.5711, -58.4233])
marker_two = folium.Marker([-34.5895, -58.3974])
marker_three = folium.Marker([-34.6212, -58.3731])
marker_four = folium.Marker([-34.6177, -58.3621])
marker_five = folium.Marker([-34.603722,  -58.381592])
marker_six = folium.Marker([-34.6345, -58.3631])
neighborhood_markers = [marker_one, marker_two, marker_three, marker_four, marker_five, marker_six]
buenos_map = folium.Map([-34.6037, -58.3816], zoom_start = 12)
for marker in neighborhood_markers:
    marker.add_to(buenos_map)
buenos_map

