import os, inspect, sys

from pathlib import Path

# Correction folder path because main.exe is two folders deep from main directory
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
currentdir = parentdir
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from Part1.SearchSite import main, tempforAPG, ICAOcodeforAPG, grooveforAPG
from Part2.BrowsingAPG import part2
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

ans = 'Yes'
skipans = 0

# VERSION CHECK

bombardierIDs = []
mystr = os.path.dirname(os.path.realpath(__file__))
mystr = Path(mystr)
mystr = mystr.parent.parent
f = open(str(mystr) + "\Part1\Bombardier ID.txt", "r")
lines = f.readlines()

for i in range(len(lines)):
    if ':' in lines[i]:
        idstring = lines[i][lines[i].find(':') + 1:-1]
        bombardierIDs.append(idstring.strip())
f.close()

filepathlist = [
    'Bombardier\Sales Engineering - Documents\Sales Engineering - DO NOT SYNC\Performance Tools\The Dream\Synced Files',
    'Bombardier\Sales Engineering - Sales Engineering - DO NOT SYNC\Performance Tools\The Dream\Synced Files',
    'Bombardier\Sales Engineering - Performance Tools\The Dream\Synced Files',
    'Bombardier\Sales Engineering - The Dream\Synced Files', 'Bombardier\Sales Engineering - Synced Files']
for i in range(len(bombardierIDs)):
    for j in range(len(filepathlist)):
        try:
            sharepointFile = open(
                f"C:\\Users\\{bombardierIDs[i]}\\{filepathlist[j]}\Latest Version.txt", "r")
        except:
            pass

dataLatest = sharepointFile.readlines()
localFile = open(str(mystr) + "\\Version Info.txt", "r")
dataLocal = localFile.readlines()
versionLatest = dataLatest[0].strip("\n")
dateLatest = dataLatest[1].strip("\n")
versionLocal = dataLocal[0].strip("\n")
dateLocal = dataLocal[1].strip("\n")

if versionLatest != versionLocal or dateLatest != dateLocal:
    print(
        f"Your version of The Dream is out of date.\n\nLatest available version: {versionLatest}\nUpdated on: {dateLatest}\n\nYour current version: {versionLocal}\nUpdated on: {dateLocal}\n\nPlease reinstall for best results.\n\n")
else:
    print(
        f"The Dream is running up to date with the latest version: {versionLocal}\t Last update on: {dateLocal}")
sharepointFile.close()
localFile.close()

# VERSION CHECK - END

while ans.upper().startswith('Y'):
    while True:
        try:
            skipans = int(input('\n1. Start "The Dream"\t2. Go directly to Part 2 with the last Part 1 Source file\n'))
            if skipans not in (1, 2):
                print('Please choose either Option 1 or Option 2.\n')
                continue
        except:
            print('Unexpected error occurred... Make sure you are typing a number!\n')
            continue
        break

    if skipans == 1:
        airportcode = main()
        if airportcode == 0:
            ans = input("Part 1 Source file ready\n\n*FRESH START* Go again? Y for yes, otherwise for no.\n")
        else:
            part2ans = input(
                'Part 1 Source file ready.\nMake sure you CONFIRM TEMPERATURES in Part 1!\nGo into Part 2? Y for yes, otherwise for no.\n')
            if part2ans.upper().startswith('Y'):
                while True:
                    temperatures = tempforAPG(airportcode)
                    if type(temperatures) == int:
                        if temperatures == 0:
                            print(
                                '\nError occurred. You may not have confirmed temperatures in Excel file.\nClick the CONFIRM TEMPERATURE button now.')
                            ans = input('Press Enter once ready!\n')
                            continue
                        elif temperatures == 1:
                            print(
                                '\nLength mismatch between ICAO codes in current Source file, and confirmed temperatures.\nMake sure to import from Part 1 Source file, and then confirm temperatures.')
                            ans = input('Press Enter once ready!\n')
                            continue
                        else:
                            print('am i here?')
                            pass
                    break

                (grooveicaocodelist, tempgroovelist, nongrooveicaocodelist, tempnongroovelist) = grooveforAPG()
                part2(temperatures, airportcode, grooveicaocodelist, tempgroovelist, nongrooveicaocodelist,
                      tempnongroovelist)
                ans = input("\n*FRESH START* Go again? Y for yes, otherwise for no.\n")
            else:
                ans = input("\n*FRESH START* Go again? Y for yes, otherwise for no.\n")

    elif skipans == 2:
        airportcode = ICAOcodeforAPG()
        while True:
            temperatures = tempforAPG(airportcode)
            if type(temperatures) == int:
                if temperatures == 0:
                    print(
                        '\nError occurred. You may not have confirmed temperatures in Excel file.\nClick the CONFIRM TEMPERATURE button now.')
                    ans = input('Press Enter once ready!\n')
                    continue
                elif temperatures == 1:
                    print(
                        '\nLength mismatch between ICAO codes in current Source file, and confirmed temperatures.\nMake sure to import from Part 1 Source file, and then confirm temperatures.')
                    ans = input('Press Enter once ready!\n')
                    continue
                else:
                    pass
            break
        (grooveicaocodelist, tempgroovelist, nongrooveicaocodelist, tempnongroovelist) = grooveforAPG()
        part2(temperatures, airportcode, grooveicaocodelist, tempgroovelist, nongrooveicaocodelist,
              tempnongroovelist)
        ans = input("\n*FRESH START* Go again? Y for yes, otherwise for no.\n")
