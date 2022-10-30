import os
import unittest
import json


def read_json(file):
    """Reads a JSON document, decodes the file content, and returns a
    dictionary.

    Parameter:
        file (str): path to file

    Returns:
        dict: dict representations of the decoded JSON document
    """

    pass


def top_movies(rated, data):
    """Returns the top three movies on the basis of the rated specified.

    Parameters:
        rated (str): movie rating category. Example: "PG"
        data (dict): dict representations of a decoded JSON document

    Returns:
        list: top three movies in a list ranked by their imdbRating
    """
    pass


def main():
    pass


class TestDiscussion9(unittest.TestCase):
    def setUp(self):
        self.movies = read_json('movies.json')

    def test_read_json(self):

        pass

    def test_top_movies(self):

        pass



if __name__ == "__main__":
    main()
    # You can comment this out to test with just the main function,
    # But be sure to uncomment it and test that you pass the unittests before you submit!
    unittest.main(verbosity=2)

