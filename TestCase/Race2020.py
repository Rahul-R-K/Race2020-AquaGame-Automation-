import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from Functions.common_function import getBalance, getExposure, editStake, assertion, getBalanceAfterBet, getExposureAfterbet
from Functions.BetPlacing import Spade_bet, Heart_bet, Club_bet, Dimond_bet, totalcard_backbet,totalcard_Lay,totalPoints_Back,Winwith6,Winwith5,Winwith7,Winwith15,Winwith16,Winwith17
from Functions.Payoff import payoff_SpadeBack, payoff_HeartBack, payoff_ClubBack, payoff_TotalCard,payoff_Totalpoint, payoff_winwith5,payoff_winwith15,payoff_winwith16,payoff_winwith17,payoff_winwith6, payoff_winwith7,payoff_DiamondBack
from Functions.BetStake import BetStake, BetStake2, BetStake3,BetStake4, BetStake5, BetStake6,BetStake7,BetStake8
from Functions.Result import SPADE_CARD, animation, result, totalcard, totalPoint
from Functions.LayBetPlacing import SpadeLay_bet, HeartLay_bet, ClubLay_bet, DimondLay_bet, totalPoints_lay
from Functions.LayPayoff import payoff_SpadeLay, payoff_HeartLay, payoff_DimondLay, payoff_ClubLay,payoff_Totalcardlay, payoff_Totalpointlay
import pytest
from driver import Base
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestCase(Base):

    def test_getBalance_and_Exposure(self):
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)

    def test_EditStake(self):
        EditStake = editStake(self.driver)

    def test_Spade_Back_Bet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        Spade_bet(self.driver)
        SpadeBackPayoff = payoff_SpadeBack(self.driver)
        Betstake = BetStake(self.driver)
        Payoff_SpadeBack = payoff_SpadeBack(self.driver)
        Result_Suit = result(self.driver)
        if Result_Suit in ['SPADE']:
            print("Spade Back Won")
            Automated_Balance = Balance + Payoff_SpadeBack
            print("Automated Balance = " + str(Automated_Balance))
        elif Result_Suit in ['CLUB','HEART', 'DIAMOND']:
            print("Spade Back Loss")
            Automated_Balance = Balance - Betstake
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")



    def test_Heart_Back_Bet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        Heart_bet(self.driver)
        Betstake = BetStake(self.driver)
        Payoff_HeartBack = payoff_HeartBack(self.driver)
        Result_Suit = result(self.driver)
        if Result_Suit in ['HEART']:
            print("Heart Back Won")
            Automated_Balance = Balance + Payoff_HeartBack
            print("Automated Balance = " + str(Automated_Balance))
        elif Result_Suit in ['CLUB','SPADE', 'DIAMOND']:
            print("Heart Back Loss")
            Automated_Balance = Balance - Betstake
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")



    def test_Club_Back_Bet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        Club_bet(self.driver)
        Betstake = BetStake(self.driver)
        Payoff_ClubBack = payoff_ClubBack(self.driver)
        Result_Suit = result(self.driver)
        if Result_Suit in ['CLUB']:
            print("Club Back Won")
            Automated_Balance = Balance + Payoff_ClubBack
            print("Automated Balance = " + str(Automated_Balance))
        elif Result_Suit in ['HEART','SPADE', 'DIAMOND']:
            print("Club Back Loss")
            Automated_Balance = Balance - Betstake
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")
    #SPADE-0 DIAMOND-0 CLUB-1 HEART-0


    def test_Dimond_Back_Bet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        Dimond_bet(self.driver)
        Betstake = BetStake(self.driver)
        Payoff_Diamondback = payoff_DiamondBack(self.driver)
        Result_Suit = result(self.driver)
        if Result_Suit in ['DIAMOND']:
            print("Dimond Back Won")
            Automated_Balance = Balance + Payoff_Diamondback
            print("Automated Balance = " + str(Automated_Balance))
        elif Result_Suit in ['HEART','SPADE', 'CLUB']:
            print("Dimond Back Loss")
            Automated_Balance = Balance - Betstake
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")
    #SPADE-0 DIAMOND-0 CLUB-1 HEART-0



    def test_Spade_Lay_Bet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        SpadeLay_bet(self.driver)
        Betstake = BetStake(self.driver)
        AfterbetExposure = getExposureAfterbet(self.driver)
        Payoff_Spadelay = payoff_SpadeLay(self.driver)
        Result_Suit = result(self.driver)
        if Result_Suit in ['SPADE']:
            print("Spade lay loss")
            Automated_Balance = Balance - AfterbetExposure
            print("Automated Balance = " + str(Automated_Balance))
        elif Result_Suit in ['HEART','DIAMOND', 'CLUB']:
            print("Spade Lay won")
            Automated_Balance = Balance + Payoff_Spadelay
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")
    #SPADE-0 DIAMOND-0 CLUB-1 HEART-0



    def test_Heart_Lay_Bet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        HeartLay_bet(self.driver)
        Betstake = BetStake(self.driver)
        AfterbetExposure = getExposureAfterbet(self.driver)
        Payoff_Heartlay = payoff_HeartLay(self.driver)
        Result_Suit = result(self.driver)
        if Result_Suit in ['HEART']:
            print("Heart lay loss")
            Automated_Balance = Balance - AfterbetExposure
            print("Automated Balance = " + str(Automated_Balance))
        elif Result_Suit in ['SPADE','DIAMOND', 'CLUB']:
            print("Heart Lay won")
            Automated_Balance = Balance + Payoff_Heartlay
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")

    def test_Club_Lay_Bet(self):
            global Automated_Balance
            Balance = getBalance(self.driver)
            Exposure = getExposure(self.driver)
            ClubLay_bet(self.driver)
            Betstake = BetStake(self.driver)
            AfterbetExposure = getExposureAfterbet(self.driver)
            Payoff_Clublay = payoff_ClubLay(self.driver)
            Result_Suit = result(self.driver)
            if Result_Suit in ['HEART']:
                print("Club lay loss")
                Automated_Balance = Balance - AfterbetExposure
                print("Automated Balance = " + str(Automated_Balance))
            elif Result_Suit in ['SPADE','DIAMOND', 'CLUB']:
                print("Club Lay won")
                Automated_Balance = Balance + Payoff_Clublay
                print("Automated Balance = " + str(Automated_Balance))
            time.sleep(1)
            Balance_After_Result = getBalanceAfterBet(self.driver)
            assert Balance_After_Result == Automated_Balance
            if Balance_After_Result == Automated_Balance:
                print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
            else:
                print("Something wrong in payoff check it manually (or) Check the server speed ")

    def test_Dimond_Lay_Bet(self):
            global Automated_Balance
            Balance = getBalance(self.driver)
            Exposure = getExposure(self.driver)
            DimondLay_bet(self.driver)
            Betstake = BetStake(self.driver)
            AfterbetExposure = getExposureAfterbet(self.driver)
            Payoff_Dimondlay = payoff_DimondLay(self.driver)
            Result_Suit = result(self.driver)
            if Result_Suit in ['DIMOND']:
                print("Dimond lay loss")
                Automated_Balance = Balance - AfterbetExposure
                print("Automated Balance = " + str(Automated_Balance))
            elif Result_Suit in ['SPADE','HEART', 'CLUB']:
                print("Dimond Lay won")
                Automated_Balance = Balance + Payoff_Dimondlay
                print("Automated Balance = " + str(Automated_Balance))
            time.sleep(1)
            Balance_After_Result = getBalanceAfterBet(self.driver)
            assert Balance_After_Result == Automated_Balance
            if Balance_After_Result == Automated_Balance:
                print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
            else:
                print("Something wrong in payoff check it manually (or) Check the server speed ")


    def test_TotalCard_Bet(self):
            global Automated_Balance
            Balance = getBalance(self.driver)
            Exposure = getExposure(self.driver)
            totalcard_backbet(self.driver)
            Betstake = BetStake(self.driver)
            AfterbetExposure = getExposureAfterbet(self.driver)
            Payoff_Totalcard = payoff_TotalCard(self.driver)
            TotalCard = int(totalcard(self.driver))

            if TotalCard == 13:
                print("TotalCard bet wins")
                Automated_Balance = Balance + Payoff_Totalcard
                print("Automated Balance = " + str(Automated_Balance))
            elif TotalCard != 13:
                print("TotalCard bet loss")
                Automated_Balance = Balance - AfterbetExposure
                print("Automated Balance = " + str(Automated_Balance))
            time.sleep(1)
            Balance_After_Result = getBalanceAfterBet(self.driver)
            assert Balance_After_Result == Automated_Balance
            if Balance_After_Result == Automated_Balance:
                print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
            else:
                print("Something wrong in payoff check it manually (or) Check the server speed ")


    def test_TotalCardlay_Bet(self):
            global Automated_Balance
            Balance = getBalance(self.driver)
            Exposure = getExposure(self.driver)
            totalcard_Lay(self.driver)
            Betstake = BetStake(self.driver)
            AfterbetExposure = getExposureAfterbet(self.driver)
            PayoffTotalCardlay = payoff_Totalcardlay(self.driver)
            TotalCard = int(totalcard(self.driver))
            if TotalCard >= 13:
                print("TotalCard lay fails")
                Automated_Balance = Balance - AfterbetExposure
                print("Automated Balance = " + str(Automated_Balance))
            elif TotalCard < 13 :
                print("TotalCard lay win")
                Automated_Balance =  Balance + PayoffTotalCardlay
                print("Automated Balance = " + str(Automated_Balance))
            time.sleep(1)
            Balance_After_Result = getBalanceAfterBet(self.driver)
            assert Balance_After_Result == Automated_Balance
            if Balance_After_Result == Automated_Balance:
                print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
            else:
                print("Something wrong in payoff check it manually (or) Check the server speed ")


    def test_TotalPoint_Bet(self):
            global Automated_Balance
            Balance = getBalance(self.driver)
            Exposure = getExposure(self.driver)
            totalPoints_Back(self.driver)
            Betstake = BetStake(self.driver)
            AfterbetExposure = getExposureAfterbet(self.driver)
            Payoff_Totalpoint = payoff_Totalpoint(self.driver)
            TotalCard = int(totalPoint(self.driver))

            if TotalCard == 83:
                print("TotalPoint bet wins")
                Automated_Balance = Balance + Payoff_Totalpoint
                print("Automated Balance = " + str(Automated_Balance))
            elif TotalCard != 83:
                print("TotalPoint bet loss")
                Automated_Balance = Balance - AfterbetExposure
                print("Automated Balance = " + str(Automated_Balance))
            time.sleep(1)
            Balance_After_Result = getBalanceAfterBet(self.driver)
            assert Balance_After_Result == Automated_Balance
            if Balance_After_Result == Automated_Balance:
                print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
            else:
                print("Something wrong in payoff check it manually (or) Check the server speed ")



    def test_TotalPointlay_Bet(self):
            global Automated_Balance
            Balance = getBalance(self.driver)
            Exposure = getExposure(self.driver)
            totalPoints_lay(self.driver)
            Betstake = BetStake(self.driver)
            AfterbetExposure = getExposureAfterbet(self.driver)
            Payoff_Totalpointlay = payoff_Totalpointlay(self.driver)
            TotalCard = int(totalPoint(self.driver))

            if TotalCard >= 83:
                print("TotalPoint lay loss")
                Automated_Balance = Balance - AfterbetExposure
                print("Automated Balance = " + str(Automated_Balance))
            elif TotalCard < 83 :
                print("Totalpoint Lay Wins")
                Automated_Balance = Balance + Payoff_Totalpointlay
                print("Automated Balance = " + str(Automated_Balance))
            time.sleep(1)
            Balance_After_Result = getBalanceAfterBet(self.driver)
            assert Balance_After_Result == Automated_Balance
            if Balance_After_Result == Automated_Balance:
                print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
            else:
                print("Something wrong in payoff check it manually (or) Check the server speed ")



    def test_Winwith5Bet(self):
            global Automated_Balance
            Balance = getBalance(self.driver)
            Exposure = getExposure(self.driver)
            Winwith5(self.driver)
            Betstake = BetStake(self.driver)
            AfterbetExposure = getExposureAfterbet(self.driver)
            Payoff_Winwith5 = payoff_winwith5(self.driver)
            TotalCard = int(totalcard(self.driver))

            if TotalCard == 5:
                print("TotalPoint bet wins")
                Automated_Balance = Balance + Payoff_Winwith5
                print("Automated Balance = " + str(Automated_Balance))
            elif TotalCard != 5 :
                print("TotalPoint bet loss")
                Automated_Balance = Balance - AfterbetExposure
                print("Automated Balance = " + str(Automated_Balance))
            time.sleep(1)
            Balance_After_Result = getBalanceAfterBet(self.driver)
            assert Balance_After_Result == Automated_Balance
            if Balance_After_Result == Automated_Balance:
                print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
            else:
                print("Something wrong in payoff check it manually (or) Check the server speed ")


    def test_Winwith6Bet(self):
            global Automated_Balance
            Balance = getBalance(self.driver)
            Exposure = getExposure(self.driver)
            Winwith6(self.driver)
            Betstake = BetStake(self.driver)
            AfterbetExposure = getExposureAfterbet(self.driver)
            Payoff_Winwith6 = payoff_winwith6(self.driver)
            TotalCard = int(totalcard(self.driver))

            if TotalCard == 6:
                print("TotalPoint bet wins")
                Automated_Balance = Balance +  Payoff_Winwith6
                print("Automated Balance = " + str(Automated_Balance))
            elif TotalCard != 6:
                print("TotalPoint bet loss")
                Automated_Balance = Balance - AfterbetExposure
                print("Automated Balance = " + str(Automated_Balance))
            time.sleep(1)
            Balance_After_Result = getBalanceAfterBet(self.driver)
            assert Balance_After_Result == Automated_Balance
            if Balance_After_Result == Automated_Balance:
                print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
            else:
                print("Something wrong in payoff check it manually (or) Check the server speed ")



    def test_Winwith7Bet(self):
            global Automated_Balance
            Balance = getBalance(self.driver)
            Exposure = getExposure(self.driver)
            Winwith7(self.driver)
            Betstake = BetStake(self.driver)
            AfterbetExposure = getExposureAfterbet(self.driver)
            Payoff_Winwith7 = payoff_winwith7(self.driver)
            TotalCard = int(totalcard(self.driver))

            if TotalCard == 7:
                print("TotalPoint bet wins")
                Automated_Balance = Balance + Payoff_Winwith7
                print("Automated Balance = " + str(Automated_Balance))
            elif TotalCard != 7 :
                print("TotalPoint bet loss")
                Automated_Balance = Balance - AfterbetExposure
                print("Automated Balance = " + str(Automated_Balance))
            time.sleep(1)
            Balance_After_Result = getBalanceAfterBet(self.driver)
            assert Balance_After_Result == Automated_Balance
            if Balance_After_Result == Automated_Balance:
                print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
            else:
                print("Something wrong in payoff check it manually (or) Check the server speed ")


    def test_Winwith15Bet(self):
            global Automated_Balance
            Balance = getBalance(self.driver)
            Exposure = getExposure(self.driver)
            Winwith15(self.driver)
            Betstake = BetStake(self.driver)
            AfterbetExposure = getExposureAfterbet(self.driver)
            Payoff_Winwith15 = payoff_winwith15(self.driver)
            TotalCard = int(totalcard(self.driver))

            if TotalCard == 15:
                print("TotalPoint bet wins")
                Automated_Balance = Balance + Payoff_Winwith15
                print("Automated Balance = " + str(Automated_Balance))
            elif TotalCard != 15 :
                print("TotalPoint bet loss")
                Automated_Balance = Balance - AfterbetExposure
                print("Automated Balance = " + str(Automated_Balance))
            time.sleep(1)
            Balance_After_Result = getBalanceAfterBet(self.driver)
            assert Balance_After_Result == Automated_Balance
            if Balance_After_Result == Automated_Balance:
                print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
            else:
                print("Something wrong in payoff check it manually (or) Check the server speed ")


    def test_Winwith16Bet(self):
            global Automated_Balance
            Balance = getBalance(self.driver)
            Exposure = getExposure(self.driver)
            Winwith16(self.driver)
            Betstake = BetStake(self.driver)
            AfterbetExposure = getExposureAfterbet(self.driver)
            Payoff_Winwith16 = payoff_winwith16(self.driver)
            TotalCard = int(totalcard(self.driver))

            if TotalCard == 16:
                print("TotalPoint bet wins")
                Automated_Balance = Balance + Payoff_Winwith16
                print("Automated Balance = " + str(Automated_Balance))
            elif TotalCard != 16 :
                print("TotalPoint bet loss")
                Automated_Balance = Balance - AfterbetExposure
                print("Automated Balance = " + str(Automated_Balance))
            time.sleep(1)
            Balance_After_Result = getBalanceAfterBet(self.driver)
            assert Balance_After_Result == Automated_Balance
            if Balance_After_Result == Automated_Balance:
                print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
            else:
                print("Something wrong in payoff check it manually (or) Check the server speed ")


    def test_Winwith17Bet(self):
            global Automated_Balance
            Balance = getBalance(self.driver)
            Exposure = getExposure(self.driver)
            Winwith17(self.driver)
            Betstake = BetStake(self.driver)
            AfterbetExposure = getExposureAfterbet(self.driver)
            Payoff_Winwith17 = payoff_winwith17(self.driver)
            TotalCard = int(totalcard(self.driver))

            if TotalCard == 17:
                print("TotalPoint bet wins")
                Automated_Balance = Balance + Payoff_Winwith17
                print("Automated Balance = " + str(Automated_Balance))
            elif TotalCard != 17 :
                print("TotalPoint bet loss")
                Automated_Balance = Balance - AfterbetExposure
                print("Automated Balance = " + str(Automated_Balance))
            time.sleep(1)
            Balance_After_Result = getBalanceAfterBet(self.driver)
            assert Balance_After_Result == Automated_Balance
            if Balance_After_Result == Automated_Balance:
                print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
            else:
                print("Something wrong in payoff check it manually (or) Check the server speed ")


    def test_WinwithBet(self):
            global Automated_Balance
            Balance = getBalance(self.driver)
            Exposure = getExposure(self.driver)
            Winwith5(self.driver)
            Winwith6(self.driver)
            Winwith7(self.driver)
            Winwith15(self.driver)
            Winwith16(self.driver)
            Winwith17(self.driver)
            Betstake = BetStake(self.driver)
            AfterbetExposure = getExposureAfterbet(self.driver)
            Payoff_Winwith5 = payoff_winwith5(self.driver)
            Payoff_Winwith6 = payoff_winwith6(self.driver)
            Payoff_Winwith7 = payoff_winwith7(self.driver)
            Payoff_Winwith15 = payoff_winwith15(self.driver)
            Payoff_Winwith16 = payoff_winwith16(self.driver)
            Payoff_Winwith17 = payoff_winwith17(self.driver)
            TotalCard = int(totalcard(self.driver))

            if TotalCard == 5:
                print("TotalCard5 bet wins")
                Automated_Balance = Balance + Payoff_Winwith5 -AfterbetExposure +100
                print("Automated Balance = " + str(Automated_Balance))
            elif TotalCard == 6:
                print("TotalCard6 bet wins")
                Automated_Balance = Balance + Payoff_Winwith6 -AfterbetExposure +100
                print("Automated Balance = " + str(Automated_Balance))
            elif TotalCard == 7:
                print("TotalCard7 bet wins")
                Automated_Balance = Balance + Payoff_Winwith7 -AfterbetExposure +100
                print("Automated Balance = " + str(Automated_Balance))
            elif TotalCard == 15:
                print("TotalCard15 bet wins")
                Automated_Balance = Balance + Payoff_Winwith15 -AfterbetExposure +100
                print("Automated Balance = " + str(Automated_Balance))
            elif TotalCard == 16:
                print("TotalCard16 bet wins")
                Automated_Balance = Balance + Payoff_Winwith16 -AfterbetExposure +100
                print("Automated Balance = " + str(Automated_Balance))
            elif TotalCard == 17:
                print("TotalCard17 bet wins")
                Automated_Balance = Balance + Payoff_Winwith17 -AfterbetExposure +100
                print("Automated Balance = " + str(Automated_Balance))
            else:
                print("bet loss")
                Automated_Balance = Balance - AfterbetExposure
                print("Automated Balance = " + str(Automated_Balance))

            time.sleep(1)
            Balance_After_Result = getBalanceAfterBet(self.driver)
            assert Balance_After_Result == Automated_Balance
            if Balance_After_Result == Automated_Balance:
                print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
            else:
                print("Something wrong in payoff check it manually (or) Check the server speed ")


    def test_TotalPoint_TotalCard_Bet(self):
            global Automated_Balance
            Balance = getBalance(self.driver)
            Exposure = getExposure(self.driver)
            totalPoints_Back(self.driver)
            totalcard_backbet(self.driver)
            Betstake1 = BetStake(self.driver)
            Betstake2 = BetStake2(self.driver)
            AfterbetExposure = getExposureAfterbet(self.driver)
            Payoff_Totalpoint = payoff_Totalpoint(self.driver)
            Payoff_Totalcard = payoff_TotalCard(self.driver)
            TotalPoint = int(totalPoint(self.driver))
            TotalCard = int(totalcard(self.driver))

            if TotalPoint == 83 and TotalCard == 13:
                print("TotalPoint bet wins")
                Automated_Balance = Balance + Payoff_Totalpoint + Payoff_Totalcard
                print("Automated Balance = " + str(Automated_Balance))
            elif TotalPoint != 83 and TotalCard != 13:
                print("TotalPoint bet loss")
                Automated_Balance = Balance - Betstake1 - Betstake2
                print("Automated Balance = " + str(Automated_Balance))

            elif TotalPoint != 83 and TotalCard == 13:
                print("TotalPoint bet loss")
                Automated_Balance = Balance - Betstake1 + Payoff_Totalcard
                print("Automated Balance = " + str(Automated_Balance))

            elif TotalPoint == 83 and TotalCard != 13:
                print("TotalPoint bet loss")
                Automated_Balance = Balance - Betstake2 + Payoff_Totalpoint
                print("Automated Balance = " + str(Automated_Balance))

            time.sleep(1)
            Balance_After_Result = getBalanceAfterBet(self.driver)
            assert Balance_After_Result == Automated_Balance
            if Balance_After_Result == Automated_Balance:
                print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
            else:
                print("Something wrong in payoff check it manually (or) Check the server speed ")


    def test_TotalPoint_TotalCard_lay_Bet(self):
            global Automated_Balance
            Balance = getBalance(self.driver)
            Exposure = getExposure(self.driver)
            totalPoints_lay(self.driver)
            totalcard_Lay(self.driver)
            Betstake1 = BetStake(self.driver)
            Betstake2 = BetStake2(self.driver)
            AfterbetExposure = getExposureAfterbet(self.driver)
            Payoff_Totalpointlay = payoff_Totalpointlay(self.driver)
            PayoffTotalCardlay = payoff_Totalcardlay(self.driver)
            TotalPoint = int(totalPoint(self.driver))
            TotalCard = int(totalcard(self.driver))

            if TotalPoint >= 83 and TotalCard >= 13:
                print("TotalPoint lay loss")
                Automated_Balance = Balance - Betstake1 - (Betstake2 * 2.05)
                print("Automated Balance = " + str(Automated_Balance))
            elif TotalPoint < 83 and TotalCard < 13:
                print("Totalpoint Lay Wins")
                Automated_Balance = Balance + Payoff_Totalpointlay + PayoffTotalCardlay
                print("Automated Balance = " + str(Automated_Balance))
            elif TotalPoint < 83 and TotalCard >= 13:
                print("Totalpoint Lay Wins")
                Automated_Balance = Balance + Payoff_Totalpointlay - (Betstake2 * 2.05)
                print("Automated Balance = " + str(Automated_Balance))
            elif TotalPoint >= 83 and TotalCard < 13:
                print("TotalPoint lay loss")
                Automated_Balance = Balance - Betstake1 + PayoffTotalCardlay
                print("Automated Balance = " + str(Automated_Balance))

            time.sleep(1)
            Balance_After_Result = getBalanceAfterBet(self.driver)
            assert Balance_After_Result == Automated_Balance
            if Balance_After_Result == Automated_Balance:
                print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
            else:
                print("Something wrong in payoff check it manually (or) Check the server speed ")


    def test_Mainbet_Back_Bet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        Spade_bet(self.driver)
        time.sleep(1)
        Heart_bet(self.driver)
        time.sleep(1)
        Club_bet(self.driver)
        time.sleep(1)
        Dimond_bet(self.driver)
        Betstake1 = BetStake(self.driver)
        Betstake2 = BetStake2(self.driver)
        Betstake3 = BetStake3(self.driver)
        Betstake4 = BetStake4(self.driver)
        Payoff_SpadeBack = payoff_SpadeBack(self.driver)
        Payoff_HeartBack = payoff_HeartBack(self.driver)
        Payoff_ClubBack = payoff_ClubBack(self.driver)
        Payoff_Diamondback = payoff_DiamondBack(self.driver)

        Result_Suit = result(self.driver)
        if Result_Suit in ['SPADE']:
            print("Spade Back Won")
            Automated_Balance = Balance + Payoff_SpadeBack - Betstake2 -Betstake3-Betstake4
            print("Automated Balance = " + str(Automated_Balance))

        elif Result_Suit in ['HEART']:
            print("Heart Back Won")
            Automated_Balance = Balance + Payoff_HeartBack - Betstake1 -Betstake3-Betstake4
            print("Automated Balance = " + str(Automated_Balance))

        elif Result_Suit in ['DIAMOND']:
            print("Diamond Back Won")
            Automated_Balance = Balance + Payoff_Diamondback - Betstake1 -Betstake2-Betstake3
            print("Automated Balance = " + str(Automated_Balance))

        elif Result_Suit in ['CLUB']:
            print("Club Back Won")
            Automated_Balance = Balance + Payoff_ClubBack - Betstake1 -Betstake2-Betstake4
            print("Automated Balance = " + str(Automated_Balance))

        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")


    def test_Mainbet_Lay_Bet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        SpadeLay_bet(self.driver)
        HeartLay_bet(self.driver)
        ClubLay_bet(self.driver)
        DimondLay_bet(self.driver)
        Payoff_Spadelay = payoff_SpadeLay(self.driver)
        Payoff_Heartlay = payoff_HeartLay(self.driver)
        Payoff_Clublay = payoff_ClubLay(self.driver)
        Payoff_Dimondlay = payoff_DimondLay(self.driver)
        Result_Suit = result(self.driver)
        print("one lay loss")
        Automated_Balance = Balance - 15
        print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(
                f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")
