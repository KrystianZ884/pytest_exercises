'''4. Testing File I/O

Write tests for a function write_to_file(filename, content) that writes content to a file and a function read_from_file(filename) that reads the content back.

Functions to Test:
'''

def write_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def read_from_file(filename):
    with open(filename, 'r') as f:
        return f.read()