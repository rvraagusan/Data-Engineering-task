import pandas as pd 

def create_table():
    data = pd.read_json('course_data.json')
    data.reset_index()
    data.rename(columns={"course_id": "COURSE_ID", 
                      "course_title": "COURSE_TITLE",
                      "is_paid": "IS_PAID",
                      "price": "PRICE",
                      "num_subscribers": "NUM_SUBSCRIBERS",
                      "num_reviews": "NUM_REVIEWS",
                      "num_lectures": "NUM_LECTURES",
                      "level": "LEVELS",
                      "content_duration": "CONTENT_DURATION",
                      "published_timestamp": "PUBLISHED_TIMESTAMPS",
                      "subject": "SUBJECT",
                      "author": "AUTHOR"},
                       inplace=True)
    
    author = data[['AUTHOR']]
    course = data[['COURSE_ID','COURSE_TITLE','PRICE','LEVELS','CONTENT_DURATION']]
    subject = data[['COURSE_ID','SUBJECT']]
    fact = data.drop(['COURSE_TITLE','PRICE', 'LEVELS', 'CONTENT_DURATION', 'SUBJECT', 'AUTHOR'], axis =1)

    author[['FIRST_NAME', 'LAST_NAME', 'AUTHOR_CODE']] = pd.DataFrame([ x.split('_') for x in author['AUTHOR'].tolist()])
    author = author.drop(['AUTHOR'], axis=1)
    author['AUTHOR_ID'] = author.index
    subject.rename(columns={'COURSE_ID': 'SUBJECT_ID'}, inplace=True)
    course.rename(columns={'COURSE_TITLE': 'COURSE_NAME'}, inplace=True)
    # print(author.head())
    # print(fact.head())
    # print(subject.head())
    # print(course.head())

    return author, course, subject, fact


# create_table()