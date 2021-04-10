from tkinter import *  
from tkinter.ttk import Radiobutton  
import tkinter as tk
from tkcalendar import *
import datetime as dt
import calendar
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys







text_error =''

period= dt.timedelta(hours=3)
now = dt.datetime.utcnow()
msk=now +period
print(msk)
hours_time = msk.strftime('%H')
h = int(hours_time) + 3


def counter_click(steps,clickes):
    #print (steps,clickes)
    error(steps, clickes)




def start(): 
    def clicked():  
        step=0
        var=0
        counter_click(step,var)
    lbl = Label(root)   
    lbl1 = tk.Label(root, text = '')
    lbl2 = tk.Label(root, text = '')
    lbl3 = tk.Label(root, text = '')
    lbl = tk.Label(root, text = 'Добро пожаловать в наше приложение', font=("Arial Bold", 14))
    lbl.grid(column=1, row=1)
    lbl1.grid(column=3, row=3, pady=0,padx=0)
    lbl2.grid(column=0, row=1, pady=0,padx=50)
    lbl3.grid(column=1, row=0, pady=50,padx=0)


    btn = Button(root, text="Начать!", command= lambda:  [clicked(), step_1(), btn1.grid_remove(),
        btn.grid_remove(), lbl.grid_remove(),  
        lbl3.grid_remove(),lbl2.grid_remove(),
        lbl1.grid_remove()] )
    btn1 = Button(root, text="Войти в систему", command= lambda:  [step_log(), btn1.grid_remove(),
        btn.grid_remove(), lbl.grid_remove(),  
        lbl3.grid_remove(),lbl2.grid_remove(),
        lbl1.grid_remove()] )
    btn.grid(row=3, column=1,pady=20,padx=10)
    btn1.grid(row=0, column=0, sticky="N")





def step_1():
    def clicked():  
        lbl.configure(text=selected.get())
        var= selected.get()
        step=1
        counter_click(step,var)


    selected = IntVar()  
    rad1 = Radiobutton(root,text='Легковой автомобиль', value=1, variable=selected)  
    rad2 = Radiobutton(root,text='Грузовой автомобиль', value=2, variable=selected)  
    rad3 = Radiobutton(root,text='Автобус', value=3, variable=selected) 
    rad4 = Radiobutton(root,text='Микроавтобус', value=4, variable=selected) 
    rad5 = Radiobutton(root,text='Мотоцикл', value=5, variable=selected)

    btn2 = Button(root, text="Далее", command=lambda:  [clicked(),btn3.grid_remove(),
        btn1.grid_remove(), btn2.grid_remove(), 
        rad1.grid_remove(), rad2.grid_remove(), rad3.grid_remove(), 
        rad4.grid_remove(), rad5.grid_remove(),lbl1.grid_remove(),
        lbl4.grid_remove(),lbl2.grid_remove(),lbl3.grid_remove(),lbler.grid_remove(),
        lblT.grid_remove()])  

    btn1 = Button(root, text="Назад", command=lambda:  [ start(), btn3.grid_remove(),
        btn1.grid_remove(), btn2.grid_remove(), rad1.grid_remove(), 
        rad2.grid_remove(), rad3.grid_remove(), rad4.grid_remove(), 
        rad5.grid_remove(),lbl1.grid_remove(),lbl4.grid_remove(),lbler.grid_remove(),
        lbl2.grid_remove(),lbl3.grid_remove(),lblT.grid_remove()])
    btn3 = Button(root, text="Войти в систему", command=lambda:  [ start(), btn3.grid_remove(),
        btn1.grid_remove(), btn2.grid_remove(), rad1.grid_remove(), 
        rad2.grid_remove(), rad3.grid_remove(), rad4.grid_remove(), 
        rad5.grid_remove(),lbl1.grid_remove(),lbl4.grid_remove(),
        lbl2.grid_remove(),lbl3.grid_remove(),lblT.grid_remove(), lbler.grid_remove()])
    lbl = Label(root)


    x=1
    y=1
    rad1.grid(column=x+1, row=y+1, sticky="W") 
    rad2.grid(column=x+1, row=y+2, sticky="W")  
    rad3.grid(column=x+1, row=y+3, sticky="W") 
    rad4.grid(column=x+1, row=y+4, sticky="W")
    rad5.grid(column=x+1, row=y+5, sticky="W") 
    btn1.grid(column=x+0, row=y+7, sticky="W")
    btn2.grid(column=x+3, row=y+7, sticky="W")
    btn3.grid(column=0, row=0, sticky="N",pady=0,padx=0)

    lbl1 = tk.Label(root, text = '')
    lbl2 = tk.Label(root, text = 'ТЕСТ', font=("Arial Bold", 15))
    lbl3 = tk.Label(root, text = '')
    lbl4 = tk.Label(root, text = '')
    lblT = tk.Label(root, text = 'Выберите авто', font=("Arial Bold", 14))
    lbler = tk.Label(root, text = f'{text_error}', font=("Arial Bold", 5))

    lbl1.grid(column=3, row=0, pady=0,padx=0)
    lbl2.grid(column=2, row=0, pady=10,padx=0)
    lbl3.grid(column=2, row=7, pady=0,padx=0)
    lbl4.grid(column=2, row=8, pady=0,padx=70)
    lblT.grid(column=2, row=1, pady=15,padx=0,columnspan=4)
    lbler.grid(column=8, row=1, pady=15,padx=0,columnspan=4)

    root.update()
    

     

