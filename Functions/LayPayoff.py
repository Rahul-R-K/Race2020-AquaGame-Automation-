import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pyautogui




def payoff_SpadeLay(driver):
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,
                                                                    "(//span[contains(text(),'4.15')])[1]/following::span[4]")))  # waiting till the element found
    payoffarea = driver.find_element(By.XPATH, "(//span[contains(text(),'4.15')])[1]/following::span[4]").text
    print("payoff = " + payoffarea)
    payoff = payoffarea.split(" ")[1]
    payoff1 = float(payoff.replace(",", ""))
    return payoff1

def payoff_HeartLay(driver):
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,
                                                                    "(//span[contains(text(),'4.15')])[2]/following::span[4]")))  # waiting till the element found
    payoffarea = driver.find_element(By.XPATH, "(//span[contains(text(),'4.15')])[2]/following::span[4]").text
    print("payoff = " + payoffarea)
    payoff = payoffarea.split(" ")[1]
    payoff1 = float(payoff.replace(",", ""))
    return payoff1

def payoff_ClubLay(driver):
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,
                                                                    "(//span[contains(text(),'4.15')])[3]/following::span[4]")))  # waiting till the element found
    payoffarea = driver.find_element(By.XPATH, "(//span[contains(text(),'4.15')])[3]/following::span[4]").text
    print("payoff = " + payoffarea)
    payoff = payoffarea.split(" ")[1]
    payoff1 = float(payoff.replace(",", ""))
    return payoff1

def payoff_DimondLay(driver):
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,
                                                                    "(//span[contains(text(),'4.15')])[4]/following::span[4]")))  # waiting till the element found
    payoffarea = driver.find_element(By.XPATH, "(//span[contains(text(),'4.15')])[4]/following::span[4]").text
    print("payoff = " + payoffarea)
    payoff = payoffarea.split(" ")[1]
    payoff1 = float(payoff.replace(",", ""))
    return payoff1

def payoff_Totalcardlay(driver):
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,
                                                                    "(//span[contains(.,'13')])[2]/following::span[5]")))  # waiting till the element found
    payoffarea = driver.find_element(By.XPATH, "(//span[contains(.,'13')])[2]/following::span[5]").text
    print("payoff = " + payoffarea)
    payoff = payoffarea.split(" ")[1]
    payoff1 = float(payoff.replace(",", ""))
    return payoff1

def payoff_Totalpointlay(driver):
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,
                                                                    "(//span[contains(.,'79')])[1]/following::span[5]")))  # waiting till the element found
    payoffarea = driver.find_element(By.XPATH, "(//span[contains(.,'79')])[1]/following::span[5]").text
    print("payoff = " + payoffarea)
    payoff = payoffarea.split(" ")[1]
    payoff1 = float(payoff.replace(",", ""))
    return payoff1