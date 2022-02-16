# =====================
# Browse list of url subdomains
# - input : file with url list
#
# =====================
import webbrowser
import sys

browser = webbrowser.get("safari")


if len(sys.argv) < 2:
  print("Please specify url list...")
  exit(1)

output = open("flagged_urls.txt", "a")
f = open(sys.argv[1], "r")
urls = f.readlines()
urls = [x.strip() for x in urls]

count = 0
total = 0
for url in urls:
  total += 1;
  print(f'Opening -- {url}')
  browser.open(url)
  
  i = input("%")
  if i == "q":
    if total < len(urls):
      print("Saving remaining URLs in urls_remaining.txt")
      w = open("urls_remaining.txt", "w")
      for url in urls[total:]:
        w.write(url + "\n")
      
    print("TERMINATING. . .")
    output.close()
    exit(0)
  if i == "f":
    count += 1
    note = input("note: ")
    output.write(f"FLAGGED: {url}\n  --{note}\n\n")


output.close()
print(f"Completed parsing url list. {count} URLs flagged")
