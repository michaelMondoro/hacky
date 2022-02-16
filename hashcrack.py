from passlib import hash
import sys
from termcolor import cprint
from progress.bar import Bar


if len(sys.argv) < 2:
  print("Please specify hash value . . .")
  exit(1)
# elif len(sys.argv) < 3:
# print("Please specify hash type . . .")
#   exit(1)

hash2crack = sys.argv[1]

print("")
cprint (" /$$   /$$                     /$$        /$$$$$$                               /$$      ", 'blue')
cprint ("| $$  | $$                    | $$       /$$__  $$                             | $$      ", 'blue')
cprint ("| $$  | $$  /$$$$$$   /$$$$$$$| $$$$$$$ | $$  \__/  /$$$$$$  /$$$$$$   /$$$$$$$| $$   /$$", 'blue')
cprint ("| $$$$$$$$ |____  $$ /$$_____/| $$__  $$| $$       /$$__  $$|____  $$ /$$_____/| $$  /$$/", 'blue')
cprint ("| $$__  $$  /$$$$$$$|  $$$$$$ | $$  \ $$| $$      | $$  \__/ /$$$$$$$| $$      | $$$$$$/ ", 'blue')
cprint ("| $$  | $$ /$$__  $$ \____  $$| $$  | $$| $$    $$| $$      /$$__  $$| $$      | $$_  $$ ", 'blue')
cprint ("| $$  | $$|  $$$$$$$ /$$$$$$$/| $$  | $$|  $$$$$$/| $$     |  $$$$$$$|  $$$$$$$| $$ \  $$", 'blue')
cprint ("|__/  |__/ \_______/|_______/ |__/  |__/ \______/ |__/      \_______/ \_______/|__/  \__/", 'blue')
cprint ("                                                                                         ", 'blue')
cprint ("                                                                                         ", 'blue')
cprint ("                      ---------------------------------------------                      ", 'blue')
print("")
cprint(f"Running HashCrack for {hash2crack} . . .\n", "magenta")


f = open("wordlists/rockyou.txt", encoding='latin-1')
passwords = f.readlines()
passwords = [x.strip() for x in passwords] 

count = 0
with Bar('Processing =>', max=len(passwords)) as bar:
	for pwd in passwords:
		if hash.mysql323.hash(pwd) == hash2crack:
			cprint(f"\n\tHash value discovered: {pwd}\n", "red")
			exit(0)

		bar.next()

cprint("""
	----------
	No luck :(
	----------
	""", "magenta")