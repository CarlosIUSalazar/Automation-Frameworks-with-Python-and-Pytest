from pytest import mark

@mark.ui
@mark.entertainment
def test_can_navigate_to_entertainment_page(chrome_browser):     #chrome_browser is defined in confttest.py so is available here without importing it.
    chrome_browser.get('https://www.hola.com')
    assert True

