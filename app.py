import pandas as pd
import plotly.express as px
import streamlit as st
st.set_page_config(page_title="PMFBY ANALYSIS",layout="wide")
df=pd.read_excel("C:\\Users\\dell\\Desktop\\PMFBY.xlsx")
#st.dataframe(df)
st.sidebar.header("Please Select the District:")
district=st.sidebar.multiselect("Select the district:",options=df["District Name"].unique(),default=df["District Name"].unique())
df_selection=df[(df["District Name"].isin(district))]
xyz=df_selection[["Year","Total Applications"]]
fig1=px.bar(xyz,x="Year",y="Total Applications",title="<b>Total Application per Year<b>",text_auto=True)
st.plotly_chart(fig1)

x_farmers=df_selection[["Year","Farmers"]]
fig2=px.bar(x_farmers,x="Year",y="Farmers",title="<b>Total Farmers per Year<b>",text_auto=True)
st.plotly_chart(fig2)
