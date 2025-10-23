import streamlit as st
import pandas as pd
import plotly.express as px
from utils.api import get_live_matches

def render():
    st.subheader("📅 Fixture Calendar")
    matches = get_live_matches()
    data = []

    for m in matches:
        data.append({
            "Match": f"{m['teams']['home']['name']} vs {m['teams']['away']['name']}",
            "Start": m['fixture']['date'],
            "League": m['league']['name']
        })

    df = pd.DataFrame(data)
    fig = px.timeline(df, x_start="Start", x_end="Start", y="Match", color="League")
    st.plotly_chart(fig, use_container_width=True)
