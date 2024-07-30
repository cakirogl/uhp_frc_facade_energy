import streamlit as st
from xgboost.sklearn import XGBRegressor
import pandas as pd
import numpy as np

url="https://raw.githubusercontent.com/cakirogl/uhp_frc_facade_energy/main/data_4features.xlsx"
df = pd.read_excel(url, header=0, sheet_name="Sheet1")
#Total heating and cooling energy use - GJ will be predicted 
df.drop(df.columns[[0,1,42,43,44, 45, 46, 48]], inplace=True, axis=1)
x = df[df.columns[:-1]]
y = df[df.columns[-1]]

ic=st.container()
ic1,ic2 = ic.columns(2)
with ic1:
    TFA = st.number_input("**Total floor area [ft^2]**", min_value=2500, max_value=498600, step=24800, value=90735);
    WF = st.number_input("**Window fraction**", min_value=0.07, max_value=0.4, step=0.02, value=0.22)
with ic2:
    AAT = st.number_input("**Annual average temperature [F]**", min_value=27,max_value=80, step=2.5, value=57)
    OL = st.number_input("**Occupancy level**", min_value=1, max_value=30, step=1.5, value=4.2)

model = XGBRegressor()
model.fit(x,y)
oc=st.container()
new_sample = np.array([[TFA, WF,AAT, OL]], dtype=object)
with oc:
    st.write(f"Total energy consumption [GJ]: {model.predict(new_sample)[0]:.2f}")