import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pyautogui



def animation(driver):
    wait = WebDriverWait(driver, 100)
    elements = wait.until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, ".animation_blink")
    ))
    try:
        element = driver.find_element(By.XPATH, "//span[@id='SPADE-4']")
        resulttext = element.get_attribute("innerHTML")
        return resulttext
    except:
        try:
            element = driver.find_element(By.XPATH, "//span[@id='DIAMOND-4']")
            resulttext = element.get_attribute("innerHTML")
            return resulttext

        except:
            try:
                element = driver.find_element(By.XPATH, "//span[@id='CLUB-4']")
                resulttext = element.get_attribute("innerHTML")
                return resulttext

            except:
                try:
                    element = driver.find_element(By.XPATH, "//span[@id='HEART-4']")
                    resulttext = element.get_attribute("innerHTML")
                    return resulttext

                except:
                    result_0 = "No matching element found"
                    return result_0


def result(driver):
    result = animation(driver)
    result_array = result.split(" ")
    result_Suit = result_array[1]
    print(f'Result is {result_Suit}')
    return result_Suit




def GameCard(driver):
    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, "//span[@id='GameCard']")))
    span_element = driver.find_element(By.XPATH, "//span[@id='GameCard']")
    resulttext = span_element.get_attribute("innerHTML")
    # TO CONVERT STRING TO ARRAY
    result_array = resulttext.split(" ")
    Player_result_Suit = result_array[0]
    Player_result_Number = result_array[1]
    print("GameCard = " + Player_result_Number)
    return Player_result_Number
#AndarCards-0

def SPADE_CARD(driver):
    card_numbers = []

    for i in range(0,4):
        WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.XPATH, "//span[@id='SPADE-0']")))
        xpath = f"//span[@id='SPADE-{i}']"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        span_element = driver.find_element(By.XPATH, xpath)
        resulttext = span_element.get_attribute("innerHTML")

        result_array = resulttext.split(" ")
        Player_result_Number = result_array[1]
        card_numbers.append(Player_result_Number)

    return card_numbers


def totalcard(driver):
    wait = WebDriverWait(driver, 100)
    elements = wait.until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, ".animation_blink")
    ))
    totalcard = driver.find_element(By.XPATH, "(//span[contains(.,'Total Card ')])").text
    totalcard = totalcard.split()
    totalcard = totalcard[3]
    print(f'Total Card = {totalcard}')
    return totalcard


def totalPoint(driver):
    wait = WebDriverWait(driver, 100)
    elements = wait.until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, ".animation_blink")
    ))
    totalcard = driver.find_element(By.XPATH, "(//span[contains(.,'Total Point ')])").text
    totalcard = totalcard.split()
    totalcard = totalcard[3]
    print(f'Total Point = {totalcard}')
    return totalcard


#(//span[@class='total_text ng-tns-c103-11'])[1]



#spade Lay
# (//span[contains(text(),"Match Odds")])[2]/following::div[4]/following::div[2] = Spade Lay
#(//span[contains(text(),'4.15')])[1]

#Heart
# (//span[contains(text(),"Match Odds")])[2]/following::div[12] = Heart back
#(//span[contains(text(),'3.85')])[2]
#(//span[contains(text(),'4.15')])[2]
#

#Club
# (//span[contains(text(),'K')])[3]/following::div[1]/following::div[3] = club black
#(//span[contains(text(),'3.85')])[3]
# (//span[contains(text(),'K')])[3]/following::div[1]/following::div[5]
#


#Dimond
#(//span[contains(text(),'3.85')])[4]
#(//span[contains(text(),'4.15')])[4]
#
#
#
#
#
