import numpy as np

traffic = np.random.randint(50, 501, size=30)

avg_traffic = np.mean(traffic)

peak_mask = traffic > traffic.mean()
peak_days = np.sum(peak_mask)
peak_traffic = traffic[peak_mask]

marked_traffic = np.where(traffic > 450, -1, traffic)

print("Середній трафік:", round(avg_traffic, 2), "ГБ")
print("Кількість пікових днів:", peak_days)
print("Трафік у пікові дні:", peak_traffic)
print("Масив з позначками (-1 > 450 ГБ):", marked_traffic)
