import wikipedia
import os

inpt = open("pageTitleList.txt", "r")
lines = inpt.readlines()
try:
    os.mkdir("output")
except FileExistsError:
    pass

f = open("output/"+"Descriptions"+".txt", "w")

for line in lines:
    line = line.strip()
    print("Looking for: \""+line+"\"")
    
    try:
        page = wikipedia.page(line)
        print("found: \""+line+"\"")
        f.write(page.section("Gameplay"))
        print("Written to file: output/"+line+".txt \n--------------------------------------------------\n")
    except Exception as e:
        print(e)
        print("Skipping fetch for \""+line+"\" \n--------------------------------------------------\n")
f.close()        
    
