from random import randint
import unittest


class BinarySearchExact(unittest.TestCase):
    def binary_search_exact(self, sorted_array: list, target_numer: int):
        if not sorted_array:
            return False
        left_pointer, right_pointer = 0, len(sorted_array) - 1
        while right_pointer >= left_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2
            if sorted_array[middle_pointer] == target_numer:
                return True
            if sorted_array[middle_pointer] < target_numer:
                left_pointer = middle_pointer + 1
            else:
                right_pointer = middle_pointer - 1
        if left_pointer == right_pointer:
            return True
        return False

    def run_test(self, test_array_length: int, number_of_tests: int):
        for test_number in range(number_of_tests):
            test_array = [randint(0, test_array_length * 3)
                          for i in range(test_array_length)]
            test_array.sort()
            target_number = randint(test_array[0] - 10, test_array[-1] + 10)
            expected_result = target_number in test_array
            actual_result = self.binary_search_exact(test_array, target_number)
            print(
                f'test_array: {test_array}\n'
                f'target_number: {target_number}\n'
                f'expected_result: {expected_result} : '
                f'actual_result: {actual_result}')
            self.assertEqual(expected_result, actual_result)
            print(f'TEST {test_number + 1} PASSED\n')


if __name__ == '__main__':
    binary_search_exact_instance = BinarySearchExact()
    binary_search_exact_instance.run_test(10, 200)
