import streamlit as st
from folium.plugins import HeatMap
from streamlit_folium import st_folium
from utils.api import get_live_matches
from utils.geocode import geolocate
import folium

def render():
    st.subheader("🔥 Match Density Heatmap")
    matches = get_live_matches()
    map = folium.Map(location=[50, 10], zoom_start=4)
    heat_data = []

    for m in matches:
        loc = geolocate(m['fixture']['venue']['name'], m['fixture']['venue']['city'])
        if loc:
            heat_data.append([loc.latitude, loc.longitude])

    HeatMap(heat_data).add_to(map)
    st_folium(map, width=1000, height=600)
