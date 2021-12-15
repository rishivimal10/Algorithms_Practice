from unittest import TestCase

from arrays.the_dutch_national_flag_problem import dutch_national_flag_solution, is_solution


class TestDutchFlagSolution(TestCase):
    def test_dutch_national_flag_solution(self):
        self.assertTrue(is_solution(dutch_national_flag_solution([0, 1, 2, 0, 2, 1, 1], 3), 0))
        self.assertTrue(is_solution(dutch_national_flag_solution([0, 1, 2, 0, 2, 1, 1], 2), 2))


