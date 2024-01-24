from tkinter import *
from tkinter import simpledialog, messagebox
import random
#0b99e0  

#Általános paraméterek
GAME_WIDTH = 900
GAME_HEIGHT = 900 
SPEED = 200 
SPACE_SIZE = 50 
BODY_PARTS = 4 
LABEL_BG_COLOR = "#83eb13" 
FOOD_COLOR = "#FF0000" 
BACKGROUND_COLOR = "#83eb13" 


class Food: #Étel random elhelyezése az x és y koordinátán

    def __init__(self):

        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE 
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y] 
        self.cherry_image = PhotoImage(file="cseresznye.png")  # Adj meg a kép fájl nevét

        canvas.create_image(x + SPACE_SIZE / 2, y + SPACE_SIZE / 2, image=self.cherry_image, tag="food") 


random_color = "#{:06x}".format(random.randint(0,0xFFFFFF))

class Snake: #Kígyó testének létrehozása

            
    def __init__(self):
        self.body_size = BODY_PARTS #kezdeti testrész érték
        self.coordinates = [] 
        self.squares = [] #kígyó négyzetekre történő megjelenítés
    
    
        for i in range(0, BODY_PARTS): 
            self.coordinates.append([0, 0]) #Beállítjuk a testrészek koordinátáit

        for x, y in self.coordinates: #végigmegy a self.coordinates listán
            random_color = "#{:06x}".format(random.randint(0,0xFFFFFF)) #hexadecimális, random kígyó szín
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=random_color, tag="kigyo") 
            self.squares.append(square) #lista, ami a kígyó négyzeteit tartalmazza
            
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
        label.config(text="PONTSZÁM:{}".format(score))
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
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)



def change_direction(new_direction):
    global direction

    #Irányváltások****************************************
    # Irányváltás balra
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    # Irányváltás jobbra
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    # Irányváltás felfelé
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    # Irányváltás lefelé
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction



def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False
#Roland
#******************************************************************************************************************


#A játék vége
def restart_game():
    global snake, food, score, direction

    # Töröljük a korábbi kígyót, ételt és eredményt
    canvas.delete(ALL)
    score = 0
    direction = 'right'
    label.config(text="Score:{}".format(score))

    # Új kígyó és étel létrehozása
    create_grid()
    snake = Snake()
    food = Food()

    # Újraindítjuk a játékot
    
    next_turn(snake, food)
    

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")

    # Hozzáadjuk a "Press R to restart" szöveget
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2 + 100,
                       font=('consolas',20), text="Press R to restart", fill="white", tag="restart_prompt")

    # Meghívjuk a restart_game függvényt a 'r' gomb lenyomásakor
    window.bind('r', lambda event: restart_game())

# ...

# Hozzáadjuk a billentyűzet eseményfigyelőt a 'r' gombhoz
    window.bind('r', lambda event: restart_game())


window = Tk()
window.title("Színváltó Sárkány")
window.resizable(False, False)

score = 0
direction = 'right'


# Pontszám kijelző létrehozása és beállítása
label = Label(window, text="PONTSZÁM:{}".format(score), font=('consolas', 40))
label.config(bg= "green")
label.pack(fill = BOTH, expand=YES)

def create_grid():
    light_color = "#a9e9a1"  
    dark_color = "#6fa36f"   

    for i in range(0, GAME_WIDTH, SPACE_SIZE):
        for j in range(0, GAME_HEIGHT, SPACE_SIZE):
            # Minden második sorban és oszlopban másik szín legyen
            if (i // SPACE_SIZE) % 2 == (j // SPACE_SIZE) % 2:
                canvas.create_rectangle(i, j, i + SPACE_SIZE, j + SPACE_SIZE, fill=light_color)
            else:
                canvas.create_rectangle(i, j, i + SPACE_SIZE, j + SPACE_SIZE, fill=dark_color)


canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
create_grid()

window.update()
#Barnabás, Roland
#******************************************************************************************************************

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