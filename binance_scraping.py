from selenium import webdriver
from datetime import datetime
import pytz
from playsound import playsound

def get_current_time():
    # get current time to check against newest listing of binance
    tz_NY = pytz.timezone('America/New_York')
    datetime_NY = datetime.now(tz_NY)
    date_ny = (str(datetime_NY)[:16])

    return date_ny
    """
    tz_London = pytz.timezone('Europe/London')
    datetime_London = datetime.now(tz_London)
    print("London time:", datetime_London.strftime("%H:%M:%S"))
    """

def check_binance_coin_listing():
    # Version 13.10.2021
    # open chrome driver and binance listing announcement page
    driver = webdriver.Chrome()
    driver.get("https://www.binance.com/en/support/announcement/c-48?navId=48")

    # Every news has an id link-0-i-p1 on binance announcement page
    counter = 0
    coin_announcement = ""
    while ("Binance Will List") not in coin_announcement:  # iterate through binance
        id = "link-0-" + str(counter) +"-p1"
        newest_coin = driver.find_element_by_id(id)
        coin_announcement = newest_coin.text
        counter += 1
    # get index of parentheses for coin name
    start = 0
    end = 0
    # iterate through listing announcement to find newest coin
    for i,letter in enumerate(coin_announcement):
        if letter == "(" :
            start = i
        elif letter == ")":
            end = i

    link = newest_coin.get_attribute("href")
    coin = coin_announcement[start+1:end]


    # get release date of listing announcement
    newest_coin.click()
    time_binance = driver.find_element_by_class_name("css-17s7mnd").text
    time_now = get_current_time()
    #print("THE NEWEST COIN IS:" , coin, "it's announcement was on ", time_binance)
    buy = False
    # 1. ) Check if it was released today
    if(time_binance[:10]) == (time_now[:10]):
        # 2.) case 1 : same hour and max 3 min difference
        if (time_binance[11:13]) == (time_now[11:13]):  # same hour ?
            if time_binance[14:] == time_now[14:]:
                buy = True
        # 2.) case 2 : not same hour but still only max 3 min difference
        if int(time_now[11:13]) - (int(time_binance[11:13])) == 1:  # only 1 hour ago
            # how many minutes from hour away did binance post
            minutes_away_from_hour_binance = abs(int(time_binance[14:]) - 60) # 16:59 will be 1 minute away from 17
            minutes_into_hour_now = time_now[14:] # minutes from 17 away now
            if minutes_away_from_hour_binance + minutes_into_hour_now <= 4:  # sum of both distances from 17 should be smaller 4
                buy = True

    driver.close()
    buy_coin(coin, buy)

    return coin

def buy_coin(coin, buy):
    a = "UNCOMMENT IF NEEDED"
    #if buy:
        #print("LETS BUY: " , coin)
    #else:
        #print("ITS TOO LATE TO BUY: ", coin)


def main_binance():
    #coin = check_binance_coin_listing()
    coin = check_binance_coin_listing()

    while True:
        coin2 = check_binance_coin_listing()
        #coin2 = check_binance_coin_listing()
        if coin != coin2 :
            print("NE COIN: ", coin2)
            playsound("alarmme.mp3")
            while True:
                print("NEW COIN: ", coin2)
        else: print("OLD COIN: ", coin2)

main_binance()