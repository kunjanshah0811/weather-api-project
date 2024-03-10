# weather-api-project
This project utilizes the OpenWeatherMap API to fetch weather data for specified cities. It provides the current temperature along with today's high and low temperatures for the given city coordinates.

## Usage
To use this project, simply create an instance of the `City` class with the desired city name, latitude, and longitude. Optionally, you can specify the temperature units (default is metric).

```python
my_city = City("Paderborn", 51.7189, 8.7575)
vacation_city = City('Vadodara', 22.310696, 73.192635)
```
## Requirements
- Python 3.x
- requests library

## How to Run
1. Install the requests library if you haven't already:
```python
  pip install requests
```

2. Run the script:
```python
   python weather.py
```
