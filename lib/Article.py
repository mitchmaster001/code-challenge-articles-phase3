import weakref


class Article:
    # list to store all article instances
    article_instances = []

    # Initializing article attributes
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        self.__class__.article_instances.append(weakref.proxy(self))

    # Getter for article's title
    @property
    def title(self):
        return self._title

    # Getter for article's author
    @property
    def author(self):
        return self._author

    # Getter for article's magazine
    @property
    def magazine(self):
        return self._magazine


# Instances of Article
Power = Article("Mitch", "Parents", "This Power")
Power = Article("Morris", "Say", "This Yes")
print(Power)
print(Power.title)
print(Power.author)
print(Power.magazine)

# List of all Article Instances
for instance in Article.article_instances:
    print(Article.article_instances)