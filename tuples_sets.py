from modules.printutils import *

big_banner("""
TUPLES are…
--------------------
• Accessed like a list
• Immutable (can't change it, no way)
• Faster than lists (because it's static)
• Safter (cause you can't change it)
• Valid keys in dictionaries
• Can have duplicate data
""")

numbers = (1, 2, 3, 4)
print(numbers)
print(3 in numbers)

alphabet = ('a', 'b', 'c', 'd', 'e')
print(alphabet)
print(type(alphabet))

banner("Examples")
# ----------------------------------------
months = ('January','February','March','April','May','June','July','August','September','October','November','December')

print(f"months: {months}")
bl()
print(f"months[0]: {months[0]}")
bl()

locations = {
    (35.6895, 39.6917): "Tokyo",
    (40.7128, 75.0078): "New York",
    (37.7749, 122.4194): "San Francisco",
}
print(f"locations: {locations}")


banner("Some dictionary methods return tuples…")
# ----------------------------------------
cat = {"name": "biscuit", "age": 0.5, "favorite_toy": "my chapstick"}
print("cat:")
jprint(cat)
print(cat.items())