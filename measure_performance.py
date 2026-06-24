import time
import random

# ========== ФУНКЦИЯ ПОИСКА (которую будем измерять) ==========
def search_tasks(tasks, keyword):
    """Ищет задачи, содержащие keyword в названии"""
    result = []
    for task in tasks:
        if keyword.lower() in task['title'].lower():
            result.append(task)
    return result

# ========== ФУНКЦИЯ СОЗДАНИЯ ТЕСТОВЫХ ДАННЫХ ==========
def generate_tasks(count):
    """Создаёт список задач с случайными названиями"""
    tasks = []
    words = ["купить", "сделать", "написать", "прочитать", "проверить", 
             "отправить", "получить", "обновить", "удалить", "создать",
             "отчёт", "проект", "задача", "работа", "встреча", "звонок",
             "план", "цель", "результат", "документ"]
    
    for i in range(count):
        title = f"{random.choice(words)} {random.choice(words)} {i}"
        tasks.append({
            "id": i,
            "title": title,
            "status": random.choice(["new", "in_progress", "done"])
        })
    return tasks

# ========== ФУНКЦИЯ ИЗМЕРЕНИЯ ==========
def measure_search(tasks, keyword, repeats=5):
    """Измеряет время поиска несколько раз и возвращает среднее"""
    times = []
    for _ in range(repeats):
        start = time.perf_counter()
        search_tasks(tasks, keyword)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)

# ========== ЗАПУСК ИЗМЕРЕНИЙ ==========
print("=" * 50)
print("ИЗМЕРЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ПОИСКА")
print("=" * 50)

# Наборы данных
sizes = [10, 100, 1000]
keyword = "проект"

results = []

for size in sizes:
    print(f"\nГенерация {size} задач...")
    tasks = generate_tasks(size)
    
    print(f"Измерение поиска по {size} задачам...")
    avg_time = measure_search(tasks, keyword)
    
    print(f"  Среднее время: {avg_time:.6f} секунд")
    results.append({"size": size, "avg_time": avg_time})

# ========== ВЫВОД ИТОГОВОЙ ТАБЛИЦЫ ==========
print("\n" + "=" * 50)
print("ИТОГОВАЯ ТАБЛИЦА")
print("=" * 50)
print(f"{'Объём данных':<15} {'Среднее время (сек)':<20}")
print("-" * 35)
for r in results:
    print(f"{r['size']:<15} {r['avg_time']:<20.6f}")