#file to test our database connection and 
#any interactions with a database through Peewee ORM

import unittest
from peewee import *
from playhouse.shortcuts import model_to_dict

from app import TimelinePost

MODELS = [TimelinePost]

#Use an in-memory SQLite fro tests
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        #bind model classes to test db. Since we have a complete list of
        #all models, we do not need to recursively bind dependencies.
        
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        
        test_db.connect()
        test_db.create_tables(MODELS)
        
    def tearDown(self):
        #Not strictly necessary since SQLite in-memory database only live
        #for the duration of the connection, and in the next step we close 
        #the connection...but a good practice all the same
        test_db.drop_tables(MODELS)
        
        #Close connection to db
        test_db.close()
        
    def test_timeline_post(self):
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hellow World, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jame@example.com', content='Hellow World, I\'m Jane!')
        assert second_post.id == 2
        # TO DO: get timeline posts and assert that they are correct
        
        posts = [
            model_to_dict(p)
            for p in TimelinePost.select()
            ]
        
        assert len(posts) == 2
        assert posts[0]['id'] == 1
        assert posts[1]['id'] == 2
         
        