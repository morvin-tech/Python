import random
import string

passcode= string.ascii_lowercase+string.ascii_uppercase+string.digits

for a in range(1,20):
  x=''.join(random.choice(passcode))
  print(x,end='')

