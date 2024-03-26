import urllib.parse
from pymongo import MongoClient
import json

# Read the existing jsonout.json file
with open('MacPEASjson.json', 'r') as infile:
    datas = json.load(infile)

# Define the list of uppercase colors
colors_to_count = ["RED", "GREEN", "YELLOW", "BLUE"]

# Initialize color counters
color_counts = {color: 0 for color in colors_to_count}

for data in datas:
	for sections in datas.get(data).get("sections", {}):
		for section in datas.get(data).get("sections", {}).get(sections):
			if section in "lines":
				for lines in datas.get(data).get("sections", {}).get(sections).get(section):
					for color in lines.get("colors"):
						for colors in color_counts.keys():
							if colors in color:
								color_counts[colors] += 1
								
# print(color_counts)
# Output dictionary
output_data = color_counts

# Write the output data to wcol.json
with open('mcol.json', 'w') as outfile:
    json.dump(output_data, outfile)

# Replace with your MongoDB Atlas connection details
mongodb_url = "mongodb+srv://urstrulyprithu:" + urllib.parse.quote(
    "test@123") + "@securelycluster.wlxqkq6.mongodb.net/?retryWrites=true&w=majority"

collection_name = "ColorsCollection"

# Connect to MongoDB Atlas
client = MongoClient(mongodb_url)
database = client.get_database("Test")
collection = database[collection_name]

# Insert the dictionary data into the collection
inserted_id = collection.insert_one(output_data).inserted_id

print(f"Data inserted with ID: {inserted_id}")

# Close the MongoDB connection
client.close()