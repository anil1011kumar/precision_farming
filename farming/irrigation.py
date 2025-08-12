def should_irrigate(soil_moisture,rain_mm):
    return soil_moisture < 400 and rain_mm < 1.0 