import pandas as pd
import plotly.express as px


covid_df = pd.read_csv('Copy+of+data+-+data.csv')
#print(covid_df)
#print(covid_df.columns)

fig1 = px.line(covid_df, x='date', y='cases', title='Covid In Each Country Per Year', color='country' )
fig1.show()

#fig2 = px.scatter(covid_df, x='date', y='cases', title='Covid In Each Country Per Year', color='country' )
#fig2.show()

#fig3 = px.bar(covid_df, x='date', y='cases', title='Covid In Each Country Per Year', color='country' )
#fig3.show()