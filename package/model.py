from package import db

class President(db.Model):
    __tablename__='presidents'
    id=db.Column(db.Integer, primary_key=True )
    name=db.Column(db.Text)
    articles=db.relationship('Article', back_populates="president")
    article_id=db.Column(db.Integer, db.ForeignKey('articles.id'))
    #a president can have many articles
    keywords=db.relationship('Keyword', back_populates='president')
    keyword_id=db.Column(db.Integer, db.ForeignKey('keywords.id'))
    #a president can have many keywords
#    sections=db.relationship('Keyword', back_populates='presidents', lazy='dynamic')

class Article(db.Model):
    __tablename__='articles'
    id=db.Column(db.Integer, primary_key=True )
    headline=db.Column(db.Text)
    url = db.Column(db.String)
    nyt_id = db.Column(db.String)
    president_id = db.Column(db.Integer)
    word_count = db.Column(db.Integer)
    section=db.Column(db.Text)
#    num_hits=db.Column(db.Integer)
    date=db.Column(db.String)
    president=db.relationship('President', back_populates='articles')
#    section=db.relationship('Section', back_populates='articles', lazy='dynamic')
    #an article can only be in one section
    keywords=db.relationship('Keyword', secondary='articlekeywords')

    #an article could have many keywords
    def to_dict(self):
        article={'id': self.id, 'headline': self.headline, 'url':self.url, 'nyt_id': self.nyt_id,  'word_count': self.word_count, 'num_hits': self.num_hits, 'date': self.date, 'section': self.section.section_name
        # ,'keywords': [keyword.to_dict() for keyword in self.keywords]
        }
        return article

class Keyword (db.Model):
    __tablename__='keywords'
    id=db.Column(db.Integer, primary_key=True )
    category= db.Column(db.Text)
    value=db.Column(db.Text)
    # article_id=db.Column(db.String)
    # articles=db.relationship('Article', back_populates='keywords')
    president_id = db.Column(db.Integer)
    president=db.relationship('President', back_populates='keywords')
    article=db.relationship('Article', secondary='articlekeywords')

    #many to many, an article could have many keywords, and one keyword can only be tag once in an article
    # def to_dict(self):
    #     keyword={'id': self.id, 'word': self.word, 'articles':[articles.to_dict() for article in self.articles]}
    #     return keyword

class ArticleKeyword(db.Model):
    __tablename__='articlekeywords'
    id=db.Column(db.Integer, primary_key=True )
    article_id=db.Column(db.Integer, db.ForeignKey('articles.nyt_id'))
    keyword_id=db.Column(db.Integer, db.ForeignKey('keywords.id'))
    # article=db.relationship('Article', backref="articlekeywords", cascade='all, delete-orphan', single_parent=True)
    # keyword=db.relationship('Keyword', backref="articlekeywords", cascade='all, delete-orphan', single_parent=True)
    article=db.relationship('Article', backref="articlekeywords")
    keyword=db.relationship('Keyword', backref="articlekeywords")


# class Section(db.Model):
#     __tablename__='sections'
#     id=db.Column(db.Integer, primary_key=True)
#     type_of_material=db.Column(db.Text)
#     rank=db.Column(db.Integer)
#     articles=db.relationship('Article', back_populates='sections')
    #a article can only be in one section

db.create_all()
