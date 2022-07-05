------------------------------------------------------ READ ME ------------------------------------------------------

El proyecto se divide en dos, por una lado tenemos la parte de funciones y por el otro la parte de sesiones.

La parte de funciones es una aplicación integrada con dos conjuntos de funciones principales. Entre ellas el conjunto 
de Restaurantes y el conjunto de Recetas. Ambas son aplicaciones que puede realizar el CRUD en los modelos de cada 
conjunto, a su vez se pueden buscar los datos en la base.

Por otro lado la parte de sesiones se encarga del registro, el login, el logout de los usuarios. El usuario a su vez
 va a poder crear editar y eliminar perfiles. 

Una vez dentro del inicio el usuario se encuentra con una pestaña que contiene todas las direcciones necesarias. En 
la parte superior se encuentra con un navBar que se encuentra presente en todas las pestañas, la misma muestra botones 
para redireccionarse a: El mismo inicio, Restaurantes, Recetas, Login y Register en el caso de no estar logueados, o 
logout y perfil en el caso de estar logueados. En el footer muestra el usuario en caso de estar logueado, y contiene 
un botón que redirecciona a la página de about us la cual brinda información sobre los desarrolladores de esta página.

Restaurantes: Restaurantes nos presenta una lista de los restaurantes disponibles. A su vez sobre esta lista podemos 
ver un buscador funcional junto a dos botones. El primero es el botón del buscador (que nos lleva a un listado de los 
restaurantes buscados) y el segundo es un botón para agregar restaurantes que nos redirige a un un formulario donde se 
solicitan todos los datos necesarios para crear una restaurante. Por cada carta de restaurant, en la misma se puede 
clickear el nombre para visualizar 
el detalle. 
En el detalle se puede ver una breve descripción de cada establecimiento, con los datos básicos que un usuario debería
saber. A su vez el restaurante puede ser editado y eliminado.
Por debajo de las descripciones, tenemos una sección de comentarios la cual contiene comentarios/críticas del restaurante. 
Esos comentarios se agregaran al tocar el botón de "Agregar Comentario" Estos también pueden ser editados al clickear 
en su detalle.

Recetas: Esta sección funciona de una manera muy similar a la de restaurantes. Cuenta con un buscador, un botón para buscar 
y otro para agregar. Las funcionalidades son idénticas a la de restaurantes con la diferencia de que las recetas no contienen 
comentarios dentro de ellas.

Login: nos redirecciona a un formulario donde ingresamos el nombre de usuario y la contraseña.

logout: cierra la sesión automáticamente

register: nos presenta un formulario para con brindar los datos necesarios (Username, Email, 
Contraseña y Repetir Contraseña)

Perfil nos muestra los datos del usuario y nos presenta otros más que no son vitales para el registro, como por ejemplo: 
nombre, apellido y edad). Todos los datos son iterables. y para confirmar se debe pulsar el botón editar.


