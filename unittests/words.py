from unittest import result
import datetime


def join_words(word_1, word_2, return_bool=False):
    correct_word = f"{word_1}-{word_2}"
    return bool(correct_word) if return_bool else correct_word


def day_of_week():
    current_date = datetime.datetime.now()
    day_of_week = current_date.weekday()
    days_of_week_text = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    current_day = days_of_week_text[day_of_week]
    return current_day


def mocked_get(*args, **kwargs):
    return "badger-racoon"