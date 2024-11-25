# Weather Fetcher - retrieves and displays real-time weather information for a specified city

import requests

api_key = "951de00d747f49c89044a471de64427e" # weather api key
base_url = "https://api.openweathermap.org/data/2.5/weather"  # Base URL for the weather API endpoint

city = input("Enter a city: ") # user input
request_url = f'{base_url}?appid={api_key}&q={city}'  # full API request URL with "city" and API key
response = requests.get(request_url)  # send getrequest to API

# Check if the request was successful (status code 200 - means "OK")
if response.status_code == 200:
    data = response.json()  # parse the JSON response from the API
    weather = data['weather'][0]['description']  # extract the weather description from the API response
    print("Weather conditions: ", weather)  # display the weather conditions

    # Convert the temperature from Kelvin to Celsius and then to Fahrenheit
    c_temperature = round(data['main']['temp'] - 273.15, 2)  # convert from Kelvin to Celsius
    f_temperature = round(c_temperature * (9/5) + 32, 2)  # convert from Celsius to Fahrenheit
    print("It is currently ", c_temperature, "°C", " or ", f_temperature, "°F")  # display the temperatures

else:
    print("An error has occurred. Try a different city.")  # display an error message if the request was unsuccessful
