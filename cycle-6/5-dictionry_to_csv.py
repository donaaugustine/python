f = open("D:\Dona-McaS1\python\Cycle_6\cycle-6\Book1.csv", "a")
import json
thisdict = {
"Fname":"Deepa",
"Lname":"Rose",
"Email":"deepa1819@gmail.com"
}
result = json.dumps(thisdict)
f.write(result)
f.close()
f = open("D:\Dona-McaS1\python\Cycle_6\cycle-6\Book1.csv", "r")
print(f.read())