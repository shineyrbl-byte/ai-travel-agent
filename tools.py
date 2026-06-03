import requests
import json
def search_flights(source, destination):

    with open("data/flights.json", "r") as f:
        flights = json.load(f)

    matching_flights = [
        flight for flight in flights
        if flight["from"].lower() == source.lower()
        and flight["to"].lower() == destination.lower()
    ]

    if not matching_flights:
        return None

    cheapest = min(
        matching_flights,
        key=lambda x: x["price"]
    )

    return cheapest

def search_hotels(city):

    with open("data/hotels.json", "r") as f:
        hotels = json.load(f)

    city_hotels = [
        hotel for hotel in hotels
        if hotel["city"].lower() == city.lower()
    ]

    if not city_hotels:
        return None

    best_hotel = max(
        city_hotels,
        key=lambda x: x["stars"]
    )

    return best_hotel

def search_places(city):

    with open("data/places.json", "r") as f:
        places = json.load(f)

    city_places = [
        place for place in places
        if place["city"].lower() == city.lower()
    ]

    city_places.sort(
        key=lambda x: x["rating"],
        reverse=True
    )

    return city_places[:5]

def get_weather():

    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=15.289983"
        "&longitude=74.142456"
        "&daily=temperature_2m_max"
        "&timezone=auto"
    )

    response = requests.get(url)

    data = response.json()

    return data["daily"]

def calculate_budget(
        flight_price,
        hotel_price,
        days):

    food_cost = 800 * days

    transport_cost = 1000

    total = (
        flight_price
        + hotel_price * days
        + food_cost
        + transport_cost
    )

    return total