## Telegram Bot (Python)

### Setup

1. Create and get your bot token from BotFather in Telegram.
2. Create `.env` with your token (or copy `env.sample` to `.env`):

```
TELEGRAM_BOT_TOKEN=123456:ABC...
```

3. Create and activate virtual environment (optional but recommended).
4. Install dependencies:

```
pip install -r requirements.txt
```

### Run

```
python file.py
```

The bot uses long polling and responds to `/start` and echoes text messages.

### SourceCraft Integration

#### Импорт в SourceCraft

1. **Импортируйте репозиторий в SourceCraft**:
   - Перейдите в SourceCraft и создайте новый проект
   - Импортируйте этот репозиторий или зеркалируйте его
   - SourceCraft автоматически обнаружит файлы конфигурации

2. **Настройка секретов**:
   - В SourceCraft добавьте секрет `TELEGRAM_BOT_TOKEN`
   - Перейдите в настройки проекта → Секреты
   - Добавьте ваш токен бота

3. **CI/CD Pipeline**:
   - Файл `.sourcecraft/ci.yaml` настроен для автоматического тестирования
   - При каждом push в main/develop запускаются тесты
   - Docker образ собирается автоматически

4. **Развёртывание**:
   - Используйте Docker для контейнеризации: `docker build -t telegram-bot .`
   - Запуск: `docker run -e TELEGRAM_BOT_TOKEN=your_token telegram-bot`
   - Или используйте встроенные возможности SourceCraft для деплоя

#### Структура проекта для SourceCraft

```
project/
├── .sourcecraft/
│   └── ci.yaml          # CI/CD конфигурация
├── .gitignore           # Игнорируемые файлы
├── Dockerfile           # Контейнеризация
├── file.py             # Основной код бота
├── requirements.txt    # Python зависимости
├── env.sample         # Пример переменных окружения
└── README.md          # Документация
```

### Development

- **Локальная разработка**: `python file.py`
- **Тестирование**: `python -c "import file; print('✅ OK')"`
- **Docker**: `docker build -t bot . && docker run -e TELEGRAM_BOT_TOKEN=token bot`

### Notes

- Requires Python 3.10+ for `python-telegram-bot` v21.
- Do not commit your real `.env`.
- If you cannot create dotfiles on your system, use `env.sample`.
- SourceCraft обеспечивает безопасное хранение секретов и автоматизацию CI/CD.

