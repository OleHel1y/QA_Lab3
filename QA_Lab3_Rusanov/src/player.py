## @file player.py
#  @brief Проигрыватель плейлиста.


## @brief Проигрыватель, воспроизводящий плейлист.
#
#  Работает как конечный автомат с тремя состояниями:
#  @dot
#  digraph PlayerStates {
#      rankdir=LR;
#      node [shape=ellipse, style=filled, fillcolor="#d2e3fc", fontname="Arial"];
#      STOPPED -> PLAYING [label="play()"];
#      PLAYING -> PAUSED  [label="pause()"];
#      PAUSED  -> PLAYING [label="play()"];
#      PLAYING -> STOPPED [label="stop() / конец плейлиста"];
#      PAUSED  -> STOPPED [label="stop()"];
#      PLAYING -> PLAYING [label="next()"];
#  }
#  @enddot
#
#  Логотип раздела:
#  @image html logo.png "Раздел «Музыка»" width=200px
class Player:

    STOPPED = "STOPPED"  ##< Ничего не играет
    PLAYING = "PLAYING"  ##< Идёт воспроизведение
    PAUSED = "PAUSED"    ##< Воспроизведение на паузе

    ## @brief Создаёт проигрыватель для плейлиста.
    #  @param playlist Объект Playlist.
    def __init__(self, playlist):
        self.playlist = playlist
        self.index = 0
        self.state = Player.STOPPED

    ## @brief Текущая запись.
    #  @return AudioTrack или None, если плейлист пуст.
    def current(self):
        if not self.playlist.tracks:
            return None
        return self.playlist.tracks[self.index]

    ## @brief Начинает или продолжает воспроизведение.
    #  @return True, если воспроизведение началось.
    def play(self):
        track = self.current()
        if track is None:
            return False
        # Прослушивание засчитываем только при старте, а не после паузы
        if self.state == Player.STOPPED:
            track.play()
        self.state = Player.PLAYING
        return True

    ## @brief Ставит воспроизведение на паузу.
    def pause(self):
        if self.state == Player.PLAYING:
            self.state = Player.PAUSED

    ## @brief Останавливает воспроизведение и возвращается к началу.
    def stop(self):
        self.state = Player.STOPPED
        self.index = 0

    ## @brief Переходит к следующей записи.
    #  @return Следующая запись или None, если плейлист закончился.
    def next(self):
        if self.index + 1 >= len(self.playlist):
            self.stop()
            return None
        self.index += 1
        track = self.current()
        if self.state == Player.PLAYING:
            track.play()
        return track
