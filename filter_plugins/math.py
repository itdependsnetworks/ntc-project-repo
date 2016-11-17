#!/usr/bin/env python

from functools import partial
import operator

def _binary_operation(operator_function, a, b):
    try:
        return operator_function(a, b)
    except TypeError as e:
        message = '%s %s' % (operator_function.__doc__, str(e))
        raise errors.AnsibleFilterError(message)

def add(a, b):
    '''add(a, b) -- Same as a / b.'''
    return int(a) + int(b)

def div(a, b):
    '''div(a, b) -- Same as a / b.'''
    return operator.truediv(a, b)

def invert(original_dict):
    '''div(a, b) -- Same as a / b.'''
    inverted_dict = {v: k for k, v in original_dict.items()}
    return inverted_dict

class FilterModule(object):
     ''' Ansible math jinja2 filters '''

     def filters(self):
         return {
             # ...
             'invert': invert,
             'add': partial(_binary_operation, add),
             'sub': partial(_binary_operation, operator.sub),
             'mul': partial(_binary_operation, operator.mul),
             'div': partial(_binary_operation, div),
             'mod': partial(_binary_operation, operator.mod),
             # ...
         }
