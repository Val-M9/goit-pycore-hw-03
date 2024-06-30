from datetime import datetime
import re
import random


def get_days_from_today(date: str) -> int:
  today = datetime.today()
  try:
    result = today - datetime.strptime(date, '%Y-%m-%d')
    return result.days
  except (ValueError, TypeError):
    return 'Please, provide correct date format: YYYY-mm-dd'


def normalize_phone(phone_number: str) -> str:
  pattern = r'\D'
  formatted_phone = re.sub(pattern, '', phone_number)
  first_symbol = formatted_phone[:1]
  match first_symbol:
    case '3':
      return f'+{formatted_phone}'
    case '8':
      return f'+3{formatted_phone}'
    case '0':
      return f'+38{formatted_phone}'
    case _:
      return 'Correct phone was not provided'


def get_numbers_ticket(min_value: int, max_value: int, quantity: int):
  try:
    list_of_numbers = []
    if min_value < 1 or min_value > max_value:
      return 'Minimum start number should be greater than 0, and lesser than maximum range'
    elif max_value > 1000 or max_value < min_value:
      return 'Sorry, maximum range shouldn`t be greater than 1000 and less than min number.'
    elif quantity > (max_value - min_value) or quantity > max_value:
      return f'Please enter the quantity between tha min and max value'
    elif (max_value - min_value) < (quantity - 1):
      return 'Range should be greater than quantity. Please Provide correct numbers'
    else:
      for i in range(min_value, max_value+1):
        list_of_numbers.append(i)
      result = sorted(random.sample(list_of_numbers, quantity))
      return result
  except TypeError:
    return 'Please enter numbers only!'


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
  today = datetime.today().date()
  congratulation_list = []
  for user in users:
    name, birthday = user['name'], user['birthday']
    birthday_this_year = datetime.strptime(
        birthday, '%Y.%m.%d').date().replace(year=datetime.now().year)
    birthday_next_year = datetime.strptime(
        birthday, '%Y.%m.%d').date().replace(year=datetime.now().year + 1)
    upcoming_birthday = birthday_this_year if birthday_this_year >= today else birthday_next_year

    if (upcoming_birthday - today).days >= 0 and (upcoming_birthday - today).days <= 7:
      if upcoming_birthday.isoweekday() == 6:
        congratulation_day = upcoming_birthday.replace(
            day=upcoming_birthday.day + 2)
        congratulation_list.append(
            {'name': name, 'congratulation_date': datetime.strftime(congratulation_day, '%Y.%m.%d')})

      elif upcoming_birthday.isoweekday() == 7:
        congratulation_day = upcoming_birthday.replace(
            day=upcoming_birthday.day + 1)
        congratulation_list.append(
            {'name': name, 'congratulation_date': datetime.strftime(congratulation_day, '%Y.%m.%d')})

      else:
        congratulation_list.append(
            {'name': name, 'congratulation_date': datetime.strftime(upcoming_birthday, '%Y.%m.%d')})

  return congratulation_list


users = [
    {"name": "John Doe", "birthday": "1985.06.23"},
    {"name": "Jane Smith", "birthday": "1990.05.26"}
]

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

print(get_days_from_today('2022-10-10'))
print(get_numbers_ticket(10, 100, 6))
print([normalize_phone(num) for num in raw_numbers])
print(get_upcoming_birthdays(users))
