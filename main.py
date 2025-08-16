from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from utils.logger import logger
from utils.file_saver import save_file
from config import TELEGRAM_TOKEN


async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    document = update.message.document
    if not document:
        return
    file = await document.get_file()
    file_bytes = await file.download_as_bytearray()
    path = save_file(document.file_name, file_bytes)
    logger.info("Saved document %s from user %s", path, update.effective_user.id)


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    photo = update.message.photo
    if not photo:
        return
    file = await photo[-1].get_file()
    file_bytes = await file.download_as_bytearray()
    path = save_file(f"{file.file_unique_id}.jpg", file_bytes)
    logger.info("Saved photo %s from user %s", path, update.effective_user.id)


def main() -> None:
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    logger.info("Bot started")
    application.run_polling()


if __name__ == "__main__":
    main()
