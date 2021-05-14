import unittest
from polynomial import Polynomial


class Tests(unittest.TestCase):
    # constructor
    def test_constructor_int(self):
        p = Polynomial(1)
        self.assertEqual(p.coeffs, [1])


    def test_constructor_list(self):
        p = Polynomial([1, 2])
        self.assertEqual(p.coeffs, [1, 2])


    def test_constructor_tuple(self):
        p = Polynomial((1, 2))
        self.assertEqual(p.coeffs, [1, 2])


    def test_contstructor_polynomial(self):
        p1 = Polynomial([1, 2])
        p2 = Polynomial(p1)
        p1.coeffs[0] = 3
        self.assertEqual(p2.coeffs, [1, 2])


    def test_constructor_empty_list(self):
        self.assertRaises(Exception, Polynomial, [])


    def test_constructor_empty_tuple(self):
        self.assertRaises(Exception, Polynomial, ())


    def test_constructor_float(self):
        self.assertRaises(Exception, Polynomial, 1.2)


    def test_constructor_float_list(self):
        self.assertRaises(Exception, Polynomial, [1.2, 3.2])


    # add
    def test_add_const_int(self):
        p = Polynomial([1, 2])
        p = p + 1
        self.assertEqual(p.coeffs, [1, 3])
        p = 1 + p
        self.assertEqual(p.coeffs, [1, 4])


    def test_add_polynomial(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [1, 3, 5])


    def test_add_polynomial_with_zero_coeffs(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 0, 0, 2])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [1, 1, 2, 5])


    def test_add_const_float(self):
        self.assertRaises(Exception, lambda: Polynomial([1, 2]) + 1.2)


    # sub
    def test_sub_const_int(self):
        p = Polynomial([1, 2])
        p = p - 1
        self.assertEqual(p.coeffs, [1, 1])
        p = 1 - p
        self.assertEqual(p.coeffs, [-1, 0])


    def test_sub_polynomial(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2])
        p3 = p1 - p2
        self.assertEqual(p3.coeffs, [1, 1, 1])
        p4 = p2 - p1
        self.assertEqual(p4.coeffs, [-1, -1, -1])

    def test_sub_polynomial_with_equal_coeff(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 3, 4])
        p3 = p1 - p2
        self.assertEqual(p3.coeffs, [-1, -1]) 


    def test_sub_polynomial_with_equal_coeffs(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2, 3])
        p3 = p1 - p2
        self.assertEqual(p3.coeffs, [0]) 


    def test_sub_polynomial_with_zero_coeffs(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 0, 0, 2])
        p3 = p1 - p2
        self.assertEqual(p3.coeffs, [-1, 1, 2, 1])


    def test_sub_const_float(self):
        self.assertRaises(Exception, lambda: Polynomial([1, 2]) - 1.2)


    # mul
    def test_mul_const_int(self):
        p = Polynomial([1, 2])
        p = p * 2
        self.assertEqual(p.coeffs, [2, 4])
        p = 3 * p
        self.assertEqual(p.coeffs, [6, 12])


    def test_mul_const_zero(self):
        p = Polynomial([1, 2])
        p1 = p * 0
        self.assertEqual(p1.coeffs, [0])
        p2 = 0 * p
        self.assertEqual(p2.coeffs, [0])


    def test_mul_polynomial(self):
        p1 = Polynomial([1, 2])
        p2 = Polynomial([1, 0])
        p = p1 * p2
        self.assertEqual(p.coeffs, [1, 2, 0])   
     
        p1 = Polynomial([1, 2])
        p2 = Polynomial([2, 1])
        p = p1 * p2
        self.assertEqual(p.coeffs, [2, 5, 2])  

        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([2, -1])
        p = p1 * p2
        self.assertEqual(p.coeffs, [2, 3, 4, -3])  


    def test_mul_const_float(self):
        self.assertRaises(Exception, lambda: Polynomial([1, 2]) * 1.2)


    # eq
    def test_eq_const_int(self):
        p1 = Polynomial(1)
        self.assertTrue(p1 == 1)
        self.assertTrue(1 == p1)
        p2 = Polynomial([1, 2])
        self.assertFalse(p2 == 1)
        self.assertFalse(1 == p2)

    def test_eq_polynomial(self):
        p1 = Polynomial(1)
        p2 = Polynomial([1, 2]) 
        p3 = Polynomial([1])
        self.assertFalse(p1 == p2)
        self.assertTrue(p1 == p3)
        self.assertFalse(p2 == p3)

    def test_eq_const_float(self):
        self.assertRaises(Exception, lambda: Polynomial([1, 2]) == 1.2)


    # str
    def test_str_const_int(self):
        p = Polynomial(1)
        self.assertEqual(str(p), '1')


    def test_str_polynomial(self):
        p = Polynomial([1, 0])
        self.assertEqual(str(p), 'x')

        p = Polynomial([1, 1])
        self.assertEqual(str(p), 'x+1')

        p = Polynomial([1, -1])
        self.assertEqual(str(p), 'x-1')

        p = Polynomial([-1, 0])
        self.assertEqual(str(p), '-x')

        p = Polynomial([-1, -1])
        self.assertEqual(str(p), '-x-1')

        p = Polynomial([3, 1, 0, 2])
        self.assertEqual(str(p), '3x^3+x^2+2')

        p = Polynomial([-3, 1, 0, -2])
        self.assertEqual(str(p), '-3x^3+x^2-2')

        p = Polynomial([3, 1, 1, 2])
        self.assertEqual(str(p), '3x^3+x^2+x+2')


    # repr
    def test_repr_const_int(self):
        p = Polynomial(1)
        self.assertEqual(repr(p), 'Polynomial([1])')


    def test_repr_polynomial(self):
        p = Polynomial([1, 0])
        self.assertEqual(repr(p), 'Polynomial([1, 0])')

        p = Polynomial([1, 1])
        self.assertEqual(repr(p), 'Polynomial([1, 1])')

        p = Polynomial([1, -1])
        self.assertEqual(repr(p), 'Polynomial([1, -1])')

        p = Polynomial([-1, 0])
        self.assertEqual(repr(p), 'Polynomial([-1, 0])')

        p = Polynomial([-1, -1])
        self.assertEqual(repr(p), 'Polynomial([-1, -1])')

        p = Polynomial([3, 1, 0, 2])
        self.assertEqual(repr(p), 'Polynomial([3, 1, 0, 2])')

        p = Polynomial([-3, 1, 0, -2])
        self.assertEqual(repr(p), 'Polynomial([-3, 1, 0, -2])')

        p = Polynomial([3, 1, 1, 2])
        self.assertEqual(repr(p), 'Polynomial([3, 1, 1, 2])')


    # copy
    def test_copy(self):
        p1 = Polynomial([1, 2])
        p2 = Polynomial(p1)
        p1.coeffs[0] = 3
        self.assertEqual(p2.coeffs, [1, 2])


if __name__ == '__main__':
    unittest.main()

