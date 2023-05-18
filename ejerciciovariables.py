print("Ejecutando el programa")

#Mis librerías owo
import pandas as pd
from sklearn.metrics.pairwise import cosine_distances
import ipywidgets as widgets
from IPython.display import display , clear_output
import matplotlib.pyplot as plt

 # Cargar los datos desde la tabla de excel
datos = pd.read_csv("basepizza.csv", index_col=0)

def recomendar_usuario(nombre_usuario, k):
    clear_output() #limpiar la salida actual
    
    # Seleccionar el vector de características del usuario de interés
    vector_p = datos.loc[nombre_usuario].values
    
    # Calcular la distancia coseno entre el vector de características de P y todos los demás usuarios
    distancias = cosine_distances([vector_p], datos.values)
    
    # Seleccionar los K usuarios más cercanos a P, basados en la distancia coseno
    indices_vecinos = distancias.argsort()[0, 1:k+1]
    vecindario = datos.iloc[indices_vecinos].index.tolist()
    distancias_vecinos = distancias[0, indices_vecinos].tolist()
    
    # Presentar el vecindario de usuarios seleccionado y la distancia coseno correspondiente
    print("Vecindario de usuarios:")
    for i, usuario in enumerate(vecindario):
        print(f"{i+1}. {usuario} (distancia coseno: {distancias_vecinos[i]})")
        
    # Graficar las distancias coseno
    fig, ax = plt.subplots()
    ax.bar(vecindario, distancias_vecinos)
    ax.set_title("Distancias Coseno")
    ax.set_xlabel("Usuarios")
    ax.set_ylabel("Distancia Coseno")
    plt.show()
    
def on_button_clicked(b):
    nombre_usuario = dropdown.value
    k = 3
    recomendar_usuario(nombre_usuario,k)
    # Llamar a la función recomendar_usuario con el valor seleccionado del menú desplegable
    # vecindario = recomendar_usuario(dropdown.value, 3)
    
dropdown = widgets.Dropdown(
    options=list(pd.read_csv("basepizza.csv", index_col=0).index),
    description='Nombre:',
    disabled=False,
)

button = widgets.Button(description="Buscar")
button.on_click(on_button_clicked)

output = widgets.Output()

display(dropdown, button, output)

def mostrar_tabla(change):
    with output:
        clear_output()
        nombre_usuario = dropdown.value
        k = 3
        recomendar_usuario(nombre_usuario,k)
dropdown.observe(mostrar_tabla,'value')


