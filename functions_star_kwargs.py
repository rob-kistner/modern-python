from modules.printutils import *

big_banner("""
    Functions: *kwargs
    ----------------
    • Gathers remaining keyword arguments
      as a dict
""")

# ----------------------------------------

def dump_fav_colors(**colors):
    return colors

print(dump_fav_colors(colt="purple", ruby="red", ethel="teal"))

bl()

def fav_colors(**colors):
    for person, color in colors.items():
        print(f"{person}'s favorite color is {color}")

fav_colors(colt="purple", ruby="red", ethel="teal")


bl()

def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting David!"
    elif "David" in kwargs:
        return f"{kwargs['David']} David!"

    return "Not sure who this is..."

print(special_greeting(David='Hello')) # Hello David!
print(special_greeting(Bob='hello')) # Not sure who this is...
print(special_greeting(David='special')) # You get a special greeting David!

print(special_greeting(Heather="hello", David="special"))


banner("Exercise 58")
# ----------------------------------------
def combine_words(word, **pre_suf):
    if pre_suf.get('prefix'):
        return pre_suf['prefix'] + word
    if pre_suf.get('suffix'):
        return word + pre_suf['suffix']
    return word

print(combine_words("child"))
print(combine_words("child", prefix="man"))
print(combine_words("child", suffix="ish"))