import shelve, pathlib

file_path = pathlib.Path(__file__).parent.joinpath('shelftests', 'shelftest')
if not file_path.parent.exists():
    file_path.parent.mkdir()

# shelve的open不能放入pathlib的path object，只能放入str
with shelve.open(str(file_path)) as characters:
    characters['Lanner'] = "悲傷、無力的理想主義者"
    characters['Leah'] = "勇敢、堅強的太陽"
    characters['Ceitt'] = "悲慘、迷失的被遺棄者"
    characters['Leos'] = "憤怒、正義的騎士"
    
    print(characters['Lanner'])
    print(characters['Leos'])