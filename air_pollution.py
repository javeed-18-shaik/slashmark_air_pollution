
import time
import random
import csv
from datetime import datetime

# Thresholds (you can adjust based on sensor calibration)
MQ135_THRESHOLD = 400
MQ6_THRESHOLD = 300

# Log file name
LOG_FILE = "air_quality_data.csv"

# Initialize log file with headers
with open(LOG_FILE, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "MQ135 (PPM)", "MQ6 (PPM)", "Status"])

def simulate_sensor_reading(sensor_name):
    # Simulate realistic sensor values (or replace this with actual sensor reading logic)
    if sensor_name == "MQ135":
        return random.randint(100, 600)  # Simulated air pollution (PPM)
    elif sensor_name == "MQ6":
        return random.randint(100, 500)  # Simulated gas level (PPM)

def check_air_quality(mq135_value, mq6_value):
    if mq135_value > MQ135_THRESHOLD or mq6_value > MQ6_THRESHOLD:
        return "DANGER"
    else:
        return "SAFE"

def main():
    print("Starting IoT Air Pollution Monitoring Simulation...\n")
    try:
        while True:
            # Simulated readings
            mq135_ppm = simulate_sensor_reading("MQ135")
            mq6_ppm = simulate_sensor_reading("MQ6")
            status = check_air_quality(mq135_ppm, mq6_ppm)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Display output
            print(f"[{timestamp}] MQ135: {mq135_ppm} PPM | MQ6: {mq6_ppm} PPM | STATUS: {status}")

            # Log to CSV
            with open(LOG_FILE, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([timestamp, mq135_ppm, mq6_ppm, status])

            # Optional: sound alert or popup
            if status == "DANGER":
                print("⚠️  Alert: Air Quality Deteriorated! Take Action Immediately.\a")  # \a is bell sound

            time.sleep(2)  # 2-second interval

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    main()
