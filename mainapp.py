import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="PMFBY ANALYSIS",layout="wide")
df=pd.read_excel("PMFBY.xlsx")

def Year_Wise_Analysis():
    st.title("Year Wise Analysis of PMFBY Data 2018-2023")
    
    
    st.sidebar.header("Please Select the District:")
    district=st.sidebar.multiselect("Select the district:",options=df["District Name"].unique(),default=df["District Name"].unique())
    
    
    df_selection=df[(df["District Name"].isin(district))]
    
    
    
    xyz=df_selection[["Year","Total Applications"]]
    fig1=px.bar(xyz,x="Year",y="Total Applications",title="<b>Total Application per Year<b>",text_auto=True)
    fig1.update_traces(marker_color='green')
    st.plotly_chart(fig1)
    
    x_farmers=df_selection[["Year","Farmers"]]
    fig2=px.bar(x_farmers,x="Year",y="Farmers",title="<b>Total Farmers per Year<b>",text_auto=True)
    fig2.update_traces(marker_color='orange')
    st.plotly_chart(fig2)
    
    
    x_fa=df_selection[["Year","Farmers","Total Applications"]]
    x_fa_melted=x_fa.melt(id_vars=["Year"],value_vars=["Farmers","Total Applications"],var_name='Category',value_name="Farmers and Applications")
    fig3=px.bar(x_fa_melted,x="Year",y="Farmers and Applications",color='Category',title="<b>Total Farmers And Applications per Year<b>",barmode='group',text_auto=True,color_discrete_map={"Farmers":"#ec7c34","Total Applications":"#609cd4"})
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
    fig6=px.bar(x_area,x="Year",y="Area Insured",title="<b>Area Insured in Hectares per Year<b>",text_auto=True)
    st.plotly_chart(fig6)
    
    x_sum=df_selection[["Year","Sum Insured (In Lac.)"]]
    fig7=px.bar(x_sum,x="Year",y="Sum Insured (In Lac.)",title="<b>Sum Insured (In Lac.) per Year<b>",text_auto=True)
    fig7.update_traces(marker_color='red')
    st.plotly_chart(fig7)
    
    x_gross=df_selection[["Year","Gross Premium"]]
    fig8=px.bar(x_gross,x="Year",y="Gross Premium",title="<b>Gross Premium (In Lac.) per Year<b>",text_auto=True)
    fig8.update_traces(marker_color='brown')
    st.plotly_chart(fig8)
    
    
    x_gs=df_selection[["Year","Gross Premium","Sum Insured (In Lac.)"]]
    x_gs_melted=x_gs.melt(id_vars=["Year"],value_vars=["Gross Premium","Sum Insured (In Lac.)"],var_name='Category',value_name="Gross Premium and Sum Insured (In Lac.)")
    fig9=px.bar(x_gs_melted,x="Year",y="Gross Premium and Sum Insured (In Lac.)",color='Category',title="<b>Gross Premium And Sum Insured (In Lac.) per Year<b>",barmode='group',text_auto=True,color_discrete_map={"Gross Premium":"blue","Sum Insured (In Lac.)":"red"})
    st.plotly_chart(fig9)
    
    
    x_gt=df_selection[["Year","Gross Premium","Total Claim Paid"]]
    x_gt_melted=x_gt.melt(id_vars=["Year"],value_vars=["Gross Premium","Total Claim Paid"],var_name='Category',value_name="Gross Premium and Total Claim Paid")
    fig10=px.bar(x_gt_melted,x="Year",y="Gross Premium and Total Claim Paid",color='Category',title="<b>Gross Premium And Total Claim Paid (In Lac.) per Year<b>",barmode='group',text_auto=True,color_discrete_map={"Gross Premium":"green","Total Claim Paid":"yellow"})
    st.plotly_chart(fig10)
    
    
    x_ts=df_selection[["Year","Total Claim Paid","MT+L+PH"]]
    x_ts_melted=x_ts.melt(id_vars=["Year"],value_vars=["MT+L+PH","Total Claim Paid"],var_name='Category',value_name="Summation of Midterm,Localized,Post Harvest and Total Claim")
    fig11=px.bar(x_ts_melted,x="Year",y="Summation of Midterm,Localized,Post Harvest and Total Claim",color='Category',title="<b>Summation of Midterm,Localized,Post Harvest and Total Claim Paid (In Lac.) per Year<b>",barmode='group',text_auto=True,color_discrete_map={"Total Claim Paid":"olive","MT+L+PH":"purple"})
    st.plotly_chart(fig11)
    
    
    x_ty=df_selection[["Year","Total Claim Paid","Yield Based"]]
    x_ty_melted=x_ty.melt(id_vars=["Year"],value_vars=["Yield Based","Total Claim Paid"],var_name='Category',value_name="Yield Based and Total Claim Paid")
    fig12=px.bar(x_ty_melted,x="Year",y="Yield Based and Total Claim Paid",color='Category',title="<b>Yield Based and Total Claim Paid (In Lac.) per Year<b>",barmode='group',text_auto=True,color_discrete_map={"Total Claim Paid":"red","Yield Based":"yellow"})
    st.plotly_chart(fig12)
    
    
    x_ff=df_selection[["Year","Farmers","Total Farmer Benefit(Actual)"]]
    x_ff_melted=x_ff.melt(id_vars=["Year"],value_vars=["Total Farmer Benefit(Actual)","Farmers"],var_name='Category',value_name="Total Farmer Benefit and Farmers")
    fig13=px.bar(x_ff_melted,x="Year",y="Total Farmer Benefit and Farmers",color='Category',title="<b>Total Farmer Benefit and Farmers per Year<b>",barmode='group',text_auto=True,color_discrete_map={"Total Farmer Benefit(Actual)":"yellow","Farmers":"blue"})
    st.plotly_chart(fig13)

