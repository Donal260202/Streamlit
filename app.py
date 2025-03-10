import pandas as pd
import plotly.express as px
import streamlit as st
st.set_page_config(page_title="PMFBY ANALYSIS",layout="wide")
df=pd.read_excel("PMFBY.xlsx")
#st.dataframe(df)

st.title("Analysis of PMFBY Data 2018-2023 Year Wise")


st.sidebar.header("Please Select the District:")
district=st.sidebar.multiselect("Select the district:",options=df["District Name"].unique(),default=df["District Name"].unique())


df_selection=df[(df["District Name"].isin(district))]



xyz=df_selection[["Year","Total Applications"]]
fig1=px.bar(xyz,x="Year",y="Total Applications",title="<b>Total Application per Year<b>",text_auto=True)
st.plotly_chart(fig1)

x_farmers=df_selection[["Year","Farmers"]]
fig2=px.bar(x_farmers,x="Year",y="Farmers",title="<b>Total Farmers per Year<b>",text_auto=True)
st.plotly_chart(fig2)


x_fa=df_selection[["Year","Farmers","Total Applications"]]
x_fa_melted=x_fa.melt(id_vars=["Year"],value_vars=["Farmers","Total Applications"],var_name='Category',value_name="Farmers and Applications")
fig3=px.bar(x_fa_melted,x="Year",y="Farmers and Applications",color='Category',title="<b>Total Farmers And Applications per Year<b>",barmode='group',text_auto=True)
st.plotly_chart(fig3)


x_pr=df_selection[["Year","GP/Sum Insured"]]
x_pr["GP/Sum Insured"]=(x_pr["GP/Sum Insured"].round(2))*100
fig4 = px.line(x_pr, x="Year", y="GP/Sum Insured",title="<b>Average Premium rate per Year<b>", text="GP/Sum Insured")
fig4.update_traces(textposition="bottom center")
st.plotly_chart(fig4)

x_cap=df_selection[["Year","Claim Against Premium"]]
x_cap["Claim Against Premium"]=(x_cap["Claim Against Premium"].round(2))*100
fig5 = px.line(x_cap, x="Year", y="Claim Against Premium",title="<b>Claim Against Premium per Year<b>", text="Claim Against Premium")
fig5.update_traces(textposition="top center")
st.plotly_chart(fig5)

x_area=df_selection[["Year","Area Insured"]]
fig6=px.bar(x_area,x="Year",y="Area Insured",title="<b>Area Insured per Year<b>",text_auto=True)
st.plotly_chart(fig6)

x_sum=df_selection[["Year","Sum Insured (In Lac.)"]]
fig7=px.bar(x_sum,x="Year",y="Sum Insured (In Lac.)",title="<b>Sum Insured (In Lac.) per Year<b>",text_auto=True)
st.plotly_chart(fig7)

x_gross=df_selection[["Year","Gross Premium"]]
fig8=px.bar(x_gross,x="Year",y="Gross Premium",title="<b>Gross Premium per Year<b>",text_auto=True)
st.plotly_chart(fig8)


x_gs=df_selection[["Year","Gross Premium","Sum Insured (In Lac.)"]]
x_gs_melted=x_gs.melt(id_vars=["Year"],value_vars=["Gross Premium","Sum Insured (In Lac.)"],var_name='Category',value_name="Gross Premium and Sum Insured (In Lac.)")
fig9=px.bar(x_gs_melted,x="Year",y="Gross Premium and Sum Insured (In Lac.)",color='Category',title="<b>Gross Premium And Sum Insured (In Lac.) per Year<b>",barmode='group',text_auto=True)
st.plotly_chart(fig9)


x_gt=df_selection[["Year","Gross Premium","Total Claim Paid"]]
x_gt_melted=x_gt.melt(id_vars=["Year"],value_vars=["Gross Premium","Total Claim Paid"],var_name='Category',value_name="Gross Premium and Total Claim Paid")
fig10=px.bar(x_gt_melted,x="Year",y="Gross Premium and Total Claim Paid",color='Category',title="<b>Gross Premium And Total Claim Paid per Year<b>",barmode='group',text_auto=True)
st.plotly_chart(fig10)


x_ts=df_selection[["Year","Total Claim Paid","MT+L+PH"]]
x_ts_melted=x_ts.melt(id_vars=["Year"],value_vars=["MT+L+PH","Total Claim Paid"],var_name='Category',value_name="Summation of Midterm,Localized,Post Harvest and Total Claim")
fig11=px.bar(x_ts_melted,x="Year",y="Summation of Midterm,Localized,Post Harvest and Total Claim",color='Category',title="<b>Summation of Midterm,Localized,Post Harvest and Total Claim Paid per Year<b>",barmode='group',text_auto=True)
st.plotly_chart(fig11)


x_ty=df_selection[["Year","Total Claim Paid","Yield Based"]]
x_ty_melted=x_ty.melt(id_vars=["Year"],value_vars=["Yield Based","Total Claim Paid"],var_name='Category',value_name="Yield Based and Total Claim Paid")
fig12=px.bar(x_ty_melted,x="Year",y="Yield Based and Total Claim Paid",color='Category',title="<b>Yield Based and Total Claim Paid per Year<b>",barmode='group',text_auto=True)
st.plotly_chart(fig12)


x_ff=df_selection[["Year","Farmers","Total Farmer Benefit(Actual)"]]
x_ff_melted=x_ff.melt(id_vars=["Year"],value_vars=["Total Farmer Benefit(Actual)","Farmers"],var_name='Category',value_name="Total Farmer Benefit and Farmers")
fig13=px.bar(x_ff_melted,x="Year",y="Total Farmer Benefit and Farmers",color='Category',title="<b>Total Farmer Benefit and Farmers per Year<b>",barmode='group',text_auto=True)
st.plotly_chart(fig13)
