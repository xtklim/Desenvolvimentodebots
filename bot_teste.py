import telebot


token ='5164260190:AAFEIyPuIrzE6NcPs5dBV5VX9MclQBsvhkQ'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['milis'])
def teste(msg):
	msgs = msg.text[6:]
	print(msgs)
	try:
		h, m, s = map(int, msgs.split(':'))
		msdecimal = ((h * 60 + m) * 60 + s) * 1000
		mshex = hex(msdecimal)
		bot.send_message(msg.chat.id, f'Resultado:\n\nms decimal: ```{msdecimal}```\n\nms hex: ```{mshex}```\n\nms Long: ```{str(mshex)}L```', parse_mode='markdown')
	except:
		bot.send_message(msg.chat.id, 'Nao seja um tolo digite o seu tempo corretamente kk\nExemplo: /milis 23:23:23')

bot.infinity_polling()
