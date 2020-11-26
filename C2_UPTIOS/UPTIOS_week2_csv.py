# CSV stands for comma separated values
import csv

f = open("csv_file.txt")
csv_f = csv.reader(f)  # This is the read move of the csv file
for row in csv_f:
    name, number, role = row  # This is called unpacking in formal term
    print("Name: {}, Number:{}, Role: {}".format(name, number, role))
f.close()

# Now we will generate csv file

hosts = [["workstation", "192.168.1.10"], ["Webserver", "10.10.1.123"]]
with open("hosts.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)  # This is the write mode of the csv file
    writer.writerows(hosts)  # writerows write all the rows at once
    # for h in hosts:
    #     writer.writerow(h)  # writerow will write one row at a time

# Read an write CSV files as dictionaries
# DictReader turns each row of the data in a CSV file into a dictionary.
# We can then access the data by using the column names as keys instead of the position in the row.

with open("software.csv") as software:
    reader = csv.DictReader(software)
    for row in reader:
        print("{} has {} users".format(row["name"], row["users"]))

# DictWriter in a similar way to generate a CSV file from the contents of a list of dictionaries. This means that
# each element in the list will be a row in the file, and the values of each field will come out of each of the
# dictionaries. For this to work, we'll also need to pass a list of the keys that we want to be stored in the file

users = [{"name": "Taqi", "username": "Bear", "department": "Sensor Hardware"},
         {"name": "Aaro", "username": "Aaaaro", "department": "Sensor Hardware"},
         {"name": "Joel", "username": "Joell", "department": "Sensor Battery"}]
keys = ["name", "username", "department"]
with open("by_department.csv", "w") as department:
    writers = csv.DictWriter(department, fieldnames=keys)
    writers.writeheader()  # writeheader method will create the first line in csv file based on the keys that we passed
    writers.writerows(users)  # writerows method will turn the list of dictionaries into lines in the file
