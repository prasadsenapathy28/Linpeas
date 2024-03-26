import urllib.parse
from pymongo import MongoClient
import json

# Read JSON data from 'ex.json' file
with open('ex.json', 'r') as json_file:
    data = json.load(json_file)

# Extract relevant data
os_name_raw = data["System Information"]["sections"]["Operative system"]["lines"][1]["clean_text"]
os_name = os_name_raw.replace("Distributor ID:\t", "").replace("Description:\t", "")

os_version_raw = data["System Information"]["sections"]["Operative system"]["lines"][2]["clean_text"]
os_version = os_version_raw.replace("Description:\t", "")

hostname_raw = data["System Information"]["sections"]["Operative system"]["lines"][4]["clean_text"]
hostname = hostname_raw.replace("Codename:\t", "")

current_time = data["System Information"]["sections"]["Date & uptime"]["lines"][0]["clean_text"]

# Create a dictionary with the extracted data
extracted_data = {
    "OS Name": os_name,
    "OS Version": os_version,
    "Hostname": hostname,
    "Current Time": current_time
}

# Save the extracted data to a new JSON file
with open("linsys.json", "w") as outfile:
    json.dump(extracted_data, outfile, indent=2)

print("Extracted data has been stored in 'extracted_data.json' file.")

# # Replace with your MongoDB Atlas connection details
# mongodb_url = "mongodb+srv://urstrulyprithu:" + urllib.parse.quote(
#     "test@123") + "@securelycluster.wlxqkq6.mongodb.net/?retryWrites=true&w=majority"

# collection_name = "TestCollection"

# # Connect to MongoDB Atlas
# client = MongoClient(mongodb_url)
# database = client.get_database("Test")
# collection = database[collection_name]

# # Insert the dictionary data into the collection
# inserted_id = collection.insert_one(extracted_data).inserted_id

# print(f"Data inserted with ID: {inserted_id}")

# # Close the MongoDB connection
# client.close()