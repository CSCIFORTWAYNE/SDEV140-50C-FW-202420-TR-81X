"""
basic string demo
"""

filename = "something.txt"
splitFilename = filename.split('.')
if filename.split('.')[-1] == "txt":
    print("This is a text file!")

""" foundDot = False
filenameNoExt = filename[0:-4]
 for character in filename:
    if character != '.' and not foundDot:
        print(character)
        filenameNoExt += character
    else:
        foundDot = True 

print(filenameNoExt)

fileExt = filename[-3:]
 for character in range(-3,0):
    fileExt += filename[character] 


print(fileExt)

if ".txt" in filename:
    print("This is a text file!") """
