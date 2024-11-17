import os

# Globals
PATH = os.path.dirname(__name__)
mode = "locus/carbGenes.txt"
loci = []

def main():
    modeChange()
    reader()
    checker()
    print("Goodbye.")

def modeChange():
    global mode
    print("Currently set to carbohydrate transporting genes")
    while True:
        choice = input("Would you like to change it to non carb transporters? [Y/N]\n")
        if choice.upper() == "Y":
            mode = "locus/nonCarbGenes.txt"
            print("Mode changed to non-carbohydrate transporting genes.")
            break
        elif choice.upper() == "N":
            print("Continuing on with carbohydrate transporting genes.")
            break
def reader():
    global loci
    file = open(os.path.join(PATH, mode), "r", encoding= 'utf-8-sig')
    for i in file:
        loci.append(i)
    file.close()

def checker():
    # Opening the file up again but this time to make edits
    file = open(os.path.join(PATH, mode), "a", encoding='utf-8-sig')
    global loci
    print("To leave at any time type exit.")
    while True:
        # Reseting locusToCheck just to be sure.
        locusToCheck = ""

        print("\n")
        locusToCheck = input("Enter a locus number: ").strip("LOC")
        locusToCheck = locusToCheck + "\n"

        # Exit case that also closes our file after appending things to it
        if locusToCheck.lower() == "exit\n":
            file.close()
            break

        if locusToCheck in loci:
            print("You have already checked this before.")
        else:
            print("Not seen before. Adding to list.")
            # Have to add to both the list and the document for future runs of the program
            file.write(locusToCheck)
            loci.append(locusToCheck)
            print(loci)

if __name__ == "__main__":
    main()
