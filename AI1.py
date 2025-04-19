import streamlit as st

def run_rules(is_night, is_home, is_window_open, is_temp_low):
    output = "--- Smart Home Decision System ---\n\n"

    if is_night and is_home:
        output += "Rule: Night time & someone is home → Lights ON\n"
        output += "Action: Lights turned ON.\n\n"

    if not is_home:
        output += "Rule: No one is home → Lock Doors\n"
        output += "Action: Doors are LOCKED.\n\n"

    if is_window_open and not is_home:
        output += "Rule: Windows open & no one is home → Close Windows\n"
        output += "Action: Windows are CLOSED.\n\n"

    if is_temp_low:
        output += "Rule: Temperature is low → Turn on Heater\n"
        output += "Action: Heater is ON.\n\n"

    if output.strip() == "--- Smart Home Decision System ---":
        output += "No actions triggered based on current input."

    return output

# Streamlit UI
st.set_page_config(page_title="Smart Home Assistant", layout="centered")
st.title("🏠 Smart Home Assistant")

st.markdown("### Set Conditions:")

col1, col2 = st.columns(2)

with col1:
    is_night = st.checkbox("🌙 Is it Night Time?")
    is_home = st.checkbox("🏡 Is Someone Home?")

with col2:
    is_window_open = st.checkbox("🪟 Is Window Open?")
    is_temp_low = st.checkbox("🌡️ Is Temperature Low?")

# Buttons
if st.button("Run Assistant"):
    result = run_rules(is_night, is_home, is_window_open, is_temp_low)
    st.text_area("📝 Output", result, height=250)
elif st.button("Refresh Page"):
    st.experimental_rerun()
