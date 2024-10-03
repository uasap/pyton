from scipy import stats

# Данные
sample_size = 2350
p_value_shapiro = 0.00002
alpha = 0.05

# Шаг 1: Проверка нормальности
if p_value_shapiro < alpha:
    normality_result = "Отвергаем нулевую гипотезу о нормальности распределения."
else:
    normality_result = "Не отвергаем нулевую гипотезу о нормальности распределения."

# Шаг 2: Рекомендация по выбору статистического критерия
recommended_test = "Лучше использовать тест Манна-Уитни (U-тест), так как данные не нормально распределены."

print(normality_result, recommended_test)
