import BMI
import zodiac
import birthday
while True:
    print ("press 'bm' for BMI")
    print ("press 'z' for zodiac")
    print ("press 'b' for birthday")
    print ("press 'e' for EXIT")
    answer = input("select opinion")
    if answer == "bm":
        BMI.run()
    elif answer=="z":
        zodiac.run()
    elif answer=="b":
        birthday.run()
    elif answer=="e":
        break