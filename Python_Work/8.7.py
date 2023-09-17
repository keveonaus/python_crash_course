def make_album(artist_name, album_title, songs=None):
    """Putting together album information"""
    album_info = {'artist': artist_name, 'title': album_title}
    if songs:
        album_info['songs'] = songs
    return album_info

while True:
    print("\nPlease give me an artists name and an album they made.")
    print("(enter 'q' to quit)")

    artist = input("Artist's name: ")
    if artist == 'q':
        break

    title = input("A album title they made: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)