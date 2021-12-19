import telebot

from aiogram import Bot, types
from aiogram import Dispatcher, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import requests
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import numpy as np
Otziv=[]
b=1
np.save('C:\hgt', b)

bot = Bot(token='1654971977:AAHRC0vep_gshWreqex-dQv74Ai4KIgruMA')
dp = Dispatcher(bot, storage=MemoryStorage())
class OrderOtz(StatesGroup):
    wait_for_otz=State()
@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    global b
    button_hi = KeyboardButton('MENU',  callback_data='MENU')
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    greet_kb.add(button_hi)
    await bot.send_message(message.chat.id, "Здравствуй, я тот, кто поможет тебе немного узнать о произведении 'Ледяной ад'. Нажми на кнопку 'MENU', чтобы перейти в меню", reply_markup=greet_kb)
@dp.message_handler(text=["MENU"])
async def MENU(message: types.Message):
    button_hi1 = KeyboardButton('MENU',  callback_data='MENU')
    button_hi2 = KeyboardButton('Автор',  callback_data='MENU')
    button_hi3 = KeyboardButton('Произведение',  callback_data='MENU')
    button_hi4 = KeyboardButton('О нас',  callback_data='MENU')
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    greet_kb.add(button_hi1, button_hi2,button_hi3, button_hi4)
    await bot.send_message(message.chat.id, "Ты перешел в меню. Отсюда ты можешь перейти в раздел 'Произведение','Автор' или опять вернуться в меню", reply_markup=greet_kb)
@dp.message_handler(text=["Автор"])
async def MENU(message: types.Message):
    button_hi1 = KeyboardButton('MENU',  callback_data='MENU')
    button_hi2 = KeyboardButton('Краткая информация об авторе',  callback_data='MENU')
    button_hi3 = KeyboardButton('Полная информация об авторе',  callback_data='MENU')
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    greet_kb.add(button_hi1, button_hi2,button_hi3)
    await bot.send_message(message.chat.id, "Вы можете либо кратко узнать об авторе, либо узнать полностью", reply_markup=greet_kb)
@dp.message_handler(text=["Краткая информация об авторе"])
async def MENU(message: types.Message):
    button_hi1 = KeyboardButton('MENU',  callback_data='MENU')
    button_hi2 = KeyboardButton('Автор',  callback_data='MENU')
    button_hi3 = KeyboardButton('Полная информация об авторе',  callback_data='MENU')
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    greet_kb.add(button_hi1, button_hi2,button_hi3)
    await bot.send_message(message.chat.id, "Луи Анри Буссенар (фр. Louis Henri Boussenard, 4 октября 1847 — 11 сентября 1910) — французский писатель, автор приключенческой литературы.", reply_markup=greet_kb)
