# coding: utf-8
import math
import random
random.seed(123)

a = [random.randint(-25, 85) / 10.0 for _ in range(8)]
b = [random.randint(-50, 70) / 10.0 for _ in range(8)]
print(a)
print(b)

mean_a = sum(a) / 8
var_a = sum([(v-mean_a)**2 for v in a]) / 8
print(mean_a, var_a)

mean_b = sum(b) / 8
var_b = sum([(v-mean_b)**2 for v in b]) / 8
print(mean_b, var_b)

epsilon = 1e-5
normalized_a = [(v - mean_a)/math.sqrt(var_a + epsilon) for v in a]
normalized_b = [(v - mean_b)/math.sqrt(var_b + epsilon) for v in b]
print([round(v, 3) for v in normalized_a])
print([round(v, 3) for v in normalized_b])


print(sum(normalized_a)/8)
print(sum(normalized_b)/8)
