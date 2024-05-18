import streamlit as st

st.title('Do not click this button !!!')
tog_button = st.toggle('<--- Here')
if tog_button:
    st.write('Rwarrrrrrrrr!')
else:
    st.write('Meow')
    
animal_sound = st.select_slider(
    'Select your favourite animal sounds : ',
    options=['Meow', 'Woof', 'Moo', 'Quack', 'WHEEEEE', 'Rwarrrrr!'])
st.write('You like', animal_sound,'?')