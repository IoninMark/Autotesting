from capitalize import capitalize

if capitalize('hello') != 'Hello':
    raise Exception('Function works wrong!')

if capitalize('') != '':
    raise Exception('Function works wrong!')

print('All tests passed!')