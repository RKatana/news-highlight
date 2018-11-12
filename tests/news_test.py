import unittest
from app.models import News,Sources

class NewsTest(unittest.TestCase):
    '''
    Test class to test the instance of news articles
    '''
    def setUp(self):
        '''
        the setup method to run befor evry test
        '''
        self.new_article = News('bbc','raphael','football','manchester looses','www','src','nov','scores')
        self.new_sources = Sources('BBC','Global news','general','true')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,News))

    def test_source(self):
        self.assertTrue(isinstance(self.new_sources,Sources))

if __name__=='__main__':
    unittest.main()
