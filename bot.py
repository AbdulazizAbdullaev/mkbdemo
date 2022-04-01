import telebot
import math



token = '5131588339:AAEFrNyC6wLySA7ZD_Nt8SmUNIs3ipE5qEA'
bot = telebot.TeleBot(token)
langNumber1 = [0]

def log(message):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print("Бота использует {0} {1}. (id = {2}) \n ".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id)))
def funcRandQueue():
    CategoriasBankRus = ["Кассовые операции: перел вами ", "Оформление кредита/депозита: перел вами ",
                         "Денежные переводы: перел вами ", "Консультации: перел вами "]
    CategoriasBankKaz = ["Кассалық операциялар: сіздің алдыңызда", "Несие/депозит өндеу: сіздің алдыңызда", "Ақша аударымдары: сіздің алдыңызда", "Консультациялар: cіздің алдыңызда"]
    CategoriasBankEng = ["Cash transactions: before you ", "Registration of the loan / deposit: before you ", "Money transfers: before you ",
                         "Consultation: before you "]

    CategoriasBank = [CategoriasBankRus, CategoriasBankKaz, CategoriasBankEng]
   

@bot.message_handler(commands=['start'])
def lang(message):
    bot.send_message(message.from_user.id, "Xush kelibsiz!\nBot sizga yaqin bo`lgan \nFilial,BHM,Bankomatlarning manzilini topib beradi !")
    keyboard = telebot.types.InlineKeyboardMarkup()
   # callback_button1 = telebot.types.InlineKeyboardButton(text='rus', callback_data='r')
    callback_button2 = telebot.types.InlineKeyboardButton(text='🔰Boshlash🔰', callback_data='k')
   # callback_button3 = telebot.types.InlineKeyboardButton(text='eng', callback_data='e')
    keyboard.add(callback_button2)
    bot.send_message(message.from_user.id, 'Botni quyidagi tugmani bosish orqali ishga tushirishingiz mumkin.', reply_markup=keyboard)


listLang = ['Русский язык', '📍Joylashuvni yuboring.', 'English language']
listLang_SendLocation = ['Отправить местоположение', 'Joylashuvni yuborish', 'Send your location']
listLangDef = ['Вы выбрали:', 'Bot ishga tushdi', 'You have chosen:']

listHalyk = ['Микрокредитбанк', 'Bank №', 'Mikrokreditbank']
listBank = ['Выберите банк! ', 'Bankni tanlang! ', 'Choose bank! ']
list3Bank = ['3 ближайших банка: ', '3 ta yaqin banklar:', 'Closest 3 banks :']


listOperations = ['Операции:', 'Операциялар:', 'Operations:']

listSuc = ['Вы успешно заняли очередь на кассовые операции, ваш номер:', 'Кассалық операцияларғa кезекке тұрдыңыз, cіздің нөмірі: ',
           'You have successfully occupied a queue for cash transactions, your number: ']
listCredit = ['Вы успешно заняли очередь на оформление кредиты и депозиты, ваш номер: ', 'Несие/депозит өндеуге кезекке тұрдыңыз, cіздің нөмірі: ', 'You have successfully occupied a queue for loans and deposits, your number: ']

listCash = ['Вы успешно заняли очередь на денежные переводы, ваш номер: ', 'Ақша аударымдарғa кезекке тұрдыңыз, cіздің нөмірі: ', 'You have successfully occupied a queue for money Transfers, your number: ']
listConsul = ['Вы успешно заняли очередь на консультацию, ваш номер: ', 'Консультацияғa кезекке тұрдыңыз, cіздің нөмірі: ', 'You have successfully occupied a queue for сonsultation, your number: ']


listR_rus = ['Кассовые операции', 'Оформление кредита/депозита', 'Денежные переводы', 'Консультации']
listR_kaz = ['Кассалық операциялар', 'Несие/депозит өндеу', 'Ақша аударымдары', 'Консультациялар']
listR_eng = ["Cash transactions", "Registration of the loan / deposit", "Money transfers", "Consultation"]

listRLists = [listR_rus, listR_kaz, listR_eng]

listNumbers = ['87272590777', '87272890777', '87272590776','2','87272594777', '87232890777', '87272590756','3',
              '87272592340777', '8727223423890777', '872725546790776','4','54654', '8727289072343277', '8727123590776','5',
              '87272543590777', '87272125890777', '872725986780776','6','872753452590777', '8727289345340777', '8725672590776','7',
              '8743543272590777', '872728907123477', '87272590435776','8','8727259345340777', '87272823432490777', '87272595465476540776','9',
              '872725978880777', '872728934330777', '872666672590776','10','872725932320777', '872728903477', '872725907343476','11',]

