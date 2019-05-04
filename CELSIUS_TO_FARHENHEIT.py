
def convert_temp(Celsius_val):
    Farhenheit_val=0
    Farhenheit_val=((9/5)*Celsius_val)+32
    return Farhenheit_val
Celsius_val=98
## for run time input use  Celsius_val=input()
Result=0
Result=convert_temp(Celsius_val)
print("Farhenheit value-",Result) 
