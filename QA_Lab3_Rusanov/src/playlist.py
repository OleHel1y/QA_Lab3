## @file playlist.py
#  @brief Плейлисты пользователя.

import random


## @brief Плейлист — упорядоченный список аудиозаписей.
#
#  Одна и та же запись не может быть добавлена дважды.
class Playlist:

    ## @brief Создаёт пустой плейлист.
    #  @param name Название плейлиста.
    def __init__(self, name):
        self.name = name
        self.tracks = []

    ## @brief Добавляет запись в конец плейлиста.
    #  @param track Объект AudioTrack.
    #  @return True, если запись добавлена; False, если уже была в плейлисте.
    def add(self, track):
        if track in self.tracks:
            return False
        self.tracks.append(track)
        return True

    ## @brief Удаляет запись из плейлиста.
    #  @param track Удаляемая запись.
    #  @return True, если запись найдена и удалена.
    def remove(self, track):
        if track not in self.tracks:
            return False
        self.tracks.remove(track)
        return True

    ## @brief Суммарная длительность плейлиста.
    #  @return Длительность в секундах.
    def total_duration(self):
        return sum(t.duration for t in self.tracks)

    ## @brief Перемешивает порядок записей.
    #  @param seed Зерно генератора (для воспроизводимости в тестах).
    def shuffle(self, seed=None):
        random.Random(seed).shuffle(self.tracks)

    ## @brief Количество записей в плейлисте.
    #  @return Число записей.
    def __len__(self):
        return len(self.tracks)
