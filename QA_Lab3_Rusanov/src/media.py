## @file media.py
#  @brief Модели аудиозаписей раздела «Музыка».
#
#  Иерархия классов (три уровня):
#  @dot
#  digraph Hierarchy {
#      rankdir=BT;
#      node [shape=box, style=filled, fillcolor="#e8f0fe", fontname="Arial"];
#      AudioTrack -> MediaItem;
#      Song       -> AudioTrack;
#      Podcast    -> AudioTrack;
#  }
#  @enddot

import math


## @brief Базовый класс любого медиаобъекта.
#
#  Хранит общие для всех записей данные: идентификатор, название
#  и длительность. Напрямую не используется — от него наследуются
#  конкретные виды записей.
class MediaItem:

    ## @brief Создаёт медиаобъект.
    #  @param item_id  Уникальный идентификатор записи.
    #  @param title    Название записи.
    #  @param duration Длительность в секундах (должна быть > 0).
    #  @exception ValueError Если длительность не положительная.
    def __init__(self, item_id, title, duration):
        if duration <= 0:
            raise ValueError("Длительность должна быть больше нуля")
        self.item_id = item_id
        self.title = title
        self.duration = duration

    ## @brief Возвращает длительность в формате «м:сс».
    #  @return Строка вида "3:05".
    def duration_str(self):
        minutes, seconds = divmod(self.duration, 60)
        return f"{minutes}:{seconds:02d}"

    ## @brief Краткое текстовое описание записи.
    #  @return Строка для вывода в списке.
    def describe(self):
        return f"{self.title} ({self.duration_str()})"


## @brief Аудиозапись с исполнителем и статистикой прослушиваний.
#
#  Второй уровень иерархии. Добавляет автора, количество
#  прослушиваний и лайков, а также рейтинг популярности.
class AudioTrack(MediaItem):

    ## @brief Создаёт аудиозапись.
    #  @param item_id  Идентификатор.
    #  @param title    Название.
    #  @param duration Длительность в секундах.
    #  @param author   Исполнитель или автор.
    def __init__(self, item_id, title, duration, author):
        super().__init__(item_id, title, duration)
        self.author = author
        self.plays = 0
        self.likes = 0

    ## @brief Отмечает одно прослушивание записи.
    def play(self):
        self.plays += 1

    ## @brief Ставит записи «лайк».
    def like(self):
        self.likes += 1

    ## @brief Вычисляет рейтинг популярности записи.
    #
    #  Рейтинг учитывает долю лайков и общее число прослушиваний:
    #  \f[
    #      P = \frac{L}{N + 1} \cdot \log_{10}(N + 1) \cdot 100
    #  \f]
    #  где \f$L\f$ — количество лайков, \f$N\f$ — количество прослушиваний.
    #
    #  @return Рейтинг \f$P \ge 0\f$ (чем больше, тем популярнее).
    def popularity(self):
        # +1 защищает от деления на ноль и log10(0) у новой записи
        n = self.plays + 1
        return self.likes / n * math.log10(n) * 100

    ## @brief Описание с указанием автора.
    #  @return Строка «Автор — Название (м:сс)».
    def describe(self):
        return f"{self.author} — {super().describe()}"


## @brief Музыкальная композиция.
#
#  Третий уровень иерархии: AudioTrack с альбомом и жанром.
class Song(AudioTrack):

    ## @brief Создаёт песню.
    #  @param item_id  Идентификатор.
    #  @param title    Название песни.
    #  @param duration Длительность в секундах.
    #  @param artist   Исполнитель.
    #  @param genre    Жанр (например, "рок").
    #  @param album    Название альбома (может отсутствовать).
    def __init__(self, item_id, title, duration, artist, genre, album=None):
        super().__init__(item_id, title, duration, artist)
        self.genre = genre
        self.album = album

    ## @brief Описание песни с жанром.
    #  @return Строка для вывода в списке.
    def describe(self):
        return f"{super().describe()} [{self.genre}]"


## @brief Выпуск подкаста.
#
#  Третий уровень иерархии: AudioTrack с номером выпуска.
class Podcast(AudioTrack):

    ## @brief Создаёт выпуск подкаста.
    #  @param item_id  Идентификатор.
    #  @param title    Название выпуска.
    #  @param duration Длительность в секундах.
    #  @param host     Ведущий подкаста.
    #  @param episode  Номер выпуска.
    def __init__(self, item_id, title, duration, host, episode):
        super().__init__(item_id, title, duration, host)
        self.episode = episode

    ## @brief Описание выпуска с номером.
    #  @return Строка для вывода в списке.
    def describe(self):
        return f"#{self.episode} {super().describe()}"
