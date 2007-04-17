import unittest
from django.test.client import Client
from datetime import datetime as d
# assumes the code is installed in a module called 'testbud'
from testbud.blog.models import *

class BlogEntryTest(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_authors_print(self):
        a = Author.objects.create(name="Chris McAvoy")
        b = Author.objects.create(name="Camri McAvoy")
        c = Author.objects.create(name="Cotton McAvoy")
        self.author_list = [a,b,c]
        
        self.be = BlogEntry.objects.create(title="test",date_added=d.now())
        
        self.be.authors = self.author_list
        self.be.save()
        self.assertEqual(self.be.pretty_author_list(), "Chris McAvoy, Camri McAvoy, Cotton McAvoy")
        
        self.be.authors = [self.author_list[0]]
        self.be.save()
        self.assertEqual(self.be.pretty_author_list(), "Chris McAvoy")
        
        self.be.authors = self.author_list[0:2]
        self.be.save()
        self.assertEqual(self.be.pretty_author_list(), "Chris McAvoy, Camri McAvoy")
    
if __name__ == '__main__':
    unittest.main()