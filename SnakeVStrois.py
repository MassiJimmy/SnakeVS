# Créé par jimmy, le 06/11/2020 en Python 3.7
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
can.create_text(375,165,text="3",fill='white',font=("arial",60))

#Bouton qui ferme le menu et qui ouvre le jeu
begin= Button (menu, text= "Commencer le jeu.",background="white",foreground="black",font=("Helvetica",10),command=menu.destroy)
begin.grid(row=0,column=0)


can.create_text(250,300,text="Par Jimmy Massi",fill='yellow',font=("arial",20))
can.create_text(250,340,text="Basé sur l'idée de Martin Luth",fill='white',font=("arial",18))

menu.mainloop()

#Fenêtre du jeu
snake=Tk()
snake.geometry("1420x800")
snake.title("Snake")
can=Canvas(snake,width=1420,height=800,background='white')
can.grid(columnspan=1,rowspan=1)
#Création du stage
stage=can.create_rectangle(0,0,400,400,fill="black")

stage2=can.create_rectangle(500,0,900,400,fill="black")

stage3=can.create_rectangle(1000,0,1400,400,fill="black")

#Coordonnées de vert
cx,cy=20,20
c2x,c2y=520,20
c3x,c3y=1020,20

#Coordonnées de bleu
dx,dy=360,360
d2x,d2y=860,360
d3x,d3y=1360,360

px=140
py=140
p2x=680
p2y=180
p3x=1220
p3y=220


#vecteur
xv=20
yv=20

#Placement  des joueurs
serpent=can.create_rectangle(cx,cy,cx+20,cy+20,fill="green")
serpent2=can.create_rectangle(dx,dy,dx+20,dy+20,fill="blue")

serpentA=can.create_rectangle(c2x,c2y,c2x+20,c2y+20,fill="green")
serpentA2=can.create_rectangle(d2x,d2y,d2x+20,d2y+20,fill="blue")

serpentB=can.create_rectangle(c3x,c3y,c3x+20,c3y+20,fill="green")
serpentB2=can.create_rectangle(d3x,d3y,d3x+20,d3y+20,fill="blue")

#Placement du "fruit"
fruit=can.create_rectangle(px,py,px+20,py+20,fill="red")

fruit2=can.create_rectangle(p2x,p2y,p2x+20,p2y+20,fill="red")

fruit3=can.create_rectangle(p3x,p3y,p3x+20,p3y+20,fill="red")

#Mise en place des scores
scorej1=0
scorej2=0

#Mise en places de l'affichage des score
can.create_rectangle(300,500,600,700,fill="#33FF33")
can.create_text(450,550,text="score J1:",fill="black",font=("arial",50))
can.create_text(450,650,text=str(scorej1),fill="black",font=("arial",50))

can.create_rectangle(800,500,1100,700,fill="#5555FF")
can.create_text(950,550,text="score J2:",fill="white",font=("arial",50))
can.create_text(950,650,text=str(scorej2),fill="white",font=("arial",50))

