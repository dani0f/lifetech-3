import streamlit as st
import time

user_input = st.text_area("Pregunta", "¿Qué hago en caso de accidente?'")

# Esperar 10 segundos
time.sleep(1)

# Mostrar la primera diapositiva
styled_html = f"""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">                                                                                                    

<div class="slide" style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 50px; background-color: #007bff; color: #fff;">
  <i class="fas fa-exclamation-triangle" style="font-size: 64px; margin-bottom: 20px;"></i>
  <h2 style="font-size: 32px; margin-bottom: 10px;">Título 1: Notificación del accidente</h2>
  <p style="font-size: 18px; color: #fff;">La notificación del accidente laboral es el primer paso crucial en la gestión adecuada de la situación.</p>
</div>

"""
# Mostrar el componente HTML
component = st.components.v1.html(styled_html, width=800, height=600)

time.sleep(6)
# Eliminar el componente
component.empty()

# Mostrar la segunda diapositiva
styled_html = f"""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">                                                                                                    

<div class="slide" style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 50px; background-color: #007bff; color: #fff;">
  <i class="fas fa-exclamation-triangle" style="font-size: 64px; margin-bottom: 20px;"></i>
  <h2 style="font-size: 32px; margin-bottom: 10px;">Título 1: Notificación del accidente</h2>
  <p style="font-size: 18px; color: #fff;">La notificación del accidente laboral es el primer paso crucial en la gestión adecuada de la situación.</p>
</div>
"""
# Mostrar el componente HTML
component = st.components.v1.html(styled_html, width=800, height=600)

time.sleep(6)
# Eliminar el componente
component.empty()


# Mostrar la segunda diapositiva
styled_html = f"""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">                                                                                                    

<div class="slide" style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 50px; background-color: #dc3545; color: #fff;">
  <i class="fas fa-medkit" style="font-size: 64px; margin-bottom: 20px;"></i>
  <h2 style="font-size: 32px; margin-bottom: 10px;">Asistencia médica</h2>
  <p style="font-size: 18px; color: #fff;">Se debe brindar atención médica de emergencia al empleado accidentado si es necesario. El empleado será trasladado al centro médico más cercano o se llamará a una ambulancia según la gravedad del accidente.</p>
</div>


"""
# Mostrar el componente HTML
component = st.components.v1.html(styled_html, width=800, height=600)
time.sleep(6)
# Eliminar el componente
component.empty()

