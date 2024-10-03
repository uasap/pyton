import numpy as np
from scipy import stats

# Количество конверсий для каждого источника
conversions = np.array([25000, 30000, 32000])

# Предположим, что у всех источников было одинаковое количество трафика (например, 100000 пользователей на каждый источник)
total_visitors = 100000
conversion_rates = conversions / total_visitors

# Используем Z-тест для сравнения пропорций конверсий между тремя источниками
# H0: Конверсии одинаковы для всех источников

# Рассчитаем среднюю конверсию и стандартную ошибку
mean_conversion_rate = np.mean(conversion_rates)
std_error = np.sqrt(mean_conversion_rate * (1 - mean_conversion_rate) / total_visitors)

# Z-статистика для каждого источника
z_scores = (conversion_rates - mean_conversion_rate) / std_error

# p-value для каждого источника (двусторонний тест)
p_values = stats.norm.sf(abs(z_scores)) * 2

# Вывод результатов
for i, (rate, z, p) in enumerate(zip(conversion_rates, z_scores, p_values)):
    print(f"Источник {i+1}:")
    print(f"  Конверсия: {rate * 100:.2f}%")
    print(f"  Z-статистика: {z:.4f}")
    print(f"  P-значение: {p:.4f}")
    print()

# Проверка на значимость различий
alpha = 0.05
if any(p < alpha for p in p_values):
    print("Различия между конверсиями статистически значимы.")
else:
    print("Различия между конверсиями незначимы.")
