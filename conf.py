import os
import random
print("beginning")

s = "mv $HOME/afs/.confs/config/i3/config $HOME/afs/.confs/config/i3/config" + str(random.randint(0, 123456789))
os.system(s)

os.system('cp myconfig $HOME/afs/.confs/config/i3/config')
os.system('cp troll.jpg $HOME/afs/.confs/troll.jpg')


print("\n    Done")
