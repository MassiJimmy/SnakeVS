# Créé par jimmy, le 05/11/2020 en Python 3.7
from tkinter import*
from random import*

#Création du menu principale
menu = Tk()
menu.geometry("500x400")
menu.title("Menu")
can=Canvas(menu,width=500,height=400,background='black')
can.grid(columnspan=1,rowspan=1)

#Titre du jeu
can.create_text(150,100,text="S",fill='green',font=("arial",50))
can.create_text(190,100,text="n",fill='blue',font=("arial",50))
can.create_text(230,100,text="a",fill='green',font=("arial",50))
can.create_text(270,100,text="k",fill='blue',font=("arial",50))
can.create_text(310,100,text="e",fill='green',font=("arial",50))
can.create_text(385,100,text="VS",fill='red',font=("arial",70))
can.create_text(320,140,text="ordi",fill='white',font=("arial",20))

#Bouton qui ferme le menu et qui ouvre le jeu
begin= Button (menu, text= "Commencer le jeu.",background="white",foreground="black",font=("Helvetica",10),command=menu.destroy)
begin.grid(row=0,column=0)


can.create_text(250,300,text="Par Jimmy Massi",fill='yellow',font=("arial",20))


menu.mainloop()

#Fenêtre du jeu
snake=Tk()
snake.geometry("500x400")
snake.title("Snake")
can=Canvas(snake,width=500,height=400,background='white')
can.grid(columnspan=1,rowspan=1)
#Création du stage
stage=can.create_rectangle(0,0,400,400,fill="black")

cx,cy=20,20             #Coordonnées de vert
dx,dy=360,360           #Coordonnées de bleu
px=180
py=180

#vecteur
xv=20
yv=20
vordi=int(input("reglez la vitesse de l'ordi 1=lent et facile, 2= identique au joueur et un peu dur et >3: impossible."))
xvordi=10*vordi
yvordi=10*vordi

#mise en place de l'IA

ia=int(input("entre 1 et 3, entrez le niv de l'ordi"))

#Placement  des joueurs
serpent=can.create_rectangle(cx,cy,cx+20,cy+20,fill="green")
serpent2=can.create_rectangle(dx,dy,dx+20,dy+20,fill="blue")

#Placement du "fruit"
fruit=can.create_rectangle(px,py,px+20,py+20,fill="red")

#Mise en place des scores
scorej1=0
scorej2=0

#Mise en places de l'affichage des score
can.create_rectangle(420,50,480,90,fill="#33FF33")
can.create_text(450,60,text="score J1:",fill="black")
can.create_text(450,80,text=str(scorej1),fill="black")

can.create_rectangle(420,250,480,290,fill="#5555FF")
can.create_text(450,260,text="score J2:",fill="white")
can.create_text(450,280,text=str(scorej2),fill="white")

