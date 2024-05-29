def mean(p_array):
    v_sum = 0
    for i in p_array:
        v_sum += i
    v_mean = v_sum / len(p_array)
    return v_mean

def gen(p_age):
    v_gen = int(p_age / 10) * 10
    return v_gen