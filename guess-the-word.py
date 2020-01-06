from tkinter import *
from tkinter import messagebox


class Ask:
    def __init__(self, master):
        self.master = master
        self.gui(master)

    @staticmethod
    def gui(master):
        master.geometry('320x200+600+250')
        master.resizable(0, 0)
        master.title('ASK')

        word_entry = StringVar()
        hint_entry = StringVar()

        Label(master, text='', font=('Time New Roman', 16), anchor=W).grid(row=0, column=0)

        Label(master, text='Word:', font=('Time New Roman', 16), anchor=W).grid(row=1, column=0)
        Entry(master, textvariable=word_entry, font=('Time New Roman', 16)).grid(row=1, column=1)

        Label(master, text='', font=('Time New Roman', 16), anchor=W).grid(row=2, column=0)

        Label(master, text='Hint:', font=('Time New Roman', 16), anchor=W).grid(row=3, column=0)
        Entry(master, textvariable=hint_entry, font=('Time New Roman', 16)).grid(row=3, column=1)

        Label(master, text='', font=('Time New Roman', 16), anchor=W).grid(row=4, column=0)

        def check_special(word):
            for i in word:
                # ~`!@#£€$¢¥§%°^&*()-_+={}[]|\/:;"'<>,.?
                if i in "~`!@#£€$¢¥§%°^&*()-_+={}[]|\/:;'<>,.?" or i == '"':
                    return True
                else:
                    return False

        def submit_button_clicked():
            word = word_entry.get().upper()
            hint = hint_entry.get().upper()

            if word == '' and hint == '':
                messagebox.showerror('ERROR', "WORD AND HINT CAN'T BE EMPTY.")
            elif word == '':
                messagebox.showerror('ERROR', "WORD CAN'T BE EMPTY.")
            elif hint == '':
                messagebox.showerror('ERROR', "HINT CAN'T BE EMPTY.")
            elif len(word) < 3:
                messagebox.showerror('ERROR', "WORD SHOULD HAVE MINIMUM 3 CHARACTERS.")
            elif len(word) == 3 and ' ' in word:
                messagebox.showerror('ERROR', "3 CHARACTER WORD CAN'T HAVE SPACE.")
            elif check_special(word):
                messagebox.showerror('ERROR', "WORD CAN'T HAVE SPECIAL CHARACTER.")
            else:
                messagebox.showinfo('SUCCESSFUL', 'WORD = {}\nHint = {}'.format(word, hint))
                master.destroy()

                play_game(word, hint)

            return True

        Button(master, text='Submit', command=submit_button_clicked, padx=50, pady=10).grid(row=5, column=0, columnspan=2)


def play_game(word, hint):
    letters = ()
    for i in word.split():
        letters = letters + (len(i),)

    print('HINT: {}'.format(hint))
    print('{} WORDS {}\n'.format(len(word.split()), letters))

    encrypted_word = []
    for i in word:
        if i == ' ':
            encrypted_word.append(' ')
        else:
            encrypted_word.append('*')
    print(' '.join(encrypted_word) + '\n')

    tries = 7
    used_alphabet = []

    while '*' in encrypted_word and tries:
        print('{} TRIES LEFT'.format(tries))
        alphabet = input('ENTER ALPHABET: ').upper()

        if alphabet in used_alphabet:
            print("SAME ALPHABET CAN'T BE REPEATED")
        elif alphabet in word:
            print('CORRECT')
            for i in range(len(word)):
                if word[i] == alphabet:
                    encrypted_word[i] = alphabet
        else:
            print('INCORRECT')
            tries = tries - 1
        used_alphabet.append(alphabet)
        print(' '.join(encrypted_word))
        print('\n')

    if tries == 0:
        print('SORRY! BETTER LUCK NEXT TIME')
    else:
        print('CONGRATULATION! YOU WON')


def main():
    master = Tk()
    Ask(master)
    master.mainloop()


if __name__ == '__main__':
    main()

    root = Tk()
    root.withdraw()
    result = messagebox.showinfo('', 'THANKS FOR PLAYING')
    root.destroy()
