from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def check_exchange(coins_and_tokens):
    coins = coins_and_tokens[0]
    tokens = coins_and_tokens[1]

    for i in range(len(coins)):
        search = "coinbuddy" + " " + coins[i] + " " + tokens[i]
        google_coin_coinbuddy(search)

def google_coin_coinbuddy(search):
    # open coin_buddy
    driver = webdriver.Chrome()
    driver.get("https://www.bing.com/")
    search_bar = driver.find_element_by_name("q")
    search_bar.clear()
    search_bar.send_keys(search)
    search_bar.send_keys(Keys.RETURN)



check_exchange([['BadgerDAO', 'Rarible'], ['BADGER', 'RARI']])