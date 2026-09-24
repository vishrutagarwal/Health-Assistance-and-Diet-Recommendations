def bmi_calculator(weight,height):
    return round(weight/(height/100)**2,2)


def bmr_calculator(weight,height,age,gender):
    if gender == 'Male':
        bmr = (10*weight) + (6.25*height) - (5*age) + 5
    elif gender == 'Female':
        bmr = (10*weight) + (6.25*height) - (5*age) - 161
    return round(bmr,2)

def tdee_calculator(bmr,activity):
    activity_factor = {
        'Sedentary':1.20,
        'Lightly Active':1.375,
        'Moderatly Active':1.55,
        'Very Active':1.725,
        'Extra Active':1.90
    }
    tdee = bmr * activity_factor[activity]
    return round(tdee)

def calorie_target(tdee,target):
    if target == 'Weight Maintain':
        return tdee
    elif target == 'Weight Loss':
        return tdee - 400
    elif target == 'Weight Gain':
        return tdee + 300

# print(bmi_calculator(70,170))
# bmr = bmr_calculator(70,170,25,'Male')
# tdee = tdee_calculator(bmr,'Moderatly Active')
# print(calorie_target(tdee,'Weight Maintain'))
# print(calorie_target(tdee,'Weight Gain'))
# print(calorie_target(tdee,'Weight Loss'))