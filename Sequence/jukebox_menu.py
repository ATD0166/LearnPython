from nested_data import albums

SONG_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exit):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}, {}, {}".format(index + 1, title, artist, year))
        
    choice = int(input(">>"))
    if 1 <= choice <= len(albums):
        songs_list = albums[choice -1][SONG_LIST_INDEX]        
    else:
        break
    
    for track_number, song_title in songs_list:
        print("{}: {}".format(track_number, song_title))
    
    song_choice = int(input(">>"))
    if 1 <= song_choice <= len(songs_list):
        song = songs_list[song_choice -1][SONG_TITLE_INDEX]
        print("Playing {}...".format(song))
    
    print("=" * 40)
    
name = ['A', 'B']

    
    