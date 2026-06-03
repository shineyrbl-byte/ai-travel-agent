from tools import (
    search_flights,
    search_hotels,
    search_places,
    get_weather,
    calculate_budget
)

def generate_trip(
        source,
        destination,
        days):

    flight = search_flights(
        source,
        destination
    )

    if not flight:
        return {
            "error":
            "No flight found"
        }

    hotel = search_hotels(
        destination
    )

    places = search_places(
        destination
    )

    weather = get_weather()

    budget = calculate_budget(
        flight["price"],
        hotel["price_per_night"],
        days
    )

    itinerary = {}
    for day in range(1, days + 1):
        itinerary[f"Day {day}"] = f"Activities planned for Day {day}"

    reasoning = [
        f"Selected {flight['airline']} because it is the cheapest available flight at ₹{flight['price']}.",

        f"Selected {hotel['name']} because it has {hotel['stars']} stars.",

        "Selected top-rated attractions in the destination city.",

        "Checked weather using Open-Meteo API."
]

    result = {
        "flight": flight,
        "hotel": hotel,
        "places": places,
        "weather": weather,
        "budget": budget,
        "itinerary": itinerary,
        "reasoning": reasoning
    }

    return result