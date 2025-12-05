#!/usr/bin/env python3
"""
TODO EN UNO: CLI, GUI y Demo en un solo archivo.
"""

import sys
import os

def ejecutar_cli():
    """Ejecuta la interfaz de consola."""
    print("\n" + "="*50)
    print("       🛒 TASK SHOP - MODO CONSOLA")
    print("="*50)
    
    # Productos simples (sin imports complicados)
    productos = [
        {"id": "1", "name": "Plantilla Excel", "price": 9.99},
        {"id": "2", "name": "Curso Python", "price": 29.99},
        {"id": "3", "name": "Recarga Premium", "price": 5.00}
    ]
    
    carrito = []
    
    while True:
        print("\n" + "="*40)
        print("1. Ver productos")
        print("2. Agregar al carrito")
        print("3. Ver carrito")
        print("4. Comprar")
        print("5. Volver al menú principal")
        print("="*40)
        
        opcion = input("Elige (1-5): ")
        
        if opcion == "1":
            print("\n📦 PRODUCTOS:")
            for i, p in enumerate(productos, 1):
                print(f"{i}. {p['name']} - ${p['price']}")
        
        elif opcion == "2":
            print("\n📦 PRODUCTOS:")
            for i, p in enumerate(productos, 1):
                print(f"{i}. {p['name']} - ${p['price']}")
            
            try:
                num = int(input("\nNúmero del producto: ")) - 1
                if 0 <= num < len(productos):
                    carrito.append(productos[num])
                    print(f"✅ {productos[num]['name']} agregado")
                else:
                    print("❌ Número inválido")
            except:
                print("❌ Entrada inválida")
        
        elif opcion == "3":
            if not carrito:
                print("\n🛒 Carrito vacío")
            else:
                print("\n🛒 TU CARRITO:")
                total = 0
                for i, item in enumerate(carrito, 1):
                    print(f"{i}. {item['name']} - ${item['price']}")
                    total += item['price']
                print(f"💵 TOTAL: ${total:.2f}")
        
        elif opcion == "4":
            if not carrito:
                print("\n❌ Carrito vacío")
            else:
                total = sum(item['price'] for item in carrito)
                print(f"\n🛒 Total: ${total:.2f}")
                confirm = input("¿Confirmar compra? (s/n): ").lower()
                if confirm == "s":
                    print(f"\n✅ COMPRA EXITOSA! Total: ${total:.2f}")
                    carrito = []
        
        elif opcion == "5":
            break
        
        else:
            print("Opción no válida")

def ejecutar_demo():
    """Ejecuta demo automático."""
    print("\n" + "="*50)
    print("         🤖 TASKSHOP - DEMO AUTOMÁTICO")
    print("="*50)
    
    productos = [
        {"name": "Plantilla Excel", "price": 9.99},
        {"name": "Curso Python", "price": 29.99},
        {"name": "Recarga Premium", "price": 5.00}
    ]
    
    print("\n1. Mostrando productos...")
    for i, p in enumerate(productos, 1):
        print(f"   {i}. {p['name']} - ${p['price']}")
    
    print("\n2. Simulando compra...")
    print(f"   ✅ {productos[0]['name']} agregado al carrito")
    print(f"   💰 Total simulado: ${productos[0]['price']}")
    
    print("\n3. Checkout simulado...")
    print("   ✅ Pago procesado exitosamente")
    print("   📧 Correo de confirmación enviado")
    
    print("\n🎯 ¡Demo completado!")

def main():
    """Menú principal."""
    while True:
        print("\n" + "="*50)
        print("           🛒 TASK SHOP - MENÚ PRINCIPAL")
        print("="*50)
        print("1. Interfaz de Consola (interactiva)")
        print("2. Demo Automático")
        print("3. Ejecutar GUI (ventana gráfica)")
        print("4. Salir")
        print("="*50)
        
        opcion = input("Elige (1-4): ")
        
        if opcion == "1":
            ejecutar_cli()
        elif opcion == "2":
            ejecutar_demo()
        elif opcion == "3":
            print("\n⚠️  Cierra esta ventana y ejecuta: py -m src.taskshop.simple_gui")
            print("   O haz doble clic en ejecutar_gui.bat")
        elif opcion == "4":
            print("\n¡Gracias por usar TaskShop!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()