def step_2():
  
    def clicked():  
        lbl.configure(text=selected.get())
        var= selected.get()
        step=2
        counter_click(step,var)

    selected = IntVar()  
    rad1 = Radiobutton(root,text='Брест', value=1, variable=selected)  
    rad2 = Radiobutton(root,text='Урбаны', value=2, variable=selected)  
    rad3 = Radiobutton(root,text='Брузги', value=3, variable=selected) 
    rad4 = Radiobutton(root,text='Котловка', value=4, variable=selected) 
    rad5 = Radiobutton(root,text='Бригоровщина', value=5, variable=selected)

    btn2 = Button(root, text="Далее", command=lambda:  [clicked(),
        btn1.grid_remove(), btn2.grid_remove(), btn3.grid_remove(),
        rad1.grid_remove(), rad2.grid_remove(),btn2.grid_remove(), rad3.grid_remove(), 
        rad4.grid_remove(), rad5.grid_remove(),lbl1.grid_remove(),
        lbl4.grid_remove(),lbl2.grid_remove(),lbl3.grid_remove(),lblT.grid_remove()])
                  

    btn1 = Button(root, text="Назад", command=lambda:  [step_1(), 
        btn2.grid_remove(), btn1.grid_remove(),btn2.grid_remove(), rad1.grid_remove(), 
        rad2.grid_remove(), rad3.grid_remove(), rad4.grid_remove(), 
        rad5.grid_remove(),lbl1.grid_remove(),lbl4.grid_remove(),
        lbl2.grid_remove(),lbl3.grid_remove(),lblT.grid_remove()])

    btn3 = Button(root, text="Войти в систему", command=lambda:  [step_log(), 
        btn2.grid_remove(), btn1.grid_remove(), btn3.grid_remove(), rad1.grid_remove(), 
        rad2.grid_remove(), rad3.grid_remove(), rad4.grid_remove(), 
        rad5.grid_remove(),lbl1.grid_remove(),lbl4.grid_remove(), lblT.grid_remove(),
        lbl2.grid_remove(),lbl3.grid_remove()])
    
    lbl = Label(root) 
    x=1
    y=1
    rad1.grid(column=x+1, row=y+1, sticky="W") 
    rad2.grid(column=x+1, row=y+2, sticky="W")   
    rad3.grid(column=x+1, row=y+3, sticky="W")
    rad4.grid(column=x+1, row=y+4, sticky="W")
    rad5.grid(column=x+1, row=y+5, sticky="W") 
    btn1.grid(column=x+0, row=y+7, sticky="W")
    btn2.grid(column=x+3, row=y+7, sticky="W")
    btn3.grid(column=0, row=0, sticky="N")

   
    lbl1 = tk.Label(root, text = '')
    lbl2 = tk.Label(root, text = 'ТЕСТ', font=("Arial Bold", 15))
    lbl3 = tk.Label(root, text = '')
    lbl4 = tk.Label(root, text = '')
    lblT = tk.Label(root, text = 'Выберите точку возврата      ', font=("Arial Bold", 14))
 


    lbl1.grid(column=5, row=0, pady=0,padx=70)
    lbl2.grid(column=2, row=0, pady=10,padx=0)
    lbl3.grid(column=2, row=7, pady=0,padx=0)
    lbl4.grid(column=2, row=8, pady=0,padx=70)
    lblT.grid(column=2, row=1, pady=15,padx=0,columnspan=4)
    

    root.update() 
   



   

