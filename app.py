from flask import Flask, render_template, request, jsonify
import requests
import os

# Load environment variables from .env file
if os.path.exists('.env'):
    with open('.env') as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

# Create Flask app
app = Flask(__name__)

# Unsplash Access Key (from environment variable)
UNSPLASH_ACCESS_KEY = os.environ.get('UNSPLASH_ACCESS_KEY', '')

# 1: Show the main home page
@app.route('/')
def show_home_page():
    # return the html template
    return render_template('index.html')

# 2: API endpoint to get weather and photo for a city
@app.route('/api/city')
def get_city_info():
    # get city name from url parameter (default is Beijing)
    city = request.args.get('city', 'Beijing')
    
    try:
        # STEP 1: get city location (latitude and longitude)
        # Call OpenStreetMap API to find the city
        location_url = "https://nominatim.openstreetmap.org/search"
        location_params = {
            "q": city,              # search query (city name)
            "format": "json",    
            "limit": 1              # only need first result
        }
        location_headers = {
            "User-Agent": "WeatherApp/1.0",
            "Accept-Language": "en"  
        }
        location_response = requests.get(location_url, params=location_params, headers=location_headers, timeout=10)
        location_data = location_response.json()
        
        # Check if city was found
        if not location_data:
            return jsonify({"error": "City not found"}), 400
        
        # extract latitude and longitude from response
        lat = float(location_data[0]["lat"])
        lon = float(location_data[0]["lon"])
        city_name = location_data[0]["name"]
        
        # STEP 2: get weather temperature
        # Call Open-Meteo API to get current temperature
        weather_url = "https://api.open-meteo.com/v1/forecast"
        weather_params = {
            "latitude": lat,                    # city latitude
            "longitude": lon,                   # city longitude
            "current": "temperature_2m",        # temperature at 2m height
            "temperature_unit": "celsius"       # use celsius unit
        }
        weather_response = requests.get(weather_url, params=weather_params, timeout=10)
        weather_data = weather_response.json()
        
        # get temperature value
        temperature = weather_data["current"]["temperature_2m"]
        
        # STEP 3: get photo from Unsplash
        photo_url = get_city_photo(city)
        
        # STEP 4: return all data as json
        result = {
            "city": city_name,
            "temp": temperature,
            "photo": photo_url
        }
        return jsonify(result)
        
    except Exception as error:
        # if anything goes wrong, return error message
        return jsonify({"error": str(error)}), 400

# Helper function to get photo from Unsplash
def get_city_photo(city_name):
    try:
        # search Unsplash for photos of this city
        unsplash_url = "https://api.unsplash.com/search/photos"
        unsplash_params = {
            "query": city_name,           # search term (city name)
            "per_page": 1,            
            "orientation": "landscape"  
        }
        unsplash_headers = {
            "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"
        }
        
        # Make request to Unsplash API
        unsplash_response = requests.get(unsplash_url, params=unsplash_params, headers=unsplash_headers, timeout=10)
        
        # if successful, get photo data
        if unsplash_response.status_code == 200:
            photo_data = unsplash_response.json()
            
            if photo_data.get("results"):
                # return the full size photo URL
                photo_url = photo_data["results"][0]["urls"]["full"]
                return photo_url
        
        # If Unsplash API failed, use fallback
        return get_fallback_photo(city_name)
        
    except:
        # if error, use fallback photo
        return get_fallback_photo(city_name)

# Helper function for fallback photo service
def get_fallback_photo(city_name):
    # replace spaces with + for url
    city_formatted = city_name.replace(' ', '+')
    photo_url = f"https://source.unsplash.com/1920x1080/?{city_formatted}"
    return photo_url

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=False)