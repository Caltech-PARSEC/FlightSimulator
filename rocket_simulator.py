def run():
    '''
    Reads data from a file 'data.txt' where each line is of the form
    'key:value' without quotes, and returns a dictionary of the data.
    '''

    file = open('data.txt')

    data = {}
    for line in file:
        # Remove the newline character from line
        line = line[:-1]

        # Get the key and value
        pos = line.index(':')
        key = line[:pos]
        val = line[pos + 1:]

        data[key] = val

    return data