def District_Wise_Analysis():
    st.title("District Wise Analysis of PMFBY Data 2018-2023")
    
    
    st.sidebar.header("Please Select the Year:")
    year=st.sidebar.multiselect("Select the Year:",options=df["Year"].unique(),default=df["Year"].unique())
    
    
    df_selection=df[(df["Year"].isin(year))]
    
    
    xyz=df_selection[["District Name","Total Applications"]]
    xyz.sort_values(by="Total Applications",ascending=False,inplace=True)
    fig1=px.bar(xyz,x="District Name",y="Total Applications",title="<b>Total Application per District<b>",text_auto=True)
    fig1.update_traces(marker_color='green')
    st.plotly_chart(fig1)
    
    x_farmers=df_selection[["District Name","Farmers"]]
    x_farmers.sort_values(by="Farmers",ascending=False,inplace=True)
    fig2=px.bar(x_farmers,x="District Name",y="Farmers",title="<b>Total Farmers per District<b>",text_auto=True)
    fig2.update_traces(marker_color='orange')
    st.plotly_chart(fig2)
    
    x_fa=df_selection[["District Name","Farmers","Total Applications"]]
    x_fa.sort_values(by="Total Applications",ascending=False,inplace=True)
    x_fa_melted=x_fa.melt(id_vars=["District Name"],value_vars=["Farmers","Total Applications"],var_name='Category',value_name="Farmers and Applications")
    fig3=px.bar(x_fa_melted,x="District Name",y="Farmers and Applications",color='Category',title="<b>Total Farmers And Applications per District<b>",barmode='group',text_auto=True,color_discrete_map={"Farmers":"#ec7c34","Total Applications":"#609cd4"})
    st.plotly_chart(fig3)
    
    
    x_pr=df_selection[["District Name","GP/Sum Insured"]]
    x_pr.sort_values(by="GP/Sum Insured",ascending=False,inplace=True)
    x_pr["GP/Sum Insured"]=(x_pr["GP/Sum Insured"].round(2))*100
    fig4 = px.line(x_pr, x="District Name", y="GP/Sum Insured",title="<b>Average Premium rate per District Name<b>", text="GP/Sum Insured")
    fig4.update_traces(textposition="bottom center")
    st.plotly_chart(fig4)
    
    x_cap=df_selection[["District Name","Claim Against Premium"]]
    x_cap.sort_values(by="Claim Against Premium",ascending=False,inplace=True)
    x_cap["Claim Against Premium"]=(x_cap["Claim Against Premium"].round(2))*100
    fig5 = px.line(x_cap, x="District Name", y="Claim Against Premium",title="<b>Claim Against Premium per District<b>", text="Claim Against Premium")
    fig5.update_traces(textposition="top center")
    st.plotly_chart(fig5)
    
    x_area=df_selection[["District Name","Area Insured"]]
    x_area.sort_values(by="Area Insured",ascending=False,inplace=True)
    fig6=px.bar(x_area,x="District Name",y="Area Insured",title="<b>Area Insured in Hectares per District<b>",text_auto=True)
    st.plotly_chart(fig6)
    
    x_sum=df_selection[["District Name","Sum Insured (In Lac.)"]]
    x_sum.sort_values(by="Sum Insured (In Lac.)",ascending=False,inplace=True)
    fig7=px.bar(x_sum,x="District Name",y="Sum Insured (In Lac.)",title="<b>Sum Insured (In Lac.) per District <b>",text_auto=True)
    fig7.update_traces(marker_color='red')
    st.plotly_chart(fig7)
    
    x_gross=df_selection[["District Name","Gross Premium"]]
    x_gross.sort_values(by="Gross Premium",ascending=False,inplace=True)
    fig8=px.bar(x_gross,x="District Name",y="Gross Premium",title="<b>Gross Premium (In Lac.) per District <b>",text_auto=True)
    fig8.update_traces(marker_color='brown')
    st.plotly_chart(fig8)
    
    x_gs=df_selection[["District Name","Gross Premium","Sum Insured (In Lac.)"]]
    x_gs.sort_values(by="Sum Insured (In Lac.)",ascending=False,inplace=True)
    x_gs_melted=x_gs.melt(id_vars=["District Name"],value_vars=["Gross Premium","Sum Insured (In Lac.)"],var_name='Category',value_name="Gross Premium and Sum Insured (In Lac.)")
    fig9=px.bar(x_gs_melted,x="District Name",y="Gross Premium and Sum Insured (In Lac.)",color='Category',title="<b>Gross Premium And Sum Insured (In Lac.) per District <b>",barmode='group',text_auto=True,color_discrete_map={"Gross Premium":"blue","Sum Insured (In Lac.)":"red"})
    st.plotly_chart(fig9)
    
    x_gt=df_selection[["District Name","Gross Premium","Total Claim Paid"]]
    x_gt.sort_values(by="Total Claim Paid",ascending=False,inplace=True)
    x_gt_melted=x_gt.melt(id_vars=["District Name"],value_vars=["Gross Premium","Total Claim Paid"],var_name='Category',value_name="Gross Premium and Total Claim Paid")
    fig10=px.bar(x_gt_melted,x="District Name",y="Gross Premium and Total Claim Paid",color='Category',title="<b>Gross Premium And Total Claim Paid (In Lac.) per District<b>",barmode='group',text_auto=True,color_discrete_map={"Gross Premium":"green","Total Claim Paid":"yellow"})
    st.plotly_chart(fig10)
    
    x_ts=df_selection[["District Name","Total Claim Paid","MT+L+PH"]]
    x_ts.sort_values(by="Total Claim Paid",ascending=False,inplace=True)
    x_ts_melted=x_ts.melt(id_vars=["District Name"],value_vars=["MT+L+PH","Total Claim Paid"],var_name='Category',value_name="Summation of Midterm,Localized,Post Harvest and Total Claim")
    fig11=px.bar(x_ts_melted,x="District Name",y="Summation of Midterm,Localized,Post Harvest and Total Claim",color='Category',title="<b>Summation of Midterm,Localized,Post Harvest and Total Claim Paid (In Lac.) per District <b>",barmode='group',text_auto=True,color_discrete_map={"Total Claim Paid":"olive","MT+L+PH":"purple"})
    st.plotly_chart(fig11)
    
    
    x_ty=df_selection[["District Name","Total Claim Paid","Yield Based"]]
    x_ty.sort_values(by="Total Claim Paid",ascending=False,inplace=True)
    x_ty_melted=x_ty.melt(id_vars=["District Name"],value_vars=["Yield Based","Total Claim Paid"],var_name='Category',value_name="Yield Based and Total Claim Paid")
    fig12=px.bar(x_ty_melted,x="District Name",y="Yield Based and Total Claim Paid",color='Category',title="<b>Yield Based and Total Claim Paid (In Lac.) per District <b>",barmode='group',text_auto=True,color_discrete_map={"Total Claim Paid":"red","Yield Based":"yellow"})
    st.plotly_chart(fig12)
    
    
    x_ff=df_selection[["District Name","Farmers","Total Farmer Benefit(Actual)"]]
    x_ff.sort_values(by="Farmers",ascending=False,inplace=True)
    x_ff_melted=x_ff.melt(id_vars=["District Name"],value_vars=["Total Farmer Benefit(Actual)","Farmers"],var_name='Category',value_name="Total Farmer Benefit and Farmers")
    fig13=px.bar(x_ff_melted,x="District Name",y="Total Farmer Benefit and Farmers",color='Category',title="<b>Total Farmer Benefit and Farmers per District<b>",barmode='group',text_auto=True,color_discrete_map={"Total Farmer Benefit(Actual)":"yellow","Farmers":"blue"})
    st.plotly_chart(fig13)


page = st.sidebar.selectbox('Select Analysis',['Year_Wise_Analysis','District_Wise_Analysis']) 
if page == 'Year_Wise_Analysis':
    Year_Wise_Analysis()
else:
    District_Wise_Analysis()
