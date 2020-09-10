from pytest import mark

@mark.smoke   #Todos estos tests se ejecutan bajo smoke and or body
@mark.body
class BodyTests:   #Everything inside this class is under @mark.body
    
    @mark.ui
    def test_can_navigate_to_body_page(self, chrome_browser):     #chrome_browser is defined in confttest.py so is available here without importing it.
        chrome_browser.get('https://www.yahoo.com')
        assert True

    def test_body_functions_as_expected(self):
        assert True

    def test_windshield(self):
        assert True

    def test_bumber(self):
        assert True