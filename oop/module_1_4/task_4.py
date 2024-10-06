class MediaPlayer:

    def open(self, file: str):
        self.filename = file

        return self.filename

    # TODO: доработать


mp_1 = MediaPlayer()
mp_1.open("video.mp4")
print(mp_1.__dict__)
