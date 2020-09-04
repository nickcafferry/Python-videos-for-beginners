|Deployment Status|  |Apache License|  |Documentation Status|  |Python Online|  |Python version|  |--|  |today| 

-------------------

.. |Deployment Status| image:: https://github.com/nickcafferry/Python-videos-for-beginners/workflows/deploy/badge.svg
   :target: https://github.com/nickcafferry/Python-videos-for-beginners/runs/1054191359?check_suite_focus=true
.. |Documentation Status| image:: https://readthedocs.org/projects/python-videos-for-beginners/badge/?version=latest
   :target: https://python-videos-for-beginners.readthedocs.io/en/latest/?badge=latest
.. |Apache License| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg?style=flat)
   :target: http://www.apache.org/licenses/LICENSE-2.0
.. |Python version| image:: https://img.shields.io/badge/python-3.7,%203.8-brightgreen.svg
   :target: https://www.python.org/
.. |Python Online| image:: https://img.shields.io/badge/platform-python%20online-blue
   :target: https://python-videos-for-beginners.readthedocs.io/en/latest/pyonlineindex.html

.. |--| unicode:: U+02014 .. em dash
   :trim:

Copyright |copy| Wei MEI, |MLMS (TM)| |---|
all rights reserved. 
|bamboo|

.. |copy| unicode:: 0xA9 .. copyright sign
.. |MLMS (TM)| unicode:: MLMS U+2122
   .. with trademark sign
.. |---| unicode:: U+02014 .. em dash
   :trim:

.. |bamboo| unicode:: 0x1F024 .. bamboo

Strings
==============

Python can store and manipulate strings. Strings can be enclosed in single or double quotes. There are a number of string methods you can use to manipulate and work with strings

- `strings <https://docs.python.org/3/tutorial/introduction.html#strings>`_

Besides numbers, Python can also manipulate strings, which can be expressed in several ways. They can be enclosed in single quotes ('...') or double quotes ("...") with the same result [1]_ can be used to escape quotes:

.. code:: python
   
   >>> 'spam eggs'  # single quotes
   'spam eggs'
   >>> 'doesn\'t'  # use \' to escape the single quote...
   "doesn't"
   >>> "doesn't"  # ...or use double quotes instead
   "doesn't"
   >>> '"Yes," they said.'
   '"Yes," they said.'
   >>> "\"Yes,\" they said."
   '"Yes," they said.'
   >>> '"Isn\'t," they said.'
   '"Isn\'t," they said.'

If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:

.. code:: python
   
     >>> print('C:\some\name')  # here \n means newline!
     C:\some
     ame
     >>> print(r'C:\some\name')  # note the r before the quote
     C:\some\name   

String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line. The following example:

.. code:: python

      >>> print("""\
      Usage: thingy [OPTIONS]
           -h                        Display this usage message
           -H hostname               Hostname to connect to
      """)
 
produces the following output (note that the initial newline is not included):
 
.. code:: python

      Usage: thingy [OPTIONS]
           -h                        Display this usage message
           -H hostname               Hostname to connect to
           
Strings can be concatenated (glued together) with the + operator, and repeated with *:

.. code:: python

      >>>
      >>> # 3 times 'un', followed by 'ium'
      >>> 3 * 'un' + 'ium'
      'unununium'
      
Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.

.. code:: python


      >>> 'Py' 'thon'
      'Python'
      
This feature is particularly useful when you want to break long strings:

.. code:: python

      >>> text = ('Put several strings within parentheses '
      ...         'to have them joined together.')
      >>> text
      'Put several strings within parentheses to have them joined together.'

This only works with two literals though, not with variables or expressions:

.. code:: python


      >>> prefix = 'Py'
      >>> prefix 'thon'  # can't concatenate a variable and a string literal
      File "<stdin>", line 1
      prefix 'thon'
                      ^
      SyntaxError: invalid syntax
      
      >>> ('un' * 3) 'ium'
        File "<stdin>", line 1
          ('un' * 3) 'ium'
                         ^
      SyntaxError: invalid syntax
      
If you want to concatenate variables or a variable and a literal, use +:

.. code:: python

   >>> prefix + 'thon'
   'Python'
   
Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one:

.. code:: python

   >>> word = 'Python'
   >>> word[0]  # character in position 0
   'P'
   >>> word[5]  # character in position 5
   'n'
   
Indices may also be negative numbers, to start counting from the right:

.. code:: python

   >>> word[-1]  # last character
   'n'
   >>> word[-2]  # second-last character
   'o'
   >>> word[-6]
   'P'
   
Note that since -0 is the same as 0, negative indices start from -1.

In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain substring:

