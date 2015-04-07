#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Module uses dictionary iteration using iteritems method"""

DATA = {
    1: 11,
    2: 12,
    3: 13,
    4: 14,
    5: 15,
    6: 16,
    7: 17,
    8: 18,
    9: 19,
    10: 20
}


def iter_dict_funky_sum(dict1):
    """Function adds the values of input argument (DATA) and
       subtract the total of the keys from input(DATA).

       Arg:
           dict1(int): input dictionary of integers.
       Return:
           returns the difference of values sum and key sum.

       Examples:
               >>> iter_dict_funky_sum(DATA)
                   100
                >>>
    """
    runn_total_integer = 0
    for key, values in dict1.iteritems():
        runn_total_integer += (values - key)
    return runn_total_integer
