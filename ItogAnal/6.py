import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Создание фигуры и осей
fig, ax = plt.subplots(figsize=(12, 8))

# Удаление осей
ax.axis('off')

# Добавление прямоугольников для управленческого процесса
ax.add_patch(mpatches.Rectangle((0.1, 0.85), 0.8, 0.1, ec="black", fc="lightblue"))
ax.text(0.5, 0.9, 'Управленческий процесс', fontsize=12, ha='center')

# Дорожка управленческого процесса
process_steps = [
    '1. Определение ключевых метрик успеха',
    '2. Переговоры с банком о 99% кэшбэке',
    '3. Заключение соглашения',
    '4. Реализация и тестирование кэшбэка',
    '5. Оценка влияния на конверсию'
]

for i, step in enumerate(process_steps):
    ax.add_patch(mpatches.Rectangle((0.1, 0.7 - i*0.1), 0.8, 0.08, ec="black", fc="lightgreen"))
    ax.text(0.5, 0.74 - i*0.1, step, fontsize=10, ha='center')

# Добавление прямоугольников для архитектуры данных
ax.add_patch(mpatches.Rectangle((0.1, 0.4), 0.8, 0.1, ec="black", fc="lightblue"))
ax.text(0.5, 0.45, 'Архитектура данных', fontsize=12, ha='center')

# Дорожка архитектуры данных
data_sources = [
    'Система управления пользователями',
    'Система аналитики',
    'CRM-система',
    'Система платежей'
]

for i, source in enumerate(data_sources):
    ax.add_patch(mpatches.Rectangle((0.1, 0.3 - i*0.1), 0.8, 0.08, ec="black", fc="lightyellow"))
    ax.text(0.5, 0.34 - i*0.1, source, fontsize=10, ha='center')

# Добавление прямоугольников для внутрикомандного взаимодействия
ax.add_patch(mpatches.Rectangle((0.1, 0.1), 0.8, 0.1, ec="black", fc="lightblue"))
ax.text(0.5, 0.15, 'Внутрикомандное взаимодействие', fontsize=12, ha='center')

# Дорожка внутрикомандного взаимодействия
teams = [
    'Команда разработки',
    'Команда аналитиков',
    'Маркетинг',
    'Команда поддержки'
]

for i, team in enumerate(teams):
    ax.add_patch(mpatches.Rectangle((0.1, 0.0 - i*0.1), 0.8, 0.08, ec="black", fc="lightcoral"))
    ax.text(0.5, 0.04 - i*0.1, team, fontsize=10, ha='center')

# Показать схему
plt.title('Техническая архитектура проекта A/B-тестирования', fontsize=16)
plt.show()
