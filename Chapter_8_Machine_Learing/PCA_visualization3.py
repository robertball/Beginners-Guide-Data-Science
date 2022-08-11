import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    'height': [163, 185, 167, 184, 180, 160, 175, 174],
    'weight': [54, 93, 90, 102, 88, 50, 70, 91],
    'age': [18, 22, 68, 31, 24, 25, 32, 55],
    'iq': [90, 110, 108, 88, 90, 100, 70, 130]
})

fig = px.parallel_coordinates(df, color="height", labels={"height": "Height (cm)",
                                                          "weight": "Weight (kg)", "age": "Age (years)",
                                                          "iq": "Intelligence (iq)", })
#fig.show()
fig.write_image("Ball-Rague-Fig8.23.eps", width=750, height=350)
fig.write_image("Ball-Rague-Fig8.24.b.eps", width=450, height=350)
