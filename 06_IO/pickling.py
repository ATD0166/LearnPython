import pickle, pathlib

file_name = 'sample.pickle'
file_path = pathlib.Path(__file__).parent.joinpath(file_name)

imelda = ('More Mayhem',
          'IMelda May',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))

# dump = 寫入pickle
with open(file_path, 'bw') as pickle_file:
    pickle.dump(imelda, pickle_file)
    pickle.dump('Hello world', pickle_file)

# load = 讀取pickle
with open(file_path, 'br') as imelda_pickled:
    # imelda_copy = pickle.load(imelda_pickled)
    imelda_copy = pickle.load(imelda_pickled)
    normal_str = pickle.load(imelda_pickled)
    
album, artist, year, tracks = imelda_copy
print(album)
print(artist)
print(year)
for num, song in tracks:
    print(f"{num} - {song}")

print('*' * 40)
print(normal_str)
