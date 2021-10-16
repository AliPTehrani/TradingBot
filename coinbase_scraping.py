from selenium import webdriver
from selenium.webdriver.common.by import By


def check_coinbase_coin_listing():
    """
    Open blog page from Coinbase and check what newest coin/ coins were listed

    :return: coins : coins that were last listed by coinbase
    """

    # open coinbase
    driver = webdriver.Chrome()
    driver.get("https://blog.coinbase.com/institutional-pro/home")

    # Get all elements on page
    listOfElements = driver.find_elements_by_xpath("//div");

    # iterate through all elements and find first element that is about a listing
    for element in listOfElements:
        # <= 200 because there is an element that has the whole homepage and therefore also the launching
        if ("are launching on Coinbase Pro" in element.text) and (len(element.text) <= 200):
            break

        if (("is launching on Coinbase Pro") in element.text) and (len(element.text) <= 200):
            break

    # extract coins from announcement string
    coins = []
    announcement = element.text
    words = announcement.split()
    word_blacklist = ["and","are", "is" ,"launching", "on", "Coinbase", "Pro"]

    # get all coin names and tokens
    coins = []
    tokens = []
    for word in words:
        if word not in word_blacklist:
            if ("(" in word) and (")" in word):
                tokens.append(word[1:-1])
            else:
                coins.append(word)

    # add coin names if they are cut beacause of space
        if len(coins) != len(tokens): # some coin name was splitted
            concat_coin = False
            new_coin = ""
            new_coins = []
            for word in words:
                if (word in coins) and (not concat_coin):
                    new_coin = word
                    concat_coin = True
                elif (word in coins) and concat_coin:
                    new_coin += " " + word
                elif word[0] == "(" :
                    new_coins.append(new_coin)
                    new_coin = ""
                    concat_coin = False
            coins = new_coins


    """
    add_char = False
    coin = ""
    for char in announcement:
        if char == "(":
            add_char = True
        elif char == ")":
            add_char = False
            coins.append(coin)
            coin = ""
        elif add_char:
            coin += char
    """

    driver.close()
    return [coins, tokens]

def main_coinbase_checking():
    coins = check_coinbase_coin_listing()
    while True:
        coins2 = check_coinbase_coin_listing()
        if coins != coins2:
            print("NEW COIN LISTING ON COINBASE", print(coins2))
            break
        else:
            print("OLD COINS ON COINBASE", coins)

main_coinbase_checking()