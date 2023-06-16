import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pyautogui
from Functions.BetPlacing import Spade_bet
from Functions.Payoff import payoff_SpadeBack
from Functions.BetStake import BetStake
from Functions.Result import SPADE_CARD, animation, result




def getBalance(driver):
    #WebDriverWait(driver, 30).until(
        #EC.presence_of_element_located((By.XPATH, "//div[@class='balance']")))
    time.sleep(4)
    Balance_End = driver.find_element(By.XPATH, "//div[@class='balance']").text
    print("Game Balance on Screen Before Bet = " + Balance_End)
    Balance_Num_End_beforebet = float(Balance_End.split(" ")[0].replace(",", ""))
    return Balance_Num_End_beforebet


def getBalanceAfterBet(driver):
    #WebDriverWait(driver, 30).until(
        #EC.presence_of_element_located((By.XPATH, "//div[@class='balance']")))
    time.sleep(4)
    Balance_End = driver.find_element(By.XPATH, "//div[@class='balance']").text
    Balance_Num_End = float(Balance_End.split(" ")[0].replace(",", ""))
    print(f'Game Balance on Screen After Bet { Balance_Num_End}')
    return Balance_Num_End


def getExposure(driver):
    Exposure_After_bet = driver.find_element(By.CSS_SELECTOR, ".exposure-amount").text
    print("Exposure_Before_Bet = " + Exposure_After_bet)
    Exposure_Before_bet = float(Exposure_After_bet.split(" ")[0])
    return Exposure_Before_bet

def getExposureAfterbet(driver):
    Exposure_After_bet = driver.find_element(By.CSS_SELECTOR, ".exposure-amount").text
    print("Exposure_After_Bet = " + Exposure_After_bet)
    Exposure_After_bet = float(Exposure_After_bet.split(" ")[0])
    return Exposure_After_bet

def editStake(driver):
    driver.find_element(By.XPATH, '(//betslipheader/div/div/div)[3]').click()
    Betamount = driver.find_element(By.XPATH, '(//betslipeditstakes/div/div/div/input)[1]')
    x = Betamount.get_attribute("innerHTML")
    element = driver.find_element(By.XPATH, ' (//betslipeditstakes/div/div/div/input)[1]')
    action = ActionChains(driver)
    # double click the item
    action.double_click(on_element=element)
    # perform the operation
    action.perform()
    driver.find_element(By.XPATH, ' (//betslipeditstakes/div/div/div/input)[1]').send_keys("100")
    time.sleep(.5)
    pyautogui.click(1129, 474)

def assertion(driver):
    global Automated_Balance
    time.sleep(3)
    BalanceAfterResult = getBalanceAfterBet(driver)
    assert BalanceAfterResult == Automated_Balance
    if BalanceAfterResult == Automated_Balance:
        print(f"Successfully Completed All Scenarios are passed {BalanceAfterResult} = {Automated_Balance}")
    else:
        print("Check the server speed or calculate from next game balance")
