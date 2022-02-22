
def flatten_json(y, delimeter='_'):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + delimeter)
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + delimeter)
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out