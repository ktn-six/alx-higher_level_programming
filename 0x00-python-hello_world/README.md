0. Run Python file
mandatory
Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE

1. Run inline
mandatory
Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE

2. Hello, print
mandatory
Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.3. Print integer
mandatory
Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

You can find the source code here
The output of the script should be:
the number, followed by Battery street,
followed by a new line
You are not allowed to cast the variable number into a string
Your code must be 3 lines long



3. Print integer
mandatory
Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

You can find the source code here
The output of the script should be:
the number, followed by Battery street,
followed by a new line
You are not allowed to cast the variable number into a string
Your code must be 3 lines long



4. Print float
mandatory
Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

You can find the source code here
The output of the program should be:
Float:, followed by the float with only 2 digits
followed by a new line
You are not allowed to cast number to string
You have to use f-strings



5. Print string
mandatory
Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

You can find the source code here
The output of the program should be:
3 times the value of str
followed by a new line
followed by the 9 first characters of str
followed by a new line
You are not allowed to use any loops or conditional statement
Your program should be maximum 5 lines long



6. Play with strings
mandatory
Complete this source code to print Welcome to Holberton School!

You can find the source code here
You are not allowed to use any loops or conditional statements.
You have to use the variables str1 and str2 in your new line of code
Your program should be exactly 5 lines long



7. Copy - Cut - Paste
mandatory
Complete this source code

You can find the source code here
You are not allowed to use any loops or conditional statements
Your program should be exactly 8 lines long
word_first_3 should contain the first 3 letters of the variable word
word_last_2 should contain the last 2 letters of the variable word



8. Create a new sentence
mandatory
Complete this source code to print object-oriented programming with Python, followed by a new line.

You can find the source code here
You are not allowed to use any loops or conditional statements
Your program should be exactly 5 lines long
You are not allowed to create new variables
You are not allowed to use string literals


















Welcome to the Python world!

The first projects are more "C-oriented" - no tricks, no funky syntax - simple!
If you've already played with Python, don't worry, fun things will come.
You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
Like C, Python also has a linter / style guide like Betty, called PEP8, also now known as PyCode.

Enjoy!

- Guillaume
Resources
Read or watch:

The Python tutorial (only the first three chapters below)
Whetting Your Appetite
Using the Python Interpreter
An Informal Introduction to Python (Read up until “3.1.2. Strings” included)
How To Use String Formatters in Python 3
Learn to Program
Pycodestyle – Style Guide for Python Code
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:























A README.md file at the root of the repo, containing a description of the repository





Allowed editors: vi, vim, emacs




All your files must be executable




Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl





All your header files should be include guarded





Explicit is better than implicit.






Although practicality beats purity.



There should be one-- and preferably only one --obvious way to do it.



If the implementation is hard to explain, it's a bad idea.

Namespaces are one honking great idea -- let's do more of those!
Pycodestyle
Pycodestyle is now the new standard of Python style code





Quiz questions
Great! You've completed the quiz successfully! Keep going! (Show quiz)
Tasks
0. Run Python file
mandatory
Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE

guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 0-run
   
1. Run inline
mandatory
Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE

guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Best School: 98
guillaume@ubuntu:~/py/0x00$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 1-run_inline
   
2. Hello, print
mandatory
Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

Use the function print
guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 2-print.py
   
3. Print integer
mandatory
Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

You can find the source code here
The output of the script should be:
the number, followed by Battery street,
followed by a new line
You are not allowed to cast the variable number into a string
Your code must be 3 lines long
You have to use f-strings tips
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 3-print_number.py
   
4. Print float
mandatory
Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

You can find the source code here
The output of the program should be:
Float:, followed by the float with only 2 digits
followed by a new line
You are not allowed to cast number to string
You have to use f-strings
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 4-print_float.py
   
5. Print string
mandatory
Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

You can find the source code here
The output of the program should be:
3 times the value of str
followed by a new line
followed by the 9 first characters of str
followed by a new line
You are not allowed to use any loops or conditional statement
Your program should be maximum 5 lines long
guillaume@ubuntu:~/py/0x00$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/0x00$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 5-print_string.py
   
6. Play with strings
mandatory
Complete this source code to print Welcome to Holberton School!

You can find the source code here
You are not allowed to use any loops or conditional statements.
You have to use the variables str1 and str2 in your new line of code
Your program should be exactly 5 lines long
guillaume@ubuntu:~/py/0x00$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/0x00$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 6-concat.py
   
7. Copy - Cut - Paste
mandatory
Complete this source code

You can find the source code here
You are not allowed to use any loops or conditional statements
Your program should be exactly 8 lines long
word_first_3 should contain the first 3 letters of the variable word
word_last_2 should contain the last 2 letters of the variable word
middle_word should contain the value of the variable word without the first and last letters
guillaume@ubuntu:~/py/0x00$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on




Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 7-edges.py
   
8. Create a new sentence
mandatory
Complete this source code to print object-oriented programming with Python, followed by a new line.

You can find the source code here
You are not allowed to use any loops or conditional statements
Your program should be exactly 5 lines long
You are not allowed to create new variables
You are not allowed to use string literals
guillaume@ubuntu:~/py/0x00$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/0x00$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/0x00$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 8-concat_edges.py
   
9. Easter Egg
mandatory
Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)
