import csv

allData = []
fields = ["id", "salesAmount", "locationId"]

with open('order-items.csv', mode='r') as file:
    csvFile = csv.reader(file)
    
    next(csvFile, None)
    for line in csvFile:
        parts = line[0].split("|")
        newCol = {
            "id": parts[0],
            "salesAmount": parts[1],
            "locationId": parts[2]
        }
        allData.append(newCol)

# Display first few entries for verification
print(allData[:5])

# Writing to a new CSV
with open('updated_orderitems.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(allData)
