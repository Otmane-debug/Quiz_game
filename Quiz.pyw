from cgitb import text
from tkinter import *
from unittest import result
from webbrowser import get
  
score = 0
tmp = 0
player_name = ""
global data

questions_1 = ["In which continent France is ?", "In which Continent Egipte is ?", "In which continent Canada is ?"]
true_questions_1 = ["Europe", "Africa", "North America"]
sug_q_1 = ["Africa", "Europe", "Asie", "North America"]

questions_2 = ["Where Messi is from ?", "Where Neymar is from ?", "Where Mbapé is from ?"]
true_questions_2 = ["Argentine", "Brazil", "France"]
sug_q_2 = [["Argentine", "Brazil"], ["France", "Brazil"], ["France", "Spain"]]

questions_3 = ["what is the capital of Morocco ?", "What is the capital of France ?", "What is the capital of Spain ?"]
true_questions_3 =["Rabat", "Paris", "Madrid"]
    
    
class Menu:
    def __init__(self, f):
        self.frame_m = Frame(f, padx=5, pady=5, bg="#FF8C00")
        self.title = Label(self.frame_m, text="The Quiz", font=("Arial", 25), bg="#FF8C00")
        self.strt = Button(self.frame_m, text="Start", width=40, command= lambda : self.start(f))
        self.scores = Button(self.frame_m, text="Rank", width=40, command=lambda : self.his(f))
        self.qui = Button(self.frame_m, text="Exit", width=40, command=f.destroy)
       
        self.frame_m.pack(padx=10, pady=90)
        self.title.pack(pady=8)
        self.strt.pack()
        self.scores.pack()
        self.qui.pack()
        
    def start(self, fich):
        self.frame_m.destroy()
        self.s = Player_start(fich)

    def his(self, fich):
        global score
        score = 0
        self.frame_m.destroy()
        self.his = History(fich)

class Player_start:
    def __init__(self, f):
        self.frame_m = Frame(f, padx=5, pady=5, bg="#FF8C00")
        self.text = Label(self.frame_m, text="Enter your name :", bg="#FF8C00", font=("Arial", 15))
        self.name = Entry(self.frame_m)
        self.sub = Button(self.frame_m, text="Go", width=40, command=lambda :self.subs(self.name))

        self.frame_m.pack(padx=10, pady=80)
        self.text.pack(pady=8)
        self.name.pack()
        self.sub.pack(pady=8)
    
    def subs(self, n):
        global tmp
        global player_name

        if n.get():
            player_name = n.get()
        else:
            player_name = "anonymous"

        print(player_name)
        
        self.frame_m.destroy()
        self.f1_fenetre1 = Stage_1(main_f, questions_1[0], true_questions_1[0], sug_q_1)
        tmp += 1

class History:
    def __init__(self, f):
        self.frame_m = Frame(f, padx=5, pady=5, bg="#FF8C00")
        self.frame_m.pack(padx=10, pady=40)
        self.text = Label(self.frame_m, text="Rank", pady=8, font=("Arial", 15), bg="#FF8C00").pack(pady=8)    
        
        self.data = open("data.txt", "r")
        self.result = self.data.readlines()
        
        self.dic_data = {}
        
        for r in self.result:
            r = r.strip().split()
            ke = r[0]
            val = r[1]
            self.dic_data[ke] = val
        
        self.sorted_data = sorted(self.dic_data.keys(), key=lambda k :self.dic_data[k], reverse=True)        
        
        self.i = 1
        
        for k in self.sorted_data:
            self.text_e = "Player {} score : {}".format(k, self.dic_data[k])            
            self.lab = Label(self.frame_m, text=self.text_e, bg="#FF8C00", font=("Arial", 10)).pack()
            self.i += 1
            if self.i == 6:
                break
     
        self.men = Button(self.frame_m, text="Menu", width=40, command=lambda : self.next_s(f))
        self.qui = Button(self.frame_m, text="Exit", width=40, command=f.destroy)

        self.men.pack()
        self.qui.pack()
        
    def next_s(self, fen):    
        self.frame_m.destroy()
        self.men = Menu(fen)

class Stage_1:
    def __init__(self, f, k, true_val, sug): 
        self.true_res = true_val
               
        self.frame_m = Frame(f, padx=5, pady=5, bg="#FF8C00")
        self.text = Label(self.frame_m, text=k, font=("Arial", 15))
        
        self.frame_m.pack(padx=10, pady=80)
        self.text.pack(pady=8)
            
        for r in sug:
            self.prop = Label(self.frame_m, text=r, bg="#FF8C00", font=("Arial", 10))
            self.prop.pack()
                
        self.res = Entry(self.frame_m)
        self.next_btn = Button(self.frame_m, text="Next", width=40, command=lambda :self.next_s(self.res, self.true_res))

        self.res.pack()
        self.next_btn.pack(pady=8)
        
    def next_s(self, r, t):
        global tmp
        global score

        if r.get() == t.lower():
            score += 1
            
        print(score)

        self.frame_m.destroy()
        
        if tmp == 1:
            self.s1_f1 = Stage_1(main_f, questions_1[1], true_questions_1[1], sug_q_1)
            tmp += 1
        elif tmp == 2:
            self.s1_f2 = Stage_1(main_f, questions_1[2], true_questions_1[2], sug_q_1)
            tmp += 1
        elif tmp == 3:
            self.s2_f3 = Stage_2(main_f, questions_2[0], true_questions_2[0], sug_q_2[0])
            tmp += 1

