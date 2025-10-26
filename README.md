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

## Deployment
Deployed on Render: https://city-explorer.onrender.com  
⚠️ **Note:** Uses shared Unsplash API with 50 requests/hour limit.

## Local Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Create `.env` file with your Unsplash access key:
   ```
   UNSPLASH_ACCESS_KEY=your_key_here
   ```
3. Run the app: `python app.py`
4. Open http://localhost:5001
