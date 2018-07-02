"""@package docstring
Author Name: Abhilasha Dave
Date : 07/1/2018
Description:
Input:
Taking 2 argument:
-  “root_dir” as a root directory to start traversing 
-  “keyword” as a regular expression for example ( “^[a-zA-Z]+_TESTResult.*” ) to detect a file contains a string of interest
Functionality:
Script should recursively walk the “root_dir” and detect all the files under that dir that contain “keyword”.

For each subdir, script should count the number of file that contain “keyword”.

All results should be saved in a key:value array with key being subdir string, and value being counts of file containing “keyword” in this subdir.
Output:
A output array of all the data, for example {’a/b’: 6, ’a/b/c’: 7, ‘/a/b/c/d’:0}.
An output graph with a plot with X as subdir name string, Y as count values. 
"""

#import all the libraries
import os
import os.path
import matplotlib.pyplot as plt

#global variable declarations 
dictonary = {}

"""
Function: main
Retun value: None
Inputs: None
Description:
call the function "listFiles" to check the keywords
call the functions "plotBarGraph,plotLinearGraph" to plot the graph
"""
def main():
    root_dir = "C:\python"
    keywordSearch = '^[a-zA-Z]+_TESTResult.*'
    listFiles(root_dir,keywordSearch)
    if not bool(dictonary):
        print ("Dictonary is Empty")
    else:
        print(dictonary)
        plotBarGraph(dictonary)
        plotLinearGraph(dictonary)

"""
Function: listFiles
Retun value: None
Inputs: root_dir, keywordSearch
Description:
Do recursive walk through the root_dir and search for the keywords in text files
update the global dictionary if keyword is matched in the file
"""
def listFiles (root_dir,keywordSearch):
    count = 0  #local variable count
    #search for dir path and files that contains keyword
    try: 
        for dirpath,dirnames,filenames in os.walk(root_dir):
            for filename in [f for f in filenames if f.endswith(".txt")]:
                #check if keyword is available or not
                if keywordSearch in open(filename).read():
                    count = count+1
                #check if key word is not available
                if not keywordSearch in open(filename).read():
                    print(f"No keyword(s) found in file:{dirpath} {filename}")
            dictonary.update({dirpath: count})
            count = 0
    #trough exception error if file not found in the system
    except IOError:
        print ("Unable to open file:", filenames)
        dictonary.clear()

"""
Function: plotBarGraph
Retun value: None
Inputs: dictonary
Description:
Plot the bar graph for the key value pair of dictonary
"""
def plotBarGraph(dictonary):

    plt.bar(*zip(*sorted(dictonary.items())))
    plt.xticks(color='red',rotation = 90) #rotate the content for x values print them in red color
    plt.yticks(color='green')
    plt.xlabel('Directory Path', fontweight='bold', color = 'red', fontsize='18') #print the x-label 
    plt.ylabel('File counts', fontweight='bold', color = 'green', fontsize='18') #print the y-label 
    plt.subplots_adjust(bottom=0.5, top=0.99) #ajust the plot graph 
    plt.show()

"""
Function: plotBarGraph
Retun value: None
Inputs: dictonary
Description:
Plot the line graph for the key value pair of dictonary
"""
def plotLinearGraph(dictonary):

    plt.plot(*zip(*sorted(dictonary.items())))
    plt.xticks(color='red',rotation = 90)#rotate the content for x values print them in red color
    plt.yticks(color='green')
    plt.xlabel('Directory Path', fontweight='bold', color = 'red', fontsize='18')#print the x-label 
    plt.ylabel('File counts', fontweight='bold', color = 'green', fontsize='18')#print the y-label
    plt.subplots_adjust(bottom=0.5, top=0.99)
    plt.show()



if __name__ == '__main__':main()
