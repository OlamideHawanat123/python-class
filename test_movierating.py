import unittest
from movierating import *

class MovieRatingTest(unittest.TestCase):
	def test_that_movie_can_be_added(self):
		movie_name = "koto aye"
		actual = add_movie(movie_name)
		expected = "koto aye"
		self.assertEqual("Movie is added!", add_movie("koto aye"))

	def test_that_movies_can_be_viewed(self):
		add_movie("labo")
		add_movie("labo")
		self.assertEqual("labo","labo",view_movies(movie_stack))

	def test_that_you_can_rate_a_movie(self):
		rate_a_movie(movie_name)
		self.assertEqual(5, rate_a_movie(5))
		


				