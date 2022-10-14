from telegram import (
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove, 
    Update, 
    InlineKeyboardButton, 
    InlineKeyboardMarkup,
    InputTextMessageContent,
    InlineQueryResult
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
    InlineQueryHandler
)

import django
django.setup()

from game.models import Player
from secret import TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    message = update.message
    user_id = message.from_user.id

    Player.objects.get_or_create(
        user_id
    )
    await update.message.reply_text(
        "Hey!, I'm *XO* Bot.\nWanna play with me?",
    )

    return -1



async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the inline query. This is run when you type: @botusername <query>"""
    query = update.inline_query.query

    if query == "":
        return

    keyboard = [
        [
            InlineKeyboardButton('Wanna Play', callback_data=1)
        ]
    ]
    markup = InlineKeyboardMarkup(keyboard)

    results = [
        InlineQueryResult(
            id='1',
            title="XO",
            input_message_content=InputTextMessageContent('Wanna Play'),
            reply_markup=markup
        ),
    ]

    await update.inline_query.answer(results)


async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    user_id = query.from_user.id

    Player.objects.get_or_create(
        user_id
    )
    # keyboard = [
    #     [
    #         InlineKeyboardButton('I wanna join!', callback_data=)
    #     ]
    # ]
    # markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Send this message to your friend!"
    )

    return -1


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(InlineQueryHandler(inline_query))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()