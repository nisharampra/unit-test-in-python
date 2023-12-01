def mean(vals):
    sum = vals[0] + vals[1] + vals[2]
    return sum / 3

def mean(vals):
    sum = 0.0
    for i in range(len(vals)):
        sum += vals[i]
    return sum / len(vals)
