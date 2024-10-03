import numpy as np
from scipy import stats

# Данные
mean_a = 360  # Средняя для группы A
std_a = 40    # Отклонение для группы A
n_a = 9802    # Количество в группе A

mean_b = 352  # Средняя для группы B
std_b = 58    # Отклонение для группы B
n_b = 9789    # Количество в группе B

# Шаг 1: Расчет стандартной ошибки (SE) для обеих групп
se_a = std_a / np.sqrt(n_a)
se_b = std_b / np.sqrt(n_b)

# Шаг 2: Расчет Z-статистики
z = (mean_a - mean_b) / np.sqrt(se_a**2 + se_b**2)

# Шаг 3: Расчет p-value для двухстороннего теста
p_value = stats.norm.sf(abs(z)) * 2

# Шаг 4: Уровень значимости (alpha) для доверия 80%
alpha = 0.20

# Шаг 5: Проверка значимости
is_significant = p_value < alpha

# Шаг 6: Рекомендация о версии для продакшн
recommended_version = "A" if mean_a > mean_b else "B"

print(z, p_value, is_significant, recommended_version)
