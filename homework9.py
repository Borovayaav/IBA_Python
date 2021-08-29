class Book:
    __year = 0
    __page = 0
    __price = 0
    __pubhouse = ' '
    __cover= ' '
    __author = ' '
    __title = ' '


    def __init__(self,year0,page0,price0,pubhouse0,cover0,author0,title0  ):
        self.__year = year0
        self.__page = page0
        self.__price = price0
        self.__pubhouse = pubhouse0
        self.__cover = cover0
        self.__author = author0
        self.__title = title0
    print("A book")

    def get_year(self):
        return self.__year
    def get_page(self):
        return self.__page
    def get_price(self):
        return self.__price
    def get_pubhouse(self):
        return self.__pubhouse
    def get_cover(self):
        return self.__cover
    def get_author(self):
        return self.__author
    def get_title(self):
        return self.__title

def AboutBook(i):
    print('Author name: ' + elib[i].get_author())
    print('Book name: ' + elib[i].get_title())
    print('Book year: ' + str(elib[i].get_year()))
    print('---------------')

i=0
elib = [Book(2018, 205, 1, 'Avanta', 'hard', 'Hromyko', 'Witch fairy tale'),
    Book(2015, 618, 73, 'AST', 'hard', 'Larson', 'Girl with dragon tatoo'),
    Book(2011, 334, 91, 'Makhaon', 'flex', 'Rowling', 'Harry Potter'),
    Book(2021, 105, 19, 'Aversev', 'flex', 'Andrews', 'Flowers on the roof'),
    Book(2015, 603, 35, 'Exsmo', 'hard', 'Ridth', 'Generation X'),
    Book(2004, 814, 100, 'Czarna owca', 'hard', 'Asher', '13 reason why'),
    Book(2017, 672, 29, 'Makhaon', 'hard', 'Patterson', 'First to die'),
    Book(2001, 501, 41, 'Czarna owca', 'hard', 'Dekker', 'Tree'),
    Book(2003, 472, 31, 'Aversev', 'hard', 'Evanovich', 'One for the money'),
    Book(2004, 315, 50, 'Makhaon', 'flex', 'Clark', 'The Cinderella murder'),
    Book(2005, 934, 29, 'Czarna owca', 'hard', 'Roach', 'Stiff'),
    Book(2004, 811, 70, 'Exsmo', 'hard', 'Morrison', 'Beloved'),
    Book(2001, 191, 30, 'Aversev', 'flex', 'Dunkan', 'I,Lucifer')]

authorname = ' '
issueyear = 0

issueyear = int(input('Введите год выпуска:\n'))
while i < len(elib):
    if elib[i].get_year() >= issueyear:
        AboutBook(i)
    i+=1
i=0
authorname = (input('Какого автора книги Вы ищите?:\n'))
while i < len(elib):
    if elib[i].get_author() == authorname:
        AboutBook(i)
    i+=1