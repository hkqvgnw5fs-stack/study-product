from src.database import *

# Инициализируем базу
init_db()

print("=" * 50)
print("ПРОВЕРКА РАБОТЫ БАЗЫ ДАННЫХ")
print("=" * 50)

# 1. Все заявки
print("\n1. ВСЕ ЗАЯВКИ:")
tickets = get_all_tickets()
for t in tickets:
    print(f"  #{t[0]} | {t[1]} | {t[3]} | {t[4]}")

# 2. Одна заявка по id
print("\n2. ЗАЯВКА #1:")
ticket = get_ticket_by_id(1)
if ticket:
    print(f"  Тема: {ticket[1]}")
    print(f"  Описание: {ticket[2]}")
    print(f"  Статус: {ticket[3]}")
    print(f"  Дата: {ticket[4]}")

# 3. Комментарии к заявке #1
print("\n3. КОММЕНТАРИИ К ЗАЯВКЕ #1:")
comments = get_comments_by_ticket(1)
for c in comments:
    print(f"  #{c[0]} | {c[2]} | {c[3]}")

# 4. Фильтрация по статусу
print("\n4. ЗАЯВКИ СО СТАТУСОМ 'новая':")
new_tickets = get_tickets_by_status('новая')
for t in new_tickets:
    print(f"  #{t[0]} | {t[1]} | {t[4]}")

# 5. Создание новой заявки
print("\n5. СОЗДАНИЕ НОВОЙ ЗАЯВКИ:")
new_id = create_ticket('Тестовая заявка', 'Проверка работы базы данных')
print(f"  Создана заявка #{new_id}")

# 6. Изменение статуса
print("\n6. ИЗМЕНЕНИЕ СТАТУСА:")
update_ticket_status(new_id, 'в работе')
ticket = get_ticket_by_id(new_id)
print(f"  Заявка #{new_id} теперь имеет статус: {ticket[3]}")

# 7. Добавление комментария
print("\n7. ДОБАВЛЕНИЕ КОММЕНТАРИЯ:")
comment_id = add_comment(new_id, 'Тестовый комментарий')
print(f"  Добавлен комментарий #{comment_id}")

# 8. Проверка сохранения данных
print("\n8. ПРОВЕРКА СОХРАНЕНИЯ:")
print("  Данные сохранены в БД. Перезапустите программу, чтобы убедиться.")