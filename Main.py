"""démineur"""
"""
easy : 1chance/5 de tomber sur une bombe et comptabilise seulement les voisins adjacents
normal : 1chance/5 de tomber sur une bombe et comptabilise tous les voisins même ceux en diagonale
hardcore : 2chances/5 de tomber sur une bombe et comptabilise tous les voisins même ceux en diagonale
"""

nombre_de_cases = 100     #Valeurs possibles : 50,100,150,200,250
difficulty = 'normal'       # easy, normal ou hardcore

import tkinter as tk
import random  
import time
import math

app = tk.Tk()
app.title("Démineur")
app.minsize(1270,800)
app.resizable(width=True, height=True)
app.geometry("800x645+0+0")
app.configure(bg = "light blue")
Frame = tk.Frame(app, bg='light blue')

running = True
tricher = False
nbre_de_coups = 0
nombre_de_cases_par_ligne = int(math.sqrt(nombre_de_cases))
nombre_reel_de_cases = (int(math.sqrt(nombre_de_cases))**2)+1

coord_x,coord_y='échelle','échelle'
largeur, hauteur = 'échelle','échelle'

if nombre_de_cases == 50:
    coord_x, coord_y = 200,100
    largeur, hauteur = 6,3
    
elif nombre_de_cases == 100:
    coord_x, coord_y = 150,90
    largeur, hauteur = 5,2
    
elif nombre_de_cases == 150:
    coord_x, coord_y = 100,30
    largeur, hauteur = 5,2
    
elif nombre_de_cases == 200:
    coord_x, coord_y = 150,100
    largeur, hauteur = 3,1
    
elif nombre_de_cases == 250:
    coord_x, coord_y = 130,80
    largeur, hauteur = 3,1


class GameButton2(tk.Button):
    '''classe de boutons en dehors de la Frame'''
    
    def __init__(self,id):
        tk.Button.__init__(self,app)
        
        self.id = id
        self.state = 'eteint'
        
        if self.id == nombre_reel_de_cases + 1:
            self.config(text='Perdu', width=15, height=3, bg="red",font="GROBOLD.ttf 30",      
                relief=tk.RAISED, cursor = 'hand2',command=app.destroy)
        
        if self.id == nombre_reel_de_cases + 2:
            self.config(text='GAGNE', width=15, height=3, bg="green",font="GROBOLD.ttf 30",      
                relief=tk.RAISED, cursor = 'hand2',command=app.destroy)
                
        if self.id == nombre_reel_de_cases + 3:
            self.config(text="", width=1, height=1, bg="light blue",font="GROBOLD.ttf 1", 
            cursor = 'hand2', relief=tk.FLAT,command=self.apparaitre)
    
    def apparaitre(self):
        global tricher
        
        if tricher == False:
            tricher=True
            for i in range(len(Liste_boutons)):
                if Liste_status[i]=='bombe':
                    Liste_boutons[i].config(text='O')
        elif tricher == True:
            tricher=False
            for i in range(len(Liste_boutons)):
                if Liste_status[i]=='bombe':
                    Liste_boutons[i].config(text='')
                

