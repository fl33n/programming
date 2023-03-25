import unittest

def bubble_sort(arr):
    n = len(arr)
    res = []
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        res.append(arr)

    return res

class Tests4_3(unittest.TestCase):

    def test_1(self):
        self.assertEqual(bubble_sort([100, 3, -56, 8])[0], [-56, 3, 8, 100])

    def test_2(self):
        self.assertEqual(bubble_sort([0]), [])

    def test_3(self):
        self.assertNotEqual(bubble_sort([0, 1])[0], [1, 2, 3, 4])

    def test_4(self):
        self.assertNotEqual(bubble_sort([0, 0, 0, 0])[1], [1, 2, 3, 4])

    def test_5(self):
        self.assertEqual(bubble_sort([0, 0, 0, 0])[1], [0, 0, 0, 0])

    def test_6(self):
        self.assertIsNotNone(bubble_sort([5, 1, 6, 2]))

    def test_7(self):
        with self.assertRaises(IndexError) as e:
            bubble_sort(bubble_sort([0])[1])

    def test_8(self):
        with self.assertRaises(TypeError) as e:
            bubble_sort(['100', 3, -56, 8])

    def test_9(self):
        with self.assertRaises(NameError) as e:
            bubble_sort(burmalda)

    def test_10(self):
        with self.assertRaises(Exception) as e:
            bubble_sort(None, 1)


if __name__ == '__main__':
    unittest.main()