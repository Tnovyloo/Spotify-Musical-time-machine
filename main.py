import datetime as dt
from calendar import monthrange
from bs4 import BeautifulSoup
import requests


##Console and hnadling with errors
input = input("Input a date like YYYY-MM-DD: ").rsplit("-")


length_of_month = monthrange(int(input[0]), int(input[1]))[1]


if int(input[0]) > dt.datetime.now().year or int(input[1]) > 12 or int(input[2]) > int(length_of_month):
    print("Your input was wrong, try again")

else:
    print("Everything is okay")

##After handling with uncorrect inputs we have right link to working with it via BS4
URL = f"https://www.billboard.com/charts/hot-100/{input[0]}-{input[1]}-{input[2]}/"

response = requests.get(URL)
page = response.text

soup = BeautifulSoup(page, "html.parser")
print(soup)

#TODO From BS4 we have to get into (class="o-chart-results-list-row-container") and download title values



#TODO Connecting with Spotify API to create a Playlist with title values