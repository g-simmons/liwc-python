import os.path

import liwc

test_dir = os.path.dirname(__file__)


def test_category_names():
    _, category_names = liwc.load_token_parser(os.path.join(test_dir, "moral_foundations_dictionary.dic"))
    print(category_names)
    assert category_names == ["A", "Bravo"]


def test_parse():
    parse, categories = liwc.load_token_parser(os.path.join(test_dir, "alpha.dic"))
    sentence = "Any alpha a bravo charlie Bravo boy"
    tokens = sentence.split()
    matches = [category for token in tokens for category in parse(token)]
    # matching is case-sensitive, so the only matches are "alpha" (A), "a" (A) and "bravo" (Bravo)
    assert matches == ["A", "A", "Bravo"]

if __name__ == "__main__":
    test_category_names()
    test_parse()
    print("All tests passed")