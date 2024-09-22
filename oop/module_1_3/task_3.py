class DataBase:
    pk: int = 1
    title: str = "Классы и объекты"
    author: str = "Максим"
    views: int = 99999
    comments: int = 100


print(DataBase.__dict__)
