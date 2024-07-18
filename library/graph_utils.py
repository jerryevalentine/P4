import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

def correlation_heatmap_df(df): #Pass
    # Select only numeric columns
    numeric_cols = df.select_dtypes(include='number')
    # Compute the correlation matrix
    correlation_matrix = numeric_cols.corr().round(2)
    # Create the heatmap
    fig = px.imshow(correlation_matrix, 
                    text_auto=True, 
                    width=800, 
                    height=600,
                    labels={'color':'Correlation'},
                    title='Correlation Heatmap')
    fig.show()

def create_bar_charts_df(df):#Pass
    # Select only string columns
    string_cols = df.select_dtypes(include='object').columns.tolist()
    
    # Determine the number of rows and columns for the subplots
    num_cols = len(string_cols)
    num_rows = (num_cols + 1) // 2  # Two plots per row
    
    fig, axes = plt.subplots(num_rows, 2, figsize=(15, 5 * num_rows))
    axes = axes.flatten()  # Flatten axes array to easily iterate over it
    
    for i, col in enumerate(string_cols):
        df[col].value_counts().plot(kind="bar", ax=axes[i])
        axes[i].set_title(f"{col} distribution")
        axes[i].set_xlabel(f"{col}")
        axes[i].set_ylabel("count")
    
    # Hide any unused subplots
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])
    
    plt.tight_layout()
    plt.show()