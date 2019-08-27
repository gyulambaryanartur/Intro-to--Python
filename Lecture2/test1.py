import sys


print('Script name:', str(sys.argv[0]))
print('Arguments:', str(sys.argv[1:]))
print('# of arguments:', len(sys.argv[1:]))

#naming arguments to use in code
a = str(sys.argv[1])
print('First argument:', a)