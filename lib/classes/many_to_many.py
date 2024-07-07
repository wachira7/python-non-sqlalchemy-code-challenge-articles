# Author Class
class Author:
    def __init__(self, name):
        # Validate that name is a non-empty string
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
        self._articles = []  # Initialize an empty list for articles

    @property
    def name(self):
        return self._name  # Return the name of the author

    def articles(self):
        return self._articles  # Return the list of articles by the author

    def magazines(self):
        # Return a unique list of magazines the author has contributed to
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        # Create a new article and return it (the article is added to the author's list within the Article class)
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        # Return a unique list of topic areas (magazine categories) the author has written about
        return list(set(article.magazine.category for article in self._articles))

# Magazine Class
class Magazine:
    def __init__(self, name, category):
        # Validation of name and category 
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        self._articles = []  # Initialize an empty list for articles

    # Existing properties and methods (unchanged)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        from collections import Counter
        author_count = Counter(article.author for article in self._articles)
        result = [author for author, count in author_count.items() if count > 2]
        return result if result else None

    # New method to implement
    @classmethod
    def top_publisher(cls):
        # Count articles per magazine using a Counter
        from collections import Counter
        article_count = Counter(article.magazine for article in Article.all)
        
        if not article_count:
            return None
        
        # Find the magazine with the maximum article count
        top_magazine = max(article_count, key=article_count.get)
        return top_magazine

# Article Class
class Article:
    all = []  # Class variable to store all articles

    def __init__(self, author, magazine, title):
        # Validate author, magazine, and title
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._author = author
        self._magazine = magazine
        self._title = title
        # Add the article to the author's and magazine's list of articles
        author._articles.append(self)
        magazine._articles.append(self)
        # Add the article to the class variable 'all'
        Article.all.append(self)

    @property
    def title(self):
        return self._title  # Return the title of the article

    @property
    def author(self):
        return self._author  # Return the author of the article

    @author.setter
    def author(self, value):
        # Validate and set the author of the article
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine  # Return the magazine of the article

    @magazine.setter
    def magazine(self, value):
        # Validate and set the magazine of the article
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        self._magazine = value
