// all html elements
const cityInput = document.getElementById('cityInput');
const cityDisplay = document.getElementById('cityDisplay');
const tempValue = document.getElementById('tempValue');
const unitDisplay = document.getElementById('unitDisplay');
const unitSelect = document.getElementById('unitSelect');
const searchBtn = document.getElementById('searchBtn');
const bgElement = document.querySelector('.bg');

let currentTemp = 0; 

// Convert celsius to fahrenheit
function celsiusToFahrenheit(c) {
  return (c * 9/5) + 32;
}

// Update the temperature display based on selected unit
function updateTempDisplay() {
  const unit = unitSelect.value;
  if (unit === 'celsius') {
    tempValue.textContent = Math.round(currentTemp);
    unitDisplay.textContent = '°C';
  } else {
    const fahrenheit = celsiusToFahrenheit(currentTemp);
    tempValue.textContent = Math.round(fahrenheit);
    unitDisplay.textContent = '°F';
  }
}

// Setup all event listeners
function setupEventListeners() {
    searchBtn.addEventListener('click', loadWeather);
    cityInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') loadWeather();
    });
    unitSelect.addEventListener('change', updateTempDisplay);
}

// load weather data and photo for the city
async function loadWeather() {
  const city = cityInput.value || 'Philadelphia';
  cityDisplay.textContent = 'Loading...';
  
  try {
    // fetch weather data from api
    const res = await fetch(`/api/city?city=${city}`);
    const data = await res.json();
    cityDisplay.textContent = data.city;
    currentTemp = data.temp;
    updateTempDisplay();
    
    // Set background image
    if (data.photo && bgElement) {
      console.log('Setting background:', data.photo);
      bgElement.style.backgroundImage = `url("${data.photo}")`;
      bgElement.style.backgroundSize = 'cover';
      bgElement.style.backgroundPosition = 'center';
    } else {
      console.error('Photo data missing or bgElement not found');
    }
  } catch(e) {
    console.error('Error loading weather:', e);
    cityDisplay.textContent = 'Error: ' + e.message;
  }
}

// Start the app when page is loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
        setupEventListeners();
        loadWeather();
    });
} else {
    setupEventListeners();
    loadWeather();
}
