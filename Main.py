from os import listdir, rename, path
from tkinter.filedialog import askdirectory, Tk
from sys import exit

try:
    Tk().withdraw() # Avoids showing tk window
    filename = askdirectory()
    listFiles = listdir(filename)

    for file in listFiles:
        result = None
        while result is None:
            inp = str(input(f"{file} change to: "))
            if inp:
                try:
                    inpAreYouSure = str(input("Are you sure you want to change this file? Press [Enter] for yes"))
                    if inpAreYouSure:
                        continue
                    else:
                        rename(filename + "/" + file, filename + "/" + inp + path.splitext(file)[1])
                        result = True
                    # print(filename+"/"+file, filename+"/"+inp+path.splitext(file)[1])
                except (FileExistsError, OSError) as e:
                    print(e)
            else:
                inpAreYouSure = str(input("Press [Enter] to not change file"))
                if inpAreYouSure:
                    continue
                else:
                    result = True

except FileNotFoundError:
    exit(0)

