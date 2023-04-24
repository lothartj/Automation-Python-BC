import tkinter as tk
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest
import time
import re
import datetime
import os
import sys
import pyautogui as py
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username2 = input('')
password2 = input('')

itemNo = input('Enter item No: ')
description = input('Enter item description: ')
uom = input("Enter item Unit of measure: ")
weight = input("Enter item weight: ")
barcode = input("Enter item barcode: ")

PATH = ('C:/chromedriver.exe')
driver = webdriver.Chrome(PATH)
driver.get(
    'https://bc.deepcatchgroup.com/DT_BC21_UAT_UP/SignIn?ReturnUrl=%2FDT_BC21_UAT_UP%2F')
# wait for the iframe element to load

driver.maximize_window()
time.sleep(2)
time.sleep(2)

py.hotkey('tab')
py.typewrite(username2)
py.hotkey('tab')
py.typewrite(password2)
py.hotkey('enter')

time.sleep(10)

# # switch to the iframe
# iframe = driver.find_element(By.CSS_SELECTOR, 'iframe.designer-client-frame')
# driver.switch_to.frame(iframe)


# Change link to Items
driver.get(
    'https://bc.deepcatchgroup.com/DT_BC21_UAT_UP/?company=Deep%20Catch%20Trading%20(Pty)%20Ltd&node=00002338-752d-0000-0c5f-2f00836bd2d2&page=31&dc=0&bookmark=31%3bGwAAAAJ7%2fzIANABJAEMARQAwADAAMQAwADA%3d')
time.sleep(15)

# switch to the iframe
iframe = driver.find_element(By.CSS_SELECTOR, 'iframe.designer-client-frame')
driver.switch_to.frame(iframe)

# wait for the element to be visible, to click new
newBTN = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div/div[2]/form/div/div[2]/div[2]/div/div/nav/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div/button'))
)

# click the element
newBTN.click()

time.sleep(5)

# iframeDesigner = driver.find_element(By.CSS_SELECTOR, 'designer-client-frame')
# driver.switch_to.frame(iframeDesigner)

No = py.typewrite(itemNo)
time.sleep(5)
py.hotkey('tab')
desc = py.typewrite(description)

time.sleep(3)

Baw_UOM = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[3]/form/main/div[2]/div[6]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[7]/div/input'))
)

# click the element
Baw_UOM.click()

if uom == 'BAG':
    # wait for the element to be visible
    UOM_BAG = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[1]/div[4]/form/div[2]/div/div[1]/div/div/div[2]/table/tbody/tr[1]'))
    )

    # click the element
    UOM_BAG.click()

if uom == 'CS':
    UOM_CS = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[1]/div[4]/form/div[2]/div/div[1]/div/div/div[2]/table/tbody/tr[2]'))
    )

    # click the element
    UOM_CS.click()

if uom == 'EA':
    UOM_EA = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[1]/div[4]/form/div[2]/div/div[1]/div/div/div[2]/table/tbody/tr[3]'))
    )

    # click the element
    UOM_EA.click()

if uom == 'KG':
    UOM_KG = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[1]/div[4]/form/div[2]/div/div[1]/div/div/div[2]/table/tbody/tr[4]'))
    )

