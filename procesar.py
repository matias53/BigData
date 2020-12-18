import os
import pandas as pd
'''
    For the given path, get the List of all files in the directory tree 
'''

def processFile(path):
    print(path)
    f=pd.read_csv(path)
    keep_col = ['date','serial_number','model','capacity_bytes','failure']
    new_f = f[keep_col]
    new_f.to_csv(path, index=False)



def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles


def main():
    
    dirName = 'C:\\users\\mlset\\bigdata'
    
    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dirName)
    
    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
        
        
    #Print the files    
    for elem in listOfFiles:
        if elem.endswith('.csv'):
            processFile(elem)
         
if __name__ == '__main__':
    main()