# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:28:21 2020
@author: Sam
"""

import math as mt
import streamlit as st

# Title and info
st.title("Solvency Calculator")
st.info("This tool projects monthly financial solvency using contributor and recipient data.")

# Sidebar inputs
st.sidebar.header('User Input Features')

t = st.sidebar.slider('T (days)', 10, 90)

# Contributors and Recipients Inputs
init_pop_cont = int(st.text_input("Initial Population of Contributors", "100000"))

init_lump_pop1 = float(st.text_input("Initial Lump Sum Recipient Population (First time)", "100000"))
init_lump_pop2 = float(st.text_input("Initial Lump Sum Recipient Population (Last time)", "100000"))
init_pen_pop = float(st.text_input("Initial Pension Recipient Population", "100000"))

Ave_cont = st.sidebar.slider("Average Contribution per Person", 100.0, 200.0)
Ave_lump1 = st.sidebar.slider("Average Lump Sum (First time)", 12000.0, 20000.0)
Ave_lump2 = st.sidebar.slider("Average Lump Sum (Last time)", 3000.0, 10000.0)
Ave_pen = st.sidebar.slider("Average Pension per Person", 500.0, 1000.0)
invest = st.sidebar.slider("Estimated Investment Income", 1_000_000.0, 200_000_000.0)
expend = st.sidebar.slider("Estimated Monthly Expenditure", 1_000_000.0, 200_000_000.0)

# Default advanced parameters
epsilon1 = 0.00002
epsilon2 = 0.00005
mu1 = 0.00005
mu2 = 0.00006
lam1 = 0.0003
lam2 = 0.0004

# Advanced Options
with st.expander("⚙️ Advanced Parameters"):
    epsilon1 = float(st.text_input("Epsilon 1", value=str(epsilon1)))
    epsilon2 = float(st.text_input("Epsilon 2", value=str(epsilon2)))
    mu1 = float(st.text_input("Mu 1", value=str(mu1)))
    mu2 = float(st.text_input("Mu 2", value=str(mu2)))
    lam1 = float(st.text_input("Lambda 1", value=str(lam1)))
    lam2 = float(st.text_input("Lambda 2", value=str(lam2)))

# --- Core Calculations ---

# Contributors
term1 = (epsilon1 / (lam1 - mu1)) * mt.exp((lam1 - mu1) * t)
term2 = init_pop_cont * mt.exp((lam1 - mu1) * t)
entire_pop_cont = int(term1 + term2)
total_cont = entire_pop_cont * Ave_cont

# Lump Sum Recipients
lump_pop1 = init_lump_pop1 * (1 - mt.exp(-mu2 * t))
lump_pop2 = init_lump_pop2 * (1 - mt.exp(-epsilon2 * t))
total_lump = lump_pop1 * Ave_lump1 + lump_pop2 * Ave_lump2

# Pension Recipients
term3 = (epsilon2 / (lam2 - mu2)) * mt.exp((lam2 - mu2) * t)
term4 = init_pen_pop * mt.exp((lam2 - mu2) * t)
pen_pop = int(term3 + term4)
total_pen = pen_pop * Ave_pen

# Surplus Calculation
if st.button("💰 Compute Monthly Surplus"):
    surplus = total_cont - total_lump - total_pen + invest - expend
    st.subheader("📊 Surplus Projection")
    st.metric(label="Estimated Surplus", value=f"{surplus:,.2f}")