@dp.message_handler(text=["Полная информация об авторе"])
async def MENU(message: types.Message):
    button_hi1 = KeyboardButton('MENU',  callback_data='MENU')
    button_hi2 = KeyboardButton('Автор',  callback_data='MENU')
    button_hi3 = KeyboardButton('Краткая информация об авторе',  callback_data='MENU')
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    greet_kb.add(button_hi1, button_hi2,button_hi3)
    await bot.send_message(message.chat.id, u"Луи Буссенар родился в 1847 году в деревне Эскренн, Франция. Его родители — Луи-Антуан Буссенар (1794—1855)[4], управляющий эскреннским замком, сборщик коммунальных налогов, вдовец, и Элоиза Ланс (1826—1932)[5] — кастелянша и горничная замка, дочь ткача-ремесленника (заключили официальный брак в 1850 году).Во время франко-прусской войны 1870—1871 годов Буссенар был призван в армию и служил полковым врачом. Был ранен под Шампиньи. После войны Буссенар некоторое время продолжал своё медицинское образование, но вскоре окончательно порвал с профессией и занялся литературой."+" 1 августа 1875 года воскресное приложение к газете Le Figaro опубликовало первый рассказ Луи Буссенара – «Охота в Австралии»[6]. В последующие годы он работает научным обозревателем, репортёром и хроникёром в разных парижских газетах (Le Corsaire, Le Petit Parisien, La Justice и др).В 1878 году Буссенар начал сотрудничать в еженедельнике Journal des voyages et des aventures de terre et de mer («Журнал путешествий и приключений на суше и на море»), ведущим автором которого он останется до конца своей жизни. На страницах этого издания один за другим выходят в свет остросюжетные приключенческие романы Буссенара, насыщенные научно-популярными сведениями о флоре, фауне, нравах и обычаях экзотических стран."+u" Наибольший успех приносит писателю его второй роман — «Кругосветное путешествие юного парижанина» (1880). После публикации на страницах журнала большинство романов Буссенара издаются отдельными книгами.По поручению редакции «Журнала путешествий» и при поддержке министерства народного просвещения Буссенар совершил путешествие во Французскую Гвиану (6 августа 1880 – 31 января 1881 года)[7], где почерпнул местный колорит и нашёл новые идеи для творчества. Впоследствии он посетил Марокко (1883) и Сьерра-Леоне (1884). Предположительно, в 1870-е годы он побывал также в Австралии и Индонезии[8], однако достоверных данных на настоящий момент пока не найдено[9].С 1880-х годов Буссенар оставляет Париж и поселяется в провинции, в родном департаменте Луаре, живя сначала в Нанто-сюр-Эсоне и Вилльтаре (деревни близ Мальзерба), а после в самом Мальзербе, посвящая свободное от литературного труда время охоте, рыбной ловле, спортивной гребле, велосипедным прогулкам."+u"Буссенар был дважды женат, детей не имел. 2 июня 1881 года он женился на 30-летней Розали Леша из Монтаржи[10], но супруги вскоре поссорились и расстались. Их брак был расторгнут судом в 1909 году[11]. "+" В 1902 году Буссенар возвращается к журналистской деятельности и на протяжении восьми лет под псевдонимом Франсуа Девин публикует на страницах регионального еженедельника Le Gâtinais «Письма крестьянина», написанные на босеронском диалекте, в которых выражает свои взгляды на политику, религию и общество[14]."+"Последний год жизни Буссенара прошёл в Орлеане. В июне 1910 года внезапно умирает любимая жена писателя, Альбертина Делафуа, с которой он прожил 27 лет."+"Луи Буссенар пережил её менее чем на три месяца и скончался в сентябре 1910 года в одной из орлеанских клиник в результате продолжительной болезни и после проведённой операции. Похоронен в родной деревне Эскренн."+u" Г. Чхартишви́ли выдвигает версию о самоубийстве Буссенара[15]. Данная версия оспаривается другими исследователями биографии Буссенара[16]."+"Согласно завещанию Буссенара все личные бумаги и рукописи его произведений были сожжены. Его мать, Элоиза Ланс, скончалась в возрасте 106 лет, пережив своего сына на 22 года."+"В 1911 году в России вышло собрание сочинений Луи Буссенара в 40 томах. Также отдельные произведения переиздавались в советские времена — прежде всего, роман «Капитан Сорви-голова»."+"В 1991—2001 годах издательство «Ладомир» выпустило полное собрание романов писателя в 30 томах (32 книгах).", reply_markup=greet_kb)
@dp.message_handler(text=["О нас"])
async def MENU(message: types.Message):
    button_hi1 = KeyboardButton('MENU',  callback_data='MENU')
    button_hi2 = KeyboardButton('Оставить отзыв',  callback_data='MENU')
    button_hi3 = KeyboardButton('Посмтортеть отзывы',  callback_data='MENU')
    button_hi5 = KeyboardButton('ДА')
    button_hi6 = KeyboardButton('НЕТ')
    button_hi4 = KeyboardButton('Посмотреть отзывы')
    greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
    greet_kb1.add(button_hi5, button_hi6)
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    greet_kb.add(button_hi1, button_hi2,button_hi3, button_hi4)


    await bot.send_message(message.chat.id, "Оставь отзыв о нас или посмтори другии. Но пока что система работает неккоректно, и ты можешь оставить сразу много отзывов. Пожалуйста не злоупотребляй этим ", reply_markup=greet_kb)
    await bot.send_message(message.chat.id, "хотите увидть моего создателя? ", reply_markup=greet_kb1)
@dp.message_handler(text=["ДА"])
async def MENU(message: types.Message):
    inline_kb_full = InlineKeyboardMarkup(row_width=2)
    inline_kb_full.add(InlineKeyboardButton('Вот вк', url='https://vk.com/mmolchanov90'))
    await bot.send_message(message.chat.id, "Вот вк", reply_markup=inline_kb_full)
    button_hi1 = KeyboardButton('MENU',  callback_data='MENU')
    button_hi2 = KeyboardButton('Оставить отзыв',  callback_data='MENU')
    button_hi3 = KeyboardButton('Посмотреть отзывы',  callback_data='MENU')


    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    greet_kb.add(button_hi1, button_hi2,button_hi3)
    await bot.send_message(message.chat.id, "Раздел 'О нас'", reply_markup=greet_kb)
