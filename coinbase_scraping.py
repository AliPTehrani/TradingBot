from selenium import webdriver
from playsound import playsound


def check_coinbase_coin_listing():
    # Version 13.10.2021
    # open chrome driver and binance listing announcement page
    driver = webdriver.Chrome()
    driver.get("https://blog.coinbase.com/institutional-pro/home")
    driver.maximize_window()
    announcement = driver.find_element_by_class_name("u-letterSpacingTight u-lineHeightTighter u-breakWord u-textOverflowEllipsis u-lineClamp3 u-fontSize24")
    announcement.click()

check_coinbase_coin_listing()

