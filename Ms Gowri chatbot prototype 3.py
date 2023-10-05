from tkinter import * 


root = Tk()
root.title("Ms Gowri")
root.geometry("600x400")
root.configure(background="cyan")

enter_word = Entry(root)
enter_word.place(relx = 0.5, rely= 0.4, anchor=CENTER)
label_instruction = Label(root, text="type in hi or hey")

label = Label(root, text="Ms Gowri: ", fg="black")

def Enter():
    input_up = enter_word.get()
    input_word = input_up.lower()
    
    
    if  "hi" in input_word:
        label["text"] = "Ms Gowri: Hi there fellow student!"
        
    elif "hey" in input_word:
        label["text"] = "Ms Gowri: Hey there fellow student!"
    
    elif "hello" in input_word:
        label["text"] = "Ms Gowri: Hello there fellow student!"
        
    elif "hola" in input_word:
        label["text"] = "Ms Gowri: Hola!"
        
    elif "how old are you" in input_word:
        label["text"] = "Ms Gowri: That's a secret!"
        
    elif "I need some advice" in input_word:
        label["text"] = "Ms Gowri: If I were you I would ask a friend or go to Google"
        
    elif "i need some advice" in input_word:
        label["text"] = "Ms Gowri: If I were you I would ask a friend or go to Google"
        
    elif "what's your job" in input_word:
        label["text"] = "Ms Gowri: Im a teacher"
        
    elif "I didn't do my homework" in input_word:
        label["text"] = "Ms Gowri: You have until tomorrow and tomorrow only!"
        
    elif "i didn't do my homework" in input_word:
        label["text"] = "Ms Gowri: You have until tomorrow and tomorrow only!"
        
    elif input_word == "I need help":
        label["text"] = "Ms Gowri: Go to therapy"
        
    elif input_word == "i need help":
         label["text"] = "Ms Gowri: Go to therapy"

    elif "how are you" in input_word:
        label["text"] = "Ms Gowri: Im doing good!"
        
    elif "what is your name" in input_word:
        label["text"] = "Ms Gowri: It's pretty obvious....."
        
    elif "code something" in input_word:
        label["text"] = "Ms Gowri: I am a math techer not a coder"
        
    elif "I hate math" in input_word:
        label["text"] = "ALERT: We have sent a hitman to go to your house in the next 30 minutes because you hate math. Have a good life."
    
    elif "i hate math" in input_word:
        label["text"] = "ALERT: We have sent a hitman to go to your house in the next 30 minutes because you hate math. Have a good life."
    
    elif "I hate maths" in input_word:
        label["text"] = "ALERT: We have sent a hitman to go to your house in the next 30 minutes because you hate math. Have a good life."
        
    elif "i hate maths" in input_word:
        label["text"] = "ALERT: We have sent a hitman to go to your house in the next 30 minutes because you hate math. Have a good life."
        
    else:
        label["text"] = "Ms Gowri: I'm sorry, but my programmer has not programmed me to answer to this."
        
btn = Button(root, text="Enter", command=Enter, bg="red")
btn.place(relx = 0.5, rely = 0.5, anchor=CENTER)
label.place(relx = 0.5, rely = 0.6, anchor=CENTER)

root.mainloop()