def game():
    global x,y,dx,dy,d2x,d2y,d3x,d3y,cx,cy,c2x,c2y,c3x,c3y,px,py,p2x,p2y,p3x,p3y,serpent,serpent2,fruit,scorej1,scorej2

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
        can.create_rectangle(300,500,600,700,fill="#33FF33")
        can.create_text(450,550,text="score J1:",fill="black",font=("arial",50))
        can.create_text(450,650,text=str(scorej1),fill="black",font=("arial",50))

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
        can.create_rectangle(800,500,1100,700,fill="#5555FF")
        can.create_text(950,550,text="score J2:",fill="white",font=("arial",50))
        can.create_text(950,650,text=str(scorej2),fill="white",font=("arial",50))

    #Si le joueur 1 prend le carré rouge on repositionne aléatoirement et on ajoute 1 à son score.

    if (c2x==p2x and c2y==p2y):
        p2x=randint(500,881)
        p2y=randint(0,381)
        #on s'assure que le cube rouge soit bien positionné afin que le joueur 1 peut le reprendre
        while p2x%20!=0:
            p2x=randint(500,881)
        while p2y%20!=0:
            p2y=randint(0,381)
        scorej1+=1
        can.coords(fruit2,p2x,p2y,p2x+20,p2y+20)
        #mise à jour de l'affichage des données
        can.create_rectangle(300,500,600,700,fill="#33FF33")
        can.create_text(450,550,text="score J1:",fill="black",font=("arial",50))
        can.create_text(450,650,text=str(scorej1),fill="black",font=("arial",50))

    #Si le joueur 2 prend le carré rouge on repositionne aléatoirement et on ajoute 1 à son score.

    if (d2x==p2x and d2y==p2y):
        p2x=randint(500,881)
        p2y=randint(0,381)
        #on s'assure que le cube rouge soit bien positionné afin que le joueur 2 peut le reprendre
        while p2x%20!=0:
            p2x=randint(500,881)
        while p2y%20!=0:
            p2y=randint(0,381)
        scorej2+=1
        can.coords(fruit2,p2x,p2y,p2x+20,p2y+20)
        #mise à jour de l'affichage des données
        can.create_rectangle(800,500,1100,700,fill="#5555FF")
        can.create_text(950,550,text="score J2:",fill="white",font=("arial",50))
        can.create_text(950,650,text=str(scorej2),fill="white",font=("arial",50))

    #Si le joueur 1 prend le carré rouge on repositionne aléatoirement et on ajoute 1 à son score.

    if (c3x==p3x and c3y==p3y):
        p3x=randint(1000,1381)
        p3y=randint(0,381)
        #on s'assure que le cube rouge soit bien positionné afin que le joueur 1 peut le reprendre
        while p3x%20!=0:
            p3x=randint(1000,1381)
        while p3y%20!=0:
            p3y=randint(0,381)
        scorej1+=1
        can.coords(fruit3,p3x,p3y,p3x+20,p3y+20)
        #mise à jour de l'affichage des données
        can.create_rectangle(300,500,600,700,fill="#33FF33")
        can.create_text(450,550,text="score J1:",fill="black",font=("arial",50))
        can.create_text(450,650,text=str(scorej1),fill="black",font=("arial",50))

    #Si le joueur 2 prend le carré rouge on repositionne aléatoirement et on ajoute 1 à son score.

    if (d3x==p3x and d3y==p3y):
        p3x=randint(1000,1381)
        p3y=randint(0,381)
        #on s'assure que le cube rouge soit bien positionné afin que le joueur 2 peut le reprendre
        while p3x%20!=0:
            p3x=randint(1000,1381)
        while p3y%20!=0:
            p3y=randint(0,381)
        scorej2+=1
        can.coords(fruit3,p3x,p3y,p3x+20,p3y+20)
        #mise à jour de l'affichage des données
        can.create_rectangle(800,500,1100,700,fill="#5555FF")
        can.create_text(950,550,text="score J2:",fill="white",font=("arial",50))
        can.create_text(950,650,text=str(scorej2),fill="white",font=("arial",50))


    if scorej1>=15:
        if scorej1 == scorej2:
            can.create_rectangle(25,525,275,675,fill="white")
            can.create_text(150,575,text="Le J1 est egal",fill="red",font=("arial",25))
            can.create_text(150,625,text="avec le J2",fill="red",font=("arial",25))
        elif scorej1 < scorej2:
            can.create_rectangle(25,525,275,675,fill="white")
            can.create_text(150,575,text="Le J1 peut être",fill="red",font=("arial",25))
            can.create_text(150,625,text="mangé par le J2",fill="red",font=("arial",25))
        else :
            can.create_rectangle(25,525,275,675,fill="white")
            can.create_text(150,575,text="Le J1 peut",fill="red",font=("arial",25))
            can.create_text(150,625,text="manger le J2",fill="red",font=("arial",25))
            if cx==dx and cy==dy:
                can.create_rectangle(0,0,1420,800,fill="black")
                can.create_text(710,400,text="Le joueur 1 a gagné.",fill="green",font=("Arial",60))

    if scorej2>=15:
        if scorej2 == scorej1:
            can.create_rectangle(1125,525,1375,675,fill="white")
            can.create_text(1250,575,text="Le J2 est égal",fill="red",font=("arial",25))
            can.create_text(1250,625,text="avec le J1",fill="red",font=("arial",25))
        elif scorej2 < scorej1:
            can.create_rectangle(1125,525,1375,675,fill="white")
            can.create_text(1250,575,text="Le J2 peut être",fill="red",font=("arial",25))
            can.create_text(1250,625,text="mangé par le J1",fill="red",font=("arial",25))
        else :
            can.create_rectangle(1125,525,1375,675,fill="white")
            can.create_text(1250,575,text="Le J2 peut",fill="red",font=("arial",25))
            can.create_text(1250,625,text="manger le J1",fill="red",font=("arial",25))
            if cx==dx and cy==dy:
                can.create_rectangle(0,0,1420,800,fill="black")
                can.create_text(710,400,text="Le joueur 2 a gagné.",fill="blue",font=("Arial",60))

    #repositionnement des joueurs si ils ressortent de la zone

    if cx>=400:
        cx=0
    if cy>=400:
        cy=0
    if cx<0:
        cx=380
    if cy<0:
        cy=380

    if dx>=400:
        dx=0
    if dy>=400:
        dy=0
    if dx<0:
        dx=380
    if dy<0:
        dy=380

    #stage 2

    if c2x>=900:
        c2x=500
    if c2y>=400:
        c2y=0
    if c2x<500:
        c2x=880
    if c2y<0:
        c2y=380

    if d2x>=900:
        d2x=500
    if d2y>=400:
        d2y=0
    if d2x<500:
        d2x=880
    if d2y<0:
        d2y=380

    #stage 3

    if c3x>=1400:
        c3x=1000
    if c3y>=400:
        c3y=00
    if c3x<1000:
        c3x=1380
    if c3y<0:
        c3y=380

    if d3x>=1400:
        d3x=1000
    if d3y>=400:
        d3y=0
    if d3x<1000:
        d3x=1380
    if d3y<0:
        d3y=380


    def clavier(evt):
        global xv,yv,cx,cy,c2x,c2y,c3x,c3y,dx,dy,d2x,d2y,d3x,d3y,serpent,serpent2

        # touche du clavier pour mouvoir le joueur 1 (vert)

        if evt.keysym == 'z' or evt.keysym == 'Z':
            cy-=yv
            c2y-=yv
            c3y-=yv

        if evt.keysym == 'q' or evt.keysym == 'Q':
            cx-=xv
            c2x-=xv
            c3x-=xv

        if evt.keysym == 's' or evt.keysym == 'S':
            cy+=yv
            c2y+=yv
            c3y+=yv

        if evt.keysym == 'd' or evt.keysym == 'D':
            cx+=xv
            c2x+=xv
            c3x+=xv

        # touche du clavier pour mouvoir le joueur 2 (bleu)

        if evt.keysym == 'Up':
            dy-=yv
            d2y-=yv
            d3y-=yv

        if evt.keysym == 'Left':
            dx-=xv
            d2x-=xv
            d3x-=xv

        if evt.keysym == 'Down' :
            dy+=yv
            d2y+=yv
            d3y+=yv

        if evt.keysym == 'Right':
            dx+=xv
            d2x+=xv
            d3x+=xv

        can.coords(serpent,cx,cy,cx+20,cy+20)
        can.coords(serpent2,dx,dy,dx+20,dy+20)
        can.coords(serpentA,c2x,c2y,c2x+20,c2y+20)
        can.coords(serpentA2,d2x,d2y,d2x+20,d2y+20)
        can.coords(serpentB,c3x,c3y,c3x+20,c3y+20)
        can.coords(serpentB2,d3x,d3y,d3x+20,d3y+20)

    snake.bind_all('<Key>', clavier)
    snake.after(5,game)

game()


snake.mainloop()
