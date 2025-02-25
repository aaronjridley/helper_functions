#!/usr/bin/env python

# Functions to manually set the sizes of plots in python, since the
# python defaults suck

def convert_month_string_to_number(inMonth):

    months = {'jan': 1,
              'feb': 2,
              'mar': 3,
              'apr': 4,
              'may': 5,
              'jun': 6,
              'jul': 7,
              'aug': 8,
              'sep': 9,
              'oct': 10,
              'nov': 11,
              'dec': 12}

    return months[inMonth]

