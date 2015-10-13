# !/usr/bin/python
'''
Programmer: Matthew Griffin

Description: A script that deletes all files in a user-inputted dir

'''
try:
    import os
    import shutil
    import sys

except:
    print("Python " + str(sys.version()) + "Is not installed correctly. Try re-installing.")

class Delete:
    def __init__(self):
        direct = input("Enter a dir: ")

        # Making a seperation barrier
        for x in range(0,20):
            print("-", end = "")

        # Trying to find the dir the user inputted
        try:
            print("\n")
            
            # Checking if there are any files in the dir
            if not(os.listdir(direct) == []):
                for filename in os.listdir(direct):
                    print("FOUND FILE: " + str(filename))
                    print("--- REMOVING " + str(filename))
                    
                    os.remove(direct + "/" + filename) # Actually removing files 

            # If there are no files in the directory
            else:
                print("No files found to remove in dir, " + "' " + str(direct.upper()) + " '")
                sys.exit(0)
                
        # If the user enters a dir that doesn't exit
        except FileNotFoundError:
            print("The dir that you have inputted does not exist")
            sys.exit(0)

if(__name__ == "__main__"):
    delete = Delete()

