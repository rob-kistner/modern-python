# ------------------------------
#   Project:
#   Mileage Converter
# ------------------------------

print()
userinput = input("Enter the distance you ran today (in km): ")

def convert_to_miles(kms):
    FACTOR = 1.60934
    return round(float(kms) / FACTOR, 2)

print()
print(f"{userinput} kilometers = {convert_to_miles(userinput)} miles")
print()