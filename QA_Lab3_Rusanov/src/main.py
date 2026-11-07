## @file main.py
#  @brief Точка входа: демонстрация работы раздела «Музыка».

from media import Song, Podcast
from playlist import Playlist
from player import Player
from library import MusicLibrary


## @brief Заполняет библиотеку тестовыми данными и показывает работу классов.
def main():
    lib = MusicLibrary("Олег Русанов")
    songs = [
        Song(1, "Кукла колдуна", 203, "Король и Шут", "рок"),
        Song(2, "Группа крови", 286, "Кино", "рок"),
        Song(3, "Blinding Lights", 200, "The Weeknd", "поп"),
        Song(4, "Звезда по имени Солнце", 225, "Кино", "рок"),
    ]
    podcast = Podcast(5, "Как устроен ВК", 1820, "Tech Talk", episode=12)
    for item in songs + [podcast]:
        lib.add_item(item)

    pl = Playlist("Для учёбы")
    for item in songs:
        pl.add(item)
    lib.add_playlist(pl)

    player = Player(pl)
    player.play()
    player.next()
    player.next()
    songs[1].like()
    songs[2].like()
    songs[2].like()

    print(f"Плейлист «{pl.name}»: {len(pl)} трека, {pl.total_duration() // 60} мин.")
    print("Сейчас играет:", player.current().describe())
    print("Поиск «кино»:", [s.title for s in lib.search("кино")])
    print("Топ:", [s.title for s in lib.top(2)])
    print("Похожие на «Группа крови»:", [s.title for s in lib.recommend(songs[1])])
    print("Подкаст:", podcast.describe())


if __name__ == "__main__":
    main()
