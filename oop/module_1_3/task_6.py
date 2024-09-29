class Notes:
    uid: int = 1005435  # unique id (identifier)
    title: str = 'Шутка'
    author: str = 'И.С.Бах'
    pages: int = 2


s = getattr(Notes, 'author')
print(s)

# s = Notes.author
# print(s)
