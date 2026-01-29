import streamlit as st
import datetime
import requests
import pandas as pd
import plotly.express as px

#   FUNCTION FOR GETTING THE ICON BASED ON THE WEATHER
def get_weather_emoji(condition, icon_code):
    condition = condition.lower()
    is_night = icon_code.endswith("n")

    if "clear" in condition:
        return "🌕" if is_night else "☀️"
    elif "cloud" in condition:
        return "☁️" if is_night else "⛅"
    elif "rain" in condition:
        return "🌧️"
    elif "thunder" in condition:
        return "⛈️"
    elif "snow" in condition:
        return "❄️"
    elif "mist" in condition or "fog" in condition:
        return "🌫️"
    else:
        return "🌍"
# OPEN_WEATHERMAP API KEY FOR ACCESSING THE REAL TIME WEATHER FROM THE STATIONS
WEATHER_API_KEY = 'b87dcc8900c22fd984d274de1d3c6ed0'
st.set_page_config(layout="wide",page_title="Weather Forecast",page_icon='☀️' )
st.header("Weather Dashboard ⛅")
st.markdown("---")
st.write("## CITY")
city_name = st.text_input("")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={WEATHER_API_KEY}"
response = requests.get(url)
data = response.json()

# SUCCESS MESSAGE IF THE CITY IS FOUND
if city_name:
    if data["cod"] == 200:
        st.success(":blue[WEATHER CONDITION FOUND!]")
else:
    st.write(":blue[please enter a city name to get the weather, check that you have entered a valid city name]")

col1, col2 = st.columns(2,border=True,gap="small")
""" COLUMN 1 FOR DISPLAYING THE 
        1) CITY NAME
        2) TEMPERATURE
        3) DESCRIPTION
 """
with col1:
    st.write("# TODAY's WEATHER")
    st.markdown("---")
    if city_name:
        if data["cod"] == 200:
            try:
                condition = data["weather"][0]["main"]
                icon_code = data["weather"][0]["icon"]

                emoji = get_weather_emoji(condition, icon_code)

                st.markdown(
                    f"<h1 style='font-size:100px;text-align:center'>{emoji}</h1>",
                    unsafe_allow_html=True
                )
                city_name = data["name"]
                temperature = f"{round(data["main"]["temp"] - 273.15)}°f"
                descriptions = f"{data['weather'][0]['description']}"
                st.write(f"### CITY NAME: {city_name} ")
                st.write(f"### TEMPERATURE: {temperature}")
                st.write(f"### DESCRIPTIONS: {descriptions}")
            except requests.exceptions:
                st.write(":red[please check your city name]")
    else:
        st.write("## weather condition:")

""" COLUMN 2 FOR DISPLAYING THE 
        1) FEELS LIKE CONDITION
        2) HUMIDITY
        3) WIND SPEED
        4) PRESSURE """

with col2:
    if city_name:
        if data["cod"] == 200:
            try:
                today = datetime.datetime.now()
                day_name = today.strftime("%A")
                st.write(f"### DAY: {day_name.upper()}")
                st.markdown("---")
                feel_like = data["main"]["feels_like"]
                humid = data["main"]["humidity"]
                wind_speeds = data["wind"]["speed"]
                pressures = data["main"]["pressure"]
                st.write(f"## FEEL LIKE: {round(feel_like - 273.15)}°f")

                st.metric( label="pressure", value=f"{pressures}pas" ,delta="1pas",border=True)
                st.metric(label="humidity", value=f"{humid}g/m3",delta="1g/m3",border=True)
                st.metric(label="wind speed", value=f"{wind_speeds}m/s",delta="1m/s",border=True)
            except Exception as e:
                st.write(str(e))

    else:
        st.write("# ATTRIBUTES")

"""------------------------------------------------------------------------- 
              THIS IS CODE FOR DISPLAYING THE PLOT BETWEEN THE HUMIDITY AND THE PRESSURE """
weather_df = pd.DataFrame({
    "Parameter": ["Humidity", "Pressure"],
    "Value": [humid, pressures]
})


fig = px.bar(
    weather_df,
    x="Parameter",
    y="Value",
    title="Humidity & Pressure Levels",
    text="Value"
)

fig.update_layout(
    title_x=0.5,
    height=400
)

st.plotly_chart(fig, use_container_width=True)

with col2:
    if city_name:
        if data["cod"] == 200:
            today = datetime.datetime.now()
            day_name = today.strftime("%A")

            st.write(f"### DAY: {day_name.upper()}")
            st.markdown("---")

            feel_like = data["main"]["feels_like"]
            humid = data["main"]["humidity"]
            wind_speeds = data["wind"]["speed"]
            pressures = data["main"]["pressure"]

            st.write(f"## FEELS LIKE: {round(feel_like - 273.15)}°C")

            st.metric("Pressure", f"{pressures} hPa")
            st.metric("Humidity", f"{humid} %")
            st.metric("Wind Speed", f"{wind_speeds} m/s")

            # 🔽 PLOT
            weather_df = pd.DataFrame({
                "Parameter": ["Humidity", "Pressure"],
                "Value": [humid, pressures]
            })

            fig = px.bar(
                weather_df,
                x="Parameter",
                y="Value",
                title="Humidity & Pressure Levels",
                text="Value"
            )

            st.plotly_chart(fig, use_container_width=True)