def step_3():
    
    a = calendar.LocaleTextCalendar(locale='russian_Russia')
    cal= Calendar(root, selectmode="day",)
    cal.grid(row=3, column=2, pady=0)
    def grab_date():
        my_label.config(text=cal.get_date())
        step=3
        var=cal.get_date()
        counter_click(step,var)

    my_button= Button(root, text="далее",command=lambda:  [grab_date(),  
        my_button.grid_remove(), my_button2.grid_remove(), my_label.grid_remove(), my_button3.grid_remove(),
        cal.grid_remove(),lbl1.grid_remove(),lbl4.grid_remove(),lbl2.grid_remove(),
        lbl3.grid_remove(),lblT.grid_remove()])
    my_button2= Button(root, text="назад",command=lambda:  [step_2(),  
        my_button2.grid_remove(), my_button.grid_remove(), my_button3.grid_remove(),
        my_label.grid_remove(), cal.grid_remove(),
        lbl1.grid_remove(),lbl4.grid_remove(),lbl2.grid_remove(),
        lbl3.grid_remove(),lblT.grid_remove()])
    my_button3= Button(root, text="Вход в систему",command=lambda:  [step_log(),  
        my_button2.grid_remove(), my_button.grid_remove(), my_button3.grid_remove(),
        my_label.grid_remove(), cal.grid_remove(),
        lbl1.grid_remove(),lbl4.grid_remove(),lbl2.grid_remove(),
        lbl3.grid_remove(),lblT.grid_remove()])
    

    my_label = Label(root, text='')
    my_button.grid(column=4, row=5, sticky="W")
    my_label.grid(column=5, row=5, sticky="W")
   
    my_button2.grid(column=1, row=5, sticky="W") 
    my_button3.grid(column=0, row=0, sticky="N", pady=0,padx=0) 
    
    
    lbl1 = tk.Label(root, text = '')
    lbl2 = tk.Label(root, text = 'ТЕСТ', font=("Arial Bold", 15))
    lbl3 = tk.Label(root, text = '')
    lbl4 = tk.Label(root, text = '')
    lblT = tk.Label(root, text = 'Выберите дату         ', font=("Arial Bold", 14))


    #lbl1.grid(column=0, row=0, pady=0,padx=50)
    lbl2.grid(column=2, row=0, pady=5,padx=0)
    lbl3.grid(column=2, row=4, pady=0,padx=0)
    lbl4.grid(column=2, row=5, pady=0,padx=70)
    lblT.grid(column=2, row=1, pady=5,padx=0,columnspan=5,  sticky="N")


    root.update()



