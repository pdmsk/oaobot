import time
import telebot
from telebot import types


bot = telebot.TeleBot('5475926231:AAGqqxETj_qjX-JP2z19stjAy0zKpLTutGk')


def get_answ(message):
    answer = ''
    i = 0
    for let in message:
        if i % 2 == 0:
            answer += let.upper()
        elif i % 2 == 1:
            answer += let.lower()
        if let != ' ':
            i += 1
    return answer


# @bot.inline_handler(lambda query: query.query == 'test')
# def test(inline_query):
#     print('AAAAAABBBBBBBBBBBBBBBBAAAAAAAAAAAA')
#     r = types.InlineQueryResultArticle(
#         id = '1',
#         title = 'Result1',
#         input_message_content = types.InputTextMessageContent('hi'))
#     bot.answer_inline_query(inline_query.id, [r])\


@bot.inline_handler(lambda query: query.query)
def text(inline_query):
    # print(inline_query.query)
    # print('AAAAAAAAAAAAAAA')
    text = get_answ(inline_query.query)
    r = types.InlineQueryResultArticle(
        id = '1',
        title = 'возвращаем ОаОаОа культуру',
        input_message_content = types.InputTextMessageContent(text))
    bot.answer_inline_query(inline_query.id, [r])


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # print('AAAAAAAAAAAAAAAa')
    bot.send_message(message.from_user.id, get_answ(message.text))



while True:
    try:
        bot.polling(True)
    except:
        time.sleep(5)

# bot.polling(none_stop=True, interval=0)