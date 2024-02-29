class Song:
    def __init__(self,title,author):
        self.title = title
        self.author = author



class Player:
    def __init__(self,song_list):
        self.__song_list = song_list
    def start (self):
        menu = self._menu()

    def _menu(self):
        meny = {
            1:'AddSong',
            2:'RemoveSong',
            3:'PlaySong'
        }
        print(f'Options\n'
              '1:AddSongs\n'
              '2:RemoveSongs\n'
              '3:PlaySong\n')
        option = input('What option do you want choose?')

        if option == 1:
            meny = meny.get(1)
        elif option == 2:
            meny = meny.get(2)
        elif option == 3:
            meny = meny.get(3)


        if meny == 'RemoveSongs':
            self._show_song()
            choice = self._get_choice()
            song = self.__song_list[choice]
            self._play(song)
    def delete_song(self, song):
        if song in self.__song_list:
            self.__song_list.remove(song)
            print(f"{song.title} has been deleted.")
        else:
            print(f"{song.title} is not in the list.")




    def _show_song(self):
        show_lines()
        for i, song in enumerate(self.__song_list):
            print(f"{i+1}. {song.title.ljust(10)} - {song.author}")
    def _get_choice(self):
        show_lines()
        choice = input("Which song do you want listen (number)?")
        try:
            choice = int(choice)
            if 0 > choice or len(self.__song_list)< choice:
                raise ValueError
        except ValueError:
            print('Your choice should be a number from song list.')
            choice = self._get_choice()
        return choice -1

    def _play(self,song):
        print(f"Now playing {song.title}")
def show_lines(n=20):
    print("."*n)

song_list = [
    Song("nightmares","skyfall"),
    Song("Lemon Boy","Cavetown&"),
    Song("Telescope","Cavetown"),
    Song("Everybody",'One Republic')
]


player = Player(song_list)
player.start()