def step_4():
    def clicked(query):
        var=query
        counter_click(5,var)
        


    btn1 = tk.Button(root,text='00-01', command = lambda: [clicked(1)])
    btn2 = tk.Button(root,text='01-02', command = lambda: [clicked(2)])
    btn3 = tk.Button(root,text='02-03', command = lambda: [clicked(3)])
    btn4 = tk.Button(root,text='03-04', command = lambda: [clicked(4)])
    btn5 = tk.Button(root,text='04-05', command = lambda: [clicked(5)])
    btn6 = tk.Button(root,text='05-06', command = lambda: [clicked(6)])
    btn7 = tk.Button(root,text='06-07', command = lambda: [clicked(7)])
    btn8 = tk.Button(root,text='07-08', command = lambda: [clicked(8)])
    btn9 = tk.Button(root,text='08-09', command = lambda: [clicked(9)])
    btn10 = tk.Button(root,text='09-10', command = lambda: [clicked(10)])
    btn11 = tk.Button(root,text='10-11', command = lambda: [clicked(11)])
    btn12 = tk.Button(root,text='11-12', command = lambda: [clicked(12)])
    btn13 = tk.Button(root,text='12-13', command = lambda: [clicked(13)])
    btn14 = tk.Button(root,text='13-14', command = lambda: [clicked(14)])
    btn15 = tk.Button(root,text='14-15', command = lambda: [clicked(15)])
    btn16 = tk.Button(root,text='15-16', command = lambda: [clicked(16)])
    btn17 = tk.Button(root,text='16-17', command = lambda: [clicked(17)])
    btn18 = tk.Button(root,text='17-18', command = lambda: [clicked(18)])
    btn19 = tk.Button(root,text='18-19', command = lambda: [clicked(19)])
    btn20 = tk.Button(root,text='19-20', command = lambda: [clicked(20)])
    btn21 = tk.Button(root,text='20-21', command = lambda: [clicked(21)])
    btn22 = tk.Button(root,text='21-22', command = lambda: [clicked(22)])
    btn23 = tk.Button(root,text='22-23', command = lambda: [clicked(23)])
    btn00 = tk.Button(root,text='23-00', command = lambda: [clicked(00)])
    y=1
    x=2
    p_y=0
    p_x=0
    btn1.grid(row=y+1, column= x+1, pady=p_y, padx=p_x)
    btn2.grid(row=y+1, column= x+2, pady=p_y, padx=p_x)
    btn3.grid(row=y+1, column= x+3, pady=p_y, padx=p_x)
    btn4.grid(row=y+1, column= x+4, pady=p_y, padx=p_x)
    btn5.grid(row=y+1, column= x+5, pady=p_y, padx=p_x)
    btn6.grid(row=y+1, column= x+6, pady=p_y, padx=p_x)
    btn7.grid(row=y+2, column= x+1, pady=p_y, padx=p_x)
    btn8.grid(row=y+2, column= x+2, pady=p_y, padx=p_x)
    btn9.grid(row=y+2, column= x+3, pady=p_y, padx=p_x)
    btn10.grid(row=y+2, column= x+4, pady=p_y, padx=p_x)
    btn11.grid(row=y+2, column= x+5, pady=p_y, padx=p_x)
    btn12.grid(row=y+2, column= x+6, pady=p_y, padx=p_x)
    btn13.grid(row=y+3, column= x+1, pady=p_y, padx=p_x)
    btn14.grid(row=y+3, column= x+2, pady=p_y, padx=p_x)
    btn15.grid(row=y+3, column= x+3, pady=p_y, padx=p_x)
    btn16.grid(row=y+3, column= x+4, pady=p_y, padx=p_x)
    btn17.grid(row=y+3, column= x+5, pady=p_y, padx=p_x)
    btn18.grid(row=y+3, column= x+6, pady=p_y, padx=p_x)
    btn19.grid(row=y+4, column= x+1, pady=p_y, padx=p_x)
    btn20.grid(row=y+4, column= x+2, pady=p_y, padx=p_x)
    btn21.grid(row=y+4, column= x+3, pady=p_y, padx=p_x)
    btn22.grid(row=y+4, column= x+4, pady=p_y, padx=p_x)
    btn23.grid(row=y+4, column= x+5, pady=p_y, padx=p_x)
    btn00.grid(row=y+4, column= x+6, pady=p_y, padx=p_x)    
    
    btn_in = Button(root, text="Войти в систему", command=lambda:  [step_log(), lbl1.grid_remove(),btn_in.grid_remove(),

    btn1.grid_remove(),lbl1.grid_remove(), lbl2.grid_remove(), lblT.grid_remove(),
    btn2.grid_remove(),
    btn3.grid_remove(),
    btn4.grid_remove(),btn_exit.grid_remove(), btn_next.grid_remove(),
    btn5.grid_remove(),
    btn6.grid_remove(),
    btn7.grid_remove(),
    btn8.grid_remove(),
    btn9.grid_remove(),
    btn10.grid_remove(),
    btn11.grid_remove(),
    btn12.grid_remove(),
    btn13.grid_remove(),
    btn14.grid_remove(),
    btn15.grid_remove(),
    btn16.grid_remove(),lbl1.grid_remove(),
    btn17.grid_remove(),
    btn18.grid_remove(),
    btn19.grid_remove(),
    btn20.grid_remove(),
    btn21.grid_remove(),
    btn22.grid_remove(),
    btn23.grid_remove(), lbl3.grid_remove(),
    btn00.grid_remove()
])
    btn_exit = Button(root, text="назад", command=lambda:  [start(), lbl1.grid_remove(),btn_in.grid_remove(),

    btn1.grid_remove(), lbl2.grid_remove(), lblT.grid_remove(),
    btn2.grid_remove(),btn_exit.grid_remove(), btn_next.grid_remove(),
    btn3.grid_remove(),lbl1.grid_remove(),
    btn4.grid_remove(),
    btn5.grid_remove(),
    btn6.grid_remove(),
    btn7.grid_remove(),
    btn8.grid_remove(),
    btn9.grid_remove(),
    btn10.grid_remove(),
    btn11.grid_remove(),
    btn12.grid_remove(),
    btn13.grid_remove(),
    btn14.grid_remove(),
    btn15.grid_remove(),
    btn16.grid_remove(),
    btn17.grid_remove(), lbl3.grid_remove(),
    btn18.grid_remove(),
    btn19.grid_remove(),
    btn20.grid_remove(),
    btn21.grid_remove(),
    btn22.grid_remove(),
    btn23.grid_remove(),
    btn00.grid_remove()
])
    btn_next = Button(root, text="Далее", command=lambda:  [step_log(), lbl1.grid_remove(),btn_in.grid_remove(),
            btn1.grid_remove(), lbl2.grid_remove(), lblT.grid_remove(),
        btn2.grid_remove(),
        btn3.grid_remove(),lbl1.grid_remove(),
        btn4.grid_remove(),
        btn5.grid_remove(),btn_exit.grid_remove(), btn_next.grid_remove(),
        btn6.grid_remove(),
        btn7.grid_remove(),
        btn8.grid_remove(), lbl3.grid_remove(),
        btn9.grid_remove(),
        btn10.grid_remove(),
        btn11.grid_remove(),
        btn12.grid_remove(),
        btn13.grid_remove(),
        btn14.grid_remove(),
        btn15.grid_remove(),
        btn16.grid_remove(),
        btn17.grid_remove(),
        btn18.grid_remove(),
        btn19.grid_remove(),
        btn20.grid_remove(),
        btn21.grid_remove(),
        btn22.grid_remove(),
        btn23.grid_remove(),
        btn00.grid_remove()
])

    lbl2 = tk.Label(root, text = 'ТЕСТ', font=("Arial Bold", 15))
    lblT = tk.Label(root, text = 'Выберите дату ', font=("Arial Bold", 14))
    lbl1 = tk.Label(root, text = ' ')
    lbl3 = tk.Label(root, text = ' ')
    lbl2.grid(column=3, row=0, pady=0,padx=0,columnspan=10)
    lblT.grid(column=3, row=1, pady=0,padx=0,columnspan=10,  sticky="N")
    lbl1.grid(column=3, row=7, pady=0,padx=0,columnspan=10)
    lbl3.grid(column=2, row=7, pady=0,padx=20,)
    btn_next.grid(row=9, column= 9, pady=0, padx=0, sticky="N",columnspan=10,)
    btn_exit.grid(row=9, column= 1, pady=0, padx=0, sticky="N",columnspan=2,)
    btn_in.grid(row=0, column= 0, pady=0, padx=0,sticky="N")


    root.update()
    