.. code:: python


      >>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
      'Py'
      >>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
      'tho'

Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s:

.. code:: python

     >>> word[:2] + word[2:]
     'Python'
     >>> word[:4] + word[4:]
     'Python'
     
Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.

.. code:: python

      >>> word[:2]   # character from the beginning to position 2 (excluded)
      'Py'
      >>> word[4:]   # characters from position 4 (included) to the end
      'on'
      >>> word[-2:]  # characters from the second-last (included) to the end
      'on'
      
One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0. Then the right edge of the last character of a string of n characters has index n, for example:

.. code:: python

    +---+---+---+---+---+---+
   | P | y | t | h | o | n |
    +---+---+---+---+---+---+
    0   1   2   3   4   5   6
   -6  -5  -4  -3  -2  -1
   
The first row of numbers gives the position of the indices 0…6 in the string; the second row gives the corresponding negative indices. The slice from i to j consists of all characters between the edges labeled i and j, respectively.

For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds. For example, the length of word[1:3] is 2.

Attempting to use an index that is too large will result in an error:

.. code:: python


   >>> word[42]  # the word only has 6 characters
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   IndexError: string index out of range
   
However, out of range slice indexes are handled gracefully when used for slicing:

.. code:: python

   >>> word[4:42]
   'on'
   >>> word[42:]
   ''
   
Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error:

.. code:: python

   >>> word[0] = 'J'
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'str' object does not support item assignment
   >>> word[2:] = 'py'
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'str' object does not support item assignment
   
If you need a different string, you should create a new one:

.. code:: python

   >>> 'J' + word[1:]
   'Jython'
   >>> word[:2] + 'py'
   'Pypy'
   
The built-in function len() returns the length of a string:

.. code:: python

   >>> s = 'supercalifragilisticexpialidocious'
   >>> len(s)
   34

- `string methods <https://docs.python.org/3/library/stdtypes.html#string-methods>`_

.. py:class:: str(object=b'', encoding='utf-8', errors='strict')

   Return a str version of object. See str() for details.
   
   str is the built-in string class. For general information about strings, see Text Sequence Type — str.

.. literalinclude:: strings_in_variables.py
   :language: python
   :linenos:

Converting to string values

.. literalinclude:: string_functions.py 
   :language: python
   :linenos:

- `str <https://docs.python.org/3/library/functions.html#func-str>`_

When naming variables follow the PEP-8 Style Guide for Python Code

- `PEP-8 Style Guide <https://www.python.org/dev/peps/pep-0008/#naming-conventions>`_

.. literalinclude:: format_strings.py
   :language: python
   :linenos:

.. literalinclude:: combine_strings.py
   :language: python
   :linenos:

String Concepts
================

Let's get in and take a look at probably one of the most common things that you'll be doing in programming, and that is working with strings.
Now, when it comes to strings and actually just variables in Python, it's relatively straightforward to take a string and store it inside of a variable.

Now as a real quick aside, if you're not already familiar with variables, variables windup acting as placeholders inside of your code for some values.

.. raw:: html

    <video poster="../../_static/images/GCC.png" width="690" height="402" controls="controls">
        <source src="//huya-w21.huya.com/2022/344499848/yuanhua/b2a3b82de7a64afb08ee5ddeeee9f903.mp4" type="video/mp4">
    </video>

Demo: Strings
=============

So let's take a look at some of those neat little string functions that we saw previously.

So I'm going to start off by just simply typing in first_name equals Christopher, we'll just skip that stored, and then last_name, equals Harrison.

Perfect. Now, like we have already seen, we can concatenate things together by using that plus sign. So if I say "Print" and I say "first_name," and by the way, a little IntelliSense Beta functionality for you.

.. raw:: html

    <video poster="../../_static/images/GCC.png" width="690" height="402" controls="controls">
        <source src="//huya-w20.huya.com/2022/344510334/yuanhua/236f68b8914c7c3c3a829c20f8a8d582.mp4" type="video/mp4">
    </video>

PPT Demonstrations
===================

.. raw:: html

    <div class="slideshow">

            <iframe style="border: none; width: 100%; height: 402px" name="embedded_lecture1_anywhere" src="../../_static/P4All_Lecture5/main.html"></iframe>

        </div>

Challenges time
=================

Check the following script and try to find the mistake:

.. literalinclude:: code_challenge.py
   :language: python
   :linenos:

solutions:

.. literalinclude:: code_challenge_solution.py
   :language: python
   :linenos:


.. rubric:: Footnotes

.. [1] Unlike other languages, special characters such as \n have the same meaning with both single ('...') and double ("...") quotes. The only difference between the two is that within single quotes you don’t need to escape " (but you have to escape \') and vice versa.
