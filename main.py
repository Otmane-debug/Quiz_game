from tkinter import *
  
score = 0
tmp = 0

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
        self.frame_m = Frame(f, padx=5, pady=5)
        self.frame_m.pack(padx=10, pady=10)

        self.text = Label(self.frame_m, text="Enter your name :")
        self.name = Entry(self.frame_m)
        
        self.sub = Button(self.frame_m, text="S'inscrire", width=40, command=lambda :self.subs())
        self.strt = Button(self.frame_m, text="Start", width=40, command= lambda :self.start())
        self.qui = Button(self.frame_m, text="Exit", width=40, command=f.destroy)

        self.text.pack(pady=20)
        self.name.pack(pady=20)
        self.sub.pack()
        self.strt.pack()
        self.qui.pack()
    
    def subs(self): 
        print(self.name.get())
        
    def start(self):
        global tmp
        self.frame_m.destroy()
        tmp += 1
        self.f1_fenetre1 = Stage_1(main_f, questions_1[0], true_questions_1[0], sug_q_1)

        
class Stage_1:
    def __init__(self, f, k, true_val, sug): 
        self.true_res = true_val
               
        self.frame_m = Frame(f, padx=5, pady=5)
        self.frame_m.pack(padx=10, pady=10)
        self.text = Label(self.frame_m, text=k)
        self.text.pack()
            
        for r in sug:
            self.prop = Label(self.frame_m, text=r)
            self.prop.pack()
                
        self.res = Entry(self.frame_m)
        self.next_btn = Button(self.frame_m, text="Next", command=lambda :self.next_s(self.res, self.true_res))

        self.res.pack()
        self.next_btn.pack()
        
    def next_s(self, r, t):
        global tmp
        global score

        if r.get() == t:
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
               
        self.frame_m = Frame(f, padx=5, pady=5)
        self.frame_m.pack(padx=10, pady=10)
        self.text = Label(self.frame_m, text=k)
        self.text.pack()
            
        for r in sug:
            self.prop = Label(self.frame_m, text=r)
            self.prop.pack()
                
        self.res = Entry(self.frame_m)
        self.next_btn = Button(self.frame_m, text="Next", command=lambda : self.next_s(self.res, self.true_res))
        self.res.pack()
        self.next_btn.pack()
        
    def next_s(self, r, t):
        global tmp
        global score
        
        if r.get() == t:
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
               
        self.frame_m = Frame(f, padx=5, pady=5)
        self.text = Label(self.frame_m, text=k)  
        self.res = Entry(self.frame_m)
        self.next_btn = Button(self.frame_m, text="Next", command=lambda :self.next_f(self.res, self.true_res))
        
        self.frame_m.pack(padx=10, pady=10)
        self.text.pack()
        self.res.pack()
        self.next_btn.pack()
    
    def next_f(self, r, t):
        global tmp
        global score

        if r.get() == t:
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
            self.men = Menu(main_f)


main_f = Tk()
main_f.geometry("500x300")
main_f.title("Quiz Game")

game_start =  Menu(main_f) 

main_f.mainloop()