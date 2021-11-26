import datetime as dt
from calendar import monthrange
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class Spotify_Playlist_Creator:
    def __init__(self, URL=str):
        self.URL = URL
        self.top100 = []

    def __str__(self):
        return self.URL

    def Start(self):
        program = Spotify_Playlist_Creator()
        program.Inputting_Data()
        program.Importing_Data_From_URL(URL=program.URL, top100=program.top100)
        program.Connecting_With_Spotify()

    def Inputting_Data(self):
        """Console and handling with errors"""
        global length_of_month

        UserInput = input("Input a date like YYYY-MM-DD: ").rsplit("-")

        #Checking if month and day is not null
        if UserInput[1] and UserInput[2] != 0:
            length_of_month = monthrange(int(UserInput[0]), int(UserInput[1]))[1]
        else:
            print("You didn't type month or day. Please try again")

        #Verificate Data from UserInput
        if int(UserInput[0]) > dt.datetime.now().year or int(UserInput[1]) > 12 or int(UserInput[2]) > int(length_of_month):
            print("Your input was wrong, try again with correct Data Time")
        else:
            print("Everything is okay! I am going to next step!")

            #Returning the right URL to work with it
            self.URL = f"https://www.billboard.com/charts/hot-100/{UserInput[0]}-{UserInput[1]}-{UserInput[2]}/"
            # print(f"Link to work: {self.URL}")
            return self.URL

    def Importing_Data_From_URL(self, URL, top100):
        # self.song_name : str

        #Connecting to URL with Requests
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, "html.parser")

        #Using Beatifull soup to get songs name
        songs = soup.find_all("h3",
                              class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size"
                                     "-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max "
                                     "a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only",
                              id="title-of-a-story")

        first_song = soup.find("h3", class_="c-title a-font-primary-bold-l a-font-primary-bold-m@mobile-max "
                                            "lrv-u-color-black u-color-white@mobile-max lrv-u-margin-r-150",
                               id="")

        first_song_text = first_song.get_text().replace("\n", "")
        top100.append(first_song_text)

        for song in songs:
            title = song.get_text().replace("\n", "")
            top100.append(title)

        # print(top100, "\n", len(top100))

    def Connecting_With_Spotify(self):
        #TODO Connecting with Spotify API to create a Playlist with title values (top100 variable)

        CLIENTID = "5048455b249843b1a3949af560d29f3a"
        CLIENTSECRET = "133760dbb7704ab2ab35fcef5e13636f"

        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENTID,
                                                                   client_secret=CLIENTSECRET))

        # results = sp.search(q='weezer', limit=20)
        # for idx, track in enumerate(results['tracks']['items']):
        #     print(idx, track['name'])


