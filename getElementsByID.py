import csv
#open the html file as txt
f = open ('html.txt', 'r')
lst = []
#loop over the html text to get all the element which has and id
for l in f:
    if "id" in l:
        lst.append(l)
#open a new file to write in the ids of the elments
with open('out.csv' , 'w', newline = '')as file:
    writer = csv.writer(file)
    for i in lst:
        if "input " in i:
            #if the line has the word input it will split by " and will the the 5th element as it usualy can be the id
            print (i.split('"')[5])
            #it will write it in the csv file
            writer.writerow([i.split('"')[5]])
