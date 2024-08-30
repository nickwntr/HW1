from divmthds import fake_math
from divmthds import true_math
results = []
results.append(fake_math.divide(12, 6))
results.append(fake_math.divide(150, 0))
results.append(true_math.divide(77, 11))
results.append(true_math.divide(1560, 0))
print(results)
