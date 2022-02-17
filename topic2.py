import csv
import pickle
import pandas as pd
import os

wordsToReplace = []

# 1) Word Count Occurence
def One():
    file = open("wordcount.txt", "r")
    data = file.read()
    occurrences = data.count("hi")
    wordsToReplace.append(data)
    print('Number of occurrences of the word :', occurrences)

# 2) Replace words with other words
def Two():
    One()
    def changeWords(word, required):
        newWords = str(wordsToReplace)
        changed = newWords.replace("{}".format(word), "{}".format(required))
        return changed
    print (changeWords(word='hi', required='CHANGED'))

# 3) Accept console info and store to CSV
def Three():
    lst = []
    userInput1 = input("Enter Name: ")
    userInput2 = input("Enter Course: ")
    userInput3 = input("Enter Fees: ")
    lst.append(userInput1)
    lst.append(userInput2)
    lst.append(userInput3)
    print(lst)
    with open('consoleExport.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(lst)

# 4) Access File and print Report
def Four():
    file = open("consoleExport.csv", "r")
    csv_reader = csv.reader(file)
    lists_from_csv = []
    for row in csv_reader:
        lists_from_csv.append(row)
    print(lists_from_csv)


# 5) create class with patient details
class patient():
    def __init__(self, name, address, contact, complaint):
        self.name = name
        self.address=address
        self.contact = contact
        self.complaint = complaint

# 6) Class object to pickles to save, then also read pickles
def Six():
    steve = patient("steve","uk","+441-58585","Ill")
    ad = steve.address
    with open('steveAddress.pkl', 'wb') as file:
        pickle.dump(ad, file)
    readPickles = pd.read_pickle(r'steveAddress.pkl')
    print (readPickles)

# 7) Show all python files in current working directory
def Seven():
    cwd = os.getcwd()
    for file in os.listdir(cwd):
        if file.endswith(".py"):
            print(os.path.join(cwd, file))

# 8) Display all image files in directory (JPG)
def Eight():
    cwd = os.getcwd()
    for file in os.listdir(cwd):
        if file.endswith(".jpg"):
            print(os.path.join(cwd, file))


if __name__ == "__main__":
    One()
    # Two()
    # Three()
    # Four()
    # steve = patient("steve","uk","+441-58585","Ill")
    # print (steve.address)
    # Six()
    # Seven()
    # Eight()
