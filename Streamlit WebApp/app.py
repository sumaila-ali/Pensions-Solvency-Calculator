# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:28:21 2020
@author: Sam
"""

import math as mt
import streamlit as st

# Title and info
st.set_page_config(page_title="Solvency Calculator")
st.title("Solvency Calculator")
st.info("This tool forecasts financial solvency by modeling the growth of the population of pension contributors and recipients using the logistic function.")

st.title("Tool Assumptions")
st.info("1. Pension recipients first get a lump sum followed by monthly annuities and a final lump sum upon the death of the contributor." \
"2. ")
# Sidebar inputs
st.sidebar.header('User Input Features')

t = st.sidebar.slider('T (Monthly)', 1, 100,36)

# Contributors and Recipients Inputs
initialContributorPopulation = int(st.text_input("Initial Population of Contributors", "100,000").replace(",", ""))

initialLumpSumRecipients = int(st.text_input("Initial Lump Sum Recipient Population (First time retirees)", "1,000").replace(",", ""))
finalLumpSumRecipients = float(st.text_input("Final Lump Sum Recipient Population (Dead Pensioners)", "100").replace(",", ""))
initialAnnuityRecipients = float(st.text_input("Annuity Pension Recipient Population", "10,000").replace(",", ""))

averageContribution = st.sidebar.slider("Average Contribution per Person", 100, 100000, 500)
averageFirstLumpSum = st.sidebar.slider("Average Lump Sum (First time)", 12000, 200000, 15000)
averageLastLumpSum = st.sidebar.slider("Average Lump Sum (Last time)", 3000, 100000, 30000)
averageAnnuityPaid = st.sidebar.slider("Average Pension per Person", 500, 100000,2000)
# invest = st.sidebar.slider("Estimated Investment Income", 1_000_000.0, 200_000_000.0)
expenditure = st.sidebar.slider("Estimated Monthly Expenditure", 500000.0, 200_000_000.0)

# Default advanced parameters
epsilon1 = 0.00002
mu1 = 0.00005
lam1 = 0.0003


epsilon2 = 0.00005
mu2 = 0.00006
lam2 = 0.0004



# Advanced Options
with st.expander("⚙️ Advanced Parameters"):
    '''

Epsilon (ε): External or Constant Inflow
Represents: A fixed or external input into the system that is not dependent on current population size.

λ1 is a constant that models the rate at which people join the scheme
μ1 is a constnat that models the rate at which peple die from the scheme. 

The difference (λ1 - μ1) governs the rate of exponential growth or decay e^((λ1 - μ1)t):
If (λ1 - μ1) is positive, the term represents exponential growth. 
If it is negative, it represents exponential decay. 
If (λ1 - μ1) is zero, the term is simply 1, resulting in a constant term.


'''
    epsilon1 = float(st.text_input("Epsilon 1", value=str(epsilon1)))
    epsilon2 = float(st.text_input("Epsilon 2", value=str(epsilon2)))
    mu1 = float(st.text_input("Mu 1", value=str(mu1)))
    mu2 = float(st.text_input("Mu 2", value=str(mu2)))
    lam1 = float(st.text_input("Lambda 1", value=str(lam1)))
    lam2 = float(st.text_input("Lambda 2", value=str(lam2)))
    

# --- Core Calculations ---

# Contributors
populationModelwithExternalInflux = (epsilon1 / (lam1 - mu1)) * mt.exp((lam1 - mu1) * t)
populationModelonInternalInflux = initialContributorPopulation * mt.exp((lam1 - mu1) * t)
totalPopulation = int(populationModelwithExternalInflux + populationModelonInternalInflux)
totalContributions = totalPopulation * averageContribution

# Lump Sum Recipients
initialLumpSumPopulation = initialLumpSumRecipients * (1 - mt.exp(-mu2 * t))
finalLumpSumPopulation = finalLumpSumRecipients * (1 - mt.exp(-epsilon2 * t))
totalLumpSumPayment = initialLumpSumPopulation * averageFirstLumpSum + finalLumpSumPopulation * averageLastLumpSum

# Pension Recipients
annuityRecipientPopulationWithExternalinflux = (epsilon2 / (lam2 - mu2)) * mt.exp((lam2 - mu2) * t)
annuityRecipientPopulationWithInternalInflux = initialAnnuityRecipients * mt.exp((lam2 - mu2) * t)
annuityPopulation = int(annuityRecipientPopulationWithExternalinflux + annuityRecipientPopulationWithInternalInflux)
totalPensionsPaid = annuityPopulation * averageAnnuityPaid
totalExpenditure = expenditure * t



# Surplus Calculation
if st.button("💰 Compute Monthly Surplus"):
    surplus = totalContributions - totalLumpSumPayment - totalPensionsPaid - totalExpenditure
    st.subheader("📊 Surplus Projection")
    st.metric(label="Estimated Surplus", value=f"{surplus:,.2f}")
    
    
    
    # TODO: Plot a chart that represents the movement of funds for the scheme over time. 
    #import numpy as np
    #import plotly.graph_objects as go

    # def cumulative_trapezoid(y, x):
    #     dx = np.diff(x)
    #     avg_y = (y[:-1] + y[1:]) / 2
    #     integral = np.zeros_like(y)
    #     integral[1:] = np.cumsum(avg_y * dx)
    #     return integral

    # t_vals = np.linspace(0, t, 300)

    # # Contributors
    # term1_array = (epsilon1 / (lam1 - mu1)) * np.exp((lam1 - mu1) * t_vals)
    # term2_array = initialContributorPopulation * np.exp((lam1 - mu1) * t_vals)
    # entire_pop_cont = cumulative_trapezoid(term1_array + term2_array, t_vals)
    # total_cont_array = entire_pop_cont * averageContribution

    # # Lump Sum Recipients
    # lump_pop1_array = initialLumpSumPopulation * (1 - np.exp(-mu2 * t_vals))
    # lump_pop2_array = finalLumpSumPopulation * (1 - np.exp(-epsilon2 * t_vals))
    # total_lump_array = lump_pop1_array * averageFirstLumpSum + lump_pop2_array * averageLastLumpSum

    # # Pension Recipients
    # term3_array = (epsilon2 / (lam2 - mu2)) * np.exp((lam2 - mu2) * t_vals)
    # term4_array = initialAnnuityRecipients * np.exp((lam2 - mu2) * t_vals)
    # pen_pop_array = cumulative_trapezoid(term3_array + term4_array, t_vals)
    # total_pen_array = pen_pop_array * averageAnnuityPaid

    # total_pensions_payment = total_pen_array + total_lump_array + totalExpenditure

    # fig = go.Figure()
    # fig.add_trace(go.Scatter(x=t_vals, y=total_cont_array, mode='lines', name='Total Contributions'))
    # # fig.add_trace(go.Scatter(x=t_vals, y=total_lump_array, mode='lines', name='Total Lump Sum Payments'))
    # fig.add_trace(go.Scatter(x=t_vals, y=total_pen_array, mode='lines', name='Total Annuity Payments'))
    # fig.add_trace(go.Scatter(x=t_vals, y=total_pensions_payment, mode='lines', name='Total Pensions Payments'))
    

    # fig.update_layout(
    #     title='Pension System Cash Flows Over Time',
    #     xaxis_title='Time (months)',
    #     yaxis_title='Amount',
    #     template='plotly_white',
    #     legend_title='Flow Type',
    #     width=800,
    #     height=500
    # )

    # st.plotly_chart(fig)

    