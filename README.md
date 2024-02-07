# Weather City
<p align="center">
  <img src="screenshots/pc.jpeg" alt="mobile device" width="400" />
</p>

This application allows you to view the following weather details for any city you desire, thanks to the OpenWeatherMap API:

- Current weather condition (sunny, rainy, cloudy)
- Current temperature
- Minimum and maximum temperature
- Sunrise and sunset times
- Humidity percentage
- Wind speed in m/s

## Getting Started

These instructions will guide you on how to run this application on your local machine.

### Prerequisites

- Python 3 installed on your machine.
- An API key from OpenWeatherMap.

### Installation

1. Clone the repository to your local machine.

```bash
git clone https://github.com/AlexGioffDev/weather
```

2. Navigate to the project directory.
```bash
cd weather
```

3. Install the required Python packages using the requirements.txt file
```bash
pip install -r requirements.txt
```

4.Create a .env file in the weather_main directory and add your OpenWeatherMap API key in the following format:
```bash
API_KEY_WEATHER=<your_api_key>
```

5.Navigate to the weather_main directory in your terminal and run the following command to start the server:
```bash
python3 manage.py runserver
```
