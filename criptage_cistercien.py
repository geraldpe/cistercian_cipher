#coding:utf-8


import tkinter as tk
from base_elements_cubic_matrix import BaseElements


BACKGROUND_COLOR = "grey"

def get_info_in_tk_entry(entry: tk.Entry) -> int:
    """
    récupération de la chaine de caractères dans une Entry tkinter
    returns None if the text is not a integer under 9999
    """
    text = entry.get()
    try:
        result = int(text)
        if 1 <= result <= 9999:
            return result
        else:
            return None
    except:
        return None

def decompose_number_in_tenth_base(number: int) -> list:
    """
    décompose un nombre de quatre digits maximum (entre 1 et 9999) en une liste de 4 éléments représentant
    les unités, les dizaines, les centaines et enfin les miliers
    """
    result = [0]*4
    index = 3
    while number != 0 and index > -1:
        result[index] = number % 10
        number //= 10
        index -= 1
    
    return result

def generate_line_list_from_decomposed_number(decomposed_number_list: list) -> list:
    result = []
    for index in range(len(decomposed_number_list)):
        if decomposed_number_list[index] != 0:
            new_element = BaseElements[index][decomposed_number_list[index]-1]
            try:
                test = new_element[0][0]
                result.append(new_element)
            except:
                result.append([new_element])
        else:
            result.append(())
    
    return result

def button_function(entry: tk.Entry, canvas: tk.Canvas) -> None:
    number = get_info_in_tk_entry(entry=entry)
    if number is None:
        print("vous avez entré une valeur incorrecte")
        return

    canvas.delete("line")
    decomposed_number_list = decompose_number_in_tenth_base(number=number)
    to_draw_line_list = generate_line_list_from_decomposed_number(decomposed_number_list)

    for element in to_draw_line_list:
        for line in element:
            x0 = line[0]
            y0 = line[1]
            x1 = line[2]
            y1 = line[3]
            canvas.create_line(x0, y0, x1, y1, tag="line")
    canvas.pack()

def app_initialisation() -> tk.Tk:
    root = tk.Tk()
    root.geometry("800x600")
    root.config(bg=BACKGROUND_COLOR)
    root.title("application de criptage cistercien")

    #creation du canvas d'affichage du nombre cripté
    display_canvas = tk.Canvas(root)
    display_canvas.config(width=400, height=400)
    display_canvas.create_line(200, 50, 200, 350)

    display_canvas.pack(side="left", expand=True)

    #creation et configuration de la frame de l'Entry
    entry_frame = tk.Frame(root, bg=BACKGROUND_COLOR)

    #creation de l'Entry du nombre à crypter
    entry_label = tk.Label(entry_frame, text="entrez votre nombre ici :", bg=BACKGROUND_COLOR, fg="white")
    entry_label.pack()
    number_entry = tk.Entry(entry_frame)
    number_entry.pack(side=tk.TOP, expand=True)
    
    #creation du bouton pour lancer le cryptage
    cipher_launch_button = tk.Button(
                                entry_frame, 
                                text="lancer le criptage", 
                                command=lambda: button_function(entry=number_entry, canvas=display_canvas)
                        )
    cipher_launch_button.pack(side=tk.TOP, expand=True, pady=20)

    entry_frame.pack(side="left", expand=True)

    return root

def main():
    #création et configuration de la fenêtre principale
    root = app_initialisation()

    #lancement de la fenêtre
    root.mainloop()

if __name__ == "__main__":
    main()