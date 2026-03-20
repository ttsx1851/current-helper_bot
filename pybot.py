import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8751756821:AAGyOg4m6vMWLEeDh9Vt7ktra_F1Mt-f_bs"

# Получаем курс
def get_rates():
    url = "https://open.er-api.com/v6/latest/USD"
    data = requests.get(url).json()
    return data["rates"]

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("START команда пришла")
    await update.message.reply_text("Напиши /rates чтобы узнать курс валют 💱")

# Команда /chart
async def chart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(
            "📊 Открыть график",
            web_app=WebAppInfo(url="https://current-help-bot.netlify.app")
        )]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Нажми кнопку ниже 👇",
        reply_markup=reply_markup
    )

# Команда /rates
async def rates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("RATES команда пришла")
    
    rates = get_rates()
    
    usd = 1
    rub = rates.get("RUB")
    uzs = rates.get("UZS")

    text = f"""
💵 USD: {usd}
🇷🇺 RUB: {rub}
🇺🇿 UZS: {uzs}
"""
    await update.message.reply_text(text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("rates", rates))
app.add_handler(CommandHandler("chart", chart))

app.run_polling()
print("Бот запущен...")