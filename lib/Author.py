from Article import Article


# Initializing author attributes
class Author:
    def __init__(self, name):
        self._name = name
        self._article = []

    # getter for authors name
    @property
    def name(self):
        return self._name
    
    # list of Article instances the author has written
    @property
    def articles(self):
        return self._article

    # **unique** list of Magazine instances for which the author has contributed to
    def magazine(self):
        pk_magazines = set()
        for article in self._article:
            pk_magazines.add(article.magazine())
        return list(pk_magazines)

    # Creates a new Article instance and associates it with that author and that magazine.
    def article_instance(self, magazine, title):
        article = Article(self, magazine, title)
        self._article.append(article)
    
    #  **unique** list of strings with the categories of the magazines the author has contributed to
    def topic_areas(self):
        pk_mag_categories = set()
        for article in self._article:
            pk_mag_categories.add(article.magazine().category())
        return list(pk_mag_categories)



mitch = Author("Tefflon")
print(mitch.name)
