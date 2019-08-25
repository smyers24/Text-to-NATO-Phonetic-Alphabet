import csv

MilDictionary = {}
translated_string = ""

file = open('Q:/Coding/Python Stuff/NATO_Dictionary/nato.csv', mode='r')
csv_reader = csv.reader(file)

for row in csv_reader:
    MilDictionary[row[0]] = row[1]

text = (input("What do you want to translate? ").lower())
for characters in text:
    if characters in MilDictionary:
        translated_string += MilDictionary[characters] + " "
    else:
        print("Please only enter valid NATO characters")
        break

print(translated_string)

