class MediaPlayer:
    def open(self, file):
        self.filename = file

    def play(self):
        print(f'Воспроизведение{self.filename}')


media1 = MediaPlayer()
media2 = MediaPlayer()
media1.open('filemedia')
media2.open('filemedia')