def game():
    global x,y,dx,dy,cx,cy,px,py,serpent,serpent2,fruit,scorej1,scorej2

    #Si le joueur 1 prend le carré rouge on repositionne aléatoirement et on ajoute 1 à son score.

    if (cx==px and cy==py):
        px=randint(0,381)
        py=randint(0,381)
        #on s'assure que le cube rouge soit bien positionné afin que le joueur 1 peut le reprendre
        while px%20!=0:
            px=randint(0,381)
        while py%20!=0:
            py=randint(0,381)
        scorej1+=1
        can.coords(fruit,px,py,px+20,py+20)
        #mise à jour de l'affichage des données
        can.create_rectangle(420,50,480,90,fill="#33FF33")
        can.create_text(450,60,text="score J1:",fill="black")
        can.create_text(450,80,text=str(scorej1),fill="black")

    #Si le joueur 2 prend le carré rouge on repositionne aléatoirement et on ajoute 1 à son score.

    if (dx==px and dy==py):
        px=randint(0,381)
        py=randint(0,381)
        #on s'assure que le cube rouge soit bien positionné afin que le joueur 2 peut le reprendre
        while px%20!=0:
            px=randint(0,381)
        while py%20!=0:
            py=randint(0,381)
        scorej2+=1
        can.coords(fruit,px,py,px+20,py+20)
        #mise à jour de l'affichage des données
        can.create_rectangle(420,250,480,290,fill="#5555FF")
        can.create_text(450,260,text="score J2:",fill="white")
        can.create_text(450,280,text=str(scorej2),fill="white")

    if scorej1>=10:
        if scorej1 == scorej2:
            can.create_rectangle(400,90,500,130,fill="white")
            can.create_text(450,100,text="Le J1 est egal",fill="red")
            can.create_text(450,120,text="avec le J2",fill="red")
        if scorej1 < scorej2:
            can.create_rectangle(400,90,500,130,fill="white")
            can.create_text(450,100,text="Le J1 peut être",fill="red")
            can.create_text(450,120,text="mangé par le J2",fill="red")
        if scorej1 > scorej2:
            can.create_rectangle(400,90,500,130,fill="white")
            can.create_text(450,100,text="Le J1 peut",fill="red")
            can.create_text(450,120,text="manger le J2",fill="red")
            if cx==dx and cy==dy:
                can.create_rectangle(0,0,500,400,fill="black")
                can.create_text(250,150,text="Le joueur a gagné.",fill="green",font=("Arial",25))
                can.create_text(250,250,text="WIN",fill="red",font=("Arial",35))

    if scorej2>=10:
        if scorej2 == scorej1:
            can.create_rectangle(400,290,500,330,fill="white")
            can.create_text(450,300,text="Le J2 est égal",fill="red")
            can.create_text(450,320,text="avec le J1",fill="red")
        if scorej2 < scorej1:
            can.create_rectangle(400,290,500,330,fill="white")
            can.create_text(450,300,text="Le J2 peut être",fill="red")
            can.create_text(450,320,text="mangé par le J1",fill="red")
        if scorej2 > scorej1:
            can.create_rectangle(400,290,500,330,fill="white")
            can.create_text(450,300,text="Le J2 peut",fill="red")
            can.create_text(450,320,text="manger le J1",fill="red")
            if cx==dx and cy==dy:
                can.create_rectangle(0,0,500,400,fill="black")
                can.create_text(250,150,text="L'ordi a gagné.",fill="blue",font=("Arial",25))
                can.create_text(250,250,text="GAME OVER",fill="red",font=("Arial",35))

    #repositionnement des joueurs si ils ressortent de la zone

    if cx>=400:
        cx=0
    if cy>=400:
        cy=0
    if cx<0:
        cx=380
    if cy<0:
        cy=380

    if dx>400:
        if ia == 1:
            dx=400
        if ia > 1:
            dx=0
    if dy>400:
        if ia > 1:
            dy=400
        if ia > 1:
            dy=0
    if dx<0:
        if ia > 1:
            dx=0
        if ia > 1:
            dx=380
    if dy<0:
        if ia > 1:
            dy=0
        if ia > 1:
            dy=380
    can.coords(serpent2,dx,dy,dx+20,dy+20)

    can.coords(serpent,cx,cy,cx+20,cy+20)


    def clavier(evt):
        global xv,yv,cx,cy,dx,dy,px,py,serpent

        # touche du clavier pour mouvoir le joueur 1 (vert)

        if evt.keysym == 'z' or evt.keysym == 'Z':
            cy-=yv

        if evt.keysym == 'q' or evt.keysym == 'Q':
            cx-=xv

        if evt.keysym == 's' or evt.keysym == 'S':
            cy+=yv

        if evt.keysym == 'd' or evt.keysym == 'D':
            cx+=xv

        can.coords(serpent,cx,cy,cx+20,cy+20)


    snake.bind_all('<Key>', clavier)

    def ArtificialIntelligence():
        global serpent2,scorej2,dx,dy,xv,yv
         #pour mouvoir l'ordi (bleu)
        if ia == 1:
            if scorej2 < 10:
                if dx > px:
                    print("a")
                    dx-=xvordi

                elif dx < px:
                    print("b")
                    dx+=xvordi

                elif dy > py:
                    print("c")
                    dy-=yvordi

                elif dy < py:
                    print("d")
                    dy+=yvordi
            if scorej2 >= 10:
                if scorej2 <= scorej1:
                    if dx > px:
                        print("a")
                        dx-=xvordi

                    elif dx < px:
                        print("b")
                        dx+=xvordi

                    elif dy > py:
                        print("c")
                        dy-=yvordi

                    elif dy < py:
                        print("d")
                        dy+=yvordi

                if scorej2 > scorej1:
                    if dx > cx:
                        print("a")
                        dx-=xvordi

                    elif dx < cx:
                        print("b")
                        dx+=xvordi

                    elif dy > cy:
                        print("c")
                        dy-=yvordi

                    elif dy < cy:
                        print("d")
                        dy+=yvordi

        elif ia == 2:
            if scorej2 < 10:
                if dx > px:
                    print("a")
                    dx-=xvordi

                if dx < px:
                    print("b")
                    dx+=xvordi

                elif dy > py:
                    print("c")
                    dy-=yvordi

                elif dy < py:
                    print("d")
                    dy+=yvordi
            if scorej2 >= 10:
                if scorej2 <= scorej1:
                    if dx > px:
                        print("a")
                        dx-=xvordi

                    if dx < px:
                        print("b")
                        dx+=xvordi

                    elif dy > py:
                        print("c")
                        dy-=yvordi

                    elif dy < py:
                        print("d")
                        dy+=yvordi

                if scorej2 > scorej1:
                    if dx > cx:
                        print("a")
                        dx-=xvordi

                    if dx < cx:
                        print("b")
                        dx+=xvordi

                    elif dy > cy:
                        print("c")
                        dy-=yvordi

                    elif dy < cy:
                        print("d")
                        dy+=yvordi

        else:
            if scorej2 < 10:
                if dx > px:
                    print("a")
                    dx-=xvordi

                if dx < px:
                    print("b")
                    dx+=xvordi

                elif dy > py:
                    print("c")
                    dy-=yvordi

                elif dy < py:
                    print("d")
                    dy+=yvordi
            if scorej2 >= 10:
                if scorej2 <= scorej1:
                    if dx > px:
                        print("a")
                        dx-=xvordi

                    if dx < px:
                        print("b")
                        dx+=xvordi

                    elif dy > py:
                        print("c")
                        dy-=yvordi

                    elif dy < py:
                        print("d")
                        dy+=yvordi

                if scorej2 > scorej1:
                    if dx > cx:
                        print("a")
                        dx-=xvordi

                    if dx < cx:
                        print("b")
                        dx+=xvordi

                    elif dy > cy:
                        print("c")
                        dy-=yvordi

                    elif dy < cy:
                        print("d")
                        dy+=yvordi


        can.coords(serpent2,dx,dy,dx+20,dy+20)
        snake.after(10,game)

    ArtificialIntelligence()

game()




snake.mainloop()
