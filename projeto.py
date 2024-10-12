import streamlit as st
import pandas as pd
import numpy as np
from scipy.integrate import odeint






st.title('Equação Diferencial Ordinária')


st.latex(r'\displaystyle  \frac{dQ}{dt}= \frac{r}{4} - \frac{rQ}{100}')

st.write('Nesse exemplo, o valor de r = 8,69.')

r=8.69


@st.cache_data
def f(y,t):
  f=r/4- r*y/100
  return f


t=np.linspace(0,50, 1000)

y0 = st.number_input("Valor de Q0: ", value=100)

#y0 = 30

sol = odeint(f, y0, t)

df = pd.DataFrame()
df['tempo'] = pd.DataFrame(t)
df['Q(t)'] = pd.DataFrame(sol)

#st.dataframe(df.head(5))
st.line_chart(df, x='tempo', y='Q(t)')