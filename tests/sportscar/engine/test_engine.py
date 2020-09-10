from pytest import mark

@mark.smoke
@mark.engine
@mark.ui
def test_engine_functions_as_expected():
    assert True

def test_can_navigate_to_engine_page(chrome_browser):     #chrome_browser is defined in confttest.py so is available here without importing it.
    chrome_browser.get('https://www.icarlospro.com')
    assert True
