"""
WILL WORK ONLY AFTER Altair 4.2 release candidate
"""
import altair as alt
import pandas as pd

category = ['Sky','Shadyside of pyramid','sunny side of pyramid']
color = ['#416D9D', '#674028','#DEAC58']

df = pd.DataFrame({
    'category' : category,
    'color' : color,
    'value' : [75,10,15],
    'order' : [3,1,2]
})

chart = alt.Chart(df).mark_arc(outerRadius=80).encode(
    alt.Theta('value:Q', scale=alt.Scale(range=[2.356, 8.639])),
    alt.Color('category:N',scale=alt.Scale(domain=category, range=color),legend=alt.Legend(orient='right', title=None)),
    order='order:Q'   
).properties(width=150, height=150).configure_view(strokeOpacity=0)

chart.show()