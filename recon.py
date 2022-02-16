import os
import sys
from termcolor import colored
from termcolor import cprint

print (" _______                                      ")
print ("|       \                                     ")
print ("| $$$$$$$\ ______   _______  ______  _______  ")
print ("| $$__| $$/      \ /       \/      \|       \ ")
print ("| $$    $|  $$$$$$|  $$$$$$|  $$$$$$| $$$$$$$\\")
print ("| $$$$$$$| $$    $| $$     | $$  | $| $$  | $$")
print ("| $$  | $| $$$$$$$| $$_____| $$__/ $| $$  | $$")
print ("| $$  | $ \$$      \\$$       $$    $| $$  | $$")
print (" \$$   \$$ \$$$$$$$ \$$$$$$$ \$$$$$$ \$$   \$$")
print ("                                              ")





sublister = "python3 /Users/michaelmondoro/Desktop/hacky/tool_folders/Sublist3r/sublist3r.py"

if len(sys.argv) < 2:
	cprint("Please specify target domain . . .",'red')
	exit()


os.system("mkdir results")
# -----
# Amass
# -----
cprint("-----", 'cyan')
cprint("Amass", 'cyan')
cprint("-----", 'cyan')

print (f"Running amass on target: {sys.argv[1]}")
os.system(f"amass enum -d {sys.argv[1]} -ipv4 -noalts -norecursive")

# write amass subdomains to file
print ("Writing amass subdomains to file . . .\n\n")
os.system(f"amass db -names -d {sys.argv[1]} >> results/amass_subs.txt")


# ---------
# Sublist3r
# ---------
cprint("---------", 'cyan')
cprint("Sublist3r", 'cyan')
cprint("---------", 'cyan')
print (f"Running Sublist3r on target: {sys.argv[1]}")
os.system(f"{sublister} -d {sys.argv[1]} -o results/sublister_subs.txt")


# Remove duplicate domains 
print("\n\n")
print("Removing duplicate domains . . . ")
r1 = open("results/sublister_subs.txt", "r")
r2 = open("results/amass_subs.txt", "r")

subs = r1.readlines()
subs = [x.strip() for x in subs]

subs2 = r2.readlines()
subs2 = [x.strip() for x in subs2]
[subs.append(x) for x in subs2 if x not in subs]

print("Writing master subdomain file all_subs.txt . . . \n\n")
subs_file = open('results/all_subs.txt', 'w')
for sub in subs:
	subs_file.write(sub + "\n")

subs_file.close()


# --------
# httprobe
# --------
cprint("--------", 'cyan')
cprint("httprobe", 'cyan')
cprint("--------", 'cyan')
print ("Running httprobe on subdomain lists . . . ")
print (f"URLs found: ")


os.system(f"cat results/all_subs.txt | ./httprobe.sh --prefer-https >> results/urls.txt")
os.system('wc -l results/urls.txt')


print ("\n\nURL lists written to urls.txt . . . \n\n")


# --------
# Aquatone
# --------

cprint("--------", 'cyan')
cprint("aquatone", 'cyan')
cprint("--------", 'cyan')
print("Running aquatone with urls.txt . . .")

os.system("cat results/urls.txt | /Users/michaelmondoro/Desktop/hacky/tool_folders/aquatone -out results/aquatone")


# --------
# Nmap
# --------

# cprint("----", 'cyan')
# cprint("nmap", 'cyan')
# cprint("----", 'cyan')
# print("Running nmap with all_subs.txt . . .")

# os.system("sudo nmap -v -sS -iL results/all_subs.txt -p 80,443,20,21,22,23 > results/nmap_out.txt")



print("\n\n")
print("# ---------- ")
print("#  FINISHED  ")
print("# ---------- ")