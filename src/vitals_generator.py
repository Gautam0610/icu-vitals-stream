
import time
import random

def generate_vitals():
    # Generate realistic vital signs with constraints
    heart_rate = int(random.gauss(75, 15))  # Avg 75, SD 15
    heart_rate = max(30, min(heart_rate, 180)) # Realistic range

    blood_pressure_systolic = int(random.gauss(120, 20))
    blood_pressure_systolic = max(60, min(blood_pressure_systolic, 220))

    blood_pressure_diastolic = int(random.gauss(80, 10))
    blood_pressure_diastolic = max(40, min(blood_pressure_diastolic, 140))

    oxygen_saturation = int(random.gauss(95, 3))
    oxygen_saturation = max(70, min(oxygen_saturation, 100))

    respiration_rate = int(random.gauss(16, 4))
    respiration_rate = max(8, min(respiration_rate, 30))

    temperature = round(random.gauss(37, 0.5), 1)
    temperature = max(35, min(temperature, 42))

    return {
        "heart_rate": heart_rate,
        "blood_pressure_systolic": blood_pressure_systolic,
        "blood_pressure_diastolic": blood_pressure_diastolic,
        "oxygen_saturation": oxygen_saturation,
        "respiration_rate": respiration_rate,
        "temperature": temperature
    }

if __name__ == "__main__":
    while True:
        vitals = generate_vitals()
        print(vitals)
        time.sleep(1) # Stream every 1 second
