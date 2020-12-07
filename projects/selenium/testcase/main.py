import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.PATH = 'C:\\Users\\samay\\chromedriver.exe'
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get('http://www.python.org')

    # runs automatically because of naming convention starts with 'test'
    def test_example(self):
        print('Test')
        assert True

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = 'pycon'
        mainPage.click_go_button()
        search_result_page = page.SearchResultsPage(self.driver)
        assert search_result_page.is_results_found()


    #def test_example_2(self):
    #    assert False

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
