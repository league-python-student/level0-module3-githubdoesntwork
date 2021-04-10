from tkinter import simpledialog, Tk
from playsound import playsound

can_play_sounds = False


def play_mister_zee():
    if can_play_sounds:
        playsound('shiny-objects.wav')
    else:
        print("Mister Zee requires shiny objects")


def many_shiny_objects():
    # TODO 1) Call the method above to play Mister Zee
    play_mister_zee()
    # TODO 2) Ask the user how many shiny objects they want
    val = simpledialog.askinteger("zee","number shiny")
    # TODO 3) Play the sound that many times
    can_play_sounds=True
    for i in range(val-1):
        play_mister_zee()
    pass


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    many_shiny_objects()
