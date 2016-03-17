#                    Project MyFloat

==========================================================

1, Project Requirements

    Write a program to process a file.

    1.   The path to the file is to be passed to the program as a parameter. The
         file contains zero to more lines. Each line contains zero or more float
         numbers being separated by one or more space characters.

    2.   The output of the program is the total count of numbers and the sum of
         all numbers.

    3.   list all the ways you plan to test this program.

    4.   target to finish this by 30-60 minutes.

===========================================================

2, myfloat.py

    The program first check the number of parameters, and from which take out
    file_path. Then check whether the input file_path is readable, and if it's
    readable, call the function count_and_sum to get the count and sum of
    floating-point numbers in file file_path.

    Function count_and_sum open and lock file_path, and for each line in which,
    call function count_and_sum_line to get the count and sum of floating-point,
    and then add up those results.

    Usage:
        # python myfloat.py /path/to/float.file
    E.g,
        # python myfloat.py my.txt
    Expected results like this:
        6 floats in File my.txt, whose sum is 15.4555.

    The related log is recorded in the file /var/log/float.log (you can modify
    the logfile path).

Defects or TODO:

    Multi-process/thread. For large files, we can broke file and each segment
    (some lines) is processed by one process/thread, and finally add up results
    of each process/thread (like MapReduce).

===========================================================

2, Test, testfloat.py 

    The program testfloat.py is realized based on unittet. It's maybe better if
    realized based on mock.

    The program create some test cases and perform Unit Test for function
    count_and_sum_line and count_and_sum, also perform function tests for some
    kinds of non-readable file (system or device file, file that doesn't exist,
    and so on).

    Usage:
        # python testfloat.py 
    Expected results like this: "
        ..file /dev/xuetangxvg/mysqlroot03 is NOT a readable file
        file /home/not/dir/file is NOT a readable file
        .
        ----------------------------------------------------------------------
        Ran 3 tests in 0.005s

        OK
    "

Defects or TODO

    1, may be better if based on mock
    2, Testing was somewhat simple, and did not cover as much more scenario as
       possible.
    3, did not generate more and larger test files by random, and did not perform
       performance testing for large file. There is no enough time :D


