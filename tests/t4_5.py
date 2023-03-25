import unittest

def h_sort(h, arr):
    for i in range(h, len(arr)):
        j = i
        while j >= h and arr[j] < arr[j - h]:
            arr[j], arr[j - h] = arr[j - h], arr[j]
            j -= h
    return arr

class Tests4_5(unittest.TestCase):

    def test_1(self):
        self.assertEqual(h_sort(3, [100, 3, -56, 8, 1, 47, 25, -5]), [8, -5, -56, 25, 1, 47, 100, 3])

    def test_2(self):
        self.assertEqual(h_sort(0, [0]), [0])

    def test_3(self):
        self.assertNotEqual(h_sort(3, [0, 1]), [1, 2, 3, 4])

    def test_4(self):
        self.assertNotEqual(h_sort(3, [0, 0, 0, 0]), [1, 2, 3, 4])

    def test_5(self):
        self.assertEqual(h_sort(2, [0, 0, 0, 0]), [0, 0, 0, 0])

    def test_6(self):
        self.assertIsNotNone(h_sort(3, [5, 1, 6, 2]))

    def test_7(self):
        self.assertEqual(h_sort(23, [166,1,20,00]), [166, 1, 20, 0])

    def test_8(self):
        with self.assertRaises(TypeError) as e:
            h_sort(['100', 3, -56, 8])

    def test_9(self):
        with self.assertRaises(NameError) as e:
            h_sort(burmalda)

    def test_10(self):
        with self.assertRaises(Exception) as e:
            h_sort(None, 1)


if __name__ == '__main__':
    unittest.main()