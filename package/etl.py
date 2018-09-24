from package.model import President, Article, Keyword, ArticleKeyword
from package.obama_data import obama_data
from package.trump_data import trump_data
from package import db
from ast import literal_eval as make_tuple


def make_presidents():
    barack = President(name='Obama')
    db.session.add(barack)
    donald = President(name='Trump')
    db.session.add(donald)
    db.session.commit()
#barack = President(name='Obama')
#donald = President(name='Trump')

def make_articles(articles):
    for article in articles:
        if article['president_id']==1:
            president=db.session.query(President).filter_by(name='Obama').first()
        else:
            president=db.session.query(President).filter_by(name='Trump').first()
        db.session.add(Article(date=article['date'], headline=article['headline'], president_id=president.id, nyt_id=article['id'], url=article['url'], word_count=article['word_count'], section=article['section']))
    db.session.commit()

#def find_or_create():


def make_keywords(articles):
    # articles
    for article in articles:
        # tuple ('category', 'oil crisis')
        # for cateory, name in
        for tple in make_tuple(article['keywords']):
            if article['president_id']==1:
                president=db.session.query(President).filter_by(name='Obama').first()
            else:
                president=db.session.query(President).filter_by(name='Trump').first()
            keyword = Keyword(category=tple[0], value=tple[1], president_id=president.id)
            db.session.add(keyword)
            artkey= ArticleKeyword(article_id=article['id'], keyword_id=keyword.id)
            db.session.add(artkey)
    db.session.commit()
            # if keyword does not exist create it
                # keyword = Keyword.query.filter_by(name=keyword_name)
                # article = Article.query.filter_by(nyt_id)
            # KeywordArticle(keyword_id=keyword.id, )
    #     db.session.add(Keyword())
    # db.session.commit()
# def make_all():
#     make_presidents()
#     make_articles(obama_data)
#     make_articles(trump_data)
#     make_keywords(obama_data)
#     make_keywords(trump_data)
