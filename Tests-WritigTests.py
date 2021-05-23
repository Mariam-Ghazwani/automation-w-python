
# Unit tests
'''Unit tests are used to verify that small isolated parts of a program are correct.
Unit tests are generally written alongside the code to test the behavior of 
individual pieces or units like functions or methods. '''

# Edge Case
'''Edge cases are inputs to our code that produce unexpected results, and are found 
at the extreme ends of the ranges of input we imagine our programs will typically work with. 
Edge cases usually need special handling in scripts in order for the code to continue to behave correctly. '''


#rearrange.py
#!/usr/bin/env python3
import re

def rearrange_name(need):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    return "{} {}".format(result[2], result[1])


#rearrange_test.py
#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()

###

import re 
  
my_txt = "An investment in knowledge pays the best interest."

def LetterCompiler(txt):
    result = re.findall(r'([a-c]).', txt)
    return result

print(LetterCompiler(my_txt))


import unittest

class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

# EDGE CASES HERE
    def test_three(self):
        testcase = "aebec"
        expected = ['a', 'b']
        self.assertEqual(LetterCompiler(testcase), expected)

unittest.main()


Unit Test Cheat-Sheet
Frankly, the unit testing library for Python is fairly well documented, but it can be a bit of a dry read. Instead, we suggest covering the core module concepts, and then reading in more detail later.

Best of Unit Testing Standard Library Module
Understand a Basic Example:

https://docs.python.org/3/library/unittest.html#basic-example
Understand how to run the tests using the Command Line:

https://docs.python.org/3/library/unittest.html#command-line-interface
Understand various Unit Test Design Patterns:

https://docs.python.org/3/library/unittest.html#organizing-test-code
Understand the uses of setUp, tearDown; setUpModule and tearDownModule
Understand basic assertions:

Method	Checks that	New in
assertEqual(a, b)	a == b	
assertNotEqual(a, b)	a != b	
assertTrue(x)	bool(x) is True	
assertFalse(x)	bool(x) is False	
assertIs(a, b)	a is b	3.1
assertIsNot(a, b)	a is not b	3.1
assertIsNone(x)	x is None	3.1
assertIsNotNone(x)	x is not None	3.1
assertIn(a, b)	a in b	3.1
assertNotIn(a, b)	a not in b	3.1
assertIsInstance(a, b)	isinstance(a, b)	3.2
assertNotIsInstance(a, b)	not isinstance(a, b)	3.2


Understand more specific assertions such as assertRaises

https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises