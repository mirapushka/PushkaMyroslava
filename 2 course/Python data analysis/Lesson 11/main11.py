import numpy as np

arr = np.random.normal(loc=70.0, scale=10.0, size=50000)

arr = np.where(arr < 0, 0.0, arr)

danger = (arr < 40.0) | (arr > 95.0)
danger_count = np.sum(danger)
danger_percent = (danger_count / arr.size) * 100

normal = arr[~danger]
mean_val = np.mean(normal)
median_val = np.median(normal)

print("Аварійних точок:", danger_count)
print("Відсоток аварійних:", round(danger_percent, 2), "%")
print("Середнє (норма):", round(mean_val, 2))
print("Медіана (норма):", round(median_val, 2))