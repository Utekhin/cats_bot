from aiogram import types


class BotReplyKeyboards:

    @staticmethod
    def default_reply():
        menu_markup = types.reply_keyboard.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        menu_markup.row(types.reply_keyboard.KeyboardButton('Two cats'), types.reply_keyboard.KeyboardButton('Three cats'))
        menu_markup.row(types.reply_keyboard.KeyboardButton('Text'), types.reply_keyboard.KeyboardButton('About'))

        return menu_markup


    @staticmethod
    def text_render_reply():
        menu_markup = types.reply_keyboard.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        menu_markup.add(types.reply_keyboard.KeyboardButton('Cancel'))

        return menu_markup

