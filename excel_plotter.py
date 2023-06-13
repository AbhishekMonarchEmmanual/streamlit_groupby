import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 
import streamlit as st 
import plotly.tools




st.set_page_config(page_title= 'Excel_Plotter')
st.title("Excel_plotter")
st.subheader('Feed me with the your excel file')

upload = st.file_uploader("Drop the file")

if upload is not None:
    st.markdown('____')
    df = pd.read_csv(upload)
    st.dataframe(df)

if upload is not None: 
    button1 = st.checkbox("Click Here if you want to perform the group by option")
    if button1:
        group_name = st.selectbox(("choose the column you want to group?"), 
                                ((list(df.columns))))
        
        st.text(f'this is the coulumn you choose for the group by - {group_name}')
        
        agg_name = st.selectbox(("choose the column you want to aggregate?"), 
                                ((list(df.columns))))
        
        st.text(f'this is the coulumn you choose for the aggregate by - {agg_name}')
        
        agg = st.selectbox("Choose the aggreagation you want to do on the dataframe", ("select one ", "sum", "count"))
        
        if agg == "sum": 
            sum_grouped = df.groupby(group_name, as_index=False)[agg_name].sum()
            st.dataframe(sum_grouped)
           
            if st.checkbox("would you like to plot the data"):
                st.set_option('deprecation.showPyplotGlobalUse', False)
                ax1= sns.barplot(x = group_name,y= agg_name ,data = sum_grouped)
                for bars in ax1.containers:
                    ax1.bar_label(bars)
                st.pyplot()
                
        if agg == "count": 
            count_grouped = df.groupby(group_name, as_index=False)[agg_name].count()
            st.dataframe(count_grouped)
            if st.checkbox("would you like to plot the data"):
                st.set_option('deprecation.showPyplotGlobalUse', False)
                ax = sns.barplot(x = group_name,y= agg_name ,data = count_grouped)
                for bars in ax.containers:
                    ax.bar_label(bars)
                st.pyplot()
                
                
        
    
        
            
        
        
            
        
        
    
    
    
    
    




    
    














































































