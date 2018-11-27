import unittest
import test.all_tests

testSuite = test.all_tests.create_test_suite()
text_runner = unittest.TextTestRunner().run(testSuite)

# Script from stw_dev's answer on Stack Overflow: https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure