import streamlit as st
#from streamlit_extras.let_it_rain import rain

def count_words(text):
    """Función para contar las palabras en un texto."""
    return len(text.split())

def main():
    # Título de la aplicación
    st.title("Contador de Palabras")

    # Instrucciones para el usuario
    st.write("Ingresa un texto en el cuadro de abajo y presiona el botón para contar las palabras.")

    # Cuadro de texto para ingresar el texto
    user_text = st.text_area("Ingresa tu texto aquí:", "")

    # Botón para procesar el texto
    if st.button("Contar Palabras"):
        if user_text.strip():
            word_count = count_words(user_text)
            st.success(f"El texto ingresado tiene {word_count} palabras.")
            # Animación de globos
            rain(emoji="🎈", font_size=54, falling_speed=5, animation_length="infinite")
        else:
            st.warning("Por favor, ingresa un texto válido.")

if __name__ == "__main__":
    main()
