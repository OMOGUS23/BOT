import asyncio  # Модуль для работы с асинхронным кодом и событийным циклом
import logging  # Встроенная библиотека для логирования
import os  # Доступ к переменным окружения и функциям ОС

from dotenv import load_dotenv  # Загрузка переменных окружения из файла .env
from telegram import Update  # Тип обновления от Telegram (сообщения, команды и т.д.)
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters  # Компоненты фреймворка python-telegram-bot


logging.basicConfig(  # Базовая конфигурация логгера
    level=logging.INFO,  # Уровень логирования: выводить информационные сообщения и выше
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",  # Формат строки лога
)
logger = logging.getLogger(__name__)  # Создаём логгер для текущего модуля


async def handle_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:  # Обработчик команды /start
    user_first = update.effective_user.first_name if update.effective_user else ""  # Имя пользователя, если доступно
    text = f"Привет, {user_first}! Я эхо-бот. Напиши мне что-нибудь."  # Текст приветствия
    await update.message.reply_text(text)  # Отправляем ответное сообщение пользователю


async def handle_echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:  # Обработчик обычных текстовых сообщений
    if update.message and update.message.text:  # Проверяем, что есть текст в сообщении
        await update.message.reply_text(update.message.text)  # Отправляем назад тот же текст (эхо)


async def main() -> None:  # Точка запуска бота (асинхронная)
    load_dotenv()  # Загружаем переменные окружения из .env (если есть)
    token = os.getenv("TELEGRAM_BOT_TOKEN")  # Читаем токен бота из переменной окружения
    if not token:  # Если токен не найден — останавливаем программу с ошибкой
        raise RuntimeError("TELEGRAM_BOT_TOKEN не найден. Установите переменную окружения или .env")  # Сообщение об ошибке

    application = Application.builder().token(token).build()  # Создаём приложение (экземпляр бота) с указанным токеном

    application.add_handler(CommandHandler("start", handle_start))  # Регистрируем обработчик команды /start
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_echo))  # Регистрируем обработчик текстовых сообщений (кроме команд)

    logger.info("Starting bot polling...")  # Пишем в лог, что запускается long polling
    await application.run_polling(close_loop=False)  # Запускаем опрос сервера Telegram (бот начинает принимать обновления)


if __name__ == "__main__":  # Точка входа при запуске файла как скрипта
    try:  # Пытаемся запустить основной асинхронный цикл
        asyncio.run(main())  # Запускаем корутину main() в событийном цикле
    except (KeyboardInterrupt, SystemExit):  # Корректно обрабатываем остановку программы (Ctrl+C, завершение процесса)
        logger.info("Bot stopped.")  # Пишем в лог, что бот остановлен
