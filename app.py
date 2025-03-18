import streamlit as st
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def get_coordinates(city):
    geolocator = Nominatim(user_agent="geo_distance_calculator")
    location = geolocator.geocode(city)
    if location:
        return (location.latitude, location.longitude)
    return None

def calculate_distance(capital1, capital2):
    coords1 = get_coordinates(capital1)
    coords2 = get_coordinates(capital2)
    
    if not coords1 or not coords2:
        return "❌ Impossible de trouver une ou les deux capitales."
    
    distance = geodesic(coords1, coords2).kilometers
    return f"🌍 La distance entre {capital1} et {capital2} est d'environ {round(distance, 2)} km."

st.title("🌍 Calculateur de Distance entre Capitales")

capital1 = st.text_input("Entrez la première capitale :", "Paris")
capital2 = st.text_input("Entrez la deuxième capitale :", "Berlin")

if st.button("Calculer la distance"):
    result = calculate_distance(capital1, capital2)
    st.success(result)
