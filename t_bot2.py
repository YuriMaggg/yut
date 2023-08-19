from aiogram import Bot,types,Dispatcher,executor

token='&&&&&&'
bot=Bot(token)
disp=Dispatcher(bot)
l=list()
v=list()
@disp.message_handler(commands=['startreikin'])
async def kalk(message: types.Message):
    await message.answer('это калюкулятор')
    m=0
    for k in range(3):
        for s in range(3):
            m+=1
            v.append(types.KeyboardButton(text=str(m)))
        l.append(v)
        v=[]
    l.append([types.KeyboardButton(text=str(0))])
    keybord_1=types.ReplyKeyboardMarkup(keyboard=l,rezise_keyboard=True)
    await message.answer(reply_markup=keybord_1)




