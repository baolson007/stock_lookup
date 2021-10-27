# Simple GUI using tkinter to retreive and display a given company's
# stock price when provided with the company's stock ticker. 

import tkinter as tk
from stock import get_name, get_price

# Populates the result field of the window with the result
# of the get name/price calls for the given stock
def on_click(event=None):
   ticker = ent_ticker.get()
   price = get_price( ticker )
   name = get_name( ticker )

   if price != 'NA':
      lbl_result['text'] = name + ": $" + str( price )
   else:
      lbl_result['text'] = ticker + " is an invalid ticker, try again"
   
# tkinter setup
root = tk.Tk()
root.title("Stock Price Finder")
root.geometry('400x300')
root.bind('<Return>', on_click)

# widgets
lbl_welcome = tk.Label( root, text='Welcome!' )
lbl_entry = tk.Label( root, text='Enter stock symbol (ex:GOOG): ' )
ent_ticker = tk.Entry(root, width=15)
btn_submit = tk.Button( root, text="look up price", width=10, command=on_click )
lbl_result = tk.Label( text="result" )
btn_exit = tk.Button( root, text="Exit Program", command=root.destroy )

# formatting
lbl_welcome.grid( row=1, column=1, pady=10 )
lbl_entry.grid( row=2, column=1 )
ent_ticker.grid( row=2, column=2, padx=5, sticky='N' )
btn_submit.grid( row= 3, column=1, pady=10 )
lbl_result.grid( row= 4, column=1, pady=10 )
btn_exit.grid( row= 7, column=1, padx=5, pady=20, sticky='N' )

root.mainloop()