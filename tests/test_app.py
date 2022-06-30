
import unittest
import os

os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        
    def test_home(self):
        response = self.client.get('/')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert '<title>MLH Fellow</title>' in html
        # TO DO: add more tests relating to the home page
        assert '<a href=""><li>Home</li></a>' in html
        assert '<a href="https://github.com/AbishaKugathasan">' in html
        
        
        
    def test_timeline(self):
        responseGet = self.client.get('/api/timeline_post')
        assert responseGet.status_code == 200
        assert responseGet.is_json
        json = responseGet.get_json()
        assert 'timeline_posts' in json
        assert len(json['timeline_posts']) == 0
        
        # TO DO: add more tests relating to the /api/timelines_post GET and POST apis
        responsePost = self.client.post('/api/timeline_post', data={"name":"John Doe", "email":"john@example.com", "content":"Hi there!"})
        assert responsePost.status_code == 200
        
        responseGet = self.client.get('/api/timeline_post')
        json = responseGet.get_json()
        assert len(json['timeline_posts']) == 1
        
        # TO DO: add more tests relating to the timeline page
        responseTimeline = self.client.get('/timeline')
        assert responseTimeline.status_code == 200
        html = responseTimeline.get_data(as_text=True)
        assert '<form id = "form" method = "POST" action = "/api/timeline_post">' in html
        
        
    def test_malformed_timeline_post(self):
        #POST request missing name
        response = self.client.post("/api/timeline_post", data={"email":"john@example.com", "content":"Hello World, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html
        
        #POST request with empty content
        response = self.client.post("/api/timeline_post", data={"name":"John Doe", "email":"john@example.com", "content":""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html
        
        #POST requesr with malformed email
        response = self.client.post("/api/timeline_post", data={"name":"John Doe","email":"not an email", "content":"Hello World, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
        
        
