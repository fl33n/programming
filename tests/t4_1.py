import unittest

def selection_sort(arr):
    arrs = []
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        arrs.append(arr)

    return arr, arrs

class Tests4_1(unittest.TestCase):

    def test_1(self):
        self.assertEqual(selection_sort([100, 3, -56, 8])[0], [-56, 3, 8, 100])
            
    def test_2(self):
        self.assertEqual(selection_sort([0])[1], [])

    def test_3(self):
        self.assertNotEqual(selection_sort([0, 1])[0], [1, 2, 3, 4])

    def test_4(self):
        self.assertNotEqual(selection_sort([0, 0, 0, 0])[1], [1, 2, 3, 4])

    def test_5(self):
        self.assertEqual(selection_sort([0, 0, 0, 0])[1], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

    def test_6(self):
        self.assertIsNotNone(selection_sort([5, 1, 6, 2]))

    def test_7(self):
        self.assertIsInstance(selection_sort([5, 1, 6, 2])[0], list)
        
    def test_8(self):
        with self.assertRaises(TypeError) as e:
            selection_sort(['100', 3, -56, 8])

    def test_9(self):
        with self.assertRaises(NameError) as e:
            selection_sort(burmalda)
        
    def test_10(self):
        with self.assertRaises(Exception) as e:
            selection_sort(None,1)


if __name__ == '__main__':
    unittest.main()