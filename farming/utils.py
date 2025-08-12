import requests

def get_weather_data():
    API_KEY = '65412ae8bf39f76d9e6c779206c4f1a2'
    LAT = '28.6139'
    LON = '77.2090'

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        return {
            'temprature' : data['main']['temp'],
            'humidity' : data['main']['humidity'],
            'rain' : data.get('rain',{}.get('1h',0.0))
        }
    except:
        return {'temprature' : 0, 'humidity' : 0, 'rain' : 0}
    

def get_fertilizer_recommendation(crop_type, soil_type, season):
    crop_type = crop_type.strip().lower()
    soil_type = soil_type.strip().lower()
    season = season.strip().lower()
    recommendation = {
        "wheat": {
            "loamy" : "Urea 50kg/acre, DAP 40kg/acre",
            "clayey" : "Urea 45kg/acre, SSP 50kg/acre",
            "sandy" : "Urea 55kg/acre, DAP 35kg/acre",

        },
        "rice" :{
            "loamy" : "Urea 60kg/acre, MOP 25kg/acre",
            "clayey" : "Urea 55kg/acre, DAP 30kg/acre",
            "sandy" : "Urea 65kg/acre, SSP 40kg/acre",
        },
        "maize": {
            "loamy" : "Urea 40kg/acre, DAP 35kg/acre",
            "clayey" : "Urea 38kg/acre, SSP 45kg/acre",
            "sandy" : "Urea 42kg/acre, DAP 30kg/acre",

        }
    }


    #season based adjustment
    if season.lower() =="summer":
        note= "increase irrigation frequency due to high temprature."
    elif season.lower() =="winter":
        note= "Reduce nitrogen fertiliser slightly in cold weather."
    else:
        note= "Maintain balanced fertiliser usage."

    crop_type = crop_type.lower()
    soil_type = soil_type.lower()
    result = recommendation.get(crop_type,{}).get(soil_type, "no data for given crop/soil.")
    return f"Recommended Fertiliser: {result}. Note: {note}"