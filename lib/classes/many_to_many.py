class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title
        
    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            return
        if not isinstance(value, str):
            return
        if not 5 <= len(value) <= 50:
            return
        self._title = value
        
    @property
    def author(self):
        return self._author
        
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            return
        self._author = value
        
    @property
    def magazine(self):
        return self._magazine
        
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            return
        self._magazine = value
        
        
class Author:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            return
        if not isinstance(value, str):
            return
        if len(value) == 0:
            return
        self._name = value
        
    def articles(self):
        return [article for article in Article.all if article.author == self]
        
    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))
        
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
        
    def topic_areas(self):
        if not self.articles():
            return None
        return list(set([article.magazine.category for article in self.articles()]))
        

class Magazine:
    all = []
    
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            return
        if not 2 <= len(value) <= 16:
            return
        self._name = value
        
    @property
    def category(self):
        return self._category
        
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            return
        if len(value) == 0:
            return
        self._category = value
        
    def articles(self):
        return [article for article in Article.all if article.magazine == self]
        
    def contributors(self):
        return list(set([article.author for article in self.articles()]))
        
    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]
        
    def contributing_authors(self):
        authors = {}
        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1
        
        result = [author for author, count in authors.items() if count > 2]
        return result if result else None
        
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
            
        magazine_counts = {}
        for article in Article.all:
            if article.magazine in magazine_counts:
                magazine_counts[article.magazine] += 1
            else:
                magazine_counts[article.magazine] = 1
                
        if not magazine_counts:
            return None
            
        return max(magazine_counts, key=magazine_counts.get)
