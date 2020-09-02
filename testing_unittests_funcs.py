from random import choice

def eat(food, is_healthy):
    if not isinstance(is_healthy, bool):
        raise ValueError("is_healthy must be a boolean.")
    ending = "because YOLO!"
    if is_healthy:
        ending = "because it's a healthy thing."
    return f"I'm eating {food}, {ending}"

def nap(num_hours):
    if num_hours <= 1:
        return "Feeling refreshed."
    else:
        return "Damn. Overslept."

def is_funny(person):
    if person == 'tim': return False
    return True

def laugh():
    return choice(('lol', 'haha', 'tehehe'))