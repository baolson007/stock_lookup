from tkinter import *
import yahoo_fin.stock_info as stock_info
import yahoo_fin as yf
import pandas as pd

dates = []
prices = []

def get_historic_price_data( ticker ):
	ticker_data = stock_info.get_data( ticker )# ... start_date = '09-24-2021', end_date = ''...)

	ticker_data.index = pd.to_datetime( ticker_data.index )

	for date in ticker_data.index:
		date = date.to_pydatetime().strftime( '%m-%d-%Y' )
		dates.append( date )

	for price in ticker_data['open']:
		prices.append( round( price, 2 ) )
	
	name = stock_info.get_quote_data( ticker ).get( 'shortName' )


	print( "Price history for: " + name + " (" + ticker + ") loaded" )
	return ( dates, prices )

def get_price( ticker ):
	try:
		price = round( stock_info.get_live_price( ticker ), 2 )
		return price
	except:
		return 'NA'

#try:
	#ticker = input( "Please enter a valid ticker symbol: " ).upper()
	#get_historic_price_data( ticker )
	#print( "Current price for " + ticker + ": $" + str( get_price( ticker ) ) )
#except:
	#print( "Error processing request for stock ticker \'" + ticker + " \' try again" )