class GameButton(tk.Button):
    """classe de boutons dans la frame de jeu"""
    
    def __init__(self,id):
        tk.Button.__init__(self,Frame)
        
        self.id = id
        self.state = 'caché'
        
        if self.id in list(range(nombre_reel_de_cases)):
            self.config(text="", width=largeur, height=hauteur, bg="blue",font="GROBOLD.ttf 10",      
                relief=tk.RAISED, cursor = 'hand2',command=self.lancement)
        
    
    def changer(self,event):
        '''change la couleur lorsqu'on passe au dessus du bouton'''
        try:
            if liste_autres_widgets[0]['bg']=='red':
                liste_autres_widgets[0].configure(bg='pink')
            elif liste_autres_widgets[0]['bg']=='pink':
                liste_autres_widgets[0].configure(bg='red')
        except:
            pass
        try:
            if liste_autres_widgets[1]['bg']=='green':
                liste_autres_widgets[1].configure(bg='light green')
            elif liste_autres_widgets[1]['bg']=='light green':
                liste_autres_widgets[1].configure(bg='green')
        except:
            pass
    
        
    def gagner(self):
        
        Liste_label[1].destroy()
        Liste_label[2].destroy()
        Liste_label[3].destroy()
        
        for i in range(len(Liste_boutons)):
            if Liste_status[i]=='bombe':
                Liste_boutons[i].config(text='O',bg='light green')
        
        liste_autres_widgets[1].place(x=800,y=200)
        liste_autres_widgets[1].bind("<Enter>", self.changer)
        liste_autres_widgets[1].bind("<Leave>", self.changer)
        
        Liste_label[0].config(text="Nombre de coups : {}".format(nbre_de_coups))
        Liste_label[0].place(x=800, y=400)
            
            
    def perdre(self):
        
        Liste_label[1].destroy()
        Liste_label[2].destroy()
        Liste_label[3].destroy()
        
        for i in range(len(Liste_boutons)):
            if Liste_status[i]=='bombe':
                Liste_boutons[i].config(text='O',bg='pink')
        self.config(text='X',bg='red')
        
        liste_autres_widgets[0].place(x=800,y=200)
        liste_autres_widgets[0].bind("<Enter>", self.changer)
        liste_autres_widgets[0].bind("<Leave>", self.changer)
        
        Liste_label[0].config(text="Nombre de coups : {}".format(nbre_de_coups))
        Liste_label[0].place(x=800,y=400)


    def test(self):
        global running,nbre_de_coups
        
        n_cachés=0
        for i in Liste_boutons:
            if i['bg']=='blue' or i['bg']=='grey':
                n_cachés+=1
        
        nbre_bombes=Liste_status2.count('bombe')
        
        if n_cachés == nbre_bombes:
            self.gagner()
            running = False
            
        
    def lancement(self):
        global running
        
        if running == True:
            
            if Liste_status[self.id-1] == 'bombe':
                self.perdre()
                running = False
                
            else:
                
                if self.state == 'caché':
                    
                    for i in range(len(L)//nombre_de_cases_par_ligne):
                        try :
                            emplacement = Liste_boutons_prime[i].index(self)
                            indice=i
                        except:
                            pass
    
                    # on a donc self = Liste_boutons_prime[indice][emplacement]
                    
                    self.config(bg='white')
                    self.state = 'découvert'
                    
                    voisins=[]
                    
                    if indice>0:
                        try:
                            voisins.append(Liste_status_prime[indice-1][emplacement])
                        except:
                            pass
                            
                    if emplacement<nombre_de_cases_par_ligne:
                        try:
                            voisins.append(Liste_status_prime[indice][emplacement+1])
                        except:
                            pass
                            
                    if indice<len(Lprime):
                        try:
                            voisins.append(Liste_status_prime[indice+1][emplacement])
                        except:
                            pass
                    
                    if emplacement>0:
                        try:
                            voisins.append(Liste_status_prime[indice][emplacement-1])
                        except:
                            pass
                    #
                    if difficulty == 'normal' or difficulty == 'hardcore' :
                        if emplacement<nombre_de_cases_par_ligne and indice>0:
                            try:
                                voisins.append(Liste_status_prime[indice-1][emplacement+1])
                            except:
                                pass
                        
                        if emplacement<nombre_de_cases_par_ligne and indice<len(Lprime):
                            try:
                                voisins.append(Liste_status_prime[indice+1][emplacement+1])
                            except:
                                pass
                                
                        if emplacement>0 and indice>0:
                            try:
                                voisins.append(Liste_status_prime[indice-1][emplacement-1])
                            except:
                                pass
                                
                        if emplacement>0 and indice<len(Lprime):
                            try:
                                voisins.append(Liste_status_prime[indice+1][emplacement-1])
                            except:
                                pass
                    
                    nb_bombes_voisines = voisins.count('bombe')
                    if nb_bombes_voisines != 0:
                        
                        Liste_boutons_prime[indice][emplacement].config(text=nb_bombes_voisines)
                        
                    else:
                        if indice>0:
                            try:
                                Liste_boutons_prime[indice-1][emplacement].lancement()
                            except:
                                pass
                        
                        if emplacement<nombre_de_cases_par_ligne:
                            try:
                                Liste_boutons_prime[indice][emplacement+1].lancement()
                            except:
                                pass
                        
                        if indice<len(Lprime):
                            try:
                                Liste_boutons_prime[indice+1][emplacement].lancement()
                            except:
                                pass
                        
                        if emplacement>0:
                            try:
                                Liste_boutons_prime[indice][emplacement-1].lancement()
                            except:
                                pass
                        #
                        if difficulty == 'hard' or difficulty == 'hardcore' :
                            if emplacement<nombre_de_cases_par_ligne and indice>0:
                                try:
                                    voisins.append(Liste_status_prime[indice-1][emplacement+1])
                                except:
                                    pass
                            
                            if emplacement<nombre_de_cases_par_ligne and indice<len(Lprime):
                                try:
                                    voisins.append(Liste_status_prime[indice+1][emplacement+1])
                                except:
                                    pass
                                    
                            if emplacement>0 and indice>0:
                                try:
                                    voisins.append(Liste_status_prime[indice-1][emplacement-1])
                                except:
                                    pass
                                    
                            if emplacement>0 and indice<len(Lprime):
                                try:
                                    voisins.append(Liste_status_prime[indice+1][emplacement-1])
                                except:
                                    pass
       
        self.test()
    
        
class GameLabel(tk.Label):
    
    def __init__(self,id):
        tk.Label.__init__(self,app)
        
        self.id = id
        
        if self.id == 0:
            self.config(bg='light blue',fg='red',font='Arial 30')
        elif self.id == 1:
            self.config(text='Démineur',bg='light blue',fg='blue',font='Arial 30 bold')
        elif self.id == 2:
            self.config(text='Cliquez sur toutes les cases vides en évitant',
            bg='light blue',fg='black',font='Arial 15')
        elif self.id == 3:
            self.config(text='les mines cachées.',
            bg='light blue',fg='black',font='Arial 15')
            


def plus(event):
    global nbre_de_coups,running
    if running == True:
        nbre_de_coups+=1
        
def marquer(event):
    x_clic=int(event.x_root)
    y_clic=int(event.y_root)
    
    for i in range(len(Liste_boutons)):
        x_bouton = Liste_boutons[i].winfo_rootx() 
        y_bouton = Liste_boutons[i].winfo_rooty()
        l = Liste_boutons[i].winfo_width()
        h = Liste_boutons[i].winfo_height()
        if x_clic in range(x_bouton,x_bouton+l+1) and y_clic in range(y_bouton,y_bouton+h+1):
            Liste_boutons[i].config(bg='grey')
            break
            
        
## Création des listes
L = [i for i in range(nombre_reel_de_cases+1)] 

if difficulty == 'hardcore':
    status=["bombe","bombe","vide","vide","vide","vide"]
else:
    status=["bombe","vide","vide","vide","vide"]
    

Liste_label=[]
Liste_label.append(GameLabel(0))
Liste_label.append(GameLabel(1))
Liste_label.append(GameLabel(2))
Liste_label.append(GameLabel(3))
    
# création de Lprime:
Lprime = [[]]*(len(L)//nombre_de_cases_par_ligne)
for j in range(1,(len(L)//nombre_de_cases_par_ligne)+1):
    for i in range(len(L)+1):
        if i>nombre_de_cases_par_ligne*(j-1) and i<=nombre_de_cases_par_ligne*j:
            Lprime[j-1] = Lprime[j-1] + [i]

# création de M
M = [0]*len(L)

#création de Liste_boutons
Liste_boutons=[]
for i in range(nombre_reel_de_cases+1):
    bouton = GameButton(i+1)
    Liste_boutons.append(bouton)
    
#création de Liste_boutons_prime
Liste_boutons_prime = [[]]*(len(Lprime))
for j in range(1,len(Lprime)+1):
    for i in range(1,len(L)+1):
        if i>nombre_de_cases_par_ligne*(j-1) and i<=nombre_de_cases_par_ligne*j:
            Liste_boutons_prime[j-1] = Liste_boutons_prime[j-1] + [Liste_boutons[i-1]]
nombre_de_lignes = len(Liste_boutons_prime)

#création de la liste des status des boutons
Liste_status = []
Liste_status_prime = [[]]*(len(L)//nombre_de_cases_par_ligne)
for i in range(nombre_reel_de_cases+1):
    Liste_status.append(random.choice(status))
for j in range(1,(len(L)//nombre_de_cases_par_ligne)+1):
    for i in range(len(L)+1):
        if i>nombre_de_cases_par_ligne*(j-1) and i<=nombre_de_cases_par_ligne*j:
            Liste_status_prime[j-1] = Liste_status_prime[j-1] + [Liste_status[i-1]]
            
#liste status réels (pb d'indiçage avec Liste_status
Liste_status2=[]
for j in Liste_status_prime:
    for i in j:
        Liste_status2.append(i)

#création de liste_autres_widgets
liste_autres_widgets = []
liste_autres_widgets.append(GameButton2(nombre_reel_de_cases + 1)) #bouton perdu
liste_autres_widgets.append(GameButton2(nombre_reel_de_cases + 2)) #bouton gagné
liste_autres_widgets.append(GameButton2(nombre_reel_de_cases + 3)) #bouton tricher

#affichage de la grille
for i in range(len(Lprime)):
    for j in range(len(L)//len(Lprime)):
        Liste_boutons_prime[i][j].grid(row=i,column=j, padx=2, pady=2)


app.bind('<Button-1>',plus)
app.bind('<Button-3>',marquer)

liste_autres_widgets[2].place(x=1265, y=0)
Liste_label[1].place(x=800,y=200)
Liste_label[2].place(x=800,y=300)
Liste_label[3].place(x=800,y=350)


Frame.place(x=coord_x,y=coord_y)
app.mainloop()
