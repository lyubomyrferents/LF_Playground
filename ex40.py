class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
        # Use assertion to check type of variable
        assert isinstance(self.lyrics, (list, tuple)), "Wrong data for Song() initialization"
        assert not isinstance(self.lyrics, basestring), "Wrong data for Song() initialization"

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line, "!"


happy_bday = Song(("Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"))

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
print
bulls_on_parade.sing_me_a_song()
