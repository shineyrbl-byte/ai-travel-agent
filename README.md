# AI Travel Agent

## Overview

AI Travel Agent is an intelligent travel planning application that automatically generates personalized travel itineraries using flight data, hotel recommendations, tourist attractions, weather forecasts, and budget estimation.

The project demonstrates an agentic workflow using LangChain tools, JSON datasets, and the Open-Meteo weather API.

---

## Problem Statement

Travelers often need to search across multiple websites to compare flights, hotels, attractions, and weather conditions before planning a trip. This process is time-consuming and can lead to inefficient travel plans.

This project automates the travel planning process by gathering relevant information and generating a structured itinerary tailored to the user's requirements.

---

## Features

* Flight search from JSON dataset
* Hotel recommendation from JSON dataset
* Attraction discovery from JSON dataset
* Real-time weather forecast using Open-Meteo API
* Budget estimation
* Day-wise itinerary generation
* Agent reasoning and decision explanation
* Streamlit-based user interface
* LangChain tool integration

---

## Technologies Used

* Python
* Streamlit
* LangChain
* Ollama / OpenAI
* Open-Meteo API
* JSON Datasets

---

## Project Structure

travel_agent/

├── app.py

├── agent.py

├── tools.py

├── langchain_agent.py

├── requirements.txt

└── data/

    ├── flights.json

    ├── hotels.json

    └── places.json

---

## Agent Workflow

User Input

↓

Flight Search Tool

↓

Hotel Recommendation Tool

↓

Places Discovery Tool

↓

Weather Forecast Tool

↓

Budget Estimation

↓

Itinerary Generation

↓

Final Travel Plan

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

---

## Sample Output

The system provides:

* Recommended flight
* Recommended hotel
* Top attractions
* Weather forecast
* Budget breakdown
* Day-wise itinerary
* Agent reasoning

---

## Future Enhancements

* Real-time flight APIs
* Hotel booking integration
* Multi-city trip planning
* Personalized recommendations
* Route optimization

---

## Author

Avisha Srivastava

AI Travel Agent Internship Project
