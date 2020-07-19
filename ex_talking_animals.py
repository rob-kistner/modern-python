from modules.printutils import *

big_banner("""
    Exercise 42:
    Talking Animals
""")

# Define speak below:
def speak(animal="dog"):
    sounds = {
        "pig": "oink",
        "duck": "quack",
        "cat": "meow",
        "dog": "woof"
    }
    sound = sounds.get(animal)
    if sound:
        return sound
    return "?"

print(speak())
print(speak("pig"))
print(speak("berry"))