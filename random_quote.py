import requests
import tkinter as tk
from googletrans import Translator, constants


window=tk.Tk()
window.geometry("1080x460")
window.title("Quote Generator")
window.grid_columnconfigure(0, weight=1)
window.resizable(False, False)
window.configure(bg="grey")

api="http://api.quotable.io/random"

translator = Translator()

def ran_quote():
	random=requests.get(api).json()
	quote=random["content"]+"- "+random["author"]
	quote_label.config(text=quote)

def trans_quote():
	translated_quote=translator.translate(quote_label.cget("text"), dest="sr")
	quote_label.config(text=translated_quote)

quote_label=tk.Label(window, text="Here's the quote", height=6, pady=10, wraplength=800, font=("Arial", 14))
quote_label.grid(row=0, column=0, stick="WE", padx=20, pady=10)



gen_btn=tk.Button(text="Generate", command=ran_quote)
gen_btn.grid(row=1, column=0, stick="WE", padx=20, pady=10)

toggle_btn=tk.Button(text="Toggle Language", command=trans_quote)
toggle_btn.grid(row=1, column=1, stick="WE", padx=20, pady=10)



if __name__ == '__main__':
	window.mainloop()