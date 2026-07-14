import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Set up professional page configuration
st.set_page_config(page_title="AI Cricket Scout", layout="wide")

# Title and Layout Introduction
st.title("🏏 AI Cricket Scout: Volatility-Based T20 Predictor")
st.markdown("---")

# 1. Simulate Loading Your Data State Safely
# (In production, you would read the 'ml_dataset' variable we created earlier)
@st.cache_data
def load_mock_frontend_data():
    # Creating a small sample dataset so this app runs instantly for you
    players = ['Virat Kohli', 'Rohit Sharma', 'Suryakumar Yadav', 'Hardik Pandya']
    data = []
    np.random.seed(42)
    for p in players:
        for match in range(1, 15):
            runs = int(np.random.normal(35, 20))
            runs = max(0, runs) # No negative runs
            data.append({
                'batter': p,
                'match_id': f"Match_{match}",
                'runs_scored': runs,
                'rolling_avg_3': int(np.random.normal(35, 5)),
                'runs_volatility': int(np.random.normal(15, 3))
            })
    return pd.DataFrame(data)

df_frontend = load_mock_frontend_data()

# ==========================================
# SIDEBAR CONTROLS
# ==========================================
st.sidebar.header("Scouting Filters")
selected_player = st.sidebar.selectbox("Select a Batsman to Analyze", df_frontend['batter'].unique())

# Filter dataset for the chosen player
player_df = df_frontend[df_frontend['batter'] == selected_player].reset_index(drop=True)
latest_stats = player_df.iloc[-1]

# ==========================================
# MAIN DASHBOARD VISUALS
# ==========================================

# Row 1: Key Performance Indicator (KPI) Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Recent Form (3-Match Avg)", value=f"{latest_stats['rolling_avg_3']} runs")

with col2:
    st.metric(label="Innings Consistency Risk (Volatility)", value=f"{latest_stats['runs_volatility']} SD")
    
with col3:
    # Simulate our Random Forest Classifier predictions for the upcoming match
    # Class 0: Failure, Class 1: Anchor, Class 2: Match Winner
    predicted_class = np.random.choice(["Early Dismissal (<15)", "Anchor (15-40)", "Match Winner (>40)"])
    st.metric(label="AI Predicted Output Band (Next Match)", value=predicted_class)

st.markdown("---")

# Row 2: Interactive Data Visualization Charts
col4, col5 = st.columns(2)

with col4:
    st.subheader("📈 Chronological Run Timeline")
    # Interactive line chart using Plotly
    fig_line = px.line(player_df, x='match_id', y='runs_scored', markers=True, 
                       labels={'runs_scored': 'Runs Scored', 'match_id': 'Match Timeline'},
                       title=f"Scoring Trajectory for {selected_player}")
    fig_line.update_traces(line_color='#2E86C1', line_width=3)
    st.plotly_chart(fig_line, use_container_width=True)

with col5:
    st.subheader("🎯 Distribution of Scoring Form")
    # Histogram showing the volatility spread of their scores
    fig_hist = px.histogram(player_df, x='runs_scored', nbins=5,
                            labels={'runs_scored': 'Runs Range'},
                            title=f"Innings Dispersion Profile",
                            color_discrete_sequence=['#1ABC9C'])
    st.plotly_chart(fig_hist, use_container_width=True)