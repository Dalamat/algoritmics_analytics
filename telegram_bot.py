"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""
from log_config_tg import logger
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
from telegram_client import send_group_message
import envs
from update_tables import update_table, PARAMETER_SETS

TOKEN = envs.telegram_bot_token

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Invoices Partial", callback_data="Invoices Partial"),
            InlineKeyboardButton("Invoices Full", callback_data="Invoices Full"),
        ],
        [
            InlineKeyboardButton("AMO Leads", callback_data="AMO Leads"),
            InlineKeyboardButton("AMO Budgets", callback_data="AMO Budgets")
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Please choose:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    data = query.data
    username = query.from_user.username
    chat_id = query.message.chat_id  # Получаем ID чата

    await query.answer()
    await query.edit_message_text(text=f"Selected option: {data}. In progress")
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery

    logger.info(f"{data} update has been requested by {username} via BOT")
    await send_group_message(f"{data} update has been requested by @{username} via BOT")
    match data:
        case "Invoices Partial":
            update_table(**PARAMETER_SETS["invoices_filter"])
        case "Invoices Full":
            update_table(**PARAMETER_SETS["invoices_full"])
        case "AMO Leads":
            update_table(**PARAMETER_SETS["leads_full"])
        case "AMO Budgets":
            update_table(**PARAMETER_SETS["budgets_full"])
    logger.info(f"{data} update has been completed")
    await send_group_message(f"{data} update has been completed. @{username}")

    await context.bot.send_message(chat_id, text=f"Selected option: {data}. Finished")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()