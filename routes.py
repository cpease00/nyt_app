from package.model import President, Article, Keyword, ArticleKeyword
from package import db
from sqlalchemy import func

def return_total_article_count_by_president(id):
    return len(db.session.query(Article).filter_by(president_id=id).all())

def return_monthly_article_counts_by_pres(id):
    monthly_totals = []
    articles = db.session.query(Article.date).filter_by(president_id=id).order_by(Article.date).all()
    if id == 1:
        months = ['2008-08','2008-09','2008-10','2008-11','2008-12','2009-01','2009-02','2009-03','2009-04','2009-05','2009-06','2009-07','2009-08','2009-09','2009-10','2009-11','2009-12','2010-01','2010-02','2010-03','2010-04','2010-05','2010-06','2010-07']
    else:
        months = ['2016-08','2016-09','2016-10','2016-11','2016-12','2017-01','2017-02','2017-03','2017-04','2017-05','2017-06','2017-07','2017-08','2017-09','2017-10','2017-11','2017-12','2018-01','2018-02','2018-03','2018-04','2018-05','2018-06','2018-07']
    for month in months:
        count = 0
        for i in articles:
            if (str(i)[2:9]) == month:
                count+=1
        monthly_totals.append(count)
    return monthly_totals

#OBAMA QUERIES
def return_keywords_for_pres(id):
    return db.session.query(Keyword).filter_by(president_id=id).all()

def sorted_keyword_count_for_obama():
    obama_keyword_w_count=db.session.query(Keyword.value, func.count(Keyword.value)).filter(Keyword.president_id==1).group_by(Keyword.value).all()
    obama_sorted_keyword_count=sorted(obama_keyword_w_count, key=lambda x:x[1], reverse=True)
    return obama_sorted_keyword_count

def top_fifteen_all_keywords_obama():
    obama_keyword_w_count=db.session.query(Keyword.value, func.count(Keyword.value)).filter(Keyword.president_id==1).group_by(Keyword.value).all()
    obama_sorted_keyword_count=sorted(obama_keyword_w_count, key=lambda x:x[1], reverse=True)
    final_obama_sorted_keyword_count=[i for i in obama_sorted_keyword_count if i[0].upper() != 'OBAMA, BARACK']
    return final_obama_sorted_keyword_count[:15]

def top_fifteen_people_keywords_obama():
    obama_people_keyword_w_count=db.session.query(Keyword.value, func.count(Keyword.value)).filter(Keyword.president_id==1).filter(Keyword.category=='persons').group_by(Keyword.value).all()
    obama_sorted_people_keyword_count=sorted(obama_people_keyword_w_count, key=lambda x:x[1], reverse=True)
    final_obama_sorted_people_keyword_count=[i for i in obama_sorted_people_keyword_count if i[0].upper() != 'OBAMA, BARACK']
    return final_obama_sorted_people_keyword_count[:15]

def top_fifteen_subject_keywords_obama():
    obama_subject_keyword_w_count=db.session.query(Keyword.value, func.count(Keyword.value)).filter(Keyword.president_id==1).filter(Keyword.category=='subject').group_by(Keyword.value).all()
    obama_sorted_subject_keyword_count=sorted(obama_subject_keyword_w_count, key=lambda x:x[1], reverse=True)
    return obama_sorted_subject_keyword_count[:15]

def top_fifteen_location_keywords_obama():
    obama_location_keyword_w_count=db.session.query(Keyword.value, func.count(Keyword.value)).filter(Keyword.president_id==1).filter(Keyword.category=='glocations').group_by(Keyword.value).all()
    obama_sorted_location_keyword_count=sorted(obama_location_keyword_w_count, key=lambda x:x[1], reverse=True)
    return obama_sorted_location_keyword_count[:15]

def top_fifteen_organization_keywords_obama():
    obama_organization_keyword_w_count=db.session.query(Keyword.value, func.count(Keyword.value)).filter(Keyword.president_id==1).filter(Keyword.category=='organizations').group_by(Keyword.value).all()
    obama_sorted_organization_keyword_count=sorted(obama_organization_keyword_w_count, key=lambda x:x[1], reverse=True)
    return obama_sorted_organization_keyword_count[:15]

def top_fifteen_article_sections_obama():
    obama_section_w_count=db.session.query(Article.section, func.count(Article.section)).filter(Article.president_id==1).group_by(Article.section).all()
    obama_sorted_section_count=sorted(obama_section_w_count, key=lambda x:x[1], reverse=True)
    return obama_sorted_section_count[:15]

# TRUMP QUERIES 
    
def sorted_keyword_count_for_trump():
    trump_keyword_w_count=db.session.query(Keyword.value, func.count(Keyword.value)).filter(Keyword.president_id==2).group_by(Keyword.value).all()
    trump_sorted_keyword_count=sorted(trump_keyword_w_count, key=lambda x:x[1], reverse=True)
    return trump_sorted_keyword_count

