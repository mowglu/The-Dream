from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
import numpy as np
from pathlib import Path

# TODO change back when including main
from Part2.PDFTreatment import treatWatermark
from Part2.PDFtoData import turnpdftodata, turndatatoexcel


# TODO change back when testing only this script
# from PDFTreatment import treatWatermark
# from PDFtoData import turnpdftodata, turndatatoexcel

def groovedairfield(myusername, mypassword, airplanedict, mychoice, airplanePlusFactor, grooveicaocodelist, defaultans,
                    nongrooveicaocodelist, tempgroovelist):
    if len(grooveicaocodelist) == 0:
        pass

    else:
        mystr = os.path.dirname(os.path.realpath(__file__))
        mystr = Path(mystr)
        mystr = mystr.parent.parent.parent

        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {
            "download.default_directory": str(mystr) + "\Part2\APG_Reports\\",
            # Change default directory for downloads
            "download.prompt_for_download": False,  # To auto download the file
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
        })
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(str(mystr) + '/Part2/chromedriver.exe', options=options)
        # Open the website
        driver.get('https://atlas.apgdata.com/WinPlan5/Login.aspx')

        time.sleep(1)

        login_box = driver.find_element_by_id('MainContent_LoginBox')
        password_box = driver.find_element_by_id('MainContent_Password')

        login_box.send_keys(myusername)
        password_box.send_keys(mypassword)

        login_button = driver.find_element_by_id('LoginButton')
        login_button.click()

        try:
            WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
            driver.execute_script("document.getElementById('MainContent_ddlAircraft').style.display='inline-block';")
            element = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.ID, 'MainContent_ddlAircraft')))
            # Selecting which aircraft to choose
            Select(element).select_by_value(
                airplanedict[mychoice + airplanePlusFactor])
        except Exception as ex:
            print(ex)

        onlywetrwy1 = [1, 2, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58, 10, 11, 12, 13, 25, 26, 27, 28, 29, 30, 31, 32,
                       35, 36, 37, 38, 39, 40, 46, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 74, 75, 76]
        # For WET RUNWAY (TO)
        onlywetrwy2 = [16, 17, 18, 19, 21, 22, 23, 24]
        # For Wet (TO)
        onlywetrwy3 = [69, 71, 72, 73]
        # For WET RWY (RCAM - 5) (TO)
        onlywetrwy4 = [41, 42, 43, 44]
        # For WET RWY (D) (TO)
        onlywetrwy5 = [45]

        # For wet runways...
        # For WET RWY (TO)
        wetrwy1 = [3, 51]
        # For WET RUNWAY (TO)
        wetrwy2 = [4, 5, 6, 7, 8, 9, 14, 15]
        # For WET RWY - SMOOTH SURFACE (TO)
        wetrwy3 = [20]
        # For Wet (TO)
        wetrwy4 = [70]

        # For wet grooved runways...
        # For WET - GROOVED (TO)
        wetgroovedrwy1 = [3, 6, 8, 9]
        # For WET GROOVED RWY (TO)
        wetgroovedrwy2 = [4, 14, 15]
        # For WET GROOVED RUNWAY (TO)
        wetgroovedrwy3 = [5, 7]
        # For WET RWY - GROOVED SURFACE (TO)
        wetgroovedrwy4 = [20]
        # For WET, GROOVED RWY (TO)
        wetgroovedrwy5 = [51]
        # For Wet - Grooved Runway (TO)
        wetgroovedrwy6 = [70]

        if mychoice + airplanePlusFactor in wetgroovedrwy1:
            try:
                WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
                driver.execute_script(
                    "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                element = WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                Select(element).select_by_visible_text('WET - GROOVED (TO)')
            except Exception as ex:
                print(ex)
        elif mychoice + airplanePlusFactor in wetgroovedrwy2:
            try:
                WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
                driver.execute_script(
                    "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                element = WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                Select(element).select_by_visible_text('WET GROOVED RWY (TO)')
            except Exception as ex:
                print(ex)
        elif mychoice + airplanePlusFactor in wetgroovedrwy3:
            try:
                WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
                driver.execute_script(
                    "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                element = WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                Select(element).select_by_visible_text('WET GROOVED RUNWAY (TO)')
            except Exception as ex:
                print(ex)
        elif mychoice + airplanePlusFactor in wetgroovedrwy4:
            try:
                WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
                driver.execute_script(
                    "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                element = WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                Select(element).select_by_visible_text('WET RWY - GROOVED SURFACE (TO)')
            except Exception as ex:
                print(ex)
        elif mychoice + airplanePlusFactor in wetgroovedrwy5:
            try:
                WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
                driver.execute_script(
                    "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                element = WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                Select(element).select_by_visible_text('WET, GROOVED RWY (TO)')
            except Exception as ex:
                print(ex)
        elif mychoice + airplanePlusFactor in wetgroovedrwy6:
            try:
                WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
                driver.execute_script(
                    "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                element = WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                Select(element).select_by_visible_text('Wet - Grooved Runway (TO)')
            except Exception as ex:
                print(ex)
        elif mychoice + airplanePlusFactor in onlywetrwy1 or mychoice + airplanePlusFactor in wetrwy1:
            try:
                WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
                driver.execute_script(
                    "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                element = WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                Select(element).select_by_visible_text('WET RWY (TO)')
            except Exception as ex:
                print(ex)
        elif mychoice + airplanePlusFactor in onlywetrwy2 or mychoice + airplanePlusFactor in wetrwy2:
            try:
                WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
                driver.execute_script(
                    "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                element = WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                Select(element).select_by_visible_text('WET RUNWAY (TO)')
            except Exception as ex:
                print(ex)
        elif mychoice + airplanePlusFactor in wetrwy3:
            try:
                WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located((By.ID, 'btnCompute')))
                driver.execute_script(
                    "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                element = WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                Select(element).select_by_visible_text('WET RWY - SMOOTH SURFACE (TO)')
            except Exception as ex:
                print(ex)
        elif mychoice + airplanePlusFactor in onlywetrwy3 or mychoice + airplanePlusFactor in wetrwy4:
            try:
                WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
                driver.execute_script(
                    "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                element = WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                Select(element).select_by_visible_text('Wet (TO)')
            except Exception as ex:
                print(ex)
        elif mychoice + airplanePlusFactor in onlywetrwy4:
            try:
                WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
                driver.execute_script(
                    "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                element = WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                Select(element).select_by_visible_text('WET RWY (RCAM - 5) (TO)')
            except Exception as ex:
                print(ex)
        elif mychoice + airplanePlusFactor in onlywetrwy5:
            try:
                WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
                driver.execute_script(
                    "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                element = WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                Select(element).select_by_visible_text('WET RWY (D) (TO)')
            except Exception as ex:
                print(ex)
        # nothing happens if mychoice + airplaneplusfactor is non-grooved supplementary aircraft
        else:
            pass

        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID, 'MainContent_osTOOptionSelector_OptionButton')))
        TO_Options_button = driver.find_element_by_id('MainContent_osTOOptionSelector_OptionButton')
        TO_Options_button.click()

        time.sleep(3)

        # Switching off ECS ON and APU ON and Rolling takeoff and APR OFF and Bleeds OPEN
        # For G150, APR OFF is NOT pressed! In fact, nothing needs to be pressed
        listofoptions = ["ECS ON", "APU ON", "ROLLING TAKEOFF", "ROLLING TO", "Rolling T/O", "ROLLING T/O", "APR OFF",
                         "BLEEDS OPEN",
                         "BLD OPEN", "BLD OPEN A/I OFF", "BLEEDS ON", "WITH THRUST REVERSERS", "WITH REVERSE THRUST"]
        for options in listofoptions:
            try:
                if mychoice + airplanePlusFactor == 38:  # For the G150, nothing needs to be done. If proceeded, APR OFF will be pressed, which is not desirable
                    break
                # WebDriverWait(driver, 0.1).until(
                # EC.visibility_of_element_located((By.XPATH,f'//*[@title="{options}"]')))
                button = driver.find_element_by_xpath(f'//*[@title="{options}"]')
                button.click()
            except:
                pass

        # Switching on ECS OFF and APU OFF and Static takeoff and APR ON and BLEEDS CLOSED
        done_button = driver.find_element_by_id('MainContent_osTOOptionSelector_OptionMultiSelect_done')
        listofoptions = ["APU OFF", "BLEEDS OFF", "BLEEDS CLOSED", "BLD CLSD", "STATIC TO", "STATIC TAKEOFF",
                         "Static T/O", "STATIC T/O",
                         "ECS OFF", "APR ON", "APR ARMED", "WITHOUT THRUST REVERSERS", "WITHOUT REVERSE THRUST"]
        counter = 4
        for options in listofoptions:
            try:
                # WebDriverWait(driver, 0.1).until(
                # EC.visibility_of_element_located((By.XPATH, '//*[@title="' + options + '"]')))
                checked = driver.find_element_by_xpath('//*[@title="' + options + '"]').is_selected()
                if checked == True:
                    done_button.click()
                    try:
                        driver.find_element_by_id('ui-dialog-title-option-dialog-error')
                        WebDriverWait(driver, 0.1).until(
                            EC.visibility_of_element_located(
                                (By.XPATH, '/ html / body / div[' + str(counter) + '] / div[11] / div / button')))
                        # ONLY ABSOLUTE XPATH
                        ok_button = driver.find_element_by_xpath(
                            '/ html / body / div[' + str(counter) + '] / div[11] / div / button')
                        ok_button.click()
                        counter += 1
                    except:
                        pass
                else:
                    # WebDriverWait(driver, 0.1).until(
                    # EC.visibility_of_element_located((By.XPATH, '//*[@title="' + options + '"]')))
                    driver.find_element_by_xpath('//*[@title="' + options + '"]').click()
                    done_button.click()
                    try:
                        driver.find_element_by_id('ui-dialog-title-option-dialog-error')
                        WebDriverWait(driver, 0.1).until(
                            EC.visibility_of_element_located(
                                (By.XPATH, '/ html / body / div[' + str(counter) + '] / div[11] / div / button')))
                        # ONLY ABSOLUTE XPATH
                        ok_button = driver.find_element_by_xpath(
                            '/ html / body / div[' + str(counter) + '] / div[11] / div / button')
                        ok_button.click()
                        counter += 1
                    except:
                        pass
            except:
                continue

        # In case that the ok done button in takeoff options is still up, select it and make takeoff options disappear so that ICAO codes can be entered
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.ID, 'MainContent_osTOOptionSelector_OptionMultiSelect_done')))
            driver.find_element_by_id('MainContent_osTOOptionSelector_OptionMultiSelect_done').click()
        except:
            pass

        newgrooveicaocodelist = []
        removedposlist = []
        for i in range(len(grooveicaocodelist)):
            WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located((By.ID, 'MainContent_txtICAO')))
            icao_code_box = driver.find_element_by_id('MainContent_txtICAO')
            icao_code_box.click()
            icao_code_box.send_keys(grooveicaocodelist[i])

            if defaultans.upper().startswith('Y'):
                to_button = driver.find_element_by_id('btnAddTOICAO')
                to_button.click()
                # Click ok button if ICAO code does not exist on APG
                try:
                    time.sleep(1)
                    driver.find_element_by_id('ui-dialog-title-dialog-error')
                    try:
                        driver.find_element_by_xpath("/ html / body / div[3] / div[11] / div / button").click()
                        print(f"'{grooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                        removedposlist.append(i)
                    except:
                        try:
                            driver.find_element_by_xpath("/ html / body / div[4] / div[11] / div / button").click()
                            print(f"'{grooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                            removedposlist.append(i)
                        except:
                            try:
                                driver.find_element_by_xpath("/ html / body / div[5] / div[11] / div / button").click()
                                print(f"'{grooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                                removedposlist.append(i)
                            except:
                                try:
                                    driver.find_element_by_xpath(
                                        "/ html / body / div[6] / div[11] / div / button").click()

                                    print(f"'{grooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                                    removedposlist.append(i)
                                except:
                                    newgrooveicaocodelist.append(grooveicaocodelist[i])
                except:
                    newgrooveicaocodelist.append(grooveicaocodelist[i])
                    pass

            else:
                to_ans = input(
                    f'Do you want to add takeoff, or both takeoff and landing for {grooveicaocodelist[i]}? T for only takeoff, otherwise for both\n')
                to_button = driver.find_element_by_id('btnAddTOICAO')
                both_button = driver.find_element_by_id('btnAddBothICAO')
                if to_ans.upper().startswith('T'):
                    to_button.click()
                    try:
                        time.sleep(1)
                        driver.find_element_by_id('ui-dialog-title-dialog-error')
                        try:
                            driver.find_element_by_xpath("/ html / body / div[3] / div[11] / div / button").click()
                            print(f"'{grooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                            removedposlist.append(i)
                        except:
                            try:
                                driver.find_element_by_xpath("/ html / body / div[4] / div[11] / div / button").click()
                                print(f"'{grooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                                removedposlist.append(i)
                            except:
                                try:
                                    driver.find_element_by_xpath(
                                        "/ html / body / div[5] / div[11] / div / button").click()
                                    print(f"'{grooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                                    removedposlist.append(i)
                                except:
                                    try:
                                        driver.find_element_by_xpath(
                                            "/ html / body / div[6] / div[11] / div / button").click()
                                        print(f"'{grooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                                        removedposlist.append(i)
                                    except:
                                        newgrooveicaocodelist.append(grooveicaocodelist[i])
                    except:
                        newgrooveicaocodelist.append(grooveicaocodelist[i])
                        pass
                else:
                    both_button.click()
                    try:
                        time.sleep(1)
                        driver.find_element_by_id('ui-dialog-title-dialog-error')
                        try:
                            driver.find_element_by_xpath("/ html / body / div[3] / div[11] / div / button").click()
                            print(f"'{grooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                            removedposlist.append(i)
                        except:
                            try:
                                driver.find_element_by_xpath("/ html / body / div[4] / div[11] / div / button").click()
                                print(f"'{grooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                                removedposlist.append(i)
                            except:
                                try:
                                    driver.find_element_by_xpath(
                                        "/ html / body / div[5] / div[11] / div / button").click()
                                    print(f"'{grooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                                    removedposlist.append(i)
                                except:
                                    try:
                                        driver.find_element_by_xpath(
                                            "/ html / body / div[6] / div[11] / div / button").click()
                                        print(f"'{grooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                                        removedposlist.append(i)
                                    except:
                                        newgrooveicaocodelist.append(grooveicaocodelist[i])
                    except:
                        newgrooveicaocodelist.append(grooveicaocodelist[i])
                        pass

        # Quitting code entirely if no valid ICAO codes for APG is passed.
        if len(nongrooveicaocodelist) == 0 and len(newgrooveicaocodelist) == 0:
            print('APG could not process any of the ICAO codes.\nExiting APG.')
            return (0, 0, 0, 0)
        elif len(newgrooveicaocodelist) == 0:
            print('APG could not process any of the ICAO codes for grooved airfields.\n')
            return (1, 1, 1, 1)
        else:
            # Even though below list is named isa15c_list, temperatures MAY not be that. This is simply the defult choice computed by Part 1
            isa15c_list = [round(num) for num in tempgroovelist]

            # Below code executes if some APG ICAO codes were not processed
            if len(newgrooveicaocodelist) != len(grooveicaocodelist):
                for ele in sorted(removedposlist, reverse=True):
                    del isa15c_list[ele]

            # Redefining icao code list to a list accepted by APG
            grooveicaocodelist = newgrooveicaocodelist

            time.sleep(2)

            # isa15c_list = [23, 30]
            for i in range(len(grooveicaocodelist)):
                temp_box = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="jqg' + str(i + 1) + '"]/td[10]')))
                temp_box.click()
                temp_box.send_keys(isa15c_list[i])
                driver.execute_script("arguments[0].innerText='{}'".format(str(isa15c_list[i])), temp_box)

            # make sure use temp checkbox is ticked
            for i in range(len(grooveicaocodelist)):
                check_box = driver.find_element_by_xpath('//*[@id="jqg' + str(i + 1) + '"]/td[9]/input')
                checked = check_box.is_selected()
                if checked:
                    pass
                else:
                    check_box.click()

            # SUBMIT!
            driver.find_element_by_id('btnCompute').click()

            found = False
            try_count = 0

            # Max 3 seconds of wait
            while not found and try_count <= 1:
                try_count += 1
                try:
                    WebDriverWait(driver, 3).until(
                        EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[11]/div/button'))).click()
                    found = True
                except:
                    try:
                        WebDriverWait(driver, 3).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[11]/div/button'))).click()
                        found = True
                    except:
                        try:
                            WebDriverWait(driver, 3).until(
                                EC.presence_of_element_located(
                                    (By.XPATH, '/html/body/div[6]/div[11]/div/button'))).click()
                            found = True
                        except:
                            try:
                                WebDriverWait(driver, 3).until(
                                    EC.presence_of_element_located(
                                        (By.XPATH, '/html/body/div[7]/div[11]/div/button'))).click()
                                found = True
                            except:
                                print('None of the Xpaths for OK button worked. Trying again...\n')

            # Go to next page
            driver.find_element_by_xpath('//*[@id="tabs"]/ul/li[2]').click()

            # Click checkmark and then view jobs button. If not there, wait for 5 seconds and reload page
            try:
                time.sleep(2)
                checkmark = driver.find_element_by_xpath(
                    '/html/body/form/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/div[3]/div[3]/div/table/tbody/tr[2]/td[1]/input')
                checkmark.click()

            except:
                # wait 5 seconds and then refresh page. If doesn't load up by then, try waiting another 5 seconds and refresh again. Repeat.
                while True:
                    try:
                        time.sleep(5)
                        driver.refresh()
                        time.sleep(2)
                        checkmark = driver.find_element_by_xpath(
                            '/html/body/form/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/div[3]/div[3]/div/table/tbody/tr[2]/td[1]/input')
                        checkmark.click()
                        break
                    except:
                        continue

            # Get id,date, and aircraft name from APG
            idnumber = checkmark.get_attribute("id")
            idnumber = idnumber[9:]

            startdate_el = driver.find_element_by_xpath('//*[@id="{}"]/td[4]'.format(idnumber))
            date = startdate_el.text
            date = date[:10]

            s = airplanedict[mychoice + airplanePlusFactor]
            char = '|'
            pipeposlist = [pos for pos, c in enumerate(s) if char == c]
            # Getting only 2nd and 3rd occurrence to serve as start and end
            impposlist = pipeposlist[1:3]
            aircraftname = airplanedict[mychoice + airplanePlusFactor][impposlist[0] + 1:impposlist[1]]
            # Download pdf
            driver.find_element_by_id('btnViewJobs').click()

            # Close all windows
            time.sleep(10)
            driver.quit()

            return (idnumber, date, aircraftname, grooveicaocodelist)


def part2(temperatures, icaocodelist, grooveicaocodelist, tempgroovelist, nongrooveicaocodelist, tempnongroovelist):
    while True:
        try:
            apgchoice = int(input('\n1. APG\t\t2. APG EASA\n'))
            if apgchoice not in (1, 2):
                print('Please enter either 1 or 2!\n')
                continue
            break
        except TypeError:
            print('You did not enter a number.\n')
            continue
        except:
            print('Unexpected error occurred. Please try again...\n')
            continue

    mystr = os.path.dirname(os.path.realpath(__file__))
    mystr = Path(mystr)
    mystr = mystr.parent.parent.parent

    f = open(str(mystr) + "\Part2\Login.txt", "r")
    lines = f.readlines()
    for i in range(len(lines)):
        if apgchoice == 1:
            if lines[i] == "APG\n":
                pos = lines[i + 1].find(':')
                myusername = lines[i + 1][pos + 1:]
                myusername = myusername.strip()
                pos = lines[i + 2].find(':')
                mypassword = lines[i + 2][pos + 1:]
                mypassword = mypassword.strip()
        elif apgchoice == 2:
            if lines[i] == "APGEASA\n":
                pos = lines[i + 1].find(':')
                myusername = lines[i + 1][pos + 1:]
                myusername = myusername.strip()
                pos = lines[i + 2].find(':')
                mypassword = lines[i + 2][pos + 1:]
                mypassword = mypassword.strip()
    f.close()

    diffaircraftans = 'Yes'
    maximumlist = []
    aircraftnamelist = []
    secondtime = False
    wetrwyans = 'No'
    aircraftcount = 0
    i = 0

    while diffaircraftans.upper().startswith('Y'):
        start_time = time.time()

        mystr = os.path.dirname(os.path.realpath(__file__))
        mystr = Path(mystr)
        mystr = mystr.parent.parent.parent

        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {
            "download.default_directory": str(mystr) + "\Part2\APG_Reports\\",
            # Change default directory for downloads
            "download.prompt_for_download": False,  # To auto download the file
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
        })
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(str(mystr) + '/Part2/chromedriver.exe', options=options)
        # Open the website
        driver.get('https://atlas.apgdata.com/WinPlan5/Login.aspx')

        time.sleep(1)

        login_box = driver.find_element_by_id('MainContent_LoginBox')
        password_box = driver.find_element_by_id('MainContent_Password')

        login_box.send_keys(myusername)
        password_box.send_keys(mypassword)

        login_button = driver.find_element_by_id('LoginButton')
        login_button.click()

        OEMdict = {1: 'Bombardier', 2: 'Gulfstream', 3: 'Cessna', 4: 'Dassault', 5: 'Embraer', 6: 'Other'}

        bomDictCurr = {1: 'Learjet 75', 2: 'Learjet 75 Liberty', 3: 'Challenger 350', 4: 'Challenger 650',
                       5: 'Global 5000',
                       6: 'Global 5500', 7: 'Global 6000', 8: 'Global 6500', 9: 'Global 7500'}

        bomDictOld = {1: 'Challenger 300', 2: 'Challenger 600', 3: 'Challenger 600-2C', 4: 'Challenger 601',
                      5: 'Challenger 604', 6: 'Challenger 605', 7: 'Challenger 850', 8: 'Challenger 850-FAA',
                      9: 'CRJ200', 10: 'CRJ200F68', 11: 'CRJ700', 12: 'Global 5000 (non-V)', 13: 'Global 6000 (non-V)',
                      14: 'Global Express', 15: 'Global XRS', 16: 'Learjet 31', 17: 'Learjet 35', 18: 'Learjet 40',
                      19: 'Learjet 40XR', 20: 'Learjet 45', 21: 'Learjet 45XR', 22: 'Learjet 55', 23: 'Learjet 55 ATR',
                      24: 'Learjet 55C', 25: 'Learjet 55 CATR', 26: 'Learjet 60', 27: 'Learjet 60XR', 28: 'Learjet 70'}

        gulDict = {1: 'G150', 2: 'G200', 3: 'G280', 4: 'G450', 5: 'G550', 6: 'G650', 7: 'G650ER', 8: 'G-IV', 9: 'G-V'}

        cesDict = {1: 'Citation Bravo', 2: 'Citation CJ3+', 3: 'Citation CJ4', 4: 'Citation Encore+',
                   5: 'Citation Latitude', 6: 'Citation Sovereign', 7: 'Citation Sovereign+', 8: 'Citation X',
                   9: 'Citation XL', 10: 'Citation XLS', 11: 'Citation XLS+', 12: 'Citation X+'}

        dasDict = {1: 'Falcon 2000', 2: 'Falcon 20000EX EASy', 3: 'Falcon 2000LX', 4: 'Falcon 2000LXS',
                   5: 'Falcon 2000S', 6: 'Falcon 50EX', 7: 'Falcon 7X', 8: 'Falcon 8X', 9: 'Falcon 900B',
                   10: 'Falcon 900LX'}

        embDict = {1: 'Legacy 600', 2: 'Phenom 300', 3: 'Legacy 450', 4: 'Legacy 500', 5: 'Legacy 650'}

        othDict = {1: 'Hawker 800XP', 2: 'Hawker 850XP', 3: 'Hawker 900XP'}

        planeCount = [len(bomDictCurr) + len(bomDictOld), len(gulDict), len(cesDict), len(dasDict), len(embDict)]

        print()
        for k, v in OEMdict.items():
            print(k, v)

        while True:
            try:
                mychoice = int(input('Enter your choice (should be a positive integer number)\n'))
                if mychoice not in list(range(1, len(OEMdict) + 1)):
                    print(f'Please enter a number from 1 to {len(OEMdict)}.\n')
                    continue
            except:
                print('Unexpected error occurred. Please type an integer number!')
                continue
            break

        airplanePlusFactor = 0

        if mychoice == 1:
            BAdict = {1: 'Current', 2: 'Out of production'}
            print()
            for k, v in BAdict.items():
                print(k, v)

            while True:
                try:
                    subChoice = int(input('Enter your choice (should be a positive integer number)\n'))
                    if subChoice not in list(range(1, len(BAdict) + 1)):
                        print(f'Please enter a number from 1 to {len(BAdict)}.\n')
                        continue
                except:
                    print('Unexpected error occurred. Please type an integer number!')
                    continue
                break

            if subChoice == 1:
                mydict = bomDictCurr
            else:  # out of production aircraft
                mydict = bomDictOld
                airplanePlusFactor = len(bomDictCurr)  # special case where we dont need to count the brand planes

        elif mychoice == 2:
            mydict = gulDict
        elif mychoice == 3:
            mydict = cesDict
        elif mychoice == 4:
            mydict = dasDict
        elif mychoice == 5:
            mydict = embDict
        elif mychoice == 6:
            mydict = othDict
        else:
            print('Should not be able to reach here!')

        # after the choosing is done
        if mychoice - 1 != 0:
            for i in range(mychoice - 1):
                airplanePlusFactor += planeCount[i]

        '''
            ; if 2, then just all aircraft of that OEM
        if 1, then below


        mydict = {1: 'Learjet 75', 2: 'Learjet 75 Liberty', 3: 'Challenger 350', 4: 'Challenger 650', 5: 'Global 5000',
                  6: 'Global 5500', 7: 'Global 6000', 8: 'Global 6500', 9: 'Global 7500'}
        '''

        print()
        for k, v in mydict.items():
            print(k, v)

        while True:
            try:
                mychoice = int(input('Enter your choice (should be a positive integer number)\n'))
                if mychoice not in list(range(1, len(mydict) + 1)):
                    print(f'Please enter a number from 1 to {len(mydict)}.\n')
                    continue
                elif mychoice + airplanePlusFactor in [17,
                                                       47] and apgchoice == 2:  # case for cl850FAA and citation bravo in APG EASA
                    print('Sorry, the chosen model is not available on APG EASA, but is available on APG.\n')
                    continue
                else:
                    pass
            except:
                print('Unexpected error occurred. Please type an integer number!')
                continue
            break

        if apgchoice == 1:
            aircrafttags = ''
        else:
            aircrafttags = 'EASA'

        airplanedict = {1: 'LJ75|40BR1B|LJ75|NewGen|1000|Learict{}'.format(aircrafttags),
                        2: 'LJ75|40BR1B|LJ75|NewGen|1000|Learict{}'.format(aircrafttags),
                        3: 'CL-350|HTF7350|CL350|NewGen|1000|Learict{}'.format(aircrafttags),
                        4: 'CL-650|CF34-3B|CL650|NewGen|1000|Learict{}'.format(aircrafttags),
                        5: 'GLOBAL5000V|A220|GLEX5000V|NewGen|1000|Learict{}'.format(aircrafttags),
                        6: 'GLOBAL5500|BR700-710D5-21|GLOBAL5500|NewGen|1000|Learict{}'.format(aircrafttags),
                        7: 'GLOBAL6000V|A220|GLEX6000V|NewGen|1000|Learict{}'.format(aircrafttags),
                        8: 'GLOBAL6500|BR700-710D5-21|GLOBAL6500|NewGen|1000|learict{}'.format(aircrafttags),
                        9: 'GLOBAL7500|GEP20-19BB1A|GLOBAL7500|NewGen|1000|learict{}'.format(aircrafttags),
                        10: 'CL-300|AS907|CL300|NewGen|1000|Learict{}'.format(aircrafttags),
                        11: 'CL-600|ALF502L-2|CL600|NewGen|1000|Learict{}'.format(aircrafttags),
                        12: 'CL-600|ALF502L-2C|CL6002C|NewGen|1000|Learict{}'.format(aircrafttags),
                        13: 'CL-601|CF34-3A|CL601 3A|NewGen|1000|Learict{}'.format(aircrafttags),
                        14: 'CL-604|CF34-3B|CL604|NewGen|1000|Learict{}'.format(aircrafttags),
                        15: 'CL-605|CF34-3B|CL605|NewGen|1000|Learict{}'.format(aircrafttags),
                        16: 'CL850|CF343B1|CL850|NewGen|1000|Learict{}'.format(aircrafttags),
                        17: 'CL850FAA0068|CF343B1|CL850FAAHH|NewGen|1000|Learict{}'.format(aircrafttags),
                        18: 'CRJ200|CF343B1|CRJ200|NewGen|1000|Learict{}'.format(aircrafttags),
                        19: 'CRJ200F68|CF343B1|CRJ200F68|NewGen|1000|Learict{}'.format(aircrafttags),
                        20: 'CRJ700|CF34-8C1|CRJ700|NewGen|1000|Learict{}'.format(aircrafttags),
                        21: 'GLOBAL5000|A220|GLEX5000|NewGen|1000|Learict{}'.format(aircrafttags),
                        22: 'GLOBAL6000|A220|GLEX6000|NewGen|1000|Learict{}'.format(aircrafttags),
                        23: 'GLOBALEXP|A220|GLEX|NewGen|1000|Learict{}'.format(aircrafttags),
                        24: 'GLOBALXRS|A220|GLEX XRS|NewGen|1000|Learict{}'.format(aircrafttags),
                        25: 'LJ31A|TFE73123B|LJ31A|NewGen|1000|Learict{}'.format(aircrafttags),
                        26: 'LJ35A|TFE731|LJ35A|NewGen|1000|Learict{}'.format(aircrafttags),
                        27: 'LJ40|TFE73120AR1B|LJ40|NewGen|1000|Learict{}'.format(aircrafttags),
                        28: 'LJ40XR|TFE73120BR1B|LJ40XR|NewGen|1000|Learict{}'.format(aircrafttags),
                        29: 'LJ45|20AR1B|LJ45|NewGen|1000|Learict{}'.format(aircrafttags),
                        30: 'LJ45XR|20BR1B|LJ45XR|NewGen|1000|Learict{}'.format(aircrafttags),
                        31: 'LJ55|TFE7313AR2B|LJ55 1A|NewGen|1000|Learict{}'.format(aircrafttags),
                        32: 'LJ55ATR|TFE7313AR2B|LJ55ATR|NewGen|1000|Learict{}'.format(aircrafttags),
                        33: 'LJ55C|TFE7313AR|LJ55C|NewGen|1000|Learict{}'.format(aircrafttags),
                        34: 'LJ55CATR|TFE7313AR|LJ55CATR|NewGen|1000|Learict{}'.format(aircrafttags),
                        35: 'LJ60|PW305A|LJ60|NewGen|1000|Learict{}'.format(aircrafttags),
                        36: 'LJ60XR|PW305A|LJ60XR|NewGen|1000|Learict{}'.format(aircrafttags),
                        37: 'LJ70|40BR1B|LJ70|NewGen|1000|Learict{}'.format(aircrafttags),
                        38: 'G150|TFE73140AR|G150|NewGen|1000|Learict{}'.format(aircrafttags),
                        39: 'G200|PW306A|G200|NewGen|1000|Learict{}'.format(aircrafttags),
                        40: 'G280I2|HTF7250G|G280|NewGen|1000|Learict{}'.format(aircrafttags),
                        41: 'G-450|RRTAYMK6118C|G450|NewGen|1000|Learict{}'.format(aircrafttags),
                        42: 'G-550|BR710|G550|NewGen|1000|Learict{}'.format(aircrafttags),
                        43: 'G650AB|BR700725A112|G650AB|NewGen|1000|Learict{}'.format(aircrafttags),
                        44: 'G650ERAB|BR700725A112|G650ERAB|NewGen|1000|Learict{}'.format(aircrafttags),
                        45: 'G-IVSP|MK611-8|G-IV SP|NewGen|1000|Learict{}'.format(aircrafttags),
                        46: 'G-V|BR710|G-V|NewGen|1000|Learict{}'.format(aircrafttags),
                        47: 'CITBRV|PW530A|CITBRV|NewGen|1000|Learict{}'.format(aircrafttags),
                        48: 'CITCJ3P|FJ443A|CITCJ3P|NewGen|1000|Learict{}'.format(aircrafttags),
                        49: 'CITCJ4|FJ444A|CITCJ4|NewGen|1000|Learict{}'.format(aircrafttags),
                        50: 'CITENCP|PW535B|CITENCP|NewGen|1000|Learict{}'.format(aircrafttags),
                        51: 'CITLAT|PW306D1|CITLAT|NewGen|1000|Learict{}'.format(aircrafttags),
                        52: 'CITSVN|PW306C|CITSVN|NewGen|1000|Learict{}'.format(aircrafttags),
                        53: 'CITSVNP|PW306D|CITSVNP|NewGen|1000|Learict{}'.format(aircrafttags),
                        54: 'CITX|AE3007C1|CITX C1|NewGen|1000|Learict{}'.format(aircrafttags),
                        55: 'CITXL|PW545A|CITXL|NewGen|1000|Learict{}'.format(aircrafttags),
                        56: 'CITXLS|PW545B|CITXLS|NewGen|1000|Learict{}'.format(aircrafttags),
                        57: 'CITXLSP|PW545C|CITXLSP|NewGen|1000|Learict{}'.format(aircrafttags),
                        58: 'CITXP|AE3007C2|CITXP|NewGen|1000|Learict{}'.format(aircrafttags),
                        59: 'F2000|CFE1B|DA2000|NewGen|1000|Learict{}'.format(aircrafttags),
                        60: 'F2000EXEZ|PW308C|DA2000EXEZ|NewGen|1000|Learict{}'.format(aircrafttags),
                        61: 'F2000LX|PW308C|DA2000LX|NewGen|1000|Learict{}'.format(aircrafttags),
                        62: 'F2000LXS|PW308C|DA2000LXS|NewGen|1000|Learict{}'.format(aircrafttags),
                        63: 'F2000S|PW308C|DA2000S|NewGen|1000|Learict{}'.format(aircrafttags),
                        64: 'F50EX|TFE73140|DA50EX|NewGen|1000|Learict{}'.format(aircrafttags),
                        65: 'F7X|PW307A|DA7X|NewGen|1000|Learict{}'.format(aircrafttags),
                        66: 'F8X-M1749|PW307D|DA8X|NewGen|1000|Learict{}'.format(aircrafttags),
                        67: 'F900B|TFE5BR1C|DA900B|NewGen|1000|Learict{}'.format(aircrafttags),
                        68: 'F900LX|TFE73160|DA900LX1|NewGen|1000|Learict{}'.format(aircrafttags),
                        69: 'EMB135BJF|AE3007A1P|LEG600|NewGen|1000|Learict{}'.format(aircrafttags),
                        70: 'EMB505PF|PW535E|EMB505P|NewGen|1000|Learict{}'.format(aircrafttags),
                        71: 'EMB545F|AS907-3-1E|LEG450|NewGen|1000|Learict{}'.format(aircrafttags),
                        72: 'EMB550F|AS907-3-1E|LEG500|NewGen|1000|Learict{}'.format(aircrafttags),
                        73: 'EMBREMB650F|AE3007A2|LEG650|NewGen|1000|Learict{}'.format(aircrafttags),
                        74: 'HK800XP|TFE7315BR1H|HK800XP|NewGen|1000|Learict{}'.format(aircrafttags),
                        75: 'HK850XP|TFE7315BR1H|HK850XP|NewGen|1000|Learict{}'.format(aircrafttags),
                        76: 'HK900XP|50R1H|HK900XP|NewGen|1000|Learict{}'.format(aircrafttags)
                        }
        # EASA INCLUDES extra HAWKER 4000 and FALCON 50 model. APG EASA doesn't have Citation Bravo, and CL850 FAA.
        # Since database will be based on APG, users will not have the chance to use
        # 1. Hawker 4000 2. Falcon 50 models on APG EASA
        # Users will not have the chance to choose
        # 1. Citation Bravo 2. CL850 FAA models on APG EASA, because the APG EASA doesn't have those models

        # Selecting aircraft

        try:
            WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
            driver.execute_script("document.getElementById('MainContent_ddlAircraft').style.display='inline-block';")
            element = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.ID, 'MainContent_ddlAircraft')))
            # Selecting which aircraft to choose
            Select(element).select_by_value(
                airplanedict[mychoice + airplanePlusFactor])
        except Exception as ex:
            print(ex)

        # No wet runway takeoff option
        nowetrwy = [33, 34]

        if wetrwyans.upper().startswith('Y'):
            defaultans = 'No'
            if mychoice + airplanePlusFactor in nowetrwy:
                print('Sorry, the chosen aircraft does not have wet runway performance model. Restarting APG...\n')
                driver.quit()
                continue
        else:
            if mychoice + airplanePlusFactor in nowetrwy:
                print('Chosen aircraft only has dry performance model. Default options are auto-chosen.\n')
                defaultans = 'Y'
            else:
                defaultans = input(
                    'Implement default options? (Only takeoff data on dry runways)\tY for yes, otherwise for no\n')

        # For ONLY wet runways...
        # For WET RWY (TO)
        onlywetrwy1 = [1, 2, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58, 10, 11, 12, 13, 25, 26, 27, 28, 29, 30, 31, 32,
                       35, 36, 37, 38, 39, 40, 46, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 74, 75, 76]
        # For WET RUNWAY (TO)
        onlywetrwy2 = [16, 17, 18, 19, 21, 22, 23, 24]
        # For Wet (TO)
        onlywetrwy3 = [69, 71, 72, 73]
        # For WET RWY (RCAM - 5) (TO)
        onlywetrwy4 = [41, 42, 43, 44]
        # For WET RWY (D) (TO)
        onlywetrwy5 = [45]

        # For wet runways...
        # For WET RWY (TO)
        wetrwy1 = [3, 51]
        # For WET RUNWAY (TO)
        wetrwy2 = [4, 5, 6, 7, 8, 9, 14, 15]
        # For WET RWY - SMOOTH SURFACE (TO)
        wetrwy3 = [20]
        # For Wet (TO)
        wetrwy4 = [70]

        # ONLY doing wet non-grooved airfields
        if defaultans.upper().startswith('Y'):
            # Skipping over everything wet runway related!
            pass
        else:
            if secondtime:
                # If multiple aircraft are passed, wet option is same for the multiple aircraft.
                # i.e., if your first aircraft analysis is non-wet, all following aircraft will be non-wet. vice-versa for wet.
                if wetrwyans.upper().startswith('Y'):
                    if mychoice + airplanePlusFactor in onlywetrwy1 or mychoice + airplanePlusFactor in wetrwy1:
                        try:
                            WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
                            driver.execute_script(
                                "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                            element = WebDriverWait(driver, 60).until(
                                EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                            Select(element).select_by_visible_text('WET RWY (TO)')
                        except Exception as ex:
                            print(ex)
                    elif mychoice + airplanePlusFactor in onlywetrwy2 or mychoice + airplanePlusFactor in wetrwy2:
                        try:
                            WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
                            driver.execute_script(
                                "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                            element = WebDriverWait(driver, 60).until(
                                EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                            Select(element).select_by_visible_text('WET RUNWAY (TO)')
                        except Exception as ex:
                            print(ex)
                    elif mychoice + airplanePlusFactor in wetrwy3:
                        try:
                            WebDriverWait(driver, 60).until(
                                EC.visibility_of_element_located((By.ID, 'btnCompute')))
                            driver.execute_script(
                                "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                            element = WebDriverWait(driver, 60).until(
                                EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                            Select(element).select_by_visible_text('WET RWY - SMOOTH SURFACE (TO)')
                        except Exception as ex:
                            print(ex)
                    elif mychoice + airplanePlusFactor in onlywetrwy3 or mychoice + airplanePlusFactor in wetrwy4:
                        try:
                            WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
                            driver.execute_script(
                                "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                            element = WebDriverWait(driver, 60).until(
                                EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                            Select(element).select_by_visible_text('Wet (TO)')
                        except Exception as ex:
                            print(ex)
                    elif mychoice + airplanePlusFactor in onlywetrwy4:
                        try:
                            WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
                            driver.execute_script(
                                "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                            element = WebDriverWait(driver, 60).until(
                                EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                            Select(element).select_by_visible_text('WET RWY (RCAM - 5) (TO)')
                        except Exception as ex:
                            print(ex)
                    elif mychoice + airplanePlusFactor in onlywetrwy5:
                        try:
                            WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
                            driver.execute_script(
                                "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                            element = WebDriverWait(driver, 60).until(
                                EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                            Select(element).select_by_visible_text('WET RWY (D) (TO)')
                        except Exception as ex:
                            print(ex)
                    else:
                        pass
                # If no runway contaminant, just continue!
                else:
                    pass
            else:
                # Selecting contaminants
                wetrwyans = input("Include wet runway as a contaminant? Y for yes, otherwise for no\n")
                if wetrwyans.upper().startswith('Y'):
                    if mychoice + airplanePlusFactor in onlywetrwy1 or mychoice + airplanePlusFactor in wetrwy1:
                        try:
                            WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
                            driver.execute_script(
                                "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                            element = WebDriverWait(driver, 60).until(
                                EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                            Select(element).select_by_visible_text('WET RWY (TO)')
                        except Exception as ex:
                            print(ex)
                    elif mychoice + airplanePlusFactor in onlywetrwy2 or mychoice + airplanePlusFactor in wetrwy2:
                        try:
                            WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
                            driver.execute_script(
                                "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                            element = WebDriverWait(driver, 60).until(
                                EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                            Select(element).select_by_visible_text('WET RUNWAY (TO)')
                        except Exception as ex:
                            print(ex)
                    elif mychoice + airplanePlusFactor in wetrwy3:
                        try:
                            WebDriverWait(driver, 60).until(
                                EC.visibility_of_element_located((By.ID, 'btnCompute')))
                            driver.execute_script(
                                "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                            element = WebDriverWait(driver, 60).until(
                                EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                            Select(element).select_by_visible_text('WET RWY - SMOOTH SURFACE (TO)')
                        except Exception as ex:
                            print(ex)
                    elif mychoice + airplanePlusFactor in onlywetrwy3 or mychoice + airplanePlusFactor in wetrwy4:
                        try:
                            WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
                            driver.execute_script(
                                "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                            element = WebDriverWait(driver, 60).until(
                                EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                            Select(element).select_by_visible_text('Wet (TO)')
                        except Exception as ex:
                            print(ex)
                    elif mychoice + airplanePlusFactor in onlywetrwy4:
                        try:
                            WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
                            driver.execute_script(
                                "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                            element = WebDriverWait(driver, 60).until(
                                EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                            Select(element).select_by_visible_text('WET RWY (RCAM - 5) (TO)')
                        except Exception as ex:
                            print(ex)
                    elif mychoice + airplanePlusFactor in onlywetrwy5:
                        try:
                            WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'btnCompute')))
                            driver.execute_script(
                                "document.getElementById('MainContent_msdContaminants').style.display='inline-block';")
                            element = WebDriverWait(driver, 60).until(
                                EC.visibility_of_element_located((By.ID, 'MainContent_msdContaminants')))
                            Select(element).select_by_visible_text('WET RWY (D) (TO)')
                        except Exception as ex:
                            print(ex)
                    else:
                        pass
                    # If no runway contaminant, just continue!
                else:
                    pass

        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID, 'MainContent_osTOOptionSelector_OptionButton')))
        TO_Options_button = driver.find_element_by_id('MainContent_osTOOptionSelector_OptionButton')
        TO_Options_button.click()

        # Switching off ECS ON and APU ON and Rolling takeoff and APR OFF and Bleeds OPEN
        # For G150, APR OFF is NOT pressed! In fact, nothing needs to be pressed
        time.sleep(3)
        listofoptions = ["ECS ON", "APU ON", "ROLLING TAKEOFF", "ROLLING TO", "Rolling T/O", "ROLLING T/O", "APR OFF",
                         "BLEEDS OPEN",
                         "BLD OPEN", "BLD OPEN A/I OFF", "BLEEDS ON", "WITH THRUST REVERSERS", "WITH REVERSE THRUST"]
        for options in listofoptions:
            try:
                if mychoice + airplanePlusFactor == 38:  # For the G150, nothing needs to be done. If proceeded, APR OFF will be pressed, which is not desirable
                    break
                # WebDriverWait(driver,0.1).until(EC.visibility_of_element_located((By.XPATH,f'//*[@title="{options}"]')))
                button = driver.find_element_by_xpath(f'//*[@title="{options}"]')
                button.click()
            except:
                pass

        # Switching on ECS OFF and APU OFF and Static takeoff and APR ON and BLEEDS CLOSED
        done_button = driver.find_element_by_id('MainContent_osTOOptionSelector_OptionMultiSelect_done')
        listofoptions = ["APU OFF", "BLEEDS OFF", "BLEEDS CLOSED", "BLD CLSD", "STATIC TO", "STATIC TAKEOFF",
                         "Static T/O", "STATIC T/O",
                         "ECS OFF", "APR ON", "APR ARMED", "WITHOUT THRUST REVERSERS", "WITHOUT REVERSE THRUST"]
        counter = 4
        for options in listofoptions:
            try:
                # WebDriverWait(driver, 0.1).until(
                # EC.visibility_of_element_located((By.XPATH, '//*[@title="' + options + '"]')))
                checked = driver.find_element_by_xpath('//*[@title="' + options + '"]').is_selected()
                if checked == True:
                    done_button.click()
                    try:
                        driver.find_element_by_id('ui-dialog-title-option-dialog-error')
                        WebDriverWait(driver, 0.1).until(
                            EC.visibility_of_element_located(
                                (By.XPATH, '/ html / body / div[' + str(counter) + '] / div[11] / div / button')))
                        # ONLY ABSOLUTE XPATH
                        ok_button = driver.find_element_by_xpath(
                            '/ html / body / div[' + str(counter) + '] / div[11] / div / button')
                        ok_button.click()
                        counter += 1
                    except:
                        pass
                else:
                    # WebDriverWait(driver, 0.1).until(
                    # EC.visibility_of_element_located(
                    # (By.XPATH,'//*[@title="' + options + '"]')))
                    driver.find_element_by_xpath('//*[@title="' + options + '"]').click()
                    done_button.click()
                    try:
                        driver.find_element_by_id('ui-dialog-title-option-dialog-error')
                        WebDriverWait(driver, 0.1).until(
                            EC.visibility_of_element_located(
                                (By.XPATH, '/ html / body / div[' + str(counter) + '] / div[11] / div / button')))
                        # ONLY ABSOLUTE XPATH
                        ok_button = driver.find_element_by_xpath(
                            '/ html / body / div[' + str(counter) + '] / div[11] / div / button')
                        ok_button.click()
                        counter += 1
                    except:
                        pass
            except:
                continue

        # In case that the ok done button in takeoff options is still up, select it and make takeoff options disappear so that ICAO codes can be entered
        try:
            WebDriverWait(driver, 1).until(
                EC.visibility_of_element_located((By.ID, 'MainContent_osTOOptionSelector_OptionMultiSelect_done')))
            driver.find_element_by_id('MainContent_osTOOptionSelector_OptionMultiSelect_done').click()
        except:
            pass

        # if it DOESN'T start with y, or yes, concatenate and proceed as normal. else, split and tackle each one
        if not wetrwyans.upper().startswith('Y'):

            newicaocodelist = []
            removedposlist = []
            for i in range(len(icaocodelist)):

                WebDriverWait(driver, 3).until(
                    EC.visibility_of_element_located((By.ID, 'MainContent_txtICAO')))
                icao_code_box = driver.find_element_by_id('MainContent_txtICAO')
                icao_code_box.click()
                icao_code_box.send_keys(icaocodelist[i])

                if defaultans.upper().startswith('Y'):
                    to_button = driver.find_element_by_id('btnAddTOICAO')
                    to_button.click()
                    # Click ok button if ICAO code does not exist on APG
                    try:
                        time.sleep(1)
                        driver.find_element_by_id('ui-dialog-title-dialog-error')
                        try:
                            driver.find_element_by_xpath("/ html / body / div[3] / div[11] / div / button").click()
                            print(f"'{icaocodelist[i]}' ICAO code does not exist on APG.\n")
                            removedposlist.append(i)
                        except:
                            try:
                                driver.find_element_by_xpath("/ html / body / div[4] / div[11] / div / button").click()
                                print(f"'{icaocodelist[i]}' ICAO code does not exist on APG.\n")
                                removedposlist.append(i)
                            except:
                                try:
                                    driver.find_element_by_xpath(
                                        "/ html / body / div[5] / div[11] / div / button").click()
                                    print(f"'{icaocodelist[i]}' ICAO code does not exist on APG.\n")
                                    removedposlist.append(i)
                                except:
                                    try:
                                        driver.find_element_by_xpath(
                                            "/ html / body / div[6] / div[11] / div / button").click()

                                        print(f"'{icaocodelist[i]}' ICAO code does not exist on APG.\n")
                                        removedposlist.append(i)
                                    except:
                                        newicaocodelist.append(icaocodelist[i])
                    except:
                        newicaocodelist.append(icaocodelist[i])
                        pass

                else:
                    to_ans = input(
                        f'Do you want to add takeoff, or both takeoff and landing for {icaocodelist[i]}? T for only takeoff, otherwise for both\n')
                    to_button = driver.find_element_by_id('btnAddTOICAO')
                    both_button = driver.find_element_by_id('btnAddBothICAO')
                    if to_ans.upper().startswith('T'):
                        to_button.click()
                        try:
                            time.sleep(1)
                            driver.find_element_by_id('ui-dialog-title-dialog-error')
                            try:
                                driver.find_element_by_xpath("/ html / body / div[3] / div[11] / div / button").click()
                                print(f"'{icaocodelist[i]}' ICAO code does not exist on APG.\n")
                                removedposlist.append(i)
                            except:
                                try:
                                    driver.find_element_by_xpath(
                                        "/ html / body / div[4] / div[11] / div / button").click()
                                    print(f"'{icaocodelist[i]}' ICAO code does not exist on APG.\n")
                                    removedposlist.append(i)
                                except:
                                    try:
                                        driver.find_element_by_xpath(
                                            "/ html / body / div[5] / div[11] / div / button").click()
                                        print(f"'{icaocodelist[i]}' ICAO code does not exist on APG.\n")
                                        removedposlist.append(i)
                                    except:
                                        try:
                                            driver.find_element_by_xpath(
                                                "/ html / body / div[6] / div[11] / div / button").click()
                                            print(f"'{icaocodelist[i]}' ICAO code does not exist on APG.\n")
                                            removedposlist.append(i)
                                        except:
                                            newicaocodelist.append(icaocodelist[i])
                        except:
                            newicaocodelist.append(icaocodelist[i])
                            pass
                    else:
                        both_button.click()
                        try:
                            time.sleep(1)
                            driver.find_element_by_id('ui-dialog-title-dialog-error')
                            try:
                                driver.find_element_by_xpath("/ html / body / div[3] / div[11] / div / button").click()
                                print(f"'{icaocodelist[i]}' ICAO code does not exist on APG.\n")
                                removedposlist.append(i)
                            except:
                                try:
                                    driver.find_element_by_xpath(
                                        "/ html / body / div[4] / div[11] / div / button").click()
                                    print(f"'{icaocodelist[i]}' ICAO code does not exist on APG.\n")
                                    removedposlist.append(i)
                                except:
                                    try:
                                        driver.find_element_by_xpath(
                                            "/ html / body / div[5] / div[11] / div / button").click()
                                        print(f"'{icaocodelist[i]}' ICAO code does not exist on APG.\n")
                                        removedposlist.append(i)
                                    except:
                                        try:
                                            driver.find_element_by_xpath(
                                                "/ html / body / div[6] / div[11] / div / button").click()
                                            print(f"'{icaocodelist[i]}' ICAO code does not exist on APG.\n")
                                            removedposlist.append(i)
                                        except:
                                            newicaocodelist.append(icaocodelist[i])
                        except:
                            newicaocodelist.append(icaocodelist[i])
                            pass

            if len(newicaocodelist) == 0:
                print('APG could not process any of the ICAO codes.\nExiting APG.')
                return 0

            # Even though below list is named isa15c_list, temperatures MAY not be that. This is simply the defult choice computed by Part 1
            temperatureslist = temperatures.tolist()
            isa15c_list = [round(num) for num in temperatureslist]

            # Below code executes if some APG ICAO codes were not processed
            if len(newicaocodelist) != len(icaocodelist):
                for ele in sorted(removedposlist, reverse=True):
                    del isa15c_list[ele]

            # Redefining icao code list to a list accepted by APG
            icaocodelist = newicaocodelist

            time.sleep(2)

            # isa15c_list = [23, 30]
            for i in range(len(icaocodelist)):
                temp_box = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="jqg' + str(i + 1) + '"]/td[10]')))
                temp_box.click()
                temp_box.send_keys(isa15c_list[i])
                driver.execute_script("arguments[0].innerText='{}'".format(str(isa15c_list[i])), temp_box)

            # make sure use temp checkbox is ticked
            for i in range(len(icaocodelist)):
                check_box = driver.find_element_by_xpath('//*[@id="jqg' + str(i + 1) + '"]/td[9]/input')
                checked = check_box.is_selected()
                if checked:
                    pass
                else:
                    check_box.click()

            # SUBMIT!
            driver.find_element_by_id('btnCompute').click()
            # Max 3 seconds of wait
            found = False
            try_count = 0
            while (not found) and try_count <= 1:
                try_count += 1
                try:
                    WebDriverWait(driver, 3).until(
                        EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[11]/div/button'))).click()
                    found = True
                except:
                    try:
                        WebDriverWait(driver, 3).until(
                            EC.presence_of_element_located(
                                (By.XPATH, '/html/body/div[5]/div[11]/div/button'))).click()
                        found = True
                    except:
                        try:
                            WebDriverWait(driver, 3).until(
                                EC.presence_of_element_located(
                                    (By.XPATH, '/html/body/div[6]/div[11]/div/button'))).click()
                            found = True
                        except:
                            try:
                                WebDriverWait(driver, 3).until(
                                    EC.presence_of_element_located(
                                        (By.XPATH, '/html/body/div[7]/div[11]/div/button'))).click()
                                found = True
                            except:
                                print('None of the Xpaths for OK button worked. Trying again...\n')

            # Go to next page
            driver.find_element_by_xpath('//*[@id="tabs"]/ul/li[2]').click()

            # Click checkmark and then view jobs button. If not there, wait for 5 seconds and reload page
            try:
                time.sleep(2)
                checkmark = driver.find_element_by_xpath(
                    '/html/body/form/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/div[3]/div[3]/div/table/tbody/tr[2]/td[1]/input')
                checkmark.click()

            except:
                # wait 5 seconds and then refresh page. If doesn't load up by then, try waiting another 5 seconds and refresh again. Repeat.
                while True:
                    try:
                        time.sleep(5)
                        driver.refresh()
                        time.sleep(2)
                        checkmark = driver.find_element_by_xpath(
                            '/html/body/form/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/div[3]/div[3]/div/table/tbody/tr[2]/td[1]/input')
                        checkmark.click()
                        break
                    except:
                        continue

            # Get id,date, and aircraft name from APG
            idnumber = checkmark.get_attribute("id")
            idnumber = idnumber[9:]

            startdate_el = driver.find_element_by_xpath('//*[@id="{}"]/td[4]'.format(idnumber))
            date = startdate_el.text
            date = date[:10]

            s = airplanedict[mychoice + airplanePlusFactor]
            char = '|'
            pipeposlist = [pos for pos, c in enumerate(s) if char == c]
            # Getting only 2nd and 3rd occurrence to serve as start and end
            impposlist = pipeposlist[1:3]
            aircraftname = airplanedict[mychoice + airplanePlusFactor][impposlist[0] + 1:impposlist[1]]
            # Download pdf
            driver.find_element_by_id('btnViewJobs').click()

            # Close all windows
            time.sleep(10)
            driver.quit()

            print("\n--- %s seconds for browsing ---\n" % (time.time() - start_time))

            treatWatermark(idnumber, date, aircraftname)

            if defaultans.upper().startswith('Y'):
                wetrwyans = 'N'
            else:
                wetrwyans = wetrwyans.upper()

            (uniquecodes, maximumlist, aircraftnamelist) = turnpdftodata(idnumber, icaocodelist,
                                                                         wetrwyans,
                                                                         mydict[mychoice], maximumlist,
                                                                         aircraftnamelist)

            diffaircraftans = input(
                'Would you like to repeat same airfields with different aircraft? Y for yes, otherwise for no\n')

            if diffaircraftans.upper().startswith('Y'):
                # looping back around
                secondtime = True
                continue
            break

        else:
            if len(nongrooveicaocodelist) == 0:
                driver.quit()
                # there are no non-grooved airfields. Directly process grooved airfields
                (idnumber, date, aircraftname, grooveicaocodelist) = groovedairfield(myusername, mypassword,
                                                                                     airplanedict, mychoice,
                                                                                     airplanePlusFactor,
                                                                                     grooveicaocodelist, defaultans,
                                                                                     nongrooveicaocodelist,
                                                                                     tempgroovelist)
                if (idnumber, date, aircraftname, grooveicaocodelist) == (0, 0, 0, 0):
                    print("\n--- %s seconds for browsing ---\n" % (time.time() - start_time))
                    return 0
                elif (idnumber, date, aircraftname, grooveicaocodelist) == (1, 1, 1, 1):
                    print('Should not be possible here')
                else:
                    print('Grooved airfields processed.\n')

                    print("\n--- %s seconds for browsing ---\n" % (time.time() - start_time))

                    treatWatermark(idnumber, date, aircraftname)

                    if defaultans.upper().startswith('Y'):
                        wetrwyans = 'N'
                    else:
                        wetrwyans = wetrwyans.upper()

                    (uniquecodes, maximumlist, aircraftnamelist) = turnpdftodata(idnumber, grooveicaocodelist,
                                                                                 wetrwyans,
                                                                                 mydict[mychoice], maximumlist,
                                                                                 aircraftnamelist)

                    diffaircraftans = input(
                        'Would you like to repeat same airfields with different aircraft? Y for yes, otherwise for no\n')

                    if diffaircraftans.upper().startswith('Y'):
                        # looping back around
                        secondtime = True
                        continue
                    break

            else:
                newnongrooveicaocodelist = []
                removedposlist = []
                for i in range(len(nongrooveicaocodelist)):

                    WebDriverWait(driver, 3).until(
                        EC.visibility_of_element_located((By.ID, 'MainContent_txtICAO')))
                    icao_code_box = driver.find_element_by_id('MainContent_txtICAO')
                    icao_code_box.click()
                    icao_code_box.send_keys(nongrooveicaocodelist[i])

                    if defaultans.upper().startswith('Y'):
                        to_button = driver.find_element_by_id('btnAddTOICAO')
                        to_button.click()
                        # Click ok button if ICAO code does not exist on APG
                        try:
                            time.sleep(1)
                            driver.find_element_by_id('ui-dialog-title-dialog-error')
                            try:
                                driver.find_element_by_xpath("/ html / body / div[3] / div[11] / div / button").click()
                                print(f"'{nongrooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                                removedposlist.append(i)
                            except:
                                try:
                                    driver.find_element_by_xpath(
                                        "/ html / body / div[4] / div[11] / div / button").click()
                                    print(f"'{nongrooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                                    removedposlist.append(i)
                                except:
                                    try:
                                        driver.find_element_by_xpath(
                                            "/ html / body / div[5] / div[11] / div / button").click()
                                        print(f"'{nongrooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                                        removedposlist.append(i)
                                    except:
                                        try:
                                            driver.find_element_by_xpath(
                                                "/ html / body / div[6] / div[11] / div / button").click()

                                            print(f"'{nongrooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                                            removedposlist.append(i)
                                        except:
                                            newnongrooveicaocodelist.append(nongrooveicaocodelist[i])
                        except:
                            newnongrooveicaocodelist.append(nongrooveicaocodelist[i])
                            pass

                    else:
                        to_ans = input(
                            f'Do you want to add takeoff, or both takeoff and landing for {nongrooveicaocodelist[i]}? T for only takeoff, otherwise for both\n')
                        to_button = driver.find_element_by_id('btnAddTOICAO')
                        both_button = driver.find_element_by_id('btnAddBothICAO')
                        if to_ans.upper().startswith('T'):
                            to_button.click()
                            try:
                                time.sleep(1)
                                driver.find_element_by_id('ui-dialog-title-dialog-error')
                                try:
                                    driver.find_element_by_xpath(
                                        "/ html / body / div[3] / div[11] / div / button").click()
                                    print(f"'{nongrooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                                    removedposlist.append(i)
                                except:
                                    try:
                                        driver.find_element_by_xpath(
                                            "/ html / body / div[4] / div[11] / div / button").click()
                                        print(f"'{nongrooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                                        removedposlist.append(i)
                                    except:
                                        try:
                                            driver.find_element_by_xpath(
                                                "/ html / body / div[5] / div[11] / div / button").click()
                                            print(f"'{nongrooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                                            removedposlist.append(i)
                                        except:
                                            try:
                                                driver.find_element_by_xpath(
                                                    "/ html / body / div[6] / div[11] / div / button").click()
                                                print(
                                                    f"'{nongrooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                                                removedposlist.append(i)
                                            except:
                                                newnongrooveicaocodelist.append(nongrooveicaocodelist[i])
                            except:
                                newnongrooveicaocodelist.append(nongrooveicaocodelist[i])
                                pass
                        else:
                            both_button.click()
                            try:
                                time.sleep(1)
                                driver.find_element_by_id('ui-dialog-title-dialog-error')
                                try:
                                    driver.find_element_by_xpath(
                                        "/ html / body / div[3] / div[11] / div / button").click()
                                    print(f"'{nongrooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                                    removedposlist.append(i)
                                except:
                                    try:
                                        driver.find_element_by_xpath(
                                            "/ html / body / div[4] / div[11] / div / button").click()
                                        print(f"'{nongrooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                                        removedposlist.append(i)
                                    except:
                                        try:
                                            driver.find_element_by_xpath(
                                                "/ html / body / div[5] / div[11] / div / button").click()
                                            print(f"'{nongrooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                                            removedposlist.append(i)
                                        except:
                                            try:
                                                driver.find_element_by_xpath(
                                                    "/ html / body / div[6] / div[11] / div / button").click()
                                                print(
                                                    f"'{nongrooveicaocodelist[i]}' ICAO code does not exist on APG.\n")
                                                removedposlist.append(i)
                                            except:
                                                newnongrooveicaocodelist.append(nongrooveicaocodelist[i])
                            except:
                                newnongrooveicaocodelist.append(nongrooveicaocodelist[i])
                                pass

                if len(newnongrooveicaocodelist) == 0:
                    # Redefining icao code list to a list accepted by APG
                    nongrooveicaocodelist = newnongrooveicaocodelist
                    driver.quit()
                    print(
                        'APG could not process any of the ICAO codes for non-grooved airfields.\nChecking grooved airfields...\n')
                    # Call everything groove related
                    (idnumber, date, aircraftname, grooveicaocodelist) = groovedairfield(myusername, mypassword,
                                                                                         airplanedict, mychoice,
                                                                                         airplanePlusFactor,
                                                                                         grooveicaocodelist, defaultans,
                                                                                         nongrooveicaocodelist,
                                                                                         tempgroovelist)
                    if (idnumber, date, aircraftname, grooveicaocodelist) == (0, 0, 0, 0):
                        print("\n--- %s seconds for browsing ---\n" % (time.time() - start_time))
                        return 0
                    elif (idnumber, date, aircraftname, grooveicaocodelist) == (1, 1, 1, 1):
                        print('Should not be possible here')
                    else:
                        print('Grooved airfields processed.\n')

                        print("\n--- %s seconds for browsing ---\n" % (time.time() - start_time))

                        treatWatermark(idnumber, date, aircraftname)

                        if defaultans.upper().startswith('Y'):
                            wetrwyans = 'N'
                        else:
                            wetrwyans = wetrwyans.upper()

                        (uniquecodes, maximumlist, aircraftnamelist) = turnpdftodata(idnumber, grooveicaocodelist,
                                                                                     wetrwyans,
                                                                                     mydict[mychoice], maximumlist,
                                                                                     aircraftnamelist)

                        diffaircraftans = input(
                            'Would you like to repeat same airfields with different aircraft? Y for yes, otherwise for no\n')

                        if diffaircraftans.upper().startswith('Y'):
                            # looping back around
                            secondtime = True
                            continue
                        break

                else:
                    # Even though below list is named isa15c_list, temperatures MAY not be that. This is simply the defult choice computed by Part 1
                    isa15c_list = [round(num) for num in tempnongroovelist]

                    # Below code executes if some APG ICAO codes were not processed
                    if len(newnongrooveicaocodelist) != len(nongrooveicaocodelist):
                        for ele in sorted(removedposlist, reverse=True):
                            del isa15c_list[ele]

                    # Redefining icao code list to a list accepted by APG
                    nongrooveicaocodelist = newnongrooveicaocodelist

                    time.sleep(2)

                    # isa15c_list = [23, 30]
                    for i in range(len(nongrooveicaocodelist)):
                        temp_box = WebDriverWait(driver, 2).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="jqg' + str(i + 1) + '"]/td[10]')))
                        temp_box.click()
                        temp_box.send_keys(isa15c_list[i])
                        driver.execute_script("arguments[0].innerText='{}'".format(str(isa15c_list[i])), temp_box)

                    # make sure use temp checkbox is ticked
                    for i in range(len(nongrooveicaocodelist)):
                        check_box = driver.find_element_by_xpath('//*[@id="jqg' + str(i + 1) + '"]/td[9]/input')
                        checked = check_box.is_selected()
                        if checked:
                            pass
                        else:
                            check_box.click()

                    # SUBMIT!
                    driver.find_element_by_id('btnCompute').click()
                    # Max 3 seconds of wait

                    found = False
                    try_count = 0

                    while not found and try_count <= 1:
                        try_count += 1
                        try:
                            WebDriverWait(driver, 3).until(
                                EC.presence_of_element_located(
                                    (By.XPATH, '/html/body/div[4]/div[11]/div/button'))).click()
                            found = True
                        except:
                            try:
                                WebDriverWait(driver, 3).until(
                                    EC.presence_of_element_located(
                                        (By.XPATH, '/html/body/div[5]/div[11]/div/button'))).click()
                                found = True
                            except:
                                try:
                                    WebDriverWait(driver, 3).until(
                                        EC.presence_of_element_located(
                                            (By.XPATH, '/html/body/div[6]/div[11]/div/button'))).click()
                                    found = True
                                except:
                                    try:
                                        WebDriverWait(driver, 3).until(
                                            EC.presence_of_element_located(
                                                (By.XPATH, '/html/body/div[7]/div[11]/div/button'))).click()
                                        found = True
                                    except:
                                        print('None of the Xpaths for OK button worked. Trying again...\n')

                    # Go to next page
                    driver.find_element_by_xpath('//*[@id="tabs"]/ul/li[2]').click()

                    # Click checkmark and then view jobs button. If not there, wait for 5 seconds and reload page
                    try:
                        time.sleep(2)
                        checkmark = driver.find_element_by_xpath(
                            '/html/body/form/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/div[3]/div[3]/div/table/tbody/tr[2]/td[1]/input')
                        checkmark.click()
                        idnumber = checkmark.get_attribute("id")

                    except:
                        # wait 5 seconds and then refresh page. If doesn't load up by then, try waiting another 5 seconds and refresh again. Repeat.
                        while True:
                            try:
                                time.sleep(5)
                                driver.refresh()
                                time.sleep(2)
                                checkmark = driver.find_element_by_xpath(
                                    '/html/body/form/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/div[3]/div[3]/div/table/tbody/tr[2]/td[1]/input')
                                checkmark.click()
                                break
                            except:
                                continue

                    # Get id,date, and aircraft name from APG
                    idnumber = checkmark.get_attribute("id")
                    idnumber = idnumber[9:]

                    startdate_el = driver.find_element_by_xpath('//*[@id="{}"]/td[4]'.format(idnumber))
                    date = startdate_el.text
                    date = date[:10]

                    s = airplanedict[mychoice + airplanePlusFactor]
                    char = '|'
                    pipeposlist = [pos for pos, c in enumerate(s) if char == c]
                    # Getting only 2nd and 3rd occurrence to serve as start and end
                    impposlist = pipeposlist[1:3]
                    aircraftname = airplanedict[mychoice + airplanePlusFactor][impposlist[0] + 1:impposlist[1]]
                    # Download pdf
                    driver.find_element_by_id('btnViewJobs').click()

                    # Close all windows
                    time.sleep(10)
                    driver.quit()

                    print("\n--- %s seconds for browsing ---\n" % (time.time() - start_time))

                    treatWatermark(idnumber, date, aircraftname)

                    if defaultans.upper().startswith('Y'):
                        wetrwyans = 'N'
                    else:
                        wetrwyans = wetrwyans.upper()

                    (uniquecodes, maximumlist, aircraftnamelist) = turnpdftodata(idnumber, nongrooveicaocodelist,
                                                                                 wetrwyans,
                                                                                 mydict[mychoice], maximumlist,
                                                                                 aircraftnamelist)

                    if len(grooveicaocodelist) == 0:
                        #Pretty much done. Only non-groove airfields. Prompt to continue aircraft?
                        diffaircraftans = input(
                            'Would you like to repeat same airfields with different aircraft? Y for yes, otherwise for no\n')

                        if diffaircraftans.upper().startswith('Y'):
                            # looping back around
                            secondtime = True
                            continue
                        break

                    else:
                        start_time1 = time.time()
                        (idnumber, date, aircraftname, grooveicaocodelist) = groovedairfield(myusername, mypassword,
                                                                                             airplanedict, mychoice,
                                                                                             airplanePlusFactor,
                                                                                             grooveicaocodelist, defaultans,
                                                                                             nongrooveicaocodelist,
                                                                                             tempgroovelist)
                        if (idnumber, date, aircraftname, grooveicaocodelist) == (0, 0, 0, 0):
                            print('Should not be possible to reach here')
                        elif (idnumber, date, aircraftname, grooveicaocodelist) == (1, 1, 1, 1):
                            print("\n--- %s seconds for browsing ---\n" % (time.time() - start_time1))
                            diffaircraftans = input(
                                'Would you like to repeat same airfields with different aircraft? Y for yes, otherwise for no\n')

                            if diffaircraftans.upper().startswith('Y'):
                                # looping back around
                                secondtime = True
                                continue
                            break
                        else:
                            print("\n--- %s seconds for browsing ---\n" % (time.time() - start_time1))

                            treatWatermark(idnumber, date, aircraftname)

                            if defaultans.upper().startswith('Y'):
                                wetrwyans = 'N'
                            else:
                                wetrwyans = wetrwyans.upper()

                            (uniquecodes1, maximumlist, aircraftnamelist1) = turnpdftodata(idnumber, grooveicaocodelist,
                                                                                           wetrwyans,
                                                                                           mydict[mychoice], maximumlist,
                                                                                           aircraftnamelist)
                            # uniquecodes would need to append now!
                            # and maximum list would be need to also append to 1-d (not 2-d)
                            # but aircraft name list would be the same

                            uniquecodes.extend(uniquecodes1)

                            maximumlist1 = maximumlist[-2:]
                            del maximumlist[-2:]
                            flattenlist = sum(maximumlist1, [])
                            maximumlist.extend(flattenlist)

                            newlist = maximumlist[aircraftcount:]
                            del maximumlist[aircraftcount:]
                            maximumlist.append(newlist)

                            aircraftnamelist = list(dict.fromkeys(aircraftnamelist))

                            diffaircraftans = input(
                                'Would you like to repeat same airfields with different aircraft? Y for yes, otherwise for no\n')

                            if diffaircraftans.upper().startswith('Y'):
                                # looping back around

                                secondtime = True
                                aircraftcount += 1
                                continue
                            break

    turndatatoexcel(uniquecodes, maximumlist, aircraftnamelist)
    print('\nPart 2 Source file ready!\n')
