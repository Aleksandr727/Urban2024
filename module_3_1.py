# # Домашняя работа по уроку "Пространство имён"
# Задача "Счётчик вызовов":

calls = 0

def count_calls(*args, **kwargs):
  global calls
  calls += 1

def string_info(string):
  count_calls()
  str_ = len(string), string.upper(), string.lower()
  return str_

def is_contains(string, list_to_search):
  count_calls()
  for i in list_to_search:
    i.lower()
    if i.lower() in string.lower():
      return True
    else:
      return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)