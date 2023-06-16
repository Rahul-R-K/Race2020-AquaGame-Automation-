import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pyautogui



def payoff_SpadeBack(driver):
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,
                                                                    "(//span[contains(text(),'Match Odds')])[2]/following::span[4]")))  # waiting till the element found
    payoffarea = driver.find_element(By.XPATH, "(//span[contains(text(),'Match Odds')])[2]/following::span[4]").text
    print("Spade Back payoff = " + payoffarea)
    payoff = payoffarea.split(" ")[1]
    payoff1 = float(payoff.replace(",", ""))
    return payoff1


#(//span[contains(text(),'3.85')])[2]/following::span[3]

def payoff_HeartBack(driver):
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,
                                                                    "(//span[contains(text(),'3.85')])[2]/following::span[3]")))  # waiting till the element found
    payoffarea = driver.find_element(By.XPATH, "(//span[contains(text(),'3.85')])[2]/following::span[3]").text
    print("Heart Back payoff = " + payoffarea)
    payoff = payoffarea.split(" ")[1]
    payoff1 = float(payoff.replace(",", ""))
    return payoff1


def payoff_ClubBack(driver):
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,
                                                                    "(//span[contains(text(),'3.85')])[3]/following::span[3]")))  # waiting till the element found
    payoffarea = driver.find_element(By.XPATH, "(//span[contains(text(),'3.85')])[3]/following::span[3]").text
    print("Heart Back payoff = " + payoffarea)
    payoff = payoffarea.split(" ")[1]
    payoff1 = float(payoff.replace(",", ""))
    return payoff1

def payoff_DiamondBack(driver):
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,
                                                                    "(//span[contains(text(),'3.85')])[4]/following::span[3]")))  # waiting till the element found
    payoffarea = driver.find_element(By.XPATH, "(//span[contains(text(),'3.85')])[4]/following::span[3]").text
    print("Heart Back payoff = " + payoffarea)
    payoff = payoffarea.split(" ")[1]
    payoff1 = float(payoff.replace(",", ""))
    return payoff1

def payoff_TotalCard(driver):
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,
                                                                    "(//span[contains(.,'13')])[1]/following::span[5]")))  # waiting till the element found
    payoffarea = driver.find_element(By.XPATH, "(//span[contains(.,'13')])[1]/following::span[5]").text
    print("payoff = " + payoffarea)
    payoff = payoffarea.split(" ")[1]
    payoff1 = float(payoff.replace(",", ""))
    return payoff1

def payoff_Totalpoint(driver):
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,
                                                                    "(//span[contains(.,'83')])[1]/following::span[5]")))  # waiting till the element found
    payoffarea = driver.find_element(By.XPATH, "(//span[contains(.,'83')])[1]/following::span[5]").text
    print("payoff = " + payoffarea)
    payoff = payoffarea.split(" ")[1]
    payoff1 = float(payoff.replace(",", ""))
    return payoff1


#(//span[contains(.,'Win with 5')])[1]/following::span[1]

def payoff_winwith5(driver):
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,
                                                                    "(//span[contains(.,'Win with 5')])[1]/following::span[1]")))  # waiting till the element found
    payoffarea = driver.find_element(By.XPATH, "(//span[contains(.,'Win with 5')])[1]/following::span[1]").text
    print("payoff = " + payoffarea)
    payoff = payoffarea.split(" ")[1]
    payoff1 = float(payoff.replace(",", ""))
    return payoff1

def payoff_winwith6(driver):
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,
                                                                    "(//span[contains(.,'Win with 6')])[1]/following::span[1]")))  # waiting till the element found
    payoffarea = driver.find_element(By.XPATH, "(//span[contains(.,'Win with 6')])[1]/following::span[1]").text
    print("payoff = " + payoffarea)
    payoff = payoffarea.split(" ")[1]
    payoff1 = float(payoff.replace(",", ""))
    return payoff1

def payoff_winwith7(driver):
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,
                                                                    "(//span[contains(.,'Win with 7')])[1]/following::span[1]")))  # waiting till the element found
    payoffarea = driver.find_element(By.XPATH, "(//span[contains(.,'Win with 7')])[1]/following::span[1]").text
    print("payoff = " + payoffarea)
    payoff = payoffarea.split(" ")[1]
    payoff1 = float(payoff.replace(",", ""))
    return payoff1

def payoff_winwith15(driver):
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,
                                                                    "(//span[contains(.,'Win with 15')])[1]/following::span[1]")))  # waiting till the element found
    payoffarea = driver.find_element(By.XPATH, "(//span[contains(.,'Win with 15')])[1]/following::span[1]").text
    print("payoff = " + payoffarea)
    payoff = payoffarea.split(" ")[1]
    payoff1 = float(payoff.replace(",", ""))
    return payoff1

def payoff_winwith16(driver):
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,
                                                                    "(//span[contains(.,'Win with 16')])[1]/following::span[1]")))  # waiting till the element found
    payoffarea = driver.find_element(By.XPATH, "(//span[contains(.,'Win with 16')])[1]/following::span[1]").text
    print("payoff = " + payoffarea)
    payoff = payoffarea.split(" ")[1]
    payoff1 = float(payoff.replace(",", ""))
    return payoff1

def payoff_winwith17(driver):
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,
                                                                    "(//span[contains(.,'Win with 17')])[1]/following::span[1]")))  # waiting till the element found
    payoffarea = driver.find_element(By.XPATH, "(//span[contains(.,'Win with 17')])[1]/following::span[1]").text
    print("payoff = " + payoffarea)
    payoff = payoffarea.split(" ")[1]
    payoff1 = float(payoff.replace(",", ""))
    return payoff1