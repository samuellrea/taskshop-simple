from typing import List, Dict, Any
import sys
import os

# Agregar ruta para imports locales
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from .models import Product
except ImportError:
    # Si falla, intentar import directo
    from models import Product

class CLIApp:
    """Aplicación de consola para TaskShop."""
    
    def __init__(self) -> None:
        """Inicializa la aplicación con productos de ejemplo."""
        self.products: List[Dict[str, Any]] = [
            {"id": "1", "name": "Plantilla Excel", "price": 9.99},
            {"id": "2", "name": "Curso Python", "price": 29.99},
            {"id": "3", "name": "Recarga Premium", "price": 5.00}
        ]
        self.cart: List[Dict[str, Any]] = []
    
    def show_menu(self) -> None:
        """Muestra el menú principal en consola."""
        print("\n" + "="*40)
        print("       🛒 TASK SHOP")
        print("="*40)
        print("1. Ver productos")
        print("2. Agregar al carrito")
        print("3. Ver carrito")
        print("4. Comprar")
        print("5. Salir")
    
    def run(self) -> None:
        """Ejecuta el bucle principal de la aplicación."""
        while True:
            self.show_menu()
            choice: str = input("Elige (1-5): ")
            
            if choice == "1":
                self.show_products()
            elif choice == "2":
                self.add_to_cart()
            elif choice == "3":
                self.show_cart()
            elif choice == "4":
                self.checkout()
            elif choice == "5":
                print("¡Gracias!")
                break
            else:
                print("Opción no válida")
    
    def show_products(self) -> None:
        """Muestra la lista de productos disponibles."""
        print("\n📦 PRODUCTOS:")
        for i, p in enumerate(self.products, 1):
            print(f"{i}. {p['name']} - ${p['price']}")
    
    def add_to_cart(self) -> None:
        """Permite al usuario agregar productos al carrito."""
        self.show_products()
        try:
            num: int = int(input("\nNúmero del producto: ")) - 1
            if 0 <= num < len(self.products):
                self.cart.append(self.products[num])
                print(f"✅ {self.products[num]['name']} agregado")
            else:
                print("❌ Número inválido")
        except ValueError:
            print("❌ Entrada inválida")
    
    def show_cart(self) -> None:
        """Muestra el contenido actual del carrito."""
        if not self.cart:
            print("\n🛒 Carrito vacío")
            return
        
        print("\n🛒 TU CARRITO:")
        total: float = 0.0
        for i, item in enumerate(self.cart, 1):
            print(f"{i}. {item['name']} - ${item['price']}")
            total += item['price']
        print(f"💵 TOTAL: ${total:.2f}")
    
    def checkout(self) -> None:
        """Procesa el pago del carrito."""
        if not self.cart:
            print("\n❌ Carrito vacío")
            return
        
        self.show_cart()
        confirm: str = input("\n¿Confirmar compra? (s/n): ").lower()
        if confirm == "s":
            total: float = sum(item['price'] for item in self.cart)
            print(f"\n✅ COMPRA EXITOSA! Total: ${total:.2f}")
            self.cart = []

def run_demo() -> None:
    """
    Ejecuta una demostración automática de la aplicación.
    
    Esta función muestra las capacidades básicas de TaskShop
    sin necesidad de interacción del usuario.
    """
    print("="*50)
    print("         TASKSHOP - DEMO")
    print("="*50)
    print("Demo básico de la tienda")
    
    app = CLIApp()
    print("\n🤖 DEMO AUTOMÁTICO:")
    print("1. Mostrando productos...")
    app.show_products()
    
    if app.products:
        app.cart.append(app.products[0])
        print(f"\n2. ✅ {app.products[0]['name']} agregado")
    
    print("\n3. Mostrando carrito...")
    app.show_cart()
    
    print("\n🎯 ¡Demo completado!")