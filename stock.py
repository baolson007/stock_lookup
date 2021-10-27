# Library to help simplify functions utilizing yahoo finance data
import yahoo_fin.stock_info as stock_info
import yahoo_fin as yf
import pandas as pd

dates = []
prices = []

# get all available price data, load dates and prices into 
# class variables for future use.
def get_historic_price_data( ticker ):
	ticker_data = stock_info.get_data( ticker )# ... start_date = '09-24-2021', end_date = ''...)

	ticker_data.index = pd.to_datetime( ticker_data.index )

	for date in ticker_data.index:
		date = date.to_pydatetime().strftime( '%m-%d-%Y' )
		dates.append( date )

	for price in ticker_data['open']:
		prices.append( round( price, 2 ) )
	
	name = stock_info.get_quote_data( ticker ).get( 'shortName' )
	return ( dates, prices )

# retrieve a company's name given its stock symbol.
def get_name( ticker ):
	name = stock_info.get_quote_data( ticker ).get( 'shortName' )
	return name

# retrieve current price for the given stock symbol.
# returns 'NA' if symbol does not able to be retreived 
# by the yahoo_fin API
def get_price( ticker ):
	try:
		price = round( stock_info.get_live_price( ticker ), 2 )
		return price
	except:
		return 'NA'
