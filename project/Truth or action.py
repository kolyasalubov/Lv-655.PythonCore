from tkinter import *
from random import*
import questions

# створюємо вікно
root = Tk()

root.geometry('800x450')#задаємо розмір вікна
root.title("Truth or action")# задаємо назву вікна
root.wm_attributes('-alpha', 0.9)#додали прозорісь вікна
root.resizable(width=False, height=False)#заборагили змінювати розмір вікна

image_skr = PhotoImage(file = 'E:123.png')# встановлюмо фон основного вікна
skrin = Label(root, image = image_skr)
skrin.grid()

counter_ques=0
counter_task=0
count_ques=len(questions.ques)
count_task=len(questions.task)

# логіка роботи блоку "Правда"
def quest():
    global counter_ques
    global count_ques
    lbl_result["text"] = element = choice(questions.ques)# функція рандому для запитань "Правда"
    questions.ques.remove(element)#видаляємо елемент який випав для уникнення повторів
    counter_ques+=1
    if counter_ques==count_ques or counter_task==count_task:#умова друку повідомлення про закінчення гри
        lbl_result["foreground"] ="Green"
        lbl_result["text"] ="Вітаємо!!!\nГра закінчена."
        
# логіка роботи блоку "Дія"
def quest1():
    global counter_task
    global count_task
    element= choice(questions.task)# функція рандому для завдань "Дія" 
    lbl_result["text"] = element
    questions.task.remove(element)#видаляємо елемент який випав для уникнення повторів
    counter_task+=1
    if counter_task==count_task or counter_ques==count_ques:#умова друку повідомлення про закінчення гри
        lbl_result["foreground"] ="Green"
        lbl_result["text"] ="Вітаємо!!!\nГра закінчена."
  
# створюємо кнопку "Правда"
btn = Button(root,
             text="Правда",
             width=15,
             height=2, 
             bg="green",
             font="Verdana 20 italic",
             command=quest)
btn.place(relx=0.1, rely=0.75) #Задаєм координати розміщення кнопки

# створюємо кнопку "дія"
btn1 = Button(root, 
              text="Дія",
              width=15,
              height=2, 
              bg="red",
              font="Verdana 20 italic",
              command=quest1)       
btn1.place(relx=0.56, rely=0.75)

# загаловок та текст завань
lbl_result = Label(text="Обирай сказати правду чи виконати завдання",
                   foreground="red",
                    background="White",
                    font='arial 25',
                    )
lbl_result.place(relx=.5, rely=.3, anchor="c", bordermode=OUTSIDE)

mainloop()
