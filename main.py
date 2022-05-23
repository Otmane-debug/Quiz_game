from tkinter import *
  
score = 0
tmp = 0
player_name = ""

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
        self.title = Label(self.frame_m, text="The Quiz", font=("Arial", 15))
        self.strt = Button(self.frame_m, text="Start", width=40, command= lambda :self.start(f))
        self.scores = Button(self.frame_m, text="Show Scores", width=40)
        self.qui = Button(self.frame_m, text="Exit", width=40, command=f.destroy)
       
        self.frame_m.pack(padx=10, pady=90)
        self.title.pack(pady=8)
        self.strt.pack()
        self.scores.pack()
        self.qui.pack()
        


        
    def start(self, f):
        self.frame_m.destroy()
        self.s = Player_start(f)


class Player_start:
    def __init__(self, f):
        self.frame_m = Frame(f, padx=5, pady=5)
        self.text = Label(self.frame_m, text="Enter your name :")
        self.name = Entry(self.frame_m)
        self.sub = Button(self.frame_m, text="Go", width=40, command=lambda :self.subs(self.name))

        self.frame_m.pack(padx=10, pady=80)
        self.text.pack()
        self.name.pack()
        self.sub.pack()
    
    def subs(self, n):
        global tmp
        global player_name

        player_name = n.get()
        print(player_name)
        
        self.frame_m.destroy()
        self.f1_fenetre1 = Stage_1(main_f, questions_1[0], true_questions_1[0], sug_q_1)
        tmp += 1

        
class Stage_1:
    def __init__(self, f, k, true_val, sug): 
        self.true_res = true_val
               
        self.frame_m = Frame(f, padx=5, pady=5)
        self.text = Label(self.frame_m, text=k)
        
        self.frame_m.pack(padx=10, pady=80)
        self.text.pack()
            
        for r in sug:
            self.prop = Label(self.frame_m, text=r)
            self.prop.pack()
                
        self.res = Entry(self.frame_m)
        self.next_btn = Button(self.frame_m, text="Next", width=40, command=lambda :self.next_s(self.res, self.true_res))

        self.res.pack()
        self.next_btn.pack(pady=8)
        
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
        self.text = Label(self.frame_m, text=k)
        
        self.frame_m.pack(padx=10, pady=80)        
        self.text.pack()
            
        for r in sug:
            self.prop = Label(self.frame_m, text=r)
            self.prop.pack()
                
        self.res = Entry(self.frame_m)
        self.next_btn = Button(self.frame_m, text="Next", width=40, command=lambda : self.next_s(self.res, self.true_res))
        self.res.pack()
        self.next_btn.pack(pady=8)
        
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
        self.next_btn = Button(self.frame_m, text="Next", width=40, command=lambda :self.next_f(self.res, self.true_res))
        
        self.frame_m.pack(padx=10, pady=80)
        self.text.pack()
        self.res.pack()
        self.next_btn.pack(pady=8)
    
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
            self.end = End_f(main_f)

class End_f:    
    def __init__(self, f):
        global score
        global player_name
        self.text_1 = "Well Play " + player_name + " !" 
        self.text_2 = "Your Score is : " + str(score)
        
        self.frame_m = Frame(f, padx=5, pady=5)
        self.text_f_1 = Label(self.frame_m, text=self.text_1)
        self.text_f_2 = Label(self.frame_m, text=self.text_2)
        self.next_btn = Button(self.frame_m, text="Menu", width=40, command=lambda : self.next_s(f))
        self.qui = Button(self.frame_m, text="Exit", width=40, command=f.destroy)

        self.frame_m.pack(padx=10, pady=80)
        self.text_f_1.pack()
        self.text_f_2.pack()
        self.next_btn.pack()
        self.qui.pack()
        
    def next_s(self, f):
        global score
        score = 0
        self.frame_m.destroy()
        self.men = Menu(f)
        
            

if __name__ == "__main__":
    main_f = Tk()

    main_f.geometry("500x350")
    main_f.title("Quiz Game")

    game_start =  Menu(main_f) 

    main_f.mainloop()
