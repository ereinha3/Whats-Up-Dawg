import csv
import requests

# Using CSV reader to parse file
with open('../docs/dog-stats.csv', newline='\n') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    headers = ["breed"]
    first = 1
    f = open('../docs/breeds_dict.py', 'w')
    f.write("breeds = {\n")
    for row in reader:
        if first:
            for ele in row:
                if ele!='':
                    headers.append("{}".format(ele))
            first = 0
            print(headers)
        else:
            for index in range(len(row)):
                if index == 0:
                    f.write('\t"{}" : '.format(row[index]))
                    f.write("{\n")
                else:
                    try:
                        parameter = round(float(row[index]),2)
                    except:
                        parameter = "'{}'".format(str(row[index]).replace("'", '"'))
                    print(parameter)
                    f.write("\t\t'{}': {},\n".format(headers[index], parameter))

            f.write("\t},\n")
    f.write("}")
    f.close()

with open("../docs/dog-names-and-pics.csv", newline = '\n') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    f = open('../docs/dog-pics.py', 'w')
    f.write("image_urls = {\n")
    first = 1
    for row in reader:
        if first:
            first = 0
        else:
            if row[7]:
                f.write('\t"{}" : "{}",\n'.format(row[1], row[7]))
    f.write("}")
    f.close()