def top_fifteen_all_keywords_trump():
    trump_keyword_w_count=db.session.query(Keyword.value, func.count(Keyword.value)).filter(Keyword.president_id==2).group_by(Keyword.value).all()
    trump_sorted_keyword_count=sorted(trump_keyword_w_count, key=lambda x:x[1], reverse=True)
    final_trump_sorted_keyword_count=[i for i in trump_sorted_keyword_count if i[0].upper() != 'TRUMP, DONALD J']
    return final_trump_sorted_keyword_count[:15]

def top_fifteen_people_keywords_trump():
    trump_people_keyword_w_count=db.session.query(Keyword.value, func.count(Keyword.value)).filter(Keyword.president_id==2).filter(Keyword.category=='persons').group_by(Keyword.value).all()
    trump_sorted_people_keyword_count=sorted(trump_people_keyword_w_count, key=lambda x:x[1], reverse=True)
    final_trump_sorted_people_keyword_count=[i for i in trump_sorted_people_keyword_count if i[0].upper() != 'TRUMP, DONALD J']
    return final_trump_sorted_people_keyword_count[:15]

def top_fifteen_subject_keywords_trump():
    trump_subject_keyword_w_count=db.session.query(Keyword.value, func.count(Keyword.value)).filter(Keyword.president_id==2).filter(Keyword.category=='subject').group_by(Keyword.value).all()
    trump_sorted_subject_keyword_count=sorted(trump_subject_keyword_w_count, key=lambda x:x[1], reverse=True)
    return trump_sorted_subject_keyword_count[:15]

def top_fifteen_location_keywords_trump():
    trump_location_keyword_w_count=db.session.query(Keyword.value, func.count(Keyword.value)).filter(Keyword.president_id==2).filter(Keyword.category=='glocations').group_by(Keyword.value).all()
    trump_sorted_location_keyword_count=sorted(trump_location_keyword_w_count, key=lambda x:x[1], reverse=True)
    return trump_sorted_location_keyword_count[:15]

def top_fifteen_organization_keywords_trump():
    trump_organization_keyword_w_count=db.session.query(Keyword.value, func.count(Keyword.value)).filter(Keyword.president_id==2).filter(Keyword.category=='organizations').group_by(Keyword.value).all()
    trump_sorted_organization_keyword_count=sorted(trump_organization_keyword_w_count, key=lambda x:x[1], reverse=True)
    return trump_sorted_organization_keyword_count[:15]

def top_fifteen_article_sections_trump():
    trump_section_w_count=db.session.query(Article.section, func.count(Article.section)).filter(Article.president_id==2).group_by(Article.section).all()
    trump_sorted_section_count=sorted(trump_section_w_count, key=lambda x:x[1], reverse=True)
    return trump_sorted_section_count[:15]

obama_allkeyword_labels = [key for key, value in top_fifteen_all_keywords_obama()]
obama_allkeyword_values= [value for key, value in top_fifteen_all_keywords_obama()]
obama_pplkeyword_labels = [key for key, value in top_fifteen_people_keywords_obama()]
obama_pplkeyword_values= [value for key, value in top_fifteen_people_keywords_obama()]
obama_subkeyword_labels = [key for key, value in top_fifteen_subject_keywords_obama()]
obama_subkeyword_values= [value for key, value in top_fifteen_subject_keywords_obama()]
obama_lockeyword_labels = [key for key, value in top_fifteen_location_keywords_obama()]
obama_lockeyword_values= [value for key, value in top_fifteen_location_keywords_obama()]
obama_orgkeyword_labels = [key for key, value in top_fifteen_organization_keywords_obama()]
obama_orgkeyword_values= [value for key, value in top_fifteen_location_keywords_obama()]
obama_sec_labels = [key for key, value in top_fifteen_article_sections_obama()]
obama_sec_values= [value for key, value in top_fifteen_article_sections_obama()]

trump_allkeyword_labels = [key for key, value in top_fifteen_all_keywords_trump()]
trump_allkeyword_values= [value for key, value in top_fifteen_all_keywords_trump()]
trump_pplkeyword_labels = [key for key, value in top_fifteen_people_keywords_trump()]
trump_pplkeyword_values= [value for key, value in top_fifteen_people_keywords_trump()]
trump_subkeyword_labels = [key for key, value in top_fifteen_subject_keywords_trump()]
trump_subkeyword_values= [value for key, value in top_fifteen_subject_keywords_trump()]
trump_lockeyword_labels = [key for key, value in top_fifteen_location_keywords_trump()]
trump_lockeyword_values= [value for key, value in top_fifteen_location_keywords_trump()]
trump_orgkeyword_labels = [key for key, value in top_fifteen_organization_keywords_trump()]
trump_orgkeyword_values= [value for key, value in top_fifteen_location_keywords_trump()]
trump_sec_labels = [key for key, value in top_fifteen_article_sections_trump()]
trump_sec_values= [value for key, value in top_fifteen_article_sections_trump()]