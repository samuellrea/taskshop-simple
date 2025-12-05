#!/usr/bin/env python3
"""Tests unitarios para TaskShop - Versión que SÍ funciona."""

import sys
import os

# Agregar la raíz del proyecto al path
sys.path.insert(0, os.path.abspath('.'))

def test_product_creation():
    """Test básico de creación de producto."""
    # Importar DESPUÉS de agregar el path
    from src.taskshop.models import Product
    
    p = Product("1", "Test Product", 10.0)
    assert p.name == "Test Product"
    assert p.price == 10.0
    print("✅ test_product_creation: PASADO")

def test_cart_operations():
    """Test básico del carrito."""
    from src.taskshop.models import Product, Cart
    
    # Test creación
    cart = Cart()
    assert len(cart.items) == 0
    
    # Test agregar producto
    p = Product("1", "Test", 10.0)
    cart.add(p, 2)
    assert len(cart.items) == 1
    assert cart.total() == 20.0
    
    # Test limpiar carrito
    cart.clear()
    assert len(cart.items) == 0
    assert cart.total() == 0.0
    
    print("✅ test_cart_operations: PASADO")

def test_cli_app_import():
    """Test que verifica que CLIApp se puede importar."""
    from src.taskshop.cli_app import CLIApp
    app = CLIApp()
    assert hasattr(app, 'products')
    assert hasattr(app, 'cart')
    print("✅ test_cli_app_import: PASADO")

def test_simple_gui_import():
    """Test que verifica que SimpleTaskShop se puede importar."""
    from src.taskshop.simple_gui import SimpleTaskShop
    app = SimpleTaskShop()
    assert hasattr(app, 'products')
    assert hasattr(app, 'cart')
    print("✅ test_simple_gui_import: PASADO")

def run_all_tests():
    """Ejecuta todos los tests y muestra resultado."""
    print("="*50)
    print("🧪 EJECUTANDO TESTS DE TASKSHOP")
    print("="*50)
    
    tests = [
        test_product_creation,
        test_cart_operations,
        test_cli_app_import,
        test_simple_gui_import
    ]
    
    passed = 0
    failed = 0
    
    for test_func in tests:
        try:
            test_func()
            passed += 1
        except Exception as e:
            failed += 1
            print(f"❌ {test_func.__name__}: FALLADO - {e}")
    
    print("\n" + "="*50)
    print(f"📊 RESULTADO: {passed} pasados, {failed} fallados")
    
    if failed == 0:
        print("🎉 ¡TODOS LOS TESTS PASARON!")
        return True
    else:
        print("⚠️  Algunos tests fallaron")
        return False

if __name__ == "__main__":
    # Ejecutar cuando se corre directamente
    success = run_all_tests()
    sys.exit(0 if success else 1)