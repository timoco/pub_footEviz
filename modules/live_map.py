import streamlit as st
import folium
from streamlit_folium import st_folium
from utils.api import get_live_matches
from utils.geocode import geolocate

def render():
    st.subheader("📍 Live Match Map")
    matches = get_live_matches()
    map = folium.Map(location=[50, 10], zoom_start=4)

    for m in matches:
        loc = geolocate(m['fixture']['venue']['name'], m['fixture']['venue']['city'])
        winner = None
        if m['goals']['home'] > m['goals']['away']:
            winner = m['teams']['home']
        elif m['goals']['away'] > m['goals']['home']:
            winner = m['teams']['away']

        if loc and winner:
            icon = folium.CustomIcon(winner['logo'], icon_size=(40, 40))
            popup = f"{m['teams']['home']['name']} {m['goals']['home']} - {m['goals']['away']} {m['teams']['away']['name']}"
            folium.Marker([loc.latitude, loc.longitude], popup=popup, icon=icon).add_to(map)

    st_folium(map, width=1000, height=600)
