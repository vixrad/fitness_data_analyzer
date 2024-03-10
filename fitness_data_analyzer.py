def calculate_bmi(weight, height):

    """Calculate the Body Mass Index (BMI).
    Height can be added in meters or centimeters.
    4 is used as a proxy. There aren't people taller
    than 3 meters and shorter than 40 centimeters. This
    allows the user to input meters or centimeters and
    get the same outcome."""

    if height >= 4:
        bmi = weight / ((height / 100) ** 2)
    else:
        bmi = weight / (height ** 2)
    return bmi


def calculate_calories_burned(weight, duration, intensity):
    """Calculate the estimated number of calories burned during exercise using intensity levels.
    MET is the ratio of your working metabolic rate relative to your resting metabolic rate.
    Your metabolic rate is the rate of energy used per unit of time, whether you are active or sitting still.
    It is a term that gives you an idea of the intensity level of a particular activity."""

    # Approximate MET values for different intensities
    intensity_met = {
        "low": 2.5,  # Average MET for low-intensity activities
        "moderate": 4.5,  # Average MET for moderate-intensity activities
        "high": 7.0,  # Average MET for high-intensity activities
    }

    met = intensity_met.get(intensity, 4.5)  # Default to moderate if intensity is unknown
    calories_burned_per_minute = (met * 3.5 * weight) / 200
    total_calories_burned = calories_burned_per_minute * duration
    return total_calories_burned


def filter_overweight_people(people_data):
    """Filter overweight people based on BMI."""
    overweight_people = []
    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        if bmi >= 25:
            overweight_people.append(person)
    return overweight_people


def main():
    people_data = []

    print("Enter fitness data for each person (Enter a blank name to finish):")
    while True:
        name = input("Enter person's name: ").strip()
        if not name:
            break
        while True:
            try:
                weight = float(input("Enter person's weight in kilograms: "))
                if weight <= 0:
                    raise ValueError("Weight must be greater than zero.")
                break  # Exit the loop if input is valid
            except ValueError as error:
                print(f"Invalid input - error message: {error}. Please enter a positive number for weight.")
        while True:
            try:
                height = float(input("Enter person's height in meters or centimeters: "))
                if height <= 0:
                    raise ValueError("Height must be greater than zero.")
                break  # Exit the loop if input is valid
            except ValueError as error:
                print(f"Invalid input - error message: {error}. Please enter a positive number for height.")
        while True:
            try:
                duration = float(input("Enter exercise duration in minutes: "))
                if duration <= 0:
                    raise ValueError("Duration must be greater than zero.")
                break  # Exit the loop if input is valid
            except ValueError as error:
                print(f"Invalid input - error message: {error}. Please enter a positive number for duration.")
        while True:
            try:
                intensity = input("Enter exercise intensity (low, moderate, high): ").strip().lower()
                if intensity not in ['low', 'moderate', 'high']:
                    raise ValueError("Invalid intensity. Please enter 'low', 'moderate', or 'high'.")
                break  # Exit the loop if input is valid
            except ValueError as error:
                print(f"Invalid input - error message: {error}. Please enter 'low', 'moderate', or 'high'.")

        person = {
            'name': name,
            'weight': weight,
            'height': height,
            'duration': duration,
            'intensity': intensity
        }
        people_data.append(person)

    print("\nFitness analysis:")
    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        calories_burned = calculate_calories_burned(person['weight'], person['duration'], person['intensity'])
        print(f"{person['name']}: BMI = {bmi:.2f}, Calories burned = {calories_burned}")

    overweight_people = filter_overweight_people(people_data)
    print("\nOverweight people:")
    for person in overweight_people:
        bmi = calculate_bmi(person['weight'], person['height'])
        print(f"{person['name']}: BMI = {bmi:.2f}")


if __name__ == "__main__":
    main()
