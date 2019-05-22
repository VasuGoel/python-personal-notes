# pathlib offers classes representing filesystem paths with semantics appropriate for different operating systems
from pathlib import Path


# exists() method of Path class checks if certain directory/file exists and returns a boolean
path = Path('test')
print(path.exists())

path = Path('./test/test.py')
print(path.exists())


# Create new directory inside current directory (from where this 'path.py' file reside)
path = Path('from_python_program')
if not path.exists():
    print(path.mkdir())     # Returns None
else:
    print('Directory already exists.')


# Remove directory (if it doesn't have any content in it)
path = Path('delete-me')
if path.exists():
    print(path.rmdir())     # Returns None
else:
    print('No such directory exists.')


# List all files by iterating over a glob object (The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in arbitrary order.)
path = Path('../')
print(f'\nIterating over {path.glob("*.*")} ...\n')

print('List of files in the previous directory ...')
for file in path.glob('*.*'):
    print(file)
