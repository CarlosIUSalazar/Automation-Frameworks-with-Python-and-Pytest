from titlecase import title_case

class TitleCaseTests:
    def test_text_is_uppercased_correctly(self):
        initial_text = 'this should be capitalized'  #because non of these words are in the list
        expected_text = 'This Should Be Capitalized'
        returned_text = title_case(initial_text)
        assert returned_text == expected_text
