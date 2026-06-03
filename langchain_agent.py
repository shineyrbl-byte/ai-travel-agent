from langchain_core.tools import tool

@tool
def flight_search(query: str):
    """Search flights."""
    return "Flight tool available"

@tool
def hotel_search(city: str):
    """Search hotels."""
    return "Hotel tool available"

@tool
def places_search(city: str):
    """Search attractions."""
    return "Places tool available"

@tool
def weather_search(city: str):
    """Get weather forecast."""
    return "Weather tool available"


def show_available_tools():
    return [
        flight_search.name,
        hotel_search.name,
        places_search.name,
        weather_search.name
    ]