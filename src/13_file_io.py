"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""
import os

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"


def opened():
    f = open('foo.txt', 'r')
    contents = f.read()
    print(contents)
    f.close()


opened()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain


file = 'bar.txt'
written = open(file, 'w')
written.write('\nLorem ipsum dolor sit amet, \n'
              'consectetur adipiscing elit, \n'
              'sunt in culpa qui officia deserunt mollit anim id est laborum.\n')

written.close()


def opened():
    f = open('bar.txt', 'r')
    contents = f.read()
    print(contents)
    f.close()


opened()


os.remove('bar.txt')
print('File is deleted!')
