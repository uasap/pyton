import math
from statsmodels.stats.power import NormalIndPower

# Данные задачи
current_conversion = 0.05  # Текущая конверсия 5%
expected_lift = 0.002  # Ожидаемый прирост 0.2%
alpha = 0.03  # Уровень доверия 97% (1 - 0.97 = 0.03)
power = 0.87  # Уровень мощности 87%
traffic_per_month = 40000  # Трафик в месяц

# Расчет минимально необходимого размера выборки для А/Б-теста
effect_size = (current_conversion + expected_lift - current_conversion) / math.sqrt(current_conversion * (1 - current_conversion))
analysis = NormalIndPower()
sample_size = analysis.solve_power(effect_size=effect_size, alpha=alpha, power=power, alternative='two-sided')

# Расчет дней, необходимых для теста
total_traffic_needed = sample_size * 3  # Три источника трафика
days_needed = total_traffic_needed / traffic_per_month * 30  # Количество дней для теста

print(sample_size, days_needed)