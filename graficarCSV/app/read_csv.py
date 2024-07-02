import csv 
def read_csv(path):
    with open (path, 'r' ) as csvFile:
        reader = csv.reader(csvFile,delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header,row)
            dictData = {key: value for key,value in iterable}
            data.append(dictData)
        return data