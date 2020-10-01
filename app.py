# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:28:21 2020

@author: Sam
"""


#%% Libraries
import math as mt
import streamlit as st


#%%

st.title("Solvency Calculator")

st.info("Any information for the user")


st.sidebar.header('User Input Features')

t = st.sidebar.slider('T(days)', 10, 90)

# Accepting and testing value of epsilon 1
epsilon1_var = st.text_input("Epsilon 1", "0.00002")
try:
    test = isinstance(float(epsilon1_var), (int, float))
    if test != True:
        st.error("Enter a valid Epsilon Value")
    else:
        epsilon1 = float(epsilon1_var)
except Exception:
    epsilon1 = 0.00001687
    st.error("Enter a valid Epsilon Value. In the meantime, Epsilon_1 will be set to a default value of 0.00001687")

epsilon2_var = st.text_input("Epsilon 2", "0.00005")
try:
    test = isinstance(float(epsilon2_var), (int, float))
    if test != True:
        st.error("Enter a valid Epsilon Value")
    else:
        epsilon2 = float(epsilon2_var)
except Exception:
    epsilon2 = 0.000051698
    st.error("Enter a valid Epsilon Value. In the meantime, Epsilon_2 will be set to a default value of 0.000051698")
   

init_pop_cont_var = st.text_input("Initial Population of Contributors", "100000")
try:
    test = isinstance(int(init_pop_cont_var), int)
    if test != True:
        st.error("Enter a Valid Population Value")
    else:
        init_pop_cont = int(init_pop_cont_var)
except Exception:
    init_pop_cont = 100000
    st.error("Enter a valid number. In the meantime, Initial Population of Contributors will be set to a default value of 100000")
    
    
mu1_var = st.text_input("Mu 1", "0.00005")
try:
    test = isinstance(float(mu1_var), (int, float))
    if test != True:
        st.error("Enter a valid Mu Value")
    else:
        mu1 = float(mu1_var)
except Exception:
    mu1 = 0.000047247
    st.error("Enter a valid Mu Value. In the meantime, Mu 1 will be set to a default value of 0.000047")
 

mu2_var = st.text_input("Mu 2", "0.00006")
try:
    test = isinstance(float(mu2_var), (int, float))
    if test != True:
        st.error("Enter a valid Mu Value")
    else:
        mu2 = float(mu2_var)
except Exception:
    mu2 = 0.00006
    st.error("Enter a valid Mu Value. In the meantime, Mu 2 will be set to a default value of 0.000051698")
 
    

lam1_var = st.text_input("Lambda 1", "0.0003")
#TODO write a code for zero division
try:
    test = isinstance(float(lam1_var), (int, float))
    if test != True:
        st.error("Enter a valid Lambda Value")
    else:
        lam1 = float(lam1_var)
except Exception:
    epsilon2 = 0.0003
    st.error("Enter a valid Lambda Value. In the meantime, Lamdba 1 will be set to a default value of  0.0003")
   
    
lam2_var = st.text_input("Lambda 2", "0.0004")
#TODO write a code for zero division
try:
    test = isinstance(float(epsilon2_var), (int, float))
    if test != True:
        st.error("Enter a valid Lambda Value")
    else:
        lam2 = float(lam2_var)
except Exception:
    lam2 = 0.0004
    st.error("Enter a valid Lambda Value. In the meantime, Lamdba 1 will be set to a default value of  0.0004")
 

init_lump_pop_var1 = st.text_input("Initial Lump Sum Reciepient Population.  (First time Receipients) ", "100000")
#TODO Use is instance to do the number checks
try:
    test = isinstance(float(init_lump_pop_var1), (int, float))
    if test != True:
        st.error("Enter a valid Population Value")
    else:
        init_lump_pop1 = float(init_lump_pop_var1)
except Exception:
    init_lump_pop1 = 100000
    st.error("Enter a valid Population Value. In the meantime, First time Lump Sum Receipient Population will be set to a default value of 100000")


init_lump_pop_var2 = st.text_input("Initial Lump Sum Reciepient Population.  (Last time Receipients) ", "100000")
try:
    test = isinstance(float(init_lump_pop_var2), (int, float))
    if test != True:
        st.error("Enter a valid Population Value")
    else:
        init_lump_pop2 = float(init_lump_pop_var2)
except Exception:
    init_lump_pop2 = 100000
    st.error("Enter a valid Population Value. In the meantime, Last time Lump Sum Receipient Population will be set to a default value of 100000")


init_pen_pop_var = st.text_input("Initial Pension Receipient Population", "100000")

try:
    test = isinstance(float(init_pen_pop_var), (int, float))
    if test != True:
        st.error("Enter a valid Population Value")
    else:
        init_pen_pop = float(init_pen_pop_var)
except Exception:
    init_pen_pop = 100000
    st.error("Enter a valid Population Value. In the meantime, Initial Pension Reciepients will be set to a default value of 100000")

      
Ave_cont = st.sidebar.slider("Average Contribution per Person", 100.0, 200.0)


Ave_lump1 = st.sidebar.slider("Average Lump Sum Recieved per Person.  (First time Receipients)", 12000.0,20000.0 )


Ave_lump2 = st.sidebar.slider("Average Lump Sum Recieved per Person.  (Last time Reciepients)", 3000.0, 10000.0)

    
Ave_pen = st.sidebar.slider("Average Pension Recieved per Person", 500.0, 1000.0)

    
invest = st.sidebar.slider("Estimated Investnent Income for the Month", 1000000.0, 200000000.0)


expend = st.sidebar.slider("Estimated Expenditure for the Month", 1000000.0, 200000000.0)

    
# Estimation of population
term1 = ((epsilon1)/(lam1 - mu1))*mt.exp((lam1 - mu1)*t)
term2 = init_pop_cont*mt.exp((lam1 - mu1)*t)
entire_pop_cont = int(term1 + term2)


# Estimation of the lump sum population
lump_pop1 = init_lump_pop1*(1 - mt.exp((-mu2)*t))

lump_pop2 = init_lump_pop2*(1 - mt.exp((-epsilon2)*t))


# Estimation of pensioneer population
term3 = ((epsilon2)/(lam2 - mu2))*mt.exp((lam2 - mu2)*t)
term4 = init_pen_pop*mt.exp((lam2 - mu2)*t)
pen_pop = int(term3 + term4)


# Total Population computation
total_cont = entire_pop_cont*Ave_cont


# Total Lump sum computation
total_lump = lump_pop1*Ave_lump1 + lump_pop2*Ave_lump2


# Total Pension  paid out to clients
total_pen = pen_pop*Ave_pen

if st.button("Compute Monthly Surplus"):
    surplus = total_cont - total_lump - total_pen + invest - expend
    st.subheader("Surplus Projection")
    st.write(surplus)






