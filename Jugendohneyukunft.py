import streamlit as st
import pandas as pd
import altair as alt

st.header("Jugend ohne Zukunft")
st.subheader("Anteil der befragten Jugendlichen zur Ausbildung in der Pandemie - Studiensuchende")

source = pd.DataFrame({
        'Anteil(%)': [9, 20, 27, 9],
        ' ': ['Sehr viel gemacht', 'eher viel gemacht aber noch nicht genug', 'eher wenig gemacht', 'gar nichts gemacht']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x=' :O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis: 1743 Befragte; (14 bis 20 Jahre) in Deutschland; 2021; fehlend zu 100%: Weiß nicht
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle:  Bertelsmann Stiftung")