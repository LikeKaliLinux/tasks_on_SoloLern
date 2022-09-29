#Вы работает над поисковой системой. Берегись Google!

#Данный код принимает text и word в качестве входящих данных и передает их в функцию с именем search().

#Функция search() должна вернуть "Word found", если слово представлено в тексте или "Word not found", если не представлено.

#Пример Входных Данных
#"This is awesome"
#"awesome"

#Пример Выходных Данных
#Word found

print("SL5. Search Engine")

text = input()
word = input()

def search(text, word):
    if word in text:
        print("Word found.")
    else: 
        print("Word not found.")

search(text, word)




