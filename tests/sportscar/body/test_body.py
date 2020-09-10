from pytest import mark

@mark.smoke   #Todos estos tests se ejecutan bajo smoke and or body
@mark.body
class BodyTests:   #Everything inside this class is under @mark.body
    def test_body_functions_as_expected(self):
        assert True

    def test_windshield(self):
        assert True

    def test_bumber(self):
        assert True