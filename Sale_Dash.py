import streamlit as st
import plotly.express as px
import pandas as pd


df2=pd.read_csv('../Sale_Store_Pross.csv')
#df2['year']=df2['year'].astype(str)
st.title('Sale_Store_analysis')

c1,c2,c3 =st.columns(3)
with c1:
    st.metric(label='Sales in M$:',value=(df2['Sales'].sum()/1000000).round(3))
with c2:
    st.metric(label='Profit in K$:',value=(df2['Profit'].sum()/10000).round(3))
with c3:
    st.metric(label='Avg Discount Percentage Per Year %',value=(15.5),delta='2%')
    
col1,col2 =st.columns(2)
with col1:
    st.header("Sale by Category")
    fig=px.histogram(df2,x='Category',y='Sales',histfunc='sum',color='Region',barmode="group",width=450 ,text_auto=True)
    st.plotly_chart(fig)
with col2:
    st.header('Profit by Sale using Segment')
    fig2=px.scatter(df2,x='Sales',y='Profit',color='Segment')
    st.plotly_chart(fig2)
