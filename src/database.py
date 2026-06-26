import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'database', 'tickets.db')

def get_connection():
    """Возвращает соединение с базой данных"""
    return sqlite3.connect(DB_PATH)

def init_db():
    """Создаёт таблицы, если их нет"""
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Создаём таблицу заявок
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT NOT NULL DEFAULT 'новая',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Создаём таблицу комментариев
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ticket_id INTEGER NOT NULL,
                text TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
            )
        ''')
        
        conn.commit()
        print("База данных инициализирована")

def get_all_tickets():
    """Возвращает все заявки"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tickets ORDER BY created_at DESC')
        return cursor.fetchall()

def get_ticket_by_id(ticket_id):
    """Возвращает заявку по id"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tickets WHERE id = ?', (ticket_id,))
        return cursor.fetchone()

def get_comments_by_ticket(ticket_id):
    """Возвращает все комментарии для заявки"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM comments WHERE ticket_id = ? ORDER BY created_at DESC', (ticket_id,))
        return cursor.fetchall()

def create_ticket(title, description, status='новая'):
    """Создаёт новую заявку"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO tickets (title, description, status) VALUES (?, ?, ?)',
            (title, description, status)
        )
        conn.commit()
        return cursor.lastrowid

def update_ticket_status(ticket_id, status):
    """Обновляет статус заявки"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE tickets SET status = ? WHERE id = ?',
            (status, ticket_id)
        )
        conn.commit()

def add_comment(ticket_id, text):
    """Добавляет комментарий к заявке"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO comments (ticket_id, text) VALUES (?, ?)',
            (ticket_id, text)
        )
        conn.commit()
        return cursor.lastrowid

def get_tickets_by_status(status):
    """Фильтрация заявок по статусу"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tickets WHERE status = ? ORDER BY created_at DESC', (status,))
        return cursor.fetchall()