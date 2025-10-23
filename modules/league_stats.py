import streamlit as st
import pandas as pd
import plotly.express as px
from utils.api import get_live_matches

def render():
    st.subheader("📊 League Stats")
    matches = get_live_matches()
    stats = {}

    for m in matches:
        league = m['league']['name']
        stats.setdefault(league, {"goals": 0, "matches": 0})
        stats[league]["goals"] += m['goals']['home'] + m['goals']['away']
        stats[league]["matches"] += 1

    df = pd.DataFrame([
        {"League": k, "Goals": v["goals"], "Matches": v["matches"]}
        for k, v in stats.items()
    ])

    fig = px.bar(df, x="League", y="Goals", title="Goals by League")
    st.plotly_chart(fig, use_container_width=True)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install streamlit folium streamlit-folium plotly geopy requests
