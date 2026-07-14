import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.database import get_connection, init_db

def seed_data():
    """Заполняет базу тестовыми данными"""
    
    # Проверяем, есть ли уже данные
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM tickets')
        count = cursor.fetchone()[0]
        
        if count > 0:
            print(f"В базе уже есть {count} заявок. Пропускаем вставку.")
            return
    
    # Вставляем тестовые заявки
    tickets = [
        ('Не работает проектор', 'В аудитории 203 перестал работать проектор.', 'новая'),
        ('Нужна замена клавиатуры', 'Клавиатура в кабинете 105 залипшие клавиши.', 'в работе'),
        ('Не открывается аудитория', 'Дверь в аудиторию 401 не открывается.', 'закрыта'),
        ('Проблема с Wi-Fi', 'В корпусе Б нет интернета.', 'новая'),
        ('Сгоревшая лампа', 'Проектор перестал включаться.', 'в работе')
    ]
    
    with get_connection() as conn:
        cursor = conn.cursor()
        
        for title, description, status in tickets:
            cursor.execute(
                'INSERT INTO tickets (title, description, status) VALUES (?, ?, ?)',
                (title, description, status)
            )
        
        conn.commit()
        print(f"Добавлено {len(tickets)} заявок")
    
    # Вставляем тестовые комментарии
    comments = [
        (1, 'Проблема подтверждена. Вызываем мастера.'),
        (1, 'Мастер будет завтра утром.'),
        (2, 'Ожидается поставка оборудования через 2 дня.'),
        (3, 'Дверь открыли, проблема решена.'),
        (4, 'Проверили роутер. Сейчас перезагрузим.'),
        (5, 'Лампа заказана. Приедет через неделю.')
    ]
    
    with get_connection() as conn:
        cursor = conn.cursor()
        
        for ticket_id, text in comments:
            cursor.execute(
                'INSERT INTO comments (ticket_id, text) VALUES (?, ?)',
                (ticket_id, text)
            )
        
        conn.commit()
        print(f"Добавлено {len(comments)} комментариев")
    
    print("База данных заполнена тестовыми данными!")

if __name__ == "__main__":
    init_db()
    seed_data()