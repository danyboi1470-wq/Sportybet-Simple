import streamlit as st

st.title("SportyBet Simple Betting Guide")

st.header("Football (First Half)")

underdog_odds = st.number_input("Underdog Odds", 1.01)
league_fh_bias = st.slider("League FH Goal %", 0, 100)
early_pressure = st.checkbox("Early Pressure Seen?")

if 2.40 <= underdog_odds <= 4.50 and league_fh_bias >= 80 and early_pressure:
    st.success("PLAY: FH 1Up or FH GG")
    st.write("Cash-out immediately after first goal")
else:
    st.error("SKIP MATCH")

st.divider()

st.header("Table Tennis")

time_window = st.selectbox(
    "Time Window",
    ["01:00–05:00", "16:20–18:00", "19:00–21:30"]
)

odds = st.number_input("Selected Odds", 1.01)

if time_window == "01:00–05:00" and 2.10 <= odds <= 2.80:
    st.success("PLAY: Game 1 Winner")
    st.write("Cash-out after Set 1")
elif time_window != "01:00–05:00" and 1.70 <= odds <= 2.40:
    st.success("PLAY: Game 1 Winner")
    st.write("Cash-out after Set 1")
else:
    st.error("SKIP TABLE TENNIS")
