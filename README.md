# Weather Dashboard ⛅

A real-time weather dashboard built with Streamlit that displays current weather conditions for any city in the world.

## Features

- 🌍 **Real-time Weather Data**: Get current weather information for any city
- 🎨 **Dynamic Weather Icons**: Weather emojis that change based on conditions and time of day
- 📊 **Comprehensive Metrics**: View temperature, humidity, wind speed, and pressure
- 🌡️ **Feels Like Temperature**: Experience the perceived temperature
- 🎯 **User-friendly Interface**: Clean and intuitive two-column layout
- 📱 **Responsive Design**: Works on desktop and mobile devices

## Weather Information Displayed

- **City Name**: The location you searched for
- **Temperature**: Current temperature in Fahrenheit
- **Weather Description**: Detailed weather condition
- **Feels Like**: Perceived temperature based on wind and humidity
- **Humidity**: Air moisture level
- **Wind Speed**: Current wind speed in m/s
- **Pressure**: Atmospheric pressure
- **Day**: Current day of the week
- **Weather Emoji**: Visual representation of weather conditions

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd weather-dashboard
```

2. Create a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:
   - **Windows (PowerShell)**:
   ```bash
   .\.venv\Scripts\Activate.ps1
   ```
   - **Windows (Command Prompt)**:
   ```bash
   .venv\Scripts\activate.bat
   ```
   - **macOS/Linux**:
   ```bash
   source .venv/bin/activate
   ```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
streamlit run weather.py
```

The application will open in your default web browser at `http://localhost:8501`

## Dependencies

- `streamlit`: Web framework for building the dashboard
- `requests`: HTTP library for API calls
- `pandas`: Data manipulation and analysis
- `plotly`: Interactive visualizations

See `requirements.txt` for specific versions.

## API Configuration

This application uses the **OpenWeatherMap API** to fetch real-time weather data.

**Note**: The API key is currently hardcoded in the script. For production use, it's recommended to:
- Use environment variables to store the API key
- Never commit API keys to version control

## Usage

1. Enter a city name in the text input field
2. The dashboard will automatically fetch and display weather information
3. View detailed weather metrics in the two-column layout
4. Error messages will appear if an invalid city name is entered

## Weather Emoji Legend

- ☀️ / 🌕: Clear weather (day/night)
- ⛅ / ☁️: Cloudy weather (day/night)
- 🌧️: Rainy weather
- ⛈️: Thunderstorm
- ❄️: Snow
- 🌫️: Mist/Fog
- 🌍: Unknown weather condition

## Project Structure

```
weather-dashboard/
├── weather.py          # Main application file
├── requirements.txt    # Project dependencies
└── README.md          # This file
```

## Error Handling

The application includes error handling for:
- Invalid city names
- Network connectivity issues
- API response errors

If an error occurs, a red error message will be displayed to guide the user.

## Future Enhancements

- [ ] 7-day forecast display
- [ ] Weather alerts and warnings
- [ ] Historical weather data
- [ ] Multiple city comparison
- [ ] Save favorite cities
- [ ] Dark mode theme
- [ ] Secure API key management with environment variables

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests for any improvements.

## Contact

For questions or suggestions, please open an issue in the repository.

---

**Disclaimer**: Weather data is provided by OpenWeatherMap. Please refer to their terms of service for usage guidelines.
