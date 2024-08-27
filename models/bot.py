from telebot import TeleBot
bot = TeleBot('7357580477:AAFY4uGWUNXKXxvYxl0P0TIXHZEcypHHxN8')



ids = 5322589899
def get_post(data):
    bot.send_message(chat_id=ids, text=f"Sizga yangi murojaat mavjud !\n\n\n"
                                          f"Ism: {data['name']}\n"
                                          f"Telefon Raqam: {data['phonenumber']}")