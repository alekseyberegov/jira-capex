
def flatten_json(y, delimeter='_'):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + delimeter)
        elif type(x) is list:
            out[name + 'len'] = len(x)
            for i, a in enumerate(x):
                flatten(a, name + str(i) + delimeter)
        else:
            out[name[:-1]] = x

    flatten(y)
    return out