def step_log():

    def button_click():
        text1 = enter_login.get()
        text2 = enter_rassword.get()
        data_base(10,text1)
        data_base(11,text2)
        error(4,1)
        #print(f'now {blok_l} ')
        
        
 
        

    text_enter_login = Label(text="Введите Ваш логин",)
    enter_login = Entry()
    text_enter_rassword = Label(text="Введите Ваш пароль")
    enter_rassword = Entry(show="*")
    button_enter = Button(root, text="Войти", command=lambda:  [button_click(),text_enter_login.grid_remove() ,enter_login.grid_remove() ,
                    enter_rassword.grid_remove() ,button_enter.grid_remove() ,button_reg.grid_remove() ,lbl1.grid_remove(), lbl4.grid_remove() ,lbl3.grid_remove(),
                     lbl2.grid_remove() , text_enter_rassword.grid_remove()])



    button_reg = Button(root, text="Зарегистрироваться", command=lambda:  [step_log(),step_reg(), text_enter_login.grid_remove() ,enter_login.grid_remove() ,
                    enter_rassword.grid_remove() ,button_enter.grid_remove() ,button_reg.grid_remove() ,lbl1.grid_remove(), lbl4.grid_remove() ,lbl3.grid_remove(),
                     lbl2.grid_remove() , text_enter_rassword.grid_remove()])
    text_enter_login.grid(column=1, row=5, pady=0,padx=0)
    enter_login.grid(column=3, row=5, pady=0, padx=0)
    text_enter_rassword.grid(column=1, row=6, pady=0,padx=0)
    enter_rassword.grid(column=3, row=6, pady=0, padx=0)
    button_enter.grid(column=3, row=7, pady=10, padx=0)
    button_reg.grid(column=3, row=8, pady=0, padx=0,columnspan=10)


    lbl2 = tk.Label(root, text = 'Вход в систему', font=("Arial Bold", 15))
    #lblT = tk.Label(root, text = 'Выберите дату ', font=("Arial Bold", 14))
    lbl1 = tk.Label(root, text = '')
    lbl4 = tk.Label(root, text = '')
    lbl3 = tk.Label(root, text = '')
    lbl2.grid(column=2, row=0, pady=0,padx=0,columnspan=10)
 #   lblT.grid(column=2, row=1, pady=0,padx=0,columnspan=10,  sticky="S")
    lbl1.grid(column=0, row=2, pady=0,padx=50.,columnspan=10)
    lbl4.grid(column=0, row=3, pady=0,padx=50,columnspan=10)
    lbl3.grid(column=0, row=4, pady=0,padx=50,)
    root.update()




