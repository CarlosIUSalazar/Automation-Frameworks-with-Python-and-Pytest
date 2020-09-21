from pytest import mark

@mark.skip
@mark.parametrize('tv_brand', [     #there si a parameter called TV_brand and heres a list of things you need to ask about it every time.  Paameterize 3 things that Im gonna inject in 'tv_band'. This means this test has to run 3 times cuz theres 3 parameters.
        ('Samsung'),
        ('Sony'),
        ('Vizio')
    ]
)
def test_television_turns_on(tv_brand):
    print(f"{tv_brand} turns on as expected")

#with pytest -v you get:
# test_television.py::test_television_turns_on[Samsung] Samsung turns on as expected
# PASSED
# test_television.py::test_television_turns_on[Sony] Sony turns on as expected
# PASSED
# test_television.py::test_television_turns_on[Vizio] Vizio turns on as expected
# PASSED

def test_broswer_can_navigate_to_training_ground(browser):    #For when I have a test and I need to run it against multple browsers. this needs conftest and fixtures
    browser.get('http://www.google.com')

