# EDUC5913 - Week 8 Assignment 🌆 City Weather Explorer

## Overview
Users can input a city name, select temperature units (°F/°C), and view:
- Current temperature (via **Open-Meteo API**)  
- City location (via **Nominatim / OpenStreetMap**)  
- A random background photo of the city (via **Unsplash API**) 

## Technical Stack
**Backend:** Python, Flask  
**Frontend:** HTML, CSS, JavaScript  
**APIs Used:**
- [Open-Meteo API](https://open-meteo.com/) — Current weather data  
- [Nominatim (OpenStreetMap)](https://nominatim.org/) — Geocoding (city → latitude/longitude)  
- [Unsplash API](https://unsplash.com/developers) — Random background images 

Note: Uses shared Unsplash API (50 requests/hour limit for everyone).
