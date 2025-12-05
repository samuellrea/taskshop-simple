from typing import List, Dict, Any

class Product:
    """Representa un producto en la tienda."""
    
    def __init__(self, id: str, name: str, price: float) -> None:
        """
        Inicializa un nuevo producto.
        
        Args:
            id: Identificador único del producto
            name: Nombre del producto
            price: Precio del producto
        """
        self.id = id
        self.name = name
        self.price = price
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convierte el producto a un diccionario.
        
        Returns:
            Diccionario con los datos del producto
        """
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }

class Cart:
    """Representa un carrito de compras."""
    
    def __init__(self) -> None:
        """Inicializa un carrito vacío."""
        self.items: List[Dict[str, Any]] = []
    
    def add(self, product: Product, quantity: int = 1) -> None:
        """
        Agrega un producto al carrito.
        
        Args:
            product: Producto a agregar
            quantity: Cantidad del producto (default: 1)
        """
        self.items.append({
            "product": product,
            "quantity": quantity,
            "subtotal": product.price * quantity
        })
    
    def total(self) -> float:
        """
        Calcula el total del carrito.
        
        Returns:
            Suma total de todos los items
        """
        return sum(item["subtotal"] for item in self.items)
    
    def clear(self) -> None:
        """Vacía el carrito."""
        self.items = []