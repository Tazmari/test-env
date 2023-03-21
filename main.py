# next attempt at mean regression app

#Import the libraries
from matplotlib import axis
import yfinance as yf
import streamlit as st
import pandas as pd
import numpy as np
import talib
import matplotlib.pyplot as plt
import datetime
plt.style.use('fivethirtyeight')


#Show the close price data
#Side bar start date input - default tody -200 days
start_date = st.sidebar.date_input("Start Date", datetime.datetime.now() - datetime.timedelta(days=250))
#Side bar end date input
end_date = st.sidebar.date_input('End date', datetime.datetime.now().date())
#Hard coded ticker list to be used later
ticker_list = ("ABDN.L"
,"ADM.L"
,"AML.L"
,"ARB.L"
,"AV.L"
,"BA.L"
,"BLND.L"
,"BOO.L"
,"BNC.L"
,"BP.L"
,"BT-A.L"
,"DARK.L"
,"DLG.L"
,"EZJ.L"
,"EQT.L"
,"FRES.L"
,"GSK.L"
,"IDS.L"
,"INVP.L"
,"IQE.L"
,"JUP.L"
,"LGEN.L"
,"LLOY.L"
,"MCRO.L"
,"MONY.L"
,"N91.L"
,"OCDO.L"
,"ORIT.L"
,"PETS.L"
,"PSON.L"
,"PRU.L"
,"PZC.L"
,"RKT.L"
,"SSE.L"
,"TATE.L"
,"TSCO.L"
,"ULVR.L"
,"UU.L"
,"VDTK.L"
,"VMUK.L"
,"VOD.L"
,"VSVS.L"
,"WIZZ.L")
#Ticker symbol in side bar select box
tickerSymbol = st.sidebar.selectbox('stock ticker', ticker_list)
#yfinance ticker data lookup
tickerData = yf.Ticker(tickerSymbol)
#dataframe from seleted ticker
df = tickerData.history(start=start_date, end=end_date)
#get mean of last 200 days close price. needs to be declared here for use with last_quote
mainmean = np.mean(df['Close'])
# get price
price = round(df['Close'].iloc[-1],2)
price

# price = stock.info['regularMarketPrice']
# tickers = [tickerSymbol]
# for ticker in tickers:
  #  ticker_yahoo = yf.Ticker(ticker)
   # data = ticker_yahoo.history(start=start_date, end=end_date)
    #last_quote = round(data['Close'].iloc[-1],2)
#side bar show current price
st.sidebar.metric("Current Stock Price vs Mean",round(price,2),delta=round(price-mainmean,2), delta_color='normal')

#last close prices from selected ticker for last 200 days
last_close = df['Close']
#last close price from previous day
last_close_price = round(last_close.tail(1),2)
#side bar show last close price
st.sidebar.metric("Last Close Price",last_close_price)


#side bar show mean of last 200 day close price
st.sidebar.metric("Mean",round(mainmean,2))

#if bought now needs to be sold at price
#count of stocks to be bought
stock_count = round(10500/price)
#basic cost of stock
basic_cost = round(stock_count * price)
#total cost assuming 0.005% tax
total_cost = round(basic_cost * 1.005)
#sell price required for 5% profit
sell_price = round(((total_cost * 1.05)/stock_count),2)
#total amount from sall of stock
total_sell_amount = round(total_cost * 1.05)
#profit from sale of stock
profit = round(total_sell_amount - total_cost)

col1, col2 = st.columns([2, 2])
data = np.random.randn(10, 1)

col1.subheader(f"Buy")
col1.text(f"Stock count required")
col1.write(stock_count)
col1.text(f"Stock basic cost")
col1.write(basic_cost)
col1.text(f"Total cost inc .005% tax")
col1.write(total_cost)

col2.subheader("Sell")
col2.text(f"Sell price inc 5% profit")
col2.write(sell_price)
col2.text(f"Total sell")
col2.write(total_sell_amount)
col2.text(f"Total profit")
col2.write(profit)

# SMA
df['SMA'] = talib.SMA(df['Close'], timeperiod = 10)
df['SMA-5%'] = talib.SMA(df['Close']*.95, timeperiod = 10)
df['SMA+5%'] = talib.SMA(df['Close']*1.05, timeperiod = 10)
#string_name = tickerData.info['longName']
#st.header(f"Simple Moving Average vs Adj Close {string_name}")
st.line_chart(df[['Close','SMA','SMA-5%','SMA+5%']])
sma5_list = df['SMA-5%']
sma5_last = round(sma5_list[-1],2)


#testing how to build a loop - this works
#for ticker_list_items in ticker_list:
    #ticker_list_items

# function to loop through the ticker list to see if the current price crosses below the SMA-5%
# put ticker_list in as an argument
#def check_current_price_less_than_sma(tickerData):

#  return tickerData.info['longName']

#for ticker_list_items in ticker_list:
#    print(ticker_list_items)

# python program to check if all
# values in the list are greater
# than val using traversal
 


#def check(sma5_last2, price2):

for ticker_list_items in ticker_list:
        ticker_list_objects = yf.Ticker(ticker_list_items)

current_price_df = ticker_list_objects.history(start=start_date, end=end_date)
price2 = round(current_price_df['Close'].iloc[-1],2)

current_price_df2 = ticker_list_objects.history(start=start_date, end=end_date)
current_price_df2['SMA-5%'] = talib.SMA(current_price_df2['Close']*.95, timeperiod = 10)
sma5_list2 = current_price_df2['SMA-5%']
sma5_last2 = round(sma5_list2[-1],2)

def check(sma5_last2,price2):
    if sma5_last2>= price2:
       return True
    return False
if (sma5_last2,price2):
    print("Yes")
else:
    print("No")