@bot.message_handler(content_types=['location'])
def loco(message):
    langNumber = langNumber1[0]
    location_string = str(message.location)
    location_string = location_string.replace("'longitude': ", "")
    location_string = location_string.replace("}", "")
    #location_string = location_string.replace(",", "")

    location_string = location_string.replace(" 'latitude': ", "")
    location_doubleY = float(location_string[1:10])
    location_doubleX = float(location_string[11:20])



    print("Coordinates of user: ", location_doubleX, location_doubleY)
    log(message)

    address_halyk_rus = ["d"]
    address_halyk_uz = [
                        "Чиғатой\n📍 : массив т-13 Лабзак кучаси 32 а уй\n🏙 : Тошкент шахар Шайхонтохур тумани.\n📞 : +998 (71) 202-99-99\n🕑 : 9:00 - 17:00", 
                        "Тараққиёт \n📍 : Қатортол савдо маркази 2-қаватида\n🏙 : Тошкент шаҳри Чилонзор тумани.\n📞 : +998 (71) 202-99-99\n🕑 : 9:00 - 17:00",
                        "Ёшлар \n📍 : Маҳтумқули кўчаси 87-уй\n🏙 : Тошкент шаҳри Яшнабод тумани.\n📞 : +998 (71) 202-99-99\n🕑 : 9:00 - 17:00", 
                        "Юнусобод \n📍 : 4-мавзе 19-уй 46-хонадон\n🏙 : Тошкент шаҳри Юнусобод тумани.\n📞 : +998 (71) 202-99-99\n🕑 : 9:00 - 17:00", #YUNUSOBOD
                        "Юксалиш \n📍 : А. Навоий кучаси 37 уй\n🏙 : Тошкент шахар Шайхонтохур тумани.\n📞 : +998 (71) 202-99-99\n🕑 : 9:00 - 17:00",
                                           ]
    address_halyk_eng = [""]

    adressListofLists = [address_halyk_rus, address_halyk_uz, address_halyk_eng]

    list_x = [41.327438, 41.297161, 41.293748, 41.361458, 41.321206]
              
    list_y = [69.263776, 69.205186, 69.344200, 69.280647, 69.246639]

    list_dist = []


    for i in range(0, len(list_x)):
        list_dist.append(math.sqrt((location_doubleX-list_x[i]) * (location_doubleX-list_x[i]) + (location_doubleY-list_y[i]) * (location_doubleY-list_y[i])))


    for i in range(0, len(list_x)):
        list_dist[i] = round(list_dist[i], 6)

    list_values = [x for x in range(0, len(list_x))]

    dictDistance = dict(zip(list_dist, list_values))
    SortedListDistance = list(sorted(list_dist))

    listClosest3Banks = []

    for i in range(0, 5):
        z = dictDistance.get(SortedListDistance[i])
        listClosest3Banks.append(z)

    print("Eng yaqin 3 ta banklar :", listClosest3Banks)

    for i in range(0, 5):
         minDistIndex = listClosest3Banks[i]
         
         bot.send_location(message.from_user.id, list_x[minDistIndex], list_y[minDistIndex])
         print(langNumber)
        # bot.send_message(message.from_user.id, address1=adressListofLists[langNumber][minDistIndex]) # list qo'shimch malumot beruvchi contact
        
         bot.send_message(message.from_user.id, adressListofLists[langNumber][minDistIndex]) # list qo'shimch malumot beruvchi contact


   # kb = telebot.types.InlineKeyboardMarkup(row_width=1)
   # cb1 = telebot.types.InlineKeyboardButton(text=listHalyk[langNumber] + ' %i' %(1), callback_data="b1")
   # cb2 = telebot.types.InlineKeyboardButton(text=listHalyk[langNumber] + ' %i' %(2), callback_data="b2")
   # cb3 = telebot.types.InlineKeyboardButton(text=listHalyk[langNumber] + ' %i' %(3), callback_data="b3")
   # kb.add(cb1, cb2, cb3)
   # bot.send_message(message.from_user.id, list3Bank[langNumber], reply_markup=kb)

    #um = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
   # um.row(listHalyk[langNumber] + ' %i' %(1), listHalyk[langNumber] + ' %i' %(2), listHalyk[langNumber] + ' %i' %(3))
   # bot.send_message(message.from_user.id, listBank[langNumber], reply_markup=um)


@bot.message_handler(content_types=['text'])
def mes(message):
    if message.text == listHalyk[langNumber1[0]] + ' %i' %(1) or message.text == listHalyk[langNumber1[0]] + ' %i' %(2) or message.text == listHalyk[langNumber1[0]] + ' %i' %(3):
        kbd = telebot.types.InlineKeyboardMarkup(row_width=1)
        act1 = telebot.types.InlineKeyboardButton(text=listRLists[langNumber1[0]][0], callback_data="a1")
        act2 = telebot.types.InlineKeyboardButton(text=listRLists[langNumber1[0]][1], callback_data="a2")
        act3 = telebot.types.InlineKeyboardButton(text=listRLists[langNumber1[0]][2], callback_data="a3")
        act4 = telebot.types.InlineKeyboardButton(text=listRLists[langNumber1[0]][3], callback_data="a4")
        kbd.add(act1, act2, act3, act4)
        bot.send_message(message.from_user.id, listOperations[langNumber1[0]], reply_markup=kbd)



@bot.callback_query_handler(func=lambda call: True)
def callbackLang(call):
    if call.message:
        try:
            if call.data == "r" or call.data == "k" or call.data == "e":
                if call.data == "r":
                    langNumber1[0] = 0

                elif call.data == "k":

                    langNumber1[0] = 1

                elif call.data == "e":
                    langNumber1[0] = 2


                print(langNumber1[0], listLang[langNumber1[0]])
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=listLangDef[langNumber1[0]])
                keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
                button_geo = telebot.types.KeyboardButton(text=listLang_SendLocation[langNumber1[0]], request_location=True)
                
                keyboard.add(button_geo)
                bot.send_message(call.message.chat.id,
                                 listLang[langNumber1[0]],
                                 reply_markup=keyboard)

           

            else:
                print("Error")
        except:
            print('ERROROROR')


bot.polling(none_stop=True)