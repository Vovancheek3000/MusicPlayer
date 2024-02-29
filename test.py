class Music:
    def __init__(self, title):
        self.title = title

class Player:
    def __init__(self):
        self.music_list = []

    def add_music(self, music):
        self.music_list.append(music)

    def delete_music(self, music):
        if music in self.music_list:
            self.music_list.remove(music)
            print(f"{music.title} has been deleted.")
        else:
            print(f"{music.title} is not in the list.")

    def play_music(self):
        for music in self.music_list:
            print(f"Now playing: {music.title}")

music1 = Music("Lalala")
music2 = Music("Believer")
music3 = Music("Vovan")

player = Player()

player.add_music(music1)
player.add_music(music2)
player.add_music(music3)

player.play_music()

player.delete_music(music2)

player.play_music()