def step_5():
    def button2():
            text1 = field_bron1.get()
            text2 = field_bron2.get()
            text3 = field_bron3.get()
            text4 = field_bron4.get()
            text5 = field_bron5.get()
           
            step_6()
            #print(text1, text2, text3, text4, text5)

    label_bron1 = Label(root, text="Вид")
    label_bron1.grid(column=0, row=2, sticky=E)
    field_bron1 = Entry(root, width=60)
    field_bron1.grid(column=1, row=2)

    label_bron2 = Label(root, text="Регистрационный номер")
    label_bron2.grid(column=0, row=3, sticky=E)
    field_bron2 = Entry(root, width=60)
    field_bron2.grid(column=1, row=3)

    label_bron3 = Label(root, text="Марка")
    label_bron3.grid(column=0, row=4, sticky=E)
    field_bron3 = Entry(root, width=60)
    field_bron3.grid(column=1, row=4)

    label_bron4 = Label(root, text="Модель")
    label_bron4.grid(column=0, row=5, sticky=E)
    field_bron4 = Entry(root, width=60)
    field_bron4.grid(column=1, row=5)

    label_bron5 = Label(root, text="Страна регистрации")
    label_bron5.grid(column=0, row=6, sticky=E)
    field_bron5 = Entry(root, width=60)
    field_bron5.grid(column=1, row=6)

    button = Button(root, text="Забронировать", command=lambda:  [button2(),label_bron1.grid_remove(),
                    field_bron1.grid_remove(), label_bron2.grid_remove(), label_bron2.grid_remove(),field_bron2.grid_remove(), label_bron3.grid_remove(),
                    field_bron3.grid_remove(),label_bron4.grid_remove(),button1.grid_remove(),
                        field_bron4.grid_remove(),label_bron5.grid_remove(),field_bron5.grid_remove(),button.grid_remove(),
                        lbl2.grid_remove(),lbl1.grid_remove(),
                            lbl4.grid_remove(),lbl3.grid_remove()])
    button1 = Button(root, text="Назад", command=lambda:  [step_4(),label_bron1.grid_remove(),button1.grid_remove(),
                    field_bron1.grid_remove(), label_bron2.grid_remove(), label_bron2.grid_remove(),field_bron2.grid_remove(), label_bron3.grid_remove(),
                    field_bron3.grid_remove(),label_bron4.grid_remove(),
                        field_bron4.grid_remove(),label_bron5.grid_remove(),field_bron5.grid_remove(),button.grid_remove(),
                        lbl2.grid_remove(),lbl1.grid_remove(),
                            lbl4.grid_remove(),lbl3.grid_remove()])



    button.grid(column=0, row=8, columnspan=5)
    button1.grid(column=0, row=9, columnspan=5)


    lbl2 = tk.Label(root, text = 'Вход в систему', font=("Arial Bold", 15))
    lbl1 = tk.Label(root, text = '')
    lbl4 = tk.Label(root, text = '')
    lbl3 = tk.Label(root, text = '')
    lbl2.grid(column=0, row=0, pady=0,padx=10,columnspan=5,sticky="S")
    lbl1.grid(column=0, row=0, pady=0,padx=0,columnspan=1)
    lbl4.grid(column=2, row=1, pady=20,padx=10,columnspan=1)
    lbl3.grid(column=2, row=7, pady=5,padx=10,columnspan=1)

    root.update()


