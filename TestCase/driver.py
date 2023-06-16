import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from Functions.common_function import getBalance, getExposure, editStake, assertion, getBalanceAfterBet
from Functions.BetPlacing import Spade_bet
from Functions.Payoff import payoff_SpadeBack
from Functions.BetStake import BetStake
from Functions.Result import SPADE_CARD, animation, result
import pytest


class Base():
    s_obj = Service(executable_path="D:\Rahul Files\C Files\PycharmProjects\Demo\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=s_obj, options=options)
    try:
        driver.get("http://aquaelqc.redimstg.com/")
        driver.maximize_window()
        driver.find_element(By.NAME, "username").send_keys("qctest4@test.com")  # sending Username
        element = driver.find_element(By.XPATH, "//div[8]/button")  # clicking submit button
        action = ActionChains(driver)
        action.double_click(on_element=element)
        action.perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[contains(text(),'RACE 20 - 20')]").click()
        new_window = driver.window_handles
        driver.switch_to.window(new_window[1])  # Switch from parent to Child Window
        print("Game page = " + driver.title)

                #############################################################################################################
    except:
        print("WebPage is Not Working")
    #yield
    #time.sleep(10)
    #driver.close()