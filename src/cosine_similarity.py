import math

def cosine_simil(a, b):
    dim = len(a)
    sum_a_b = 0
    sum_a_sqr = 0
    sum_b_sqr = 0
    for i in range(dim):
        sum_a_b += a[i] * b[i]
        sum_a_sqr += a[i] * a[i]
        sum_b_sqr += b[i] * b[i]

    norm_a = math.sqrt(sum_a_sqr)
    norm_b = math.sqrt(sum_b_sqr)

    if norm_a == 0 or norm_b == 0:
        return 0
    
    return sum_a_b / (norm_a * norm_b)

if __name__ == "__main__":
    print(cosine_simil([1,1], [0, 1]))
