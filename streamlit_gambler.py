import streamlit as st
import plotly_express as px
import numpy as np
import pandas as pd
import random

st.title("Welcome gambler")

initial_capital = st.number_input("Enter the inital capital: ")
winning_prob = st.number_input('Enter the winning probability: ')
betting_amount = st.number_input('Enter the betting amount: ')
reward_ratio = st.number_input('Enter the reward ratio: ')
avg_loss = st.number_input('Enter the average loss multiple: ')
no_of_trades = int(st.number_input('Enter the numger of trades: '))

trade = random.choices([True, False], weights=[winning_prob, 1-winning_prob], k=1)

current_capital = initial_capital
capital_array = []

for i in range(no_of_trades):
    trade = random.choices([True, False], weights=[winning_prob, 1-winning_prob], k=1)
 
    if trade[0] == True:
        current_capital = current_capital + (betting_amount * reward_ratio)
    else:
 	    current_capital = current_capital - (betting_amount * avg_loss)
    capital_array.append(current_capital)
    print(current_capital)


mathametical_current_capital = initial_capital + (winning_prob*betting_amount*(reward_ratio)*no_of_trades) - ((1-winning_prob)*betting_amount*(avg_loss)*no_of_trades)

st.write('The current capital is', current_capital)
st.write('The mathametically calculated current capital is', mathametical_current_capital)
st.write(capital_array)

fig = px.line(y=capital_array)
st.plotly_chart(fig, use_container_width=True)










