#####################################################################################################################################
### SIMULACIÓN DE BASES DE DATOS USANDO LISTAS DE DICCIONARIOS EN PYTHON CON OPERACIONES CRUD (Crear, Leer, Actualizar, Eliminar) ###
#####################################################################################################################################

usuarios = [] # Crea una lista vacía llamada usuarios

def crear_usuario(id, nombre, edad): # Define una función para crear un nuevo usuario con id, nombre y edad
    usuarios.append({ # ((usuarios.append("Todo lo que se ponga dentro lo empuja a la lista "usuarios"") es para listas). Agrega un nuevo diccionario con la información del usuario a la lista usuarios
        "id": id, # Asigna el valor de id al campo "id" del diccionario
        "nombre": nombre, # Asigna el valor de nombre al campo "nombre" del diccionario
        "edad": edad # Asigna el valor de edad al campo "edad" del diccionario
    }) # Cierra la función crear_usuario

 #Ejemplo de "BD" en memoria utilizando una lista de diccionarios para almacenar la información de los usuarios.
crear_usuario(1, "Alice", 30) # Crea un nuevo usuario con id 1, nombre "Alice" y edad 30, y lo agrega a la lista usuarios
crear_usuario(2, "Bob", 25) # Crea un nuevo usuario con id 2, nombre "Bob" y edad 25, y lo agrega a la lista usuarios
crear_usuario(3, "Charlie", 35) # Crea un nuevo usuario con id 3, nombre "Charlie" y edad 35, y lo agrega a la lista usuarios


def mostrar_usuarios(): # Define una función para mostrar la lista de usuarios
    for usuario in usuarios: # Inicia un bucle for que itera sobre cada usuario en la lista usuarios
        print(usuario) # Imprime cada usuario (que es un diccionario) en la lista usuarios

mostrar_usuarios() # Muestra la lista de usuarios, que contiene los usuarios creados anteriormente


def actualizar_usuario(id, nombre, edad): # Define una función para actualizar la información de un usuario existente basado en su id
    for usuario in usuarios: # Inicia un bucle for que itera sobre cada usuario en la lista usuarios
        if usuario["id"] == id: # Si el id del usuario coincide con el id proporcionado, se ejecuta el bloque de código dentro del if
            usuario["nombre"] = nombre # Actualiza el campo "nombre" del diccionario del usuario con el nuevo nombre proporcionado
            usuario["edad"] = edad # Actualiza el campo "edad" del diccionario del usuario con la nueva edad proporcionada
            return # Sale de la función después de actualizar el usuario, evitando iterar sobre los demás usuarios
        
actualizar_usuario(1, "Alice Smith", 31) # Actualiza el usuario con id 1, cambiando su nombre a "Alice Smith" y su edad a 31


def eliminar_usuario(id): # Define una función para eliminar un usuario de la lista basado en su id
    for usuario in usuarios: # Inicia un bucle for que itera sobre cada usuario en la lista usuarios
        if usuario["id"] == id: # Si el id del usuario coincide con el id proporcionado, se ejecuta el bloque de código dentro del if
            usuarios.remove(usuario) # Elimina el usuario (que es un diccionario) de la lista usuarios
            return # Sale de la función después de eliminar el usuario, evitando iterar sobre los demás usuarios
        
eliminar_usuario(2) # Elimina el usuario con id 2 de la lista usuarios


print("\nDespues de los cambios: ") # Imprime un mensaje para indicar que se mostrarán los usuarios después de los cambios realizados
mostrar_usuarios() # Muestra la lista de usuarios nuevamente, que ahora solo contiene el usuario actualizado con id 1 y 3, ya que el usuario con id 2 ha sido eliminado
