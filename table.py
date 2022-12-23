import csv , os

if os.path.exists("./weights.csv") == True:
  if os.stat("./weights.csv").st_size != 0:
    with open("./weights.csv","r+") as fp:
      fp.truncate(0)

sw = csv.writer(open("./weights.csv","w"))
with open("./weights.txt","r") as fp:
  lines = fp.readlines()
  for line in lines:
    row = line.split(",")
    row.pop(-1)
    for i in range(len(row)):
      row[i] = float(row[i])
    sw.writerow(row)
  
print("Weight table ready!")