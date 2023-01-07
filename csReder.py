import csv
# rows=[["ravi", "manger"], ["suresh", "coe"]]
# filename="prodeucts.csv"
# with open(filename, "a", newline="") as csvfile:
#     csvwriter=csv.writer(csvfile)
#     csvwriter.writerow(rows)
# with open(filename,mode="r")as file:
#     csvfile=csv.reader(file)
#     print(csvfile)
with open("prodeucts.csv",mode="r")as file:
    csvfile=csv.reader(file)
    for line in csvfile:
        print(line)