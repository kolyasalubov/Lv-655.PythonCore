#Записати в стрічку філософію Пайтона
# Знайти в заданій стрічці кількість
#входжень слів (better, never, is)
#- Вивести весь текст у верхньому регістрі (всі великі літери)
#- Замінити всі входження символу “і” на “&”

import contextlib, io
with contextlib.redirect_stdout(zen := io.StringIO()):  #  try to catch "import this" ;)
   import this

str = zen.getvalue() # obj StrinGIO to str for use str.built-In method
 
# use str.built-In method count, upper, replace


print(f"Found 'better' {str.count('better')} times")
print(f"Found 'better' {str.count('never')} times")
print(f"Found 'better' {str.count('is')} times"+"\n")

print(str.upper())

print(str.replace('i','&'))