import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes


TOKEN = "8758661967:AAHG3q33b2IvcKPISPQtseZl1nAnc9b5hoY"

# --- මෙතනින් ඔයාගේ Accounts Edit කරන්න ---
ACCOUNTS = {
    "range_1000": [
        "🔹 LVL 50 - 1000LKR - DM @Owner",
        "🔹 LVL 52 - 2500LKR - DM @Owner"
    ],
    "range_5000": [
        "🔹 LVL 60 - 6000LKR - DM @Owner",
        "🔹 LVL 65 - 15000LKR - DM @Owner"
    ],
    "range_30000": [
        "🔹 LVL 75 - 35000LKR - DM @Owner"
    ],
    "range_70000": [
        "🔹 LVL 80+ - 90000LKR - DM @Owner"
    ]
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💰 1,000 - 5,000", callback_data='range_1000')],
        [InlineKeyboardButton("💰 5,000 - 20,000", callback_data='range_5000')],
        [InlineKeyboardButton("💰 30,000 - 60,000", callback_data='range_30000')],
        [InlineKeyboardButton("💰 70,000 - 200,000", callback_data='range_70000')],
    ]
    await update.message.reply_text("❄️ FROST X!TER FAST SHOP ❄️\n⚡ 1 Sec Fast - Price එකක් තෝරන්න 👇", reply_markup=InlineKeyboardMarkup(keyboard))

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data in ACCOUNTS:
        text = f"✅ {query.data} සදහා ඇති Accounts:\n\n"
        text += "\n\n".join(ACCOUNTS[query.data])
        keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data='back')]]
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == 'back':
        keyboard = [
            [InlineKeyboardButton("💰 1,000 - 5,000", callback_data='range_1000')],
            [InlineKeyboardButton("💰 5,000 - 20,000", callback_data='range_5000')],
            [InlineKeyboardButton("💰 30,000 - 60,000", callback_data='range_30000')],
            [InlineKeyboardButton("💰 70,000 - 200,000", callback_data='range_70000')],
        ]
        await query.edit_message_text("❄️ FROST X!TER FAST SHOP ❄️\n⚡ 1 Sec Fast - Price එකක් තෝරන්න 👇", reply_markup=InlineKeyboardMarkup(keyboard))

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    print("Bot Running FAST...")
    app.run_polling()

if __name__ == "__main__":
    main()
