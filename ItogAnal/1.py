import pandas as pd
from scipy import stats

# Шаг 1: Загрузка данных
data = pd.read_csv('ab_stats.csv')

# Шаг 2: Расчет ARPPU для каждой группы
data['ARPPU'] = data['revenue'] / data['num_purchases']
arppu_a = data[data['ab_group'] == 'A']['ARPPU']
arppu_b = data[data['ab_group'] == 'B']['ARPPU']

# Шаг 3: Проверка нормальности распределения
p_value_shapiro_a = stats.shapiro(arppu_a)[1]  # p-value для группы A
p_value_shapiro_b = stats.shapiro(arppu_b)[1]  # p-value для группы B

# Определение, какой тест использовать
if p_value_shapiro_a < 0.05 or p_value_shapiro_b < 0.05:
    # Если хотя бы одна группа не нормально распределена, используем U-тест
    t_test = False
else:
    # Если обе группы нормально распределены, используем t-тест
    t_test = True

# Шаг 4: Проведение теста
if t_test:
    t_stat, p_value = stats.ttest_ind(arppu_a, arppu_b)
else:
    u_stat, p_value = stats.mannwhitneyu(arppu_a, arppu_b)

# Шаг 5: Выводы и рекомендации
alpha = 0.05
is_significant = p_value < alpha

# Результаты
print(f'P-value: {p_value}')
print(f'Статистическая значимость: {"Да" if is_significant else "Нет"}')
print(f'Рекомендуемая версия: {"A" if arppu_a.mean() > arppu_b.mean() else "B"}')