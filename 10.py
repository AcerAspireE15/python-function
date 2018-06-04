def function(weight, height):
    BMI = weight/(height**2)
    print(BMI)

function(48,5.11)


def calculate_BMI(new_weight, new_height):
    new_bmi = new_weight / (pow(new_height, 2))
    return new_bmi


weight = float(input('Enter weight in Kgs'))
height = float(input('Enter height in meters'))
bmi = calculate_BMI(weight, height)
print(bmi)