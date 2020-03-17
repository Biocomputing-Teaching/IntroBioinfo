#!/usr/local/bin/python
"""http://www.wellho.net/resources/ex.php4?item=y105/locvar.py"""
# Variable scope

first = 1

def one():
        "Double a global variable, return it + 3."
        global first
        first *= 2
        result = first+3
        return result

print one.__doc__
print one()
print one()
print one()
print "first now has the value",first
print "result has the value",result
