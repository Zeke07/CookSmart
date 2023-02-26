import csv
import json

data = list()

# script-generated attributes for dataset and look-up table for measurements
attributes = ['Itemid', 'Name', 'Serving Size', 'Calories', 'Total Fat', 'Saturated Fat', 'Cholesterol', 'Sodium', 'Choline', 'Folate', 'Folic Acid', 'Niacin', 'Pantothenic Acid', 'Riboflavin', 'Thiamin', 'Vitamin A', 'Vitamin A Rae', 'Carotene Alpha', 'Carotene Beta', 'Cryptoxanthin Beta', 'Lutein Zeaxanthin', 'Lucopene', 'Vitamin B12', 'Vitamin B6', 'Vitamin C', 'Vitamin D', 'Vitamin E', 'Tocopherol Alpha', 'Vitamin K', 'Calcium', 'Copper', 'Irom', 'Magnesium', 'Manganese', 'Phosphorous', 'Potassium', 'Selenium', 'Zink', 'Protein', 'Alanine', 'Arginine', 'Aspartic Acid', 'Cystine', 'Glutamic Acid', 'Glycine', 'Histidine', 'Hydroxyproline', 'Isoleucine', 'Leucine', 'Lysine', 'Methionine', 'Phenylalanine', 'Proline', 'Serine', 'Threonine', 'Tryptophan', 'Tyrosine', 'Valine', 'Carbohydrate', 'Fiber', 'Sugars', 'Fructose', 'Galactose', 'Glucose', 'Lactose', 'Maltose', 'Sucrose', 'Fat', 'Saturated Fatty Acids', 'Monounsaturated Fatty Acids', 'Polyunsaturated Fatty Acids', 'Fatty Acids Total Trans', 'Alcohol', 'Ash', 'Caffeine', 'Theobromine', 'Water']
nutrient_table = {'Itemid': '', 'Name': '', 'Serving Size': 'g', 'Calories': '', 'Total Fat': 'g', 'Saturated Fat': '', 'Cholesterol': '', 'Sodium': 'mg', 'Choline': 'mg', 'Folate': 'mcg', 'Folic Acid': 'mcg', 'Niacin': 'mg', 'Pantothenic Acid': 'mg', 'Riboflavin': 'mg', 'Thiamin': 'mg', 'Vitamin A': 'IU', 'Vitamin A Rae': 'mcg', 'Carotene Alpha': 'mcg', 'Carotene Beta': 'mcg', 'Cryptoxanthin Beta': 'mcg', 'Lutein Zeaxanthin': 'mcg', 'Lucopene': '', 'Vitamin B12': 'mcg', 'Vitamin B6': 'mg', 'Vitamin C': 'mg', 'Vitamin D': 'IU', 'Vitamin E': 'mg', 'Tocopherol Alpha': 'mg', 'Vitamin K': 'mcg', 'Calcium': 'mg', 'Copper': 'mg', 'Irom': 'mg', 'Magnesium': 'mg', 'Manganese': 'mg', 'Phosphorous': 'mg', 'Potassium': 'mg', 'Selenium': 'mcg', 'Zink': 'mg', 'Protein': 'g', 'Alanine': 'g', 'Arginine': 'g', 'Aspartic Acid': 'g', 'Cystine': 'g', 'Glutamic Acid': 'g', 'Glycine': 'g', 'Histidine': 'g', 'Hydroxyproline': '', 'Isoleucine': 'g', 'Leucine': 'g', 'Lysine': 'g', 'Methionine': 'g', 'Phenylalanine': 'g', 'Proline': 'g', 'Serine': 'g', 'Threonine': 'g', 'Tryptophan': 'g', 'Tyrosine': 'g', 'Valine': 'g', 'Carbohydrate': 'g', 'Fiber': 'g', 'Sugars': 'g', 'Fructose': '', 'Galactose': '', 'Glucose': '', 'Lactose': '', 'Maltose': '', 'Sucrose': '', 'Fat': 'g', 'Saturated Fatty Acids': 'g', 'Monounsaturated Fatty Acids': 'g', 'Polyunsaturated Fatty Acids': 'g', 'Fatty Acids Total Trans': 'mg', 'Alcohol': 'g', 'Ash': 'g', 'Caffeine': 'mg', 'Theobromine': 'mg', 'Water': 'g'}


# csv parser, writes cleaned data to a separate JSON to be pushed to the DB
def main():

    # read in csv, store rows in dict()
    with open("nutrition.csv") as file:
        reader = csv.reader(file, delimiter =',', quotechar ='"', quoting = csv.QUOTE_ALL)
        next(reader)
        for line in reader:
            data.append(dict())
            for i in range(2): data[-1][attributes[i]] = line[i]

            for i in range(2, len(line)):
                stat = str()
                try:
                    stat = ''.join([x for x in line[i] if x.isdigit() or x == "."])
                    data[-1][attributes[i]] = float(stat)
                except Exception:
                    data[-1][attributes[i]] = 0.0


    # write to file
    to_write = open("dump.json", "w")
    json_data = json.dumps(data)

    for line in json_data:
        to_write.write(line)



if __name__ == '__main__':
    main()

