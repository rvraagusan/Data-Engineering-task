import pandas as pd 



def load_file():
    data = pd.read_json('course_data.json')
    data.reset_index()
    data.rename(columns={"course_id": "COURSE_ID", 
                      "course_title": "COURSE_TITLE",
                      "is_paid": "IS_PAID",
                      "price": "PRICE",
                      "num_subscribers": "NUM_SUBSCRIBERS",
                      "num_reviews": "NUM_REVIEWS",
                      "num_lectures": "NUM_LECTURES",
                      "level": "LEVEL",
                      "content_duration": "CONTENT_DURATION",
                      "published_timestamp": "CONTENT_DURATION2PUBLISHED_TIMESTAMP",
                      "subject": "SUBJECT",
                      "author": "AUTHOR"},
                       inplace=True)
    # print(data)
    # data_columns = data.columns.values
    # print(data_columns)
    # data.to_csv("course_data.csv", index=False)
    return data 

# load_file()