class Stage_2:    
    def __init__(self, f, k, true_val, sug):
        self.true_res = true_val
               
        self.frame_m = Frame(f, padx=5, pady=5, bg="#FF8C00")
        self.text = Label(self.frame_m, text=k, font=("Arial", 15))
        
        self.frame_m.pack(padx=10, pady=80)        
        self.text.pack(pady=8)
            
        for r in sug:
            self.prop = Label(self.frame_m, text=r, bg="#FF8C00", font=("Arial", 10))
            self.prop.pack()
                
        self.res = Entry(self.frame_m)
        self.next_btn = Button(self.frame_m, text="Next", width=40, command=lambda : self.next_s(self.res, self.true_res))
        
        self.res.pack()
        self.next_btn.pack(pady=8)
        
    def next_s(self, r, t):
        global tmp
        global score
        
        if r.get() == t.lower():
            score += 1
        print(score)
        
        self.frame_m.destroy()
        
        if tmp == 4:
            self.s2_f4 = Stage_2(main_f, questions_2[1], true_questions_2[1], sug_q_2[1])
            tmp += 1
        elif tmp == 5:
            self.s2_f5 = Stage_2(main_f, questions_2[2], true_questions_2[2], sug_q_2[2])
            tmp += 1
        elif tmp == 6:
            self.s3_f6 = Stage_3(main_f, questions_3[0], true_questions_3[0])
            tmp += 1

class Stage_3:
    def __init__(self, f, k, true_val): 
        self.true_res = true_val
               
        self.frame_m = Frame(f, padx=5, pady=5, bg="#FF8C00")
        self.text = Label(self.frame_m, text=k, font=("Arial", 15))  
        self.res = Entry(self.frame_m)
        self.next_btn = Button(self.frame_m, text="Next", width=40, command=lambda :self.next_f(self.res, self.true_res))
        
        self.frame_m.pack(padx=10, pady=80)
        self.text.pack(pady=8)
        self.res.pack()
        self.next_btn.pack(pady=8)
    
    def next_f(self, r, t):
        global tmp
        global score

        if r.get() == t or r.get() == t.lower():
            score += 1
            
        print(score)
        
        self.frame_m.destroy()
        if tmp == 7:
            self.s3_f7 = Stage_3(main_f, questions_3[1], true_questions_3[1])
            tmp += 1
        elif tmp == 8:
            self.s3_f8 = Stage_3(main_f, questions_3[2], true_questions_3[2])
            tmp += 1
        elif tmp == 9:
            tmp = 0
            self.end = End_f(main_f)

class End_f:
    global data
    global player_name
    global score
        
    def __init__(self, f):
        self.text_1 = "Well Play " + player_name + " !" 
        self.text_2 = "Your Score is : " + str(score)
        
        self.frame_m = Frame(f, padx=5, pady=5, bg="#FF8C00")
        self.title = Label(self.frame_m, text="End Game :", bg="#FF8C00", font=("Arial", 15))
        self.text_f_1 = Label(self.frame_m, text=self.text_1, bg="#FF8C00")
        self.text_f_2 = Label(self.frame_m, text=self.text_2, bg="#FF8C00")
        self.next_btn = Button(self.frame_m, text="Menu", width=40, command=lambda : self.next_s(f))
        self.qui = Button(self.frame_m, text="Exit", width=40, command=f.destroy)

        self.frame_m.pack(padx=10, pady=80)
        self.title.pack(pady=8)
        self.text_f_1.pack()
        self.text_f_2.pack()
        self.next_btn.pack(pady=8)
        self.qui.pack()
        
        
    def next_s(self, m_fen):
        global data
        global player_name
        global score
        
        data = open("./data.txt", "a")
        
        self.frame_m.destroy()
        self.men = Menu(m_fen)

        data.write("{} {}\n".format(player_name, score))
        score = 0
        
        data.close()

        
if __name__ == "__main__":
    
    main_f = Tk()
    main_f.configure(bg="#FF8C00")
    main_f.geometry("500x400")
    main_f.title("Quiz Game")

    game_start =  Menu(main_f) 

    main_f.mainloop()
    
