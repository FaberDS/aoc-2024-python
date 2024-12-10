def split_rows(arr):
    return [list(row) for row in arr.splitlines()]

def split_2d_int_array(str):
    return [[int(char) for char in row] for row in str.split('\n')]