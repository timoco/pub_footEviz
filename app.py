import streamlit as st
from modules import live_map, heatmap, calendar_view, league_stats
from utils.session import init_session

st.set_page_config(page_title="⚽ European Football Dashboard", layout="wide")
init_session()

st.sidebar.title("Settings")
st.sidebar.checkbox("Dark Mode", key="dark_mode")
st.sidebar.slider("Refresh Interval (sec)", 30, 300, 60, key="refresh_interval")

st.sidebar.title("Visualizations")
selected_views = st.sidebar.multiselect(
    "Choose views to display:",
    ["Live Map", "Heatmap", "Calendar", "League Stats"],
    default=["Live Map"]
)

if "Live Map" in selected_views:
    live_map.render()
if "Heatmap" in selected_views:
    heatmap.render()
if "Calendar" in selected_views:
    calendar_view.render()
if "League Stats" in selected_views:
    league_stats.render()
