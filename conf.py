import os
import random
print("beginning")

print("protecting I3 config :")
tmp = "config" + str(random.randint(0, 123456789))
s = "mv $HOME/afs/.confs/config/i3/config $HOME/afs/.confs/config/i3/" + tmp
os.system(s)
print("saved as " + tmp + "\n")

print("Changing i3 confing : ", end = "")
os.system('cp myconfig $HOME/afs/.confs/config/i3/config')
print("Done\n")

print("Images : ", end = "")
os.system('cp -r images $HOME/afs/.confs/')
print("Done\n")

print("\nAll Done, enjoy")
