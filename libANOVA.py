#!/usr/bin/python

# libANOVA.py
# by Hawk Weisman - 2013
# 
# Computes some simple statistical analyses from scratch, with as few
# dependancies as possible

# Conventions:
#   + l: a list
#   + a: an average
#   + n: a number

# pyANOVA philosophy: if it can be done in one line, do it in one line

from __future__ import division # YAY WE'RE IN THE FUTURE

#=============================================================================
# One-liners: basic mathematical functions

def list_product(l):
    """Returns the product of all the numbers in a list"""
    return reduce(lambda x, y: x * y, l) 

def sqrt(n):
    """Returns the square root of n"""
    return n ** 0.5
    
def nth_root(n, root):
    """Returns the <root>th root of n"""
    return n ** (1/root)  # Hopefully this works
    
def range(l):
    """Returns the range of a list"""
    return l[len(l)] - l[0]
    
def even(n):
    """Returns true if n is even"""
    if n % 2 == 0:
        return True
    else:
        return False
       
#def median(l):
#    """Returns the median of a list"""
#    if even(len(l)):    # NOT YET IMPLEMENTED
#    else:               # NOTHING HAPPENS

#=============================================================================

#=============================================================================
# Sigma and anova functions

def arith_mean(l):
    """Returns the arithmetic mean of list l, as a float"""
    return sum(l) / len(l)

def geo_mean(l):
    """Returns the geometric mean of list l, as a float"""
    return nth_root(list_product(l), len(l))

def variance(l):
    """Returns the variance of list l from average a, as a float"""
    a = arith_mean(l)
    variance = 0      # accumulator for the rolling sum of squared differences
    for n in l:
        variance += (a - l) ** 2
    return variance / len(l)

def sigma(l):
    """Given the variance, returns the standard deviation"""
    return sqrt(variance(l))
    
#=============================================================================