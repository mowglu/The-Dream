import fitz
import os
from PIL import Image
import pytesseract
import tabula
import time
import pandas as pd
import numpy as np
from pathlib import Path


def dataframebuilder(index, valdata, coldata):
    df = pd.DataFrame(data=valdata, columns=[coldata], index=[index])
    return df


def excelwriter(df, checkval=0):
    mystr = os.path.dirname(os.path.realpath(__file__))
    mystr = Path(mystr)
    mystr = mystr.parent.parent.parent

    if checkval == 0:
        with pd.ExcelWriter(str(mystr) + "\Part2\Source\Source.xlsx", engine="openpyxl",
                            mode='w') as writer:
            df.to_excel(writer, sheet_name='DataEntry')
    else:
        print('Should not be able to reach here!')


def turnpdftodata(id='0', icaocodelist=['NA'], wetrwyans='NA', aircraftname='NA', maximumlist=['NA'],
                  aircraftnamelist=['NA']):
    start_time = time.time()

    if len(icaocodelist) > 1:
        # ONLY IF LIST OF AIRPORTS > 1
        mystr = os.path.dirname(os.path.realpath(__file__))
        mystr = Path(mystr)
        mystr = mystr.parent.parent.parent

        fname = str(mystr) + f'\Part2\APG_Reports\\treated{id}.pdf'
        doc = fitz.open(fname)  # open document
        numpages = 0
        for page in doc:  # iterate through the pages
            numpages += 1
            mat = fitz.Matrix(2.5, 2.5)  # zoom factor 2.5 in each direction
            clip = fitz.Rect(245, 0, 800, 43)  # the area we want
            pix = page.getPixmap(matrix=mat, clip=clip)
            pix.writePNG(str(mystr) + f"\Part2\APG_Reports\page-{page.number + 1}.png")

        mystr = os.path.dirname(os.path.realpath(__file__))
        mystr = Path(mystr)
        mystr = mystr.parent.parent.parent

        entirepath = str(mystr) + '\Part2\Tesseract\\tesseract.exe'
        pytesseract.pytesseract.tesseract_cmd = r'{}'.format(entirepath)
        textlist = []
        for i in range(1, numpages + 1):
            image = Image.open(str(mystr) + f"\Part2\APG_Reports\page-{i}.png", mode='r')
            textlist.append(pytesseract.image_to_string(image))

        mystr = os.path.dirname(os.path.realpath(__file__))
        mystr = Path(mystr)
        mystr = mystr.parent.parent.parent

        for page in doc:
            entirecommand = str(mystr) + "\Part2\APG_Reports\\page-{}.png".format(page.number + 1)
            os.remove(entirecommand)

        codelist = []
        for i in range(len(textlist)):
            if "OFF PERFORMANCE" in textlist[i] or "FF PERFORMANCE" in textlist[i] or "F PERFORMANCE" in textlist[i]:
                codelist.append(textlist[i][-4:])

        newcodes = []
        for codes in codelist:
            newcodes.append(codes.strip().upper())

        print("\n--- %s seconds to obtain code identifiers in PDF ---\n" % (time.time() - start_time))

        mystr = os.path.dirname(os.path.realpath(__file__))
        mystr = Path(mystr)
        mystr = mystr.parent.parent.parent

        start_time = time.time()
        dfs = tabula.read_pdf(str(mystr) + "\Part2\APG_Reports\\treated{}.pdf".format(id),
                              pages='all', multiple_tables=True, lattice=True, pandas_options={'header': None},
                              silent=True)
        print("\n--- %s seconds to obtain table information ---\n" % (time.time() - start_time))

        takeoffdfs = []
        for i in range(len(dfs)):
            if dfs[i][0][0][0] == '0' or dfs[i][0][0][0] == '+' or dfs[i][0][0][0] == '-':
                pass
            elif dfs[i][0][0][0].isdigit() or dfs[i][0][0][:2] == 'NA':
                pass
            else:
                try:
                    takeoffdfs.append(dfs[i].iloc[2])
                except:
                    takeoffdfs.append(dfs[i].iloc[1])

        def my_func(mystr):
            try:
                newstr = mystr[:mystr.find(' ')]
                newnum = float(newstr)
            except:
                newnum = 0
            return newnum

        TOWlist = []
        for i in range(len(takeoffdfs)):
            TOWlist.append(takeoffdfs[i].apply(my_func).max())

        startingcode = newcodes[0]
        changepos = []

        for i in range(len(newcodes)):
            if startingcode != newcodes[i]:
                changepos.append(i + 1)
                startingcode = newcodes[i]
                continue

        # print(changepos)

        uniquecodes = [newcodes[0]]
        for i in range(len(changepos)):
            uniquecodes.append(newcodes[changepos[i] - 1])

        # print(uniquecodes)

        start = 0
        count = 0
        endrange = len(uniquecodes)

        wetans = []
        if wetrwyans.startswith('Y'):
            for i in range(endrange):
                wetans.append('Y')
        else:
            for i in range(endrange):
                wetans.append('No')

        '''
        print(endrange)
        print(wetans)
        print(changepos)
        print(uniquecodes)
        '''

        for i in range(endrange):
            if wetans[i] == 'Y':
                if i != endrange - 1:
                    changepos.append(int((start + changepos[i + count] + 1) / 2))
                    changepos.sort()
                    uniquecodes.insert(i + 1 + count, uniquecodes[i + count])
                    count += 1
                    start = changepos[i + count] - 1
                else:
                    end = len(newcodes) + 2
                    changepos.append(int((start + end) / 2))
                    changepos.sort()
                    uniquecodes.insert(i + 1 + count, uniquecodes[i + count])

        changepos.sort()

        '''
        print(uniquecodes)
        print(changepos)
        print(TOWlist)
        '''

        start = 0
        end = changepos[0] - 1
        maximum = []
        quitval = False
        for i in range(len(changepos) + 1):
            maximum.append(max(TOWlist[start:end]))
            if quitval:
                break
            start = end
            if i == len(changepos) - 1:
                end = len(newcodes)
                quitval = True
            else:
                end = changepos[i + 1] - 1

        # maximum and aircraft name are the ones that stack up
        maximumlist.append(maximum)
        aircraftnamelist.append(aircraftname)

        return (uniquecodes, maximumlist, aircraftnamelist)

    else:
        mystr = os.path.dirname(os.path.realpath(__file__))
        mystr = Path(mystr)
        mystr = mystr.parent.parent.parent

        start_time = time.time()
        dfs = tabula.read_pdf(str(mystr) + "\Part2\APG_Reports\\treated{}.pdf".format(id),
                              pages='all', multiple_tables=True, lattice=True, pandas_options={'header': None},
                              silent=True)
        print("\n--- %s seconds obtain table information ---\n" % (time.time() - start_time))

        takeoffdfs = []
        for i in range(len(dfs)):
            if dfs[i][0][0][0] == '0' or dfs[i][0][0][0] == '+' or dfs[i][0][0][0] == '-':
                pass
            elif dfs[i][0][0][0].isdigit() or dfs[i][0][0][:2] == 'NA':
                pass
            else:
                takeoffdfs.append(dfs[i].iloc[2])

        def my_func(mystr):
            try:
                newstr = mystr[:mystr.find(' ')]
                newnum = float(newstr)
            except:
                newnum = 0
            return newnum

        TOWlist = []
        for i in range(len(takeoffdfs)):
            TOWlist.append(takeoffdfs[i].apply(my_func).max())

        newcodes = []
        for i in range(len(TOWlist)):
            newcodes.append(icaocodelist[0])

        startingcode = newcodes[0]
        changepos = []

        for i in range(len(newcodes)):
            if startingcode != newcodes[i]:
                changepos.append(i + 1)
                startingcode = newcodes[i]
                continue

        uniquecodes = [newcodes[0]]
        for i in range(len(changepos)):
            uniquecodes.append(newcodes[changepos[i]])

        startingcode = newcodes[0]
        changepos = []

        for i in range(len(newcodes)):
            if startingcode != newcodes[i]:
                changepos.append(i + 1)
                startingcode = newcodes[i]
                continue

        uniquecodes = [newcodes[0]]
        for i in range(len(changepos)):
            uniquecodes.append(newcodes[changepos[i]])

        start = 0
        count = 0
        endrange = len(uniquecodes)

        '''
        print(endrange)
        print(wetrwyans)
        print(changepos)
        print(uniquecodes)
        '''

        for i in range(endrange):
            if wetrwyans.upper().startswith('Y'):
                if i != endrange - 1:
                    changepos.append(int((start + changepos[i + count] + 1) / 2))
                    changepos.sort()
                    uniquecodes.insert(i + 1 + count, uniquecodes[i + count])
                    count += 1
                    start = changepos[i + count] - 1
                else:
                    end = len(newcodes) + 2
                    changepos.append(int((start + end) / 2))
                    changepos.sort()
                    uniquecodes.insert(i + 1 + count, uniquecodes[i + count])

        changepos.sort()

        '''
        print(uniquecodes)
        print(changepos)
        print(TOWlist)
        '''

        start = 0
        if len(changepos) > 0:
            end = changepos[0] - 1
            maximum = []
            quitval = False
            for i in range(len(changepos) + 1):
                maximum.append(max(TOWlist[start:end]))
                if quitval:
                    break
                start = end
                if i == len(changepos) - 1:
                    end = len(newcodes)
                    quitval = True
                else:
                    end = changepos[i + 1] - 1
        else:
            maximum = []
            maximum.append(max(TOWlist[:]))

        maximumlist.append(maximum)
        aircraftnamelist.append(aircraftname)

        return (uniquecodes, maximumlist, aircraftnamelist)


def turndatatoexcel(uniquecodes, maximumlist, aircraftnamelist):
    maximumlist = np.array(maximumlist).reshape(len(aircraftnamelist), len(uniquecodes))
    maximumlist = np.transpose(maximumlist)

    df = dataframebuilder(uniquecodes, maximumlist, aircraftnamelist)
    excelwriter(df)
