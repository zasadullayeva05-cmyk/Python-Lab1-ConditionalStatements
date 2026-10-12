def run():
    w=float(input("Enter weight(kg):"))
    h=float(input("Enter height(m):"))
    BMI=w/(h*h)
    if BMI<18.5:
        print("catagory: underweight")
    elif BMI<25:
        print("catagory: normal weight")
    elif BMI<30:
        print("catagory: overweight")
    else:
        print("catagory: obese")