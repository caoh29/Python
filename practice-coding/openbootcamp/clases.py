class Proveedor:
    direccion = ""
    telefono = 0
    codPostal = 0
    nombreProveedor = ""

class Categoria:

    idCategoria = 0
    nombreCategoria = ""

class Producto:

    idProducto = 0
    categoriaProducto = Categoria()
    precio = 0
    tamaño = 0
    peso = 0
    tipoProducto = 0
    CIFProveedor = Proveedor()

p = Producto()
p.CIFProveedor.nombreProveedor
p.categoriaProducto.nombreCategoria