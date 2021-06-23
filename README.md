### Project Assessment (Dj-Challenge).

#### Tareas:
    - Crear aplicacion catalogue que gestione CRUD de Product (sku, name, description, pvp) con multiples
     fotos (para muestra de galería) en un frontend.
    - Cada producto esta asociado a su categoria - Category(name, description).
        - Crear un data migrations de productos para que se registren directamente productos en bd (sqlite3).
    - Presentar una vista (controlador) de listado de productos con paginación.
     (puede ayudarse con bootstrap, dataTable, etc...), adicionar buscador, filtro por rango de precio.
    - En el listado de producto sea enlazado a ver el detalle del producto multiples imagenes, precio, etc...
    - Exponga api de productos con paginación y ordenamiento asc o desc por nombre, el serializador que muestre
     un listado de las imagenes de cada producto.
       - Bonus agregar test unitario.

     TENGA EN CUENTA QUE TODAS LAS TAREAS INDICADAS ARRIBA SON OBLIGATORIAS. Evaluaremos su envío en lo siguiente
     parámetros:
        - Calidad del código y mejores prácticas

Prerequisitos:
    - pip
    - Python 3.x
    - SQLite3
    - Algún IDE

Entorno desarrollo:

    dj-challenge application:
        - Para la aplicación usar SQLite3.

        - Puede llamar a la API utilizando cualquier herramienta, como Postman, Curl, etc.
        También puede utilizar la API navegable si desea, pero tenga en cuenta el endpoint.

Como hacer la entrega:
    Se permite el acceso al repo crear un branch con todos los cambios Ej.: feat/username1 y enviar el push de sus
    cambios maximo un día luego de la entrega del challenge.

    - Agregar unit tests segun su interes de validar el funcionamiento del aplicativo.