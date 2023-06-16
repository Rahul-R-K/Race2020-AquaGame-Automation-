import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pyautogui

def condformBet(driver):
    WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "(//tr/button)[1]")))
    driver.find_element(By.XPATH, "(//tr/button)[1]").click()
    driver.find_element(By.XPATH, '//button[contains(text(),"Place bets")]').click()

def Spade_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Match Odds')])[2]/following::div[4]")))
    driver.find_element(By.XPATH,"(//span[contains(text(),'Match Odds')])[1]").click()
    driver.find_element(By.XPATH,"(//span[contains(text(),'Match Odds')])[2]/following::div[4]").click()
    condformBet(driver)

def Heart_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'3.85')])[2]")))
    driver.find_element(By.XPATH, "(//span[contains(text(),'Match Odds')])[1]").click()
    driver.find_element(By.XPATH, "(//span[contains(text(),'3.85')])[2]").click()
    condformBet(driver)

def Club_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'3.85')])[3]")))
    driver.find_element(By.XPATH, "(//span[contains(text(),'Match Odds')])[1]").click()
    element = driver.find_element(By.XPATH, "(//span[contains(text(),'3.85')])[3]")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    #Click on the element
    actions = ActionChains(driver)
    actions.click().perform()
    condformBet(driver)

def Dimond_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'3.85')])[3]")))
    driver.find_element(By.XPATH, "(//span[contains(text(),'Match Odds')])[1]").click()
    element = driver.find_element(By.XPATH, "(//span[contains(text(),'3.85')])[4]")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    # Click on the element
    actions = ActionChains(driver)
    actions.click().perform()
    condformBet(driver)

def totalcard_backbet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'13')])[1]")))
    driver.find_element(By.XPATH, "(//span[contains(.,'Total')])[1]").click()
    element = driver.find_element(By.XPATH, "(//span[contains(.,'13')])[1]")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    # Click on the element
    actions = ActionChains(driver)
    actions.click().perform()
    condformBet(driver)

def totalcard_Lay(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'13')])[2]")))
    driver.find_element(By.XPATH, "(//span[contains(.,'Total')])[1]").click()
    element = driver.find_element(By.XPATH, "(//span[contains(.,'13')])[2]")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    # Click on the element
    actions = ActionChains(driver)
    actions.click().perform()
    condformBet(driver)

def totalPoints_Back(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'83')])")))
    driver.find_element(By.XPATH, "(//span[contains(.,'Total')])[1]").click()
    element = driver.find_element(By.XPATH, "(//span[contains(.,'83')])")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    # Click on the element
    actions = ActionChains(driver)
    actions.click().perform()
    condformBet(driver)


def Winwith5(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Win with 5')])[1]")))
    driver.find_element(By.XPATH, "(//span[contains(.,'Win With')])[1]").click()
    element = driver.find_element(By.XPATH, "(//span[contains(.,'Win with 5')])[1]")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    # Click on the element
    actions = ActionChains(driver)
    actions.click().perform()
    condformBet(driver)


def Winwith6(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Win with 6')])[1]")))
    driver.find_element(By.XPATH, "(//span[contains(.,'Win With')])[1]").click()
    element = driver.find_element(By.XPATH, "(//span[contains(.,'Win with 6')])[1]")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    # Click on the element
    actions = ActionChains(driver)
    actions.click().perform()
    condformBet(driver)

def Winwith7(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Win with 7')])[1]")))
    driver.find_element(By.XPATH, "(//span[contains(.,'Win With')])[1]").click()
    element = driver.find_element(By.XPATH, "(//span[contains(.,'Win with 7')])[1]")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    # Click on the element
    actions = ActionChains(driver)
    actions.click().perform()
    condformBet(driver)

def Winwith15(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Win with 15')])[1]")))
    driver.find_element(By.XPATH, "(//span[contains(.,'Win With')])[1]").click()
    element = driver.find_element(By.XPATH, "(//span[contains(.,'Win with 15')])[1]")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    # Click on the element
    actions = ActionChains(driver)
    actions.click().perform()
    condformBet(driver)

def Winwith16(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Win with 16')])[1]")))
    driver.find_element(By.XPATH, "(//span[contains(.,'Win With')])[1]").click()
    element = driver.find_element(By.XPATH, "(//span[contains(.,'Win with 16')])[1]")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    # Click on the element
    actions = ActionChains(driver)
    actions.click().perform()
    condformBet(driver)

def Winwith17(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Win with 17')])[1]")))
    driver.find_element(By.XPATH, "(//span[contains(.,'Win With')])[1]").click()
    element = driver.find_element(By.XPATH, "(//span[contains(.,'Win with 17')])[1]")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    # Click on the element
    actions = ActionChains(driver)
    actions.click().perform()
    condformBet(driver)