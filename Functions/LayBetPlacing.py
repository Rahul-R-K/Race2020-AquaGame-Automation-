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

def SpadeLay_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'4.15')])[1]")))
    driver.find_element(By.XPATH, "(//span[contains(text(),'Match Odds')])[1]").click()
    element = driver.find_element(By.XPATH, "(//span[contains(text(),'4.15')])[1]")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    # Click on the element
    actions = ActionChains(driver)
    actions.click().perform()
    condformBet(driver)


def HeartLay_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'4.15')])[2]")))
    driver.find_element(By.XPATH, "(//span[contains(text(),'Match Odds')])[1]").click()
    element = driver.find_element(By.XPATH, "(//span[contains(text(),'4.15')])[2]")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    # Click on the element
    actions = ActionChains(driver)
    actions.click().perform()
    condformBet(driver)

def ClubLay_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'4.15')])[3]")))
    driver.find_element(By.XPATH, "(//span[contains(text(),'Match Odds')])[1]").click()
    element = driver.find_element(By.XPATH, "(//span[contains(text(),'4.15')])[3]")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    # Click on the element
    actions = ActionChains(driver)
    actions.click().perform()
    condformBet(driver)

def DimondLay_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'4.15')])[4]")))
    driver.find_element(By.XPATH, "(//span[contains(text(),'Match Odds')])[1]").click()
    element = driver.find_element(By.XPATH, "(//span[contains(text(),'4.15')])[4]")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    # Click on the element
    actions = ActionChains(driver)
    actions.click().perform()
    condformBet(driver)



def totalPoints_lay(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'79')])")))
    driver.find_element(By.XPATH, "(//span[contains(.,'Total')])[1]").click()
    element = driver.find_element(By.XPATH, "(//span[contains(.,'79')])")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    # Click on the element
    actions = ActionChains(driver)
    actions.click().perform()
    condformBet(driver)
