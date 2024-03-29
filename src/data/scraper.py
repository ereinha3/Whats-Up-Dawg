import csv
import requests
import sys
sys.path.append("../..")
from breeds_dict import breeds
from docs.dog_pics import image_urls

# Using CSV reader to parse file
with open('../../docs/dog-stats.csv', newline='\n') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    headers = ["breed"]
    first = 1
    f = open('breeds_dict.py', 'w')
    f.write("breeds = {\n")
    for row in reader:
        if first:
            for ele in row:
                if ele!='':
                    headers.append("{}".format(ele))
            first = 0
        else:
            for index in range(len(row)):
                if index == 0:
                    f.write('\t"{}" : '.format(row[index].lower()))
                    f.write("{\n")
                else:
                    try:
                        parameter = round(float(row[index]),2)
                    except:
                        parameter = "'{}'".format(str(row[index]).replace("'", '"'))
                    f.write("\t\t'{}': {},\n".format(headers[index], parameter))

            f.write("\t},\n")
    f.write("}")
    f.close()

print("Finished getting breed info...")

with open("../../docs/dog-names-and-pics.csv", newline = '\n') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    f = open('../../docs/dog_pics.py', 'w')
    f.write("image_urls = {\n")
    first = 1
    for row in reader:
        if first:
            first = 0
        else:
            if row[7]:
                f.write('\t"{}" : "{}",\n'.format(row[1].lower(), row[7]))
    f.write("}")
    f.close()

print("Finished writing dog image locations...")

matches = []
for breed in image_urls.keys():
    if breed in breeds.keys():
        matches.append(breed)

print("Found matches...")

f = open("matches.py", 'w')
f.write("matches = [")
for match in matches:
    f.write(f'"{match}", ')
    #res = requests.get(image_urls[match])
    file_name = "../../docs/images/" + match.replace(' ', '_') + ".jpg"
'''
    with open(file_name, "wb") as image_file:
        image_file.write(res.content)
'''
f.write(']')
f.close()

