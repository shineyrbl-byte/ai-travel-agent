import streamlit as st
from agent import generate_trip
from langchain_agent import show_available_tools

st.title("AI Travel Agent")
st.sidebar.subheader("LangChain Tools")

for tool in show_available_tools():
    st.sidebar.write("✓", tool)

source = st.text_input(
    "Source City"
)

destination = st.text_input(
    "Destination City"
)

days = st.slider(
    "Trip Duration",
    1,
    7,
    3
)

if st.button("Generate Trip"):

    result = generate_trip(
        source,
        destination,
        days
    )
    st.write("### Day-wise Itinerary")
    st.json(result["itinerary"])

    st.subheader("Trip Summary")

    st.write("### Flight")
    st.json(result["flight"])

    st.write("### Hotel")
    st.json(result["hotel"])

    st.write("### Places to Visit")
    st.json(result["places"])

    st.write("### Weather Forecast")
    weather = result["weather"]
    for date, temp in zip(
            weather["time"],
            weather["temperature_2m_max"]):
        st.write(
            f"{date} : {temp}°C"
    )

    st.write("### Estimated Budget")
    st.success(f"₹{result['budget']}")

    st.write("### Agent Reasoning")
    for r in result["reasoning"]:
        st.write("•", r)

    st.subheader("Agent Workflow")

    st.markdown("""
    1. User enters trip details.
    2. Flight Search Tool finds available flights.
    3. Hotel Search Tool recommends accommodation.
    4. Places Search Tool finds attractions.
    5. Weather Search Tool fetches forecast.
    6. Budget Tool estimates total trip cost.
    7. Agent combines results into itinerary.
""")