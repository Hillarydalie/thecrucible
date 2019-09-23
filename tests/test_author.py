from app.models import Author
from app import db

def setUp(self):
        self.user_James = Author(
            id = "1",
            username = 'Admin',
            password = 'admin', 
            email = 'admin@admin-ad.com')

def tearDown(self):
        Author.query.delete()

def test_check_instance_variables(self):
        self.assertEquals(self.author,self.user_James)


