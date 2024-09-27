import random
import time

# Set the temperature threshold
threshold = 75.0

print("Starting temperature monitoring...")

try:
    while True:
        # Simulate temperature reading
        current_temperature = random.uniform(-10.0,100.0)
        print(f"Current Temperature: {current_temperature:.2f}°C")

        # Check if the temperature exceeds the threshold
        if current_temperature > threshold:
            print(f"Alert! Temperature is too high: {current_temperature:.2f}°C")

        # Wait for 2 seconds before the next reading
        time.sleep(2)

except KeyboardInterrupt:
    print("Monitoring stopped.")
