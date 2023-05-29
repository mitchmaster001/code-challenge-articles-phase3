import weakref


# Initializing magazine class attributes
class Magazine():
    # List to store all magazine instances
    magazine_instances = []

    # Initializing magazine class attributes
    def __init__ (self, name, category):
        self._name = name
        self._category = category
        self.__class__.magazine_instances.append(weakref.proxy(self))
        self.article = []
        self._contributors = []


        
    # Getter for magazine name
    @property
    def name(self):
        return self._name 

    # Setter for magazine name
    @name.setter
    def name(self, value):
        self._name = value
        
    # Getter for magazine category
    @property
    def category(self):
        return self._category

    # Setter for magazine category
    @category.setter
    def category(self, value):
        self._category = value

    @classmethod
    def all(cls):
        return cls.magazine_instances

    # list of Author instances who have written for this magazine
    def add_contributor(self, author):
        self._contributors.append(author)
    
    # Given a string of magazine's name, this method returns the first magazine object that matches
    @classmethod
    def find_by_name(cls, name):
        for magazine in cls.magazine_instances:
            if magazine.name() == name:
                return magazine
        return None

    # Returns an list strings of the titles of all articles written for that magazine        # 
    @classmethod
    def article_titles(cls):
        titles = []
        for magazine in cls.magazine_instances:
            for article in magazine.articles():
                titles.append(article.title())
        return titles

    # Returns an list of authors who have written more than 2 articles for the magazine
    def contributing_authors(self):
        author_counts = {}
        for article in self.article:
            author = article.author()
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        return [author for author, count in author_counts.items() if count > 2]

# Magazine magazine_instances
power = Magazine("Influence", "Control")

faith = Magazine("Dominance", "Knowledge")
# print(power.name)
power.name = "Hope"
print(power.name)

# print(love.category)
power.category = "Sports"
print(power.category)


# List of all Magazine magazine_instances
for instance in Magazine.magazine_instances:
    # print(instance.name)
    # print(instance.category)
    print(Magazine.magazine_instances)





