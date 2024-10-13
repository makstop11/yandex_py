class MediaPlayer:
    def open(self, file):
        self.filename = file

    def play(self):
        print(f'Воспроизведение {self.filename}')
        # print('Воспроизведение ' + self.filename)
        # print('Воспроизведение', self.filename, 20)


media1 = MediaPlayer()
media2 = MediaPlayer()

disk_1 = 'TomAndJerry.mp4'
disk_2 = 'Smeshariki.mp4'

media1.open(file=disk_1)
media2.open(disk_2)

media1.play()
media2.play()
