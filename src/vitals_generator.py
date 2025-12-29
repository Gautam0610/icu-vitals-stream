import time
import random
from collections import deque

class VitalSignAnalyzer:
    def __init__(self, history_length=5, threshold=5):
        self.history_length = history_length
        self.threshold = threshold
        self.heart_rate_history = deque(maxlen=history_length)
        self.bp_systolic_history = deque(maxlen=history_length)

    def analyze_trend(self, history, current_value, sign):
        if len(history) < self.history_length:
            return False

        trend_count = 0
        for prev_value in history:
            if sign > 0 and current_value > prev_value and (current_value - prev_value) >= self.threshold:
                trend_count += 1
            elif sign < 0 and current_value < prev_value and (prev_value - current_value) >= self.threshold:
                trend_count += 1

        return trend_count == self.history_length

    def update_history(self, heart_rate, bp_systolic):
        self.heart_rate_history.append(heart_rate)
        self.bp_systolic_history.append(bp_systolic)

    def check_abnormal_trends(self, heart_rate, bp_systolic):
        hr_increasing = self.analyze_trend(list(self.heart_rate_history), heart_rate, 1)
        hr_decreasing = self.analyze_trend(list(self.heart_rate_history), heart_rate, -1)
        bp_increasing = self.analyze_trend(list(self.bp_systolic_history), bp_systolic, 1)
        bp_decreasing = self.analyze_trend(list(self.bp_systolic_history), bp_systolic, -1)

        self.update_history(heart_rate, bp_systolic)

        trends = {}
        if hr_increasing:
            trends['hr_increasing'] = True
        if hr_decreasing:
            trends['hr_decreasing'] = True
        if bp_increasing:
            trends['bp_increasing'] = True
        if bp_decreasing:
            trends['bp_decreasing'] = True

        return trends

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
    analyzer = VitalSignAnalyzer()
    while True:
        vitals = generate_vitals()
        heart_rate = vitals['heart_rate']
        bp_systolic = vitals['blood_pressure_systolic']
        trends = analyzer.check_abnormal_trends(heart_rate, bp_systolic)
        vitals['trends'] = trends
        print(vitals)
        time.sleep(1) # Stream every 1 second
