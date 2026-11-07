## @file library.py
#  @brief Музыкальная библиотека пользователя.

from media import Song


## @brief Библиотека «Моя музыка»: хранит записи и плейлисты.
class MusicLibrary:

    ## @brief Создаёт пустую библиотеку.
    #  @param owner Имя владельца страницы.
    def __init__(self, owner):
        self.owner = owner
        self.items = []
        self.playlists = []

    ## @brief Добавляет запись в библиотеку.
    #  @param item Объект AudioTrack (Song или Podcast).
    def add_item(self, item):
        self.items.append(item)

    ## @brief Добавляет плейлист в библиотеку.
    #  @param playlist Объект Playlist.
    def add_playlist(self, playlist):
        self.playlists.append(playlist)

    ## @brief Ищет записи по названию или автору без учёта регистра.
    #  @param query Строка поиска.
    #  @return Список найденных записей.
    def search(self, query):
        q = query.lower()
        return [i for i in self.items
                if q in i.title.lower() or q in i.author.lower()]

    ## @brief Возвращает самые популярные записи.
    #  @param n Сколько записей вернуть.
    #  @return Список длиной не более n, отсортированный по AudioTrack::popularity.
    def top(self, n=3):
        return sorted(self.items, key=lambda i: i.popularity(), reverse=True)[:n]

    ## @brief Рекомендует песни того же жанра, что и указанная.
    #  @param song Песня-образец.
    #  @return Список песен того же жанра, кроме самой песни.
    def recommend(self, song):
        # Подкасты не рекомендуем — у них нет жанра
        return [i for i in self.items
                if isinstance(i, Song) and i.genre == song.genre and i is not song]
