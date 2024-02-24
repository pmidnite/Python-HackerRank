#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    even_6_20_list = range(6, 21, 2)
    # 1. Checking odd using n%2 !== 0.
    # 2. Checking if n in list of 6-20 even range list.
    if n % 2 != 0 or n in even_6_20_list:
        print('Weird')
    elif n in [2, 4] or (n > 20 and n % 2 == 0):
        print('Not Weird')
