def func():
    health_check = int(
        input(
            """Select Measuring System:
                    0 -> Metric System
                    1 -> Imperial System
                    input = """
        )
    )

    if health_check == 0:
        height = int(input("Height in cm= ")) / 100
        weight = int(input("Weight in Kg = "))
        print("BMI = ", calc_bmi(health_check, weight, height))

    elif health_check == 1:
        height = int(input("Height in inches = "))
        weight = int(input("Weight in pounds = "))
        print("BMI = ", calc_bmi(health_check, weight, height))

    else:
        print("Input not valid")
        return

    print(
        """Comparison Table:
        <18.5   \tUnder Weight
        18.5-24.9 \tNormal
        25-29.9 \tOver Weight
        30-34.9 \tObesity(Class 1)
        35-39.9 \tObesity(Class 2)
        >40     \tExtreme Obesity"""
    )
    

    return


def calc_bmi(health_check, weight, height):
    bmi = weight / (height * height)

    if health_check == 1:
        bmi = bmi * 703

    return round(bmi, 2)


func()
