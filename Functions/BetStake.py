import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pyautogui



def BetStake(driver):
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
                                                                     '((//div[contains(text(),"Markets")]/following::div)[3]/descendant::div)[2]')))  # waiting till the element found
    Bet_Markets = driver.find_element(By.XPATH,
                                      '((//div[contains(text(),"Markets")]/following::div)[3]/descendant::div)[2]').text
    #print("Bet_Markets =" + Bet_Markets)
    Bet_odds = driver.find_element(By.XPATH,
                                   '((//div[contains(text(),"Markets")]/following::div)[3]/descendant::div)[3]').text
    #print("Bet_odds =" + Bet_odds)
    Bet_Stakes1 = driver.find_element(By.XPATH,
                                      '((//div[contains(text(),"Markets")]/following::div)[3]/descendant::div)[4]').text
    print("Bet_Stakes =" + Bet_Stakes1)
    Bet_Stakes1 = int(Bet_Stakes1)
    return Bet_Stakes1


def BetStake2(driver):
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[5]/descendant::div)[1]")))
    Bet_Markets2 = driver.find_element(By.XPATH,
                                       "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[5]/descendant::div)[1]").text
    print("Bet_Markets2 =" + Bet_Markets2)

    Bet_Odds2 = driver.find_element(By.XPATH,
                                    "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[5]/descendant::div)[2]").text
    print("Bet_odds2 =" + Bet_Odds2)

    Bet_Stakes2 = driver.find_element(By.XPATH,
                                      "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[5]/descendant::div)[3]").text
    print("Bet_Stakes2 =" + Bet_Stakes2)
    Bet_Stakes2 = int(Bet_Stakes2)
    return Bet_Stakes2


def BetStake3(driver):
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[9]/descendant::div)[1]")))
    Bet_Markets3 = driver.find_element(By.XPATH,
                                       "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[9]/descendant::div)[1]").text
    print("Bet_Markets3 =" + Bet_Markets3)

    Bet_Odds3 = driver.find_element(By.XPATH,
                                    "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[9]/descendant::div)[2]").text
    print("Bet_Odds3 =" + Bet_Odds3)

    Bet_Stakes3 = driver.find_element(By.XPATH,
                                      "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[9]/descendant::div)[3]").text
    print("Bet_Stake3 =" + Bet_Stakes3)
    Bet_Stakes3 = int(Bet_Stakes3)
    return Bet_Stakes3


def BetStake4(driver):
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[13]/descendant::div)[1]")))
    Bet_Markets4 = driver.find_element(By.XPATH,
                                       "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[13]/descendant::div)[1]").text
    print("Bet_Markets4 =" + Bet_Markets4)

    Bet_Odds4 = driver.find_element(By.XPATH,
                                    "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[13]/descendant::div)[2]").text
    print("Bet_odds4 =" + Bet_Odds4)

    Bet_Stakes4 = driver.find_element(By.XPATH,
                                      "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[13]/descendant::div)[3]").text
    print("Bet_Stakes4 =" + Bet_Stakes4)
    Bet_Stakes4 = int(Bet_Stakes4)
    return Bet_Stakes4


def BetStake5(driver):
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[17]/descendant::div)[1]")))
    Bet_Markets5 = driver.find_element(By.XPATH,
                                       "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[17]/descendant::div)[1]").text
    print("Bet_Markets5 =" + Bet_Markets5)

    Bet_Odds5 = driver.find_element(By.XPATH,
                                    "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[17]/descendant::div)[2]").text
    print("Bet_odds5 =" + Bet_Odds5)

    Bet_Stakes5 = driver.find_element(By.XPATH,
                                      "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[17]/descendant::div)[3]").text
    print("Bet_stakes5 =" + Bet_Stakes5)
    Bet_Stakes5 = int(Bet_Stakes5)
    return Bet_Stakes5


def BetStake6(driver):
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[21]/descendant::div)[1]")))
    Bet_Markets6 = driver.find_element(By.XPATH,
                                       "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[21]/descendant::div)[1]").text
    print("Bet_Markets6 =" + Bet_Markets6)

    Bet_Odds6 = driver.find_element(By.XPATH,
                                    "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[21]/descendant::div)[2]").text
    print("Bet_odds6 =" + Bet_Odds6)

    Bet_Stakes6 = driver.find_element(By.XPATH,
                                      "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[21]/descendant::div)[3]").text
    print("Bet_stakes6 =" + Bet_Stakes6)
    Bet_Stakes6 = int(Bet_Stakes6)
    return Bet_Stakes6


def BetStake7(driver):
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[25]/descendant::div)[1]")))
    Bet_Markets7 = driver.find_element(By.XPATH,
                                       "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[25]/descendant::div)[1]").text
    print("Bet_Markets7 =" + Bet_Markets7)

    Bet_Odds7 = driver.find_element(By.XPATH,
                                    "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[25]/descendant::div)[2]").text
    print("Bet_odds7 =" + Bet_Odds7)

    Bet_Stakes7 = driver.find_element(By.XPATH,
                                      "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[25]/descendant::div)[3]").text
    print("Bet_stakes7 =" + Bet_Stakes7)
    Bet_Stakes7 = int(Bet_Stakes7)
    return Bet_Stakes7


def BetStake8(driver):
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[29]/descendant::div)[1]")))
    Bet_Markets8 = driver.find_element(By.XPATH,
                                       "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[29]/descendant::div)[1]").text
    print("Bet_Markets8 =" + Bet_Markets8)

    Bet_Odds8 = driver.find_element(By.XPATH,
                                    "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[29]/descendant::div)[2]").text
    print("Bet_odds8 =" + Bet_Odds8)

    Bet_Stakes8 = driver.find_element(By.XPATH,
                                      "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[29]/descendant::div)[3]").text
    print("Bet_stakes8 =" + Bet_Stakes8)
    Bet_Stakes8 = int(Bet_Stakes8)
    return Bet_Stakes8


