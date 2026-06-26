-- ============================================
-- Схема базы данных для сервиса заявок
-- ============================================

-- Удаляем таблицы, если они уже существуют
DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS tickets;

-- ============================================
-- Таблица заявок
-- ============================================
CREATE TABLE tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT NOT NULL DEFAULT 'новая',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- Таблица комментариев
-- ============================================
CREATE TABLE comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_id INTEGER NOT NULL,
    text TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);