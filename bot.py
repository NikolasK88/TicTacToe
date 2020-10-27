import telebot
#from TicTacToe import main

board = [' ' for x in range(10)]
step = 1
value = ' '
old_value = ''
winner = 'выиграл'

bot = telebot.TeleBot('1106037057:AAGtQ6dGS2soOSxfb419j_syOsl4u43rlfw')

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton(board[1], callback_data='1'),
             telebot.types.InlineKeyboardButton(board[2], callback_data='2'),
             telebot.types.InlineKeyboardButton(board[3], callback_data='3'))

keyboard.row(telebot.types.InlineKeyboardButton(board[4], callback_data='4'),
             telebot.types.InlineKeyboardButton(board[5], callback_data='5'),
             telebot.types.InlineKeyboardButton(board[6], callback_data='6'))

keyboard.row(telebot.types.InlineKeyboardButton(board[7], callback_data='7'),
             telebot.types.InlineKeyboardButton(board[8], callback_data='8'),
             telebot.types.InlineKeyboardButton(board[9], callback_data='9'))


def isWinner(board):
    if (board[7] == 'X' and board[8] == 'X' and board[9] == 'X') or (board[4] == 'X' and board[5] == 'X' and board[6] == 'X') or (board[1] == 'X' and board[2] == 'X' and board[3] == 'X') or (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or (board[3] == 'X' and board[6] == 'X' and board[9] == 'X') or (board[1] == 'X' and board[5] == 'X' and board[9] == 'X') or (board[3] == 'X' and board[5] == 'X' and board[7] == 'X'):
        return value
    elif (board[7] == 'O' and board[8] == 'O' and board[9] == 'O') or (board[4] == 'O' and board[5] == 'O' and board[6] == 'O') or (board[1] == 'O' and board[2] == 'O' and board[3] == 'O') or (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or (board[3] == 'O' and board[6] == 'O' and board[9] == 'O') or (board[1] == 'O' and board[5] == 'O' and board[9] == 'O') or (board[3] == 'O' and board[5] == 'O' and board[7] == 'O'):
        return value
    else:
        pass


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


@bot.message_handler(commands=["help", "start"])
def getMessage(message):
    global value

    if value == ' ':
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value, step, winner
    data = query.data

    if not (isBoardFull(board)):
        if not (isWinner(board, 'O')):

            if (step % 2) == 0:
                symbol = 'O'
            else:
                symbol = 'X'

            if (step % 2) == 0:
                answer = 'X'
            else:
                answer = 'O'

            for k in range(1, 10):
                if str(k) == data:
                    value = f'Теперь ходит {answer}'
                    board[k] = symbol
                    step += 1
                    print(board)
                    keyboard2 = telebot.types.InlineKeyboardMarkup()
                    keyboard2.row(telebot.types.InlineKeyboardButton(board[1], callback_data='1'),
                                 telebot.types.InlineKeyboardButton(board[2], callback_data='2'),
                                 telebot.types.InlineKeyboardButton(board[3], callback_data='3'))

                    keyboard2.row(telebot.types.InlineKeyboardButton(board[4], callback_data='4'),
                                 telebot.types.InlineKeyboardButton(board[5], callback_data='5'),
                                 telebot.types.InlineKeyboardButton(board[6], callback_data='6'))

                    keyboard2.row(telebot.types.InlineKeyboardButton(board[7], callback_data='7'),
                                 telebot.types.InlineKeyboardButton(board[8], callback_data='8'),
                                 telebot.types.InlineKeyboardButton(board[9], callback_data='9'))
        else:
            if (step % 2) == 0:
                answer = 'X'
            else:
                answer = 'O'
            value = f'Победил {answer}!'
            keyboard2 = telebot.types.InlineKeyboardMarkup()
            keyboard2.row(telebot.types.InlineKeyboardButton(board[1], callback_data='1'),
                          telebot.types.InlineKeyboardButton(board[2], callback_data='2'),
                          telebot.types.InlineKeyboardButton(board[3], callback_data='3'))

            keyboard2.row(telebot.types.InlineKeyboardButton(board[4], callback_data='4'),
                          telebot.types.InlineKeyboardButton(board[5], callback_data='5'),
                          telebot.types.InlineKeyboardButton(board[6], callback_data='6'))

            keyboard2.row(telebot.types.InlineKeyboardButton(board[7], callback_data='7'),
                          telebot.types.InlineKeyboardButton(board[8], callback_data='8'),
                          telebot.types.InlineKeyboardButton(board[9], callback_data='9'))
    else:
        print('Ничья')
        value = 'Ничья'
        keyboard2 = telebot.types.InlineKeyboardMarkup()
        keyboard2.row(telebot.types.InlineKeyboardButton(board[1], callback_data='1'),
                      telebot.types.InlineKeyboardButton(board[2], callback_data='2'),
                      telebot.types.InlineKeyboardButton(board[3], callback_data='3'))

        keyboard2.row(telebot.types.InlineKeyboardButton(board[4], callback_data='4'),
                      telebot.types.InlineKeyboardButton(board[5], callback_data='5'),
                      telebot.types.InlineKeyboardButton(board[6], callback_data='6'))

        keyboard2.row(telebot.types.InlineKeyboardButton(board[7], callback_data='7'),
                      telebot.types.InlineKeyboardButton(board[8], callback_data='8'),
                      telebot.types.InlineKeyboardButton(board[9], callback_data='9'))

    #board = [' ' for x in range(10)]


    if value != old_value:
        if value == ' ':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=keyboard2)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=keyboard2)

    old_value = value




bot.polling(none_stop = False, interval = 0 )