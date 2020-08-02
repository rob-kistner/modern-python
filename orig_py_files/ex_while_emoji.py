from modules.printutils import *

bannerline('For loop version...')
# ----------------------------------------
for x in range(3):
  for e in range(1, 11):
    print("\U0001f600" * e)
  
bannerline('While loop version...')
# ---------------------------------------
e = 1
while e <= 10:
  print("\U0001f600" * e)
  e += 1

bannerline('Unnecessary complex version...')
# without '* e' repeater 
# ---------------------------------------
for num in range(1, 11):
  count = 1
  smileys = ""
  while count <= num:
    smileys += "\U0001f600"
    count += 1
  print(smileys)