def step_6():
    def clicked():  
        start1()



    lbl = Label(root)   
    lbl1 = tk.Label(root, text = '')
    lbl2 = tk.Label(root, text = '')
    lbl3 = tk.Label(root, text = '')
    lbl = tk.Label(root, text = 'Тестовое приложение пройденно', font=("Arial Bold", 14))
    lbl.grid(column=1, row=1)
    lbl1.grid(column=3, row=3, pady=0,padx=0)
    lbl2.grid(column=0, row=1, pady=0,padx=50)
    lbl3.grid(column=1, row=0, pady=50,padx=0)


    btn = Button(root, text="проверить!", command= lambda:  [clicked(), step_6(), btn1.grid_remove(),
        btn.grid_remove(), lbl.grid_remove(),  
        lbl3.grid_remove(),lbl2.grid_remove(),
        lbl1.grid_remove()] )
    btn1 = Button(root, text="перепройти", command= lambda:  [btn1.grid_remove(),
        btn.grid_remove(), lbl.grid_remove(),  
        lbl3.grid_remove(),lbl2.grid_remove(),
        lbl1.grid_remove()] )
    btn.grid(row=3, column=1,pady=20,padx=10)
    btn1.grid(row=0, column=0, sticky="N")



def step_reg():
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver= webdriver.Chrome(chrome_options=option)
    driver=webdriver.Chrome()
    reg = driver.get('https://belarusborder.by/reg/p')



#-----------------------------------Error-------------------------------------------------------------------------

def error(step_num,click_num):

    
    if step_num == 1:
        if click_num == 0:
            step_1()
            
        else:
            step_2()
            data_base(1,click_num)

    if step_num == 2:
        if click_num == 0:
            step_2()
            
        else:
            step_3()
            data_base(2,click_num)



    if step_num == 3:
        query_t =click_num
        query_pri= query_t.split('/')
        print (query_pri[2])
        query_full= f"{query_pri[-2]}.{query_pri[-3]}.20{query_pri[-1]}"
        data_base(3,query_full)

        step_4()
        
        
    if step_num == 4:

        if 10 not in blok_l.keys():

            step_log()
        else:
            data_base(3,click_num)
            step_5()




    if step_num == 5:

        data_base(4,click_num)

            


    if step_num == 6:
        if click_num == 0:
            text_error= 'erro11r'
            step_6()
            data_base(steper,clicker)
        else:
            step_1()


    if step_num == 7:
        if click_num == 0:
            text_error= 'erro11r'
            step_7()
            data_base(steper,clicker)
        else:
            step_8()





    


















blok_l= {


    '0':'0'
    



        }
#------------------------steper-----------------------------------------------------------

def data_base(steper,clicker):


    if str(steper) not in blok_l.keys():
        blok_l[steper] = clicker




  
root = Tk()  
root.title("Добро пожаловать в приложение.test")  
root.geometry('550x350') 

root.resizable(width=False, height=False)
root.after(100, start)







