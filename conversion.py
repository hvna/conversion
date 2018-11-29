'''
convert from F to C, and from C to F
'''
degree = input(" Enter C for Celsius , or F for Fahrenheit : ")
temperature = int(input(" Enter the temperature value : "))

if degree == 'f':
    C = (temperature - 32)*5/9
    print(" the temperature in Celsius is ", round(C))
elif degree == 'c':
    F = temperature*9/5 + 32
    print(" the temperature in Fahrenheit is : ", round(F))
else :
    print("There is no such type of degree like :", degree)