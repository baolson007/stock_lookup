import tkinter as tk
from stock import get_price

def on_click(event=None):
   ticker = ent_ticker.get()
   price = get_price( ticker )
   if price != 'NA':
      lbl_result['text'] = "$" + str( price )
   else:
      lbl_result['text'] = ticker + " is an invalid ticker, try again"
   
root = tk.Tk()
root.title("Stock Price Finder")
root.geometry('400x300')
root.bind('<Return>', on_click)

lbl = tk.Label( root, text='Please enter a stock ticker symbol' )

ent_ticker = tk.Entry(root, width=15)
#txt.grid( row = 0, column = 1)
btn_submit = tk.Button( root, text="look up price", width=10, command=on_click )

lbl_result = tk.Label( text="result" )
btn_exit = tk.Button( root, text="Exit Program", command=root.destroy )

lbl.pack()
ent_ticker.pack()
btn_submit.pack()
lbl_result.pack()
btn_exit.pack()




#quote = stock.get_price(ticker)

#quote.pack()

root.mainloop()