import sys

if __name__ == '__main__':
    n = len(sys.argv)
    i = 0
    print('=== Command Quest ===')
    print(f'Program name: {sys.argv[i]}')
    i += 1
    if n - 1 != 0:
        print(f'Arguments received: {n - 1}')
    else:
        print('No arguments provided!')
    while i < n:
        if i > 0:
            print(f'Argument {i}: {sys.argv[i]}')
        i += 1
    print(f'Total arguments: {n}')
