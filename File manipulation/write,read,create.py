#  Creating, Reading and writing in file 'lorem.txt'
with open('lorem.txt', 'w+') as file:
    #  Writing
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.write('Line 3\n')

    #  Reading
    file.seek(0, 0)
    print('-' * 30)
    print('\nReading file: \n')
    print(file.read())
    print('-' * 30)

    file.seek(0, 0)
    print('\nReading line(x3): \n')
    print(file.readline(), end='')
    print(file.readline(), end='')
    print(file.readline())
    print('-' * 30)

    file.seek(0, 0)
    print('\nReading lines(for x in y:): \n')
    for line in file.readlines():
        print(line, end='')
    print('')
    print('-' * 30)
