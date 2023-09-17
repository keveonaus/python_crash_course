def make_album(artist_name, album_title, songs=None):
    """Putting together album information"""
    album_info = {'artist': artist_name, 'title': album_title}
    if songs:
        album_info['songs'] = songs
    return album_info

album = make_album('the killers', 'hot fuss', songs=12)
print(album)

album = make_album('avicii', 'true')
print(album)

album = make_album('kanye west', 'the college dropout')
print(album)