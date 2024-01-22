from tkinter import *
import random
#0b99e0  


class Food:

    def __init__(self):

        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE #véletlenszerű étel generálás az x és y koordinátán a felületen.
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y] #tároljuk az érték koordinátáit

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")  #legömbölyítés, a vászonra elhelyezzük az ételt

#Classokat tegyük felülre

random_color = "#{:06x}".format(random.randint(0,0xFFFFFF))
class Snake:

            
    def __init__(self):
        self.body_size = BODY_PARTS #kezdeti testrész érték
        self.coordinates = [] #kígyó testrészének koordinátái
        self.squares = [] #kígyó négyzetekre történő megjelenítés
    
    
        for i in range(0, BODY_PARTS): 
            self.coordinates.append([0, 0]) #Beállítjuk a testrészek koordinátáit

        for x, y in self.coordinates: #végigmegy a self.coordinates listán
            random_color = "#{:06x}".format(random.randint(0,0xFFFFFF)) #"{:06x}".format() rész a számot hexadecimális formába alakítja hat karakter hosszúságú sztringgé. ez lesz í kígyó random színe
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=random_color, tag="kigyo") #létrehozza a téglalapokat a megadott koordinátán, random színű lesz a kígyó
            self.squares.append(square) #lista, ami a kígyó négyzeteit tartalmazza


GAME_WIDTH = 900
GAME_HEIGHT = 900 
SPEED = 200 
SPACE_SIZE = 50 #Kígyó és az étel négyzete a játékban
BODY_PARTS = 4 #Beállíthatjuk a 
LABEL_BG_COLOR = "#83eb13" 
FOOD_COLOR = "#FF0000" #Étel színe
BACKGROUND_COLOR = "#83eb13" #Ablak színe

#Barnabás
#******************************************************************************************************************

def next_turn(snake, food):
    # A kígyó fejének koordinátái
    x, y = snake.coordinates[0]

    # Az irány alapján a következő pozíció kiszámolása
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Az új fej pozíciójának hozzáadása a kígyó koordinátáihoz
    snake.coordinates.insert(0, (x, y))

    # Új négyzet létrehozása a kígyó új fejének grafikus reprezentációjaként
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=random_color)

    # Az új négyzet hozzáadása a kígyó négyzeteihez
    snake.squares.insert(0, square)

    # Étel elfogyasztásának ellenőrzése
    if x == food.coordinates[0] and y == food.coordinates[1]:
        # Pontszám növelése
        global score
        score += 1
        

        label.config(text="Pontszám:{}".format(score))

        # Az ételek eltávolítása és új étel létrehozása
        canvas.delete("food")
        food = Food()
    else:
        # Ha nem ette meg az almát akkor távolítsa el a kígyó farok részét
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # Ütközés ellenőrzése
    if check_collisions(snake):
        # Ha ütközés van, akkor játék vége
        game_over()
    else:
        # Ha nincs ütközés, hívja meg újra a függvényt a következő lépéshez
        window.after(SPEED, next_turn, snake, food)



def change_direction(new_direction):
    # Globális változó 'direction' használata
    global direction

    #Irányváltások****************************************
    # Irányváltás balra
    if new_direction == 'left':
        # Csak akkor változtatjuk meg az irányt balra, ha jelenlegi irány nem jobbra mutat
        if direction != 'right':
            direction = new_direction
    # Irányváltás jobbra
    elif new_direction == 'right':
        # Csak akkor változtatjuk meg az irányt jobbra, ha jelenlegi irány nem balra mutat
        if direction != 'left':
            direction = new_direction
    # Irányváltás felfelé
    elif new_direction == 'up':
        # Csak akkor változtatjuk meg az irányt felfelé, ha jelenlegi irány nem lefelé mutat
        if direction != 'down':
            direction = new_direction
    # Irányváltás lefelé
    elif new_direction == 'down':
        # Csak akkor változtatjuk meg az irányt lefelé, ha jelenlegi irány nem felfelé mutat
        if direction != 'up':
            direction = new_direction
#Roland
#******************************************************************************************************************


def check_collisions(snake):
    # A kedzéspont a kígyónak
    x, y = snake.coordinates[0]

    # Ellenőrzi, hogy a kígyó feje kilépett-e a megadott pályáról
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    # Ellenőrzi, hogy a kígyó feje ütközik-e a testével
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    # Ha nincs ütközés, akkor a játék folytatódhat
    return False

#A játék vége
def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
    font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")


window = Tk()
window.title("Színváltó Sárkány")
window.resizable(False, False)

score = 0
direction = 'right'

# Pontszám kijelző létrehozása és beállítása
label = Label(window, text="Pontszám:{}".format(score), font=('consolas', 40))
label.config(bg= "red")
label.pack(fill = BOTH, expand=YES)

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

# Ablak pozíciójának beállítása középre
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}") 
#Enikő
#******************************************************************************************************************

# Irányváltás (bal, jobb, le, fel)
window.bind('<a>', lambda left: change_direction('left'))
window.bind('<d>', lambda right: change_direction('right'))
window.bind('<w>', lambda up: change_direction('up'))
window.bind('<s>', lambda down: change_direction('down'))
#Barnabás
#******************************************************************************************************************


snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()