@dp.message_handler(text=["НЕТ"])
async def MENU(message: types.Message):
    button_hi1 = KeyboardButton('MENU',  callback_data='MENU')
    button_hi2 = KeyboardButton('Оставить отзыв',  callback_data='MENU')
    button_hi3 = KeyboardButton('Посмотреть отзывы',  callback_data='MENU')


    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    greet_kb.add(button_hi1, button_hi2,button_hi3)
    await bot.send_message(message.chat.id, "Оставь отзыв о нас или посмтори другии. Но пока что система работает неккоректно, и ты можешь оставить сразу много отзывов. Пожалуйста не злоупотребляй этим ", reply_markup=greet_kb)

@dp.message_handler(text="Оставить отзыв", state="*")
async def Otzv(message: types.Message):


    await bot.send_message(message.chat.id, "Оставь отзыв о нас или посмтори другии. Но пока что система работает неккоректно, и ты можешь оставить сразу много отзывов. Пожалуйста не злоупотребляй этим ")

    await bot.send_message(message.chat.id, "Пишите здесь ваш отзыв")
    await OrderOtz.wait_for_otz.set()

@dp.message_handler(state=OrderOtz.wait_for_otz)
async def OTZ(msg: types.Message,  state: FSMContext):
    global Otziv
    user_ot =""
    user_ot=str(msg.from_user.first_name)+"\n"+ msg.text+"\n"+"\n"
    if len(msg.text)<250:
        Otziv.append(user_ot)
        np.save('C:\lol', Otziv)



    button_hi1 = KeyboardButton('MENU',  callback_data='MENU')
    button_hi2 = KeyboardButton('Оставить отзыв',  callback_data='MENU')
    button_hi3 = KeyboardButton('Посмотреть отзывы',  callback_data='MENU')

    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    greet_kb.add(button_hi1, button_hi2,button_hi3)
    await bot.send_message(msg.from_user.id, "Вот ваш отзыв"+"\n"+ user_ot, reply_markup=greet_kb)

    await state.finish()
@dp.message_handler(text=["Посмотреть отзывы"])
async def MENU(message: types.Message):
    global Otziv
    button_hi1 = KeyboardButton('MENU',  callback_data='MENU')
    button_hi2 = KeyboardButton('Оставить отзыв',  callback_data='MENU')
    button_hi3 = KeyboardButton('Посмотреть отзывы',  callback_data='MENU')
    prosmotr=""

    Otziv=np.load('C:\lol.npy').tolist()

    #for i in range(len(Otziv)):
        #prosmotr="\n"+Otziv[i]+prosmotr

    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    greet_kb.add(button_hi1, button_hi2,button_hi3)
    for i in range(len(Otziv)):
        await bot.send_message(message.chat.id, "Вот отзывы"+"\n"+Otziv[i], reply_markup=greet_kb)

@dp.message_handler(text=["Произведение"])
async def MENU(message: types.Message):
    button_hi1 = KeyboardButton('Краткое содержание',  callback_data='MENU')
    button_hi2 = KeyboardButton('Ссылка на само произведение',  callback_data='MENU')
    button_hi3 = KeyboardButton('Отзыв от нашего эксперта',  callback_data='MENU')
    button_hi4 = KeyboardButton('MENU',  callback_data='MENU')
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    greet_kb.add(button_hi1, button_hi4)
    greet_kb.add(button_hi2)
    greet_kb.add(button_hi3)
    await bot.send_message(message.chat.id, "Ты перешел в раздел 'Произведение'. Тебе доступны следующие функции:", reply_markup=greet_kb)

@dp.message_handler(text=["Краткое содержание"])
async def MENU(message: types.Message):
    button_hi1 = KeyboardButton('Краткое содержание',  callback_data='MENU')
    button_hi2 = KeyboardButton('Ссылка на само произведение',  callback_data='MENU')
    button_hi3 = KeyboardButton('Отзыв от нашего эксперта',  callback_data='MENU')
    button_hi4 = KeyboardButton('MENU',  callback_data='MENU')
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    greet_kb.add(button_hi1, button_hi4)
    greet_kb.add(button_hi2)
    greet_kb.add(button_hi3)
    await bot.send_message(message.chat.id, "Роман «Ледяной ад» возвращает читателей к теме золотой лихорадки. Персонажи этого произведения, движимые благородной местью — обуздать действия коварных и свирепых преступников из банды «Красная Звезда», — отправляются в Клондайк, или Ледяной ад. Пережив множество необычных приключений, они, при помощи чудодейственного элемента таблицы Менделеева — леониума, чувствительного к золоту, открывают легендарное месторождение «Золотое море».", reply_markup=greet_kb)
