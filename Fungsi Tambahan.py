def jml_rows():
    with open ('dummy.csv','r') as f:
        num_rows = 0
        lines = f.readlines()
        for line in lines:
            num_rows += 1
    return num_rows

def my_split(string, delimiter):
    substrings = []
    current_substring = ''
    for i in range (len(string)-1):
        if string[i] == delimiter:
            substrings += [current_substring]
            current_substring = ''
        elif string[i]+string[i+1]!='\n':
            current_substring += string[i]
    substrings += [current_substring]
    return substrings

def matrix_csv():
    with open ('dummy.csv','r') as f:
        num_rows=0
        lines = f.readlines()
        for line in lines:
            num_rows += 1
        matrixx = ['' for i in range(num_rows)]
        for i in range(num_rows):
            line=my_split(lines[i],';')
            matrixx[i]=line
    return matrixx