def starting(var,clic):  
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    #driver= webdriver.Chrome(chrome_options=option)
    driver=webdriver.Ie()

    #-----------------------------URL              Сюда нужно добавить икспаз через интернет експлоер------------------------------------------------------------------------------------

    def URL_query(query, value):
        
        if query == 0:
            reg = driver.get('https://belarusborder.by/reg/p')
        
        if query == 1:
            url=driver.get('https://belarusborder.by/book/category')
            choise=CLICK1(value)
        if query == 2:
            choise=CLICK1(value)
            
        if query == 3:
            choise=times_choise(value)
        
        if query == 4:
            choise=houers_chose(value)

    #--------------------chose---------------------------------------------------------------------------------------------------------------




    def CLICK1(clicks):
        sleep(1) 
        if clicks == 1:
            choise = driver.find_element_by_css_selector('#category > div:nth-child(1) > label > span.radio-custom').click()
        if clicks == 2:
            choise = driver.find_element_by_xpath('//*[@id="category"]/div[2]/label/span[1]').click()
        if clicks == 3:
            choise = driver.find_element_by_xpath('//*[@id="category"]/div[3]/label/span[1]').click()
        if clicks == 4:
            choise = driver.find_element_by_xpath('//*[@id="category"]/div[4]/label/span[1]').click()   
        if clicks == 5:
            choise = driver.find_element_by_xpath('//*[@id="category"]/div[5]/label/span[1]').click()   

    #-------------------------Time--------------------------------------------------------------------------------------------

    def times_choise(houres):
         url=driver.get(f'https://belarusborder.by/book/time?date=25.02.2021')
    def houers_chose(chose1):
      	houres_id = chose1
      	try:
    	  	choise = driver.find_element_by_xpath(f'//*[@id="content"]/div/div[2]/div/div[2]/div[1]/div/div/div[3]/div[{houres_id}]/div').click()
      	except:
      		step_4()
      		sleep(10)
    def logining():
    	sleep(2)
    	choise1 = driver.find_element_by_xpath('//*[@id="authenticationForm1"]/div[1]/input')
    	choise1.send_keys('temur')
    	choise2 = driver.find_element_by_xpath('//*[@id="authenticationForm1"]/div[2]/input')
    	choise2.send_keys('dpd.pdg123')
    	sleep(1)
    	next_click = driver.find_element_by_xpath('//*[@id="loginBtn"]').click()



    def booking1():
    	sleep(2)
    	choise1 = driver.find_element_by_xpath('//*[@id="vehicles0"]/div[3]/div[2]/div[1]/input')
    	choise1.send_keys('rey15rye1ye6')
    	choise2 = driver.find_element_by_xpath('//*[@id="vehicles0"]/div[3]/div[4]/div[1]/input')
    	choise2.send_keys('fds1213')
    	next_click1 = driver.find_element_by_xpath('//*[@id="vehicles0"]/div[3]/div[3]/div[1]/div/div[1]').click()
    	next_click11 = driver.find_element_by_xpath('//*[@id="vehicles0"]/div[3]/div[3]/div[1]/div/div[2]/div/div[1]').click()
    	next_click2 = driver.find_element_by_xpath('//*[@id="vehicles0"]/div[3]/div[5]/div[1]/div/div[1]').click()
    	next_click22 = driver.find_element_by_xpath('//*[@id="vehicles0"]/div[3]/div[5]/div[1]/div/div[2]/div/div[1]').click()
    	next_click = driver.find_element_by_xpath('//*[@id="next"]').click()


    URL_query(1,blok_l[1])
    next_click = driver.find_element_by_xpath('//*[@id="next"]').click()
    URL_query(2,blok_l[2])
    next_click = driver.find_element_by_xpath('//*[@id="next"]').click()
    URL_query(3,blok_l[3])
    next_click = driver.find_element_by_xpath('//*[@id="next"]').click()
    URL_query(4,blok_l[4])
    next_click = driver.find_element_by_xpath('//*[@id="next"]').click()
    logining()
    booking1()



    #---------------------------------Log in-------------------------------------------------------------------------------------------------------------


    def log_in(mail,password):
        URL_query()

#----------------------------------Test--------------------------------------------------------------------------------------------------------------
def start1():
    
    print (blok_l)
    starting(1,blok_l[1])
    




root.mainloop()