@dp.message_handler(text=["Отзыв от нашего эксперта"])
async def MENU(message: types.Message):
    button_hi1 = KeyboardButton('Краткое содержание',  callback_data='MENU')
    button_hi2 = KeyboardButton('Ссылка на само произведение',  callback_data='MENU')
    button_hi3 = KeyboardButton('Отзыв от нашего эксперта',  callback_data='MENU')
    button_hi4 = KeyboardButton('MENU',  callback_data='MENU')
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    greet_kb.add(button_hi1, button_hi4)
    greet_kb.add(button_hi2)
    greet_kb.add(button_hi3)
    await bot.send_message(message.chat.id, "Презентация по теме книги Ледяной ад. Немного о сюжете. Ледяной ад-впервые роман из цикла о жане Грандье. Дейсвие его происходит в конце 19 века во время вспыхнувшей 'Золотой лихорадки', когда десятки тысяч людей отправились в Клондайк на поиски драгоценного металла.Молодой ученый Леон Фортен случайно делает открытие, в результате которого получает вещество, притягивающее золото, как магнит железо. Располагая таким изобретением, Леон решает "+"отправиться в далекий Клондайк, земли которого, полны золотыми залежами. Вместе с верными друзьями ему предстоит преодолеть эту суровую, полную опасностей страну, называемую «Ледяным адом».Ледяной ад – это то место, где свирепствуют страшные холода, где еда моментально превращается в глыбу льда, и где в страшных условиях работают люди. Отзыв. "+"Я прочитал эту книгу с большим удовольствием!С самого начала произведение казалось мне очень интригующим и загадочным. Убийство, невероятный контраст и таинственный злодей не могут не заинтересовать читателя, в том числе и меня!Затем идёт ряд неоднозначных событий, которые, как по мне, заставляют читателя задуматься. Таинственная 'Красная звезда' всё чаще и чаще встречается и даёт повод для переживаний. Кровожадность этой банды поражает. От писем, написанных ими становится даже жутко. "+"Так же, произведение отлично описывает одно из самых интересных исторических событий того времени. Этим событием является Золотая лихорадка.Лично у меня это вызвало большой интерес к истории. Мы можем погрузиться в то время не от слов исторических деятелей, а с помощью тех эмоций, которыми Луи Буссенар наделил главных героев книги. Главные персонажи вызывают у меня огромное восхищение! Они очень храбры и стойко борются с обстоятельствами.В произведении мы можем можем познать настоящую дружбу, храбрость, а так же самоотверженность. Но есть в книге и не совсем правильные вещи."+"Например, я выделю месть, на основе которой завязана довольно большая часть рассказа.К заключению, я могу отметить, что текст написан лёгким языком, но этого вполне достаточно, чтобы ярко описать все действия книги. Именно из за простоты языка это произведение легко и приятно читать.На основе всех ранее сказанных мною причин я могу с уверенностью посоветовать вам этот рассказ. Как по мне, это отличное времяпровождение с пользой и интересом. Сюжет увлечёт вас, а главные герои восхитят. Особенно этот рассказ подойдёт любителям приключений!Спасибо большое за внимание!", reply_markup=greet_kb)
@dp.message_handler(text=["Ссылка на само произведение"])
async def MENU(message: types.Message):
    inline_kb_full = InlineKeyboardMarkup(row_width=2)
    inline_kb_full.add(InlineKeyboardButton('Вот здесь ты можешь прочитать произведение', url='https://www.litmir.me/br/?b=5333&p=1'))
    await bot.send_message(message.chat.id, "Ты можещь прочитать произведение здесь", reply_markup=inline_kb_full)
    button_hi1 = KeyboardButton('Краткое содержание',  callback_data='MENU')
    button_hi2 = KeyboardButton('Ссылка на само произведение',  callback_data='MENU')
    button_hi3 = KeyboardButton('Отзыв от нашего эксперта',  callback_data='MENU')
    button_hi4 = KeyboardButton('MENU',  callback_data='MENU')
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    greet_kb.add(button_hi1, button_hi4)
    greet_kb.add(button_hi2)
    greet_kb.add(button_hi3)
    await bot.send_message(message.chat.id, "Теперь можешь вернуться к разделу 'Произведение'", reply_markup=greet_kb)


if __name__ == '__main__':
    executor.start_polling(dp)
