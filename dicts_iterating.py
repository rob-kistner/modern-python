from modules.printutils import *

big_banner("""
Dictionaries:
Iterating over values
""")


instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number"
}

banner("""
keys()
Loop over keys
""")
# ----------------------------------------
for k in instructor.keys():
    print(f"{k}")


banner("""
values()
Loop over values
""")
# ----------------------------------------
for v in instructor.values():
    print(f"{v}")


banner("""
items()
Loop over key/value as tuples,
should use two vars (k,v) to separate
the keys and values in the loop
""")
# ----------------------------------------
for k, v in instructor.items():
    print(f"{k}: {v}")


banner("Exercise 28: Totaling Donations")
# ----------------------------------------
# DON'T TOUCH PLEASE!
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# DON'T TOUCH PLEASE!

# Use a loop to add together all the donations and store the resulting number in a variable called total_donations
total_donations = 0
for k, v in donations.items():
    total_donations += v

print(f"Donations List: {donations}")
print()
print(f"Total Donations: {total_donations}")