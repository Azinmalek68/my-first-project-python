W = int(input())
h = float(input())
BMI= W /(h**2)
if BMI<18.5:
    result="Underweight"
elif BMI>=18.5  and BMI<=24.9 :
    result="normal weight"
elif BMI >=25  and BMI<=29.9 : 
    result="Overweight"
elif BMI>=30  and BMI<=34.9 :       
    result="Obesity"
elif BMI>=35  and BMI<=39.9 :       
    result="Extreme Obesity"


print("bmi:", BMI)

print(result)      