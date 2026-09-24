LAST_NAME = "DAVID"
STUDENT_ID = "TUPM-26-1110"
SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME) 
FAVORITE_ARTIST = "OLIVIA"

#1 EXECISE 1: EQUIPMENT DIAGNOSTIC SYSTEM

def generate_readings():
    readings = [
        SEED_DIGIT * 10, 
        ID_SUM % 100,
        NAME_LENGTH * 5, 
        len(FAVORITE_ARTIST) *4
    ]
    return readings

def validate_reading(reading):
    try:
        if not isinstance(reading, (int, float)):
            raise ValueError("Reading must be numeric")
        if reading < 0 or reading > 100:
            raise ValueError("Reading must be betweeen 0 and 100")
        return "Valid"
    except ValueError as error:
        return f"Inavlid: {error}"

def calculate_average(readings):
    total = sum(readings)
    average = total / len(readings)
    return average

def classify_condition(average):
    if average >= 80:
        return "NORMAL"
    elif average >= 60:
        return "WARNING"
    else:
        return "CRITICAL"

def logger(func):
    def wrapper(*args, **kwargs):
        print("Executing:", func.__name__)
        result = func(*args, **kwargs)
        print("Completed:", func.__name__)
        return result
    return wrapper

@logger
def run_diagnostic():
    readings = generate_readings()
    print("Generated Equipment Data:", readings)

    print("Validation Results:")
    valid_readings = []

    for reading in readings:
        result = validate_reading(reading)
        print(reading, "-->", result)

        if result == "Valid":
            valid_readings.append(reading)

    if len(valid_readings) == 0:
        print("No valid readings available")
        return

    average = calculate_average(valid_readings)
    condition = classify_condition(average)

    print("Diagnostic Results:")
    print("Valid Readings:", valid_readings)
    print("Average:", round(average, 2))
    print("Equipment Condition:", condition)


run_diagnostic()


