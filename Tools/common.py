import re
def readlinesfromfile(file):
    with open(file) as f:
        r = f.read()
    return r.splitlines()

def readfile(file):
    with open(file) as f:
        r = f.read()
    return r

def s_to_pos_list(s):
    return re.findall(r'\d+', s)
def s_to_int_list(s):
    return re.findall(r'-?\d+', s)

def bin_string_to_int(bstring):
    ans = 0
    for i in range(len(bstring)-1, -1, -1):
        if bstring[i] == '1':
            ans += 2**(len(bstring)-i-1)
    return ans