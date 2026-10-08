

print("SMART PLANT WATERING SYSTEM")

try:
    moisture = float(input("Enter soil moisture (0-100): "))

    if not 0 <= moisture <= 100:
        print("Error: enter a number from 0 to 100.")
    else:
        dry = max(0.0, min(1.0, (50 - moisture) / 30))
        normal = max(0.0, min((moisture - 20) / 30, (80 - moisture) / 30))
        wet = max(0.0, min(1.0, (moisture - 50) / 30))

        total = dry + normal + wet
        minutes = (dry * 20 + normal * 10 + wet * 0) / total

        print("Dry membership:", round(dry, 2))
        print("Normal membership:", round(normal, 2))
        print("Wet membership:", round(wet, 2))
        print("Watering time: {:.2f} minutes".format(minutes))

except ValueError:
    print("Error: please enter numbers only.")