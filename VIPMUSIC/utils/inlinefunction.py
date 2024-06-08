from math import ceil
from pyrogram.types import InlineKeyboardButton

COLUMN_SIZES = [3, 2, 1]  # Number of buttons in each row


class EqInlineKeyboardButton(InlineKeyboardButton):
    def __eq__(self, other):
        return self.text == other.text

    def __lt__(self, other):
        return self.text < other.text

    def __gt__(self, other):
        return self.text > other.text


def paginate_modules(page_n, module_dict, prefix, chat=None):
    if not chat:
        modules = sorted(
            [
                EqInlineKeyboardButton(
                    x.__MODULE__,
                    callback_data="{}_module({},{})".format(
                        prefix, x.__MODULE__.lower(), page_n
                    ),
                )
                for x in module_dict.values()
            ]
        )
    else:
        modules = sorted(
            [
                EqInlineKeyboardButton(
                    x.__MODULE__,
                    callback_data="{}_module({},{},{})".format(
                        prefix, chat, x.__MODULE__.lower(), page_n
                    ),
                )
                for x in module_dict.values()
            ]
        )

    pairs = []
    start_idx = 0
    for size in COLUMN_SIZES:
        pairs.append(modules[start_idx : start_idx + size])
        start_idx += size

    max_num_pages = ceil(len(modules) / sum(COLUMN_SIZES)) if len(modules) > 0 else 1
    modulo_page = page_n % max_num_pages

    if len(modules) > sum(COLUMN_SIZES):
        pairs.append(
            [
                EqInlineKeyboardButton(
                    "❮",
                    callback_data="{}_prev({})".format(
                        prefix,
                        modulo_page - 1 if modulo_page > 0 else max_num_pages - 1,
                    ),
                ),
                EqInlineKeyboardButton(
                    "Bᴀᴄᴋ",
                    callback_data="settingsback_helper",
                ),
                EqInlineKeyboardButton(
                    "❯",
                    callback_data="{}_next({})".format(prefix, modulo_page + 1),
                ),
            ]
        )

    return pairs
