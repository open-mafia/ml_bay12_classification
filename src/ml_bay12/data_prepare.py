from bs4 import BeautifulSoup
import re
def clean(raw_data):
    if not isinstance(raw_data,str):
        raw_data=str(raw_data)
    review_text = BeautifulSoup(raw_data).get_text() 
    letters_only = re.sub("[^a-zA-Z]", " ", review_text) 
    words = letters_only.lower().split()
    return( " ".join(words))

def concat_users_text(post):
    return post.groupby(["thread_num","user"],sort=False)["text"].apply(lambda x: x.sum()).reset_index()

def get_users_in_game(role, concat_df):
    return  concat_df.merge(role,on=['thread_num','user'])