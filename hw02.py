# Необхідно розробити функцію яка:
# 1. приймає рядок як вхідний параметр
# 2. додає всі його символи до двосторонньої черги (deque з модуля collections в Python)
# 3. порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом
# 4. повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів
# 5. повинна бути нечутливою до регістру та пробілів

from collections import deque

def is_palindrome(s: str) -> bool:
    dq = deque(s.lower())

    while len(dq) > 1:
        if dq[0].isspace():
            dq.popleft()
            continue

        if dq[-1].isspace():
            dq.pop()
            continue

        if dq.popleft() != dq.pop():
            return False

    return True


# test cases
if __name__ == "__main__":

  assert is_palindrome('') == True  
  assert is_palindrome('а') == True
  assert is_palindrome('abba') == True  
  assert is_palindrome('Де помити мопед') == True
  assert is_palindrome('Хата на канатах') == True
  assert is_palindrome('Дорога на город') == True
  assert is_palindrome('Паліндром') == False




