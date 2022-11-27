import streamlit as st
import plotly_express as px
import numpy as np
import pandas as pd
import random

st.title("Welcome gambler")

font_css = """
<style>
div[class*="stNumberInput"] label {
font-size: 18px;
}
</style>"""

st.write(font_css, unsafe_allow_html=True)
initial_capital = st.number_input("Enter the inital capital: ", 1000)
winning_prob = st.number_input('Enter the winning probability: ', 0.6)
betting_amount = st.number_input('Enter the betting amount: ', 200)
reward_ratio = st.number_input('Enter the reward ratio: ', 0.5)
avg_loss = st.number_input('Enter the average loss multiple: ', 0.2)
no_of_trades = int(st.number_input('Enter the numger of trades: '))

trade = random.choices([True, False], weights=[winning_prob, 1-winning_prob], k=1)

current_capital = initial_capital
capital_array = []
mathametical_current_capital_array=[]

for i in range(no_of_trades):
    trade = random.choices([True, False], weights=[winning_prob, 1-winning_prob], k=1)
 
    if trade[0] == True:
        current_capital = current_capital + (betting_amount * reward_ratio)
    else:
 	    current_capital = current_capital - (betting_amount * avg_loss)
    capital_array.append(current_capital)
    mathametical_current_capital = initial_capital + (winning_prob*betting_amount*reward_ratio*i) - ((1-winning_prob)*betting_amount*avg_loss*i)
    mathametical_current_capital_array.append(mathametical_current_capital)


mathametical_current_capital = initial_capital + (winning_prob*betting_amount*(reward_ratio)*no_of_trades) - ((1-winning_prob)*betting_amount*(avg_loss)*no_of_trades)

plot_array = [capital_array, mathametical_current_capital_array]

st.write('The current capital is', current_capital)
st.write('The mathametically calculated current capital is', mathametical_current_capital)
fig = px.line(y=plot_array)
column_names = {'wide_variable_0':'Simulation', 'wide_variable_1':'Mathametical'}
fig.for_each_trace(lambda t: t.update(name = column_names[t.name],
                                      legendgroup = column_names[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, column_names[t.name])
                                     )
                  )
fig.update_layout(
autosize=True, legend_title_text='Capital')
st.plotly_chart(fig, use_column_width=False, layout='wide')

show_table = st.checkbox('Check if you wanna see the value table: ')
if show_table:
    st.write(pd.DataFrame({'Simulated capital': capital_array, 'Mathametical capital': mathametical_current_capital_array}))









