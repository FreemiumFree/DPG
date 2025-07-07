import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Data from the provided JSON
components = [
    "Cloud Computing (AWS/Azure)", 
    "GPU Computing", 
    "Simulation Software", 
    "Data Storage", 
    "Unreal Engine License", 
    "Data Transfer/Bandwidth", 
    "Asset Management", 
    "Platform Operations", 
    "Security & Compliance", 
    "Remaining Balance"
]

costs = [25.0, 18.0, 15.0, 12.0, 8.0, 7.0, 5.0, 4.0, 3.0, 3.0]
percentages = [25.0, 18.0, 15.0, 12.0, 8.0, 7.0, 5.0, 4.0, 3.0, 3.0]

# Abbreviate component names to fit 15-character limit
abbreviated_components = [
    "Cloud (AWS/Az)",
    "GPU Computing", 
    "Simulation SW",
    "Data Storage",
    "Unreal License",
    "Data Transfer",
    "Asset Mgmt",
    "Platform Ops",
    "Security",
    "Remaining Bal"
]

# Create DataFrame
df = pd.DataFrame({
    'Component': abbreviated_components,
    'Cost': costs,
    'Percentage': percentages
})

# Define colors using the brand palette
colors = ['#1FB8CD', '#FFC185', '#ECEBD5', '#5D878F', '#D2BA4C', 
          '#B4413C', '#964325', '#944454', '#13343B', '#DB4545']

# Create pie chart
fig = go.Figure(data=[go.Pie(
    labels=df['Component'],
    values=df['Cost'],
    textinfo='label+percent',
    textposition='inside',
    marker=dict(colors=colors),
    hovertemplate='<b>%{label}</b><br>' +
                  'Cost: $%{value}<br>' +
                  'Percentage: %{percent}<br>' +
                  '<extra></extra>'
)])

# Update layout
fig.update_layout(
    title="AV Digital Proving Ground - $100 Cost Breakdown",
    showlegend=True,
    legend=dict(
        orientation="v",
        yanchor="middle",
        y=0.5,
        xanchor="left",
        x=1.05
    ),
    uniformtext_minsize=14,
    uniformtext_mode='hide'
)

# Save the chart
fig.write_image("av_proving_ground_cost_breakdown.png")
print("Chart saved as av_proving_ground_cost_breakdown.png")