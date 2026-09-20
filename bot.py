import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# =========================
# BOT TOKEN
# =========================
BOT_TOKEN = os.getenv("BOT_TOKEN")


# =========================
# MAIN MENU
# =========================
keyboard = [
    ["📝 কাজ", "💵 ব্যালেন্স"],
    ["💰 টাকা উত্তোলন", "🎁 My Referrals"],
    ["🐵 সাপোর্ট", "👶 আমি নতুন"],
]

menu = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True
)


# =========================
# START
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    text = (
        f"👋 হ্যালো {user.first_name}!\n\n"
        "🤖 আমাদের Income Bot-এ স্বাগতম।\n\n"
        "নিচের মেনু থেকে একটি অপশন নির্বাচন করুন।"
    )

    await update.message.reply_text(
        text,
        reply_markup=menu
    )


# =========================
# MENU BUTTONS
# =========================
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📝 কাজ":
        await update.message.reply_text(
            "📝 কাজ\n\n"
            "বর্তমানে কোনো নতুন কাজ নেই।\n"
            "নতুন কাজ যোগ হলে এখানে দেখানো হবে।"
        )

    elif text == "💵 ব্যালেন্স":
        await update.message.reply_text(
            "💵 আপনার ব্যালেন্স\n\n"
            "🔥 ব্যালেন্স: 0.00 BDT\n"
            "📦 পেন্ডিং: 0.00 BDT\n"
            "💰 Total Income: 0.00 BDT\n\n"
            "✅ সম্পন্ন কাজ: 0 টি\n"
            "⌛ রিভিউতে আছে: 0 টি"
        )

    elif text == "💰 টাকা উত্তোলন":
        await update.message.reply_text(
            "💰 টাকা উত্তোলন\n\n"
            "আপনার বর্তমান ব্যালেন্স: 0.00 BDT\n\n"
            "⚠️ পর্যাপ্ত ব্যালেন্স না থাকায় এখন টাকা উত্তোলন করা যাবে না।"
        )

    elif text == "🎁 My Referrals":
        await update.message.reply_text(
            "🎁 My Referrals\n\n"
            "👥 আপনার Referral: 0 জন\n"
            "💰 Referral Income: 0.00 BDT\n\n"
            "আপনার Referral Link পরে এখানে দেখানো হবে।"
        )

    elif text == "🐵 সাপোর্ট":
        await update.message.reply_text(
            "🐵 Support\n\n"
            "কোনো সমস্যা হলে Admin-এর সাথে যোগাযোগ করুন।"
        )

    elif text == "👶 আমি নতুন":
        await update.message.reply_text(
            "👶 নতুনদের জন্য নির্দেশনা\n\n"
            "1️⃣ প্রথমে '📝 কাজ' এ যান।\n"
            "2️⃣ available কাজ নির্বাচন করুন।\n"
            "3️⃣ কাজ সম্পন্ন করে প্রমাণ জমা দিন।\n"
            "4️⃣ Admin যাচাই করার পর আপনার ব্যালেন্সে টাকা যোগ হবে।"
        )

    else:
        await update.message.reply_text(
            "অনুগ্রহ করে নিচের মেনু থেকে একটি অপশন নির্বাচন করুন।",
            reply_markup=menu
        )


# =========================
# RUN BOT
# =========================
def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN পাওয়া যায়নি!")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, buttons)
    )

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
