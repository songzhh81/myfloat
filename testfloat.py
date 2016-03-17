# -*- coding: utf-8 -*-
import unittest
import myfloat
import os

class TestMyfloat(unittest.TestCase):

    def setUp(self):
        # unit test cases for count_and_sum_line
        self.checklines = ['1.4 2.2        5.5555     txt',
                           'dddd     .31.5 1. .03  ',
                           '              2',
                           '34t4 jrg \n 1',
                           '888888888888888888888888   ',
                           '                   '
                           ]
        # expected results for count_and_sum_line testing
        self.linerets = [(3, 9.1555), (2, 1.03), (1, 2.0), (1, 1.0),
                         (1, 8.888888888888889e+23), (0, 0)]

        # test cases for non-readable files
        # including device file, or file does not exist, ...
        self.notfiles = [['myfloat.py', '/dev/xuetangxvg/mysqlroot03'],
                           ['myfloat.py', '/home/not/dir/file']]

        # unit test cases for count_and_sum 
        self.checkfiles = ['test1.file', 'test2.file']

        with open(self.checkfiles[0], 'w') as test1:
            test1.write('  \n') 
            test1.write('1.4 2.2        5.5555     txt\n')
            test1.write('\n')
            test1.write('\n')
            test1.write('2   .3        .   4       5v   \n')

        with open(self.checkfiles[1], 'w') as test2:
            test2.write('10.9e\n')
            test2.write('77\n1')
            test2.write('8888888888888888888.88\n')

        # expected results for count_and_sum testing
        self.filerets = [(6, 15.4555), (2, 1.888888888888889e+19)]

    def tearDown(self):
        # remove tmpfiles for testing
        for f in self.checkfiles:
            os.remove(f)

    # test count_and_sum_line
    def test_line(self):
        i = 0
        while i < 6:
            lcnt, lsum = myfloat.count_and_sum_line(self.checklines[i])
            self.assertTupleEqual((lcnt, lsum), self.linerets[i])
            i += 1

    # test non-readable file
    def test_notfile(self):
        for f in self.notfiles:
            ret = myfloat.main(f)
            self.assertEqual(ret, None)

    # test count_and_sum
    def test_file(self):
        i = 0
        while i < 2:
            fcnt, fsum = myfloat.count_and_sum(self.checkfiles[i])
            self.assertTupleEqual((fcnt, fsum), self.filerets[i])
            i += 1

if __name__ == '__main__':
    unittest.main()
