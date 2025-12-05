#!/usr/bin/env python3
"""Script simplificado para verificar código"""
import subprocess
import sys

def run_command(command: str, description: str) -> bool:
    """Ejecuta un comando y muestra resultado"""
    print(f"\n📋 {description}")
    print(f"   Comando: {command}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("   ✅ Éxito")
            if result.stdout.strip():
                print(f"   Salida: {result.stdout[:200]}...")
            return True
        else:
            print("   ❌ Falló")
            if result.stderr:
                print(f"   Error: {result.stderr[:200]}")
            return False
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def main() -> None:
    print("="*60)
    print("🔧 VERIFICADOR DE CÓDIGO TASKSHOP")
    print("="*60)
    
    # Lista de verificaciones (más simples)
    checks = [
        ("black src/ tests/ --check", "Verificar formato con Black"),
        ("ruff check src/", "Verificar estilo con Ruff (src/)"),
        ("ruff check tests/", "Verificar estilo con Ruff (tests/)"),
        ("mypy src/ --ignore-missing-imports", "Verificar tipos con mypy"),
        ("pytest tests/ -q", "Ejecutar tests con pytest"),
    ]
    
    passed = 0
    total = len(checks)
    
    for command, description in checks:
        if run_command(command, description):
            passed += 1
    
    print("\n" + "="*60)
    print(f"📊 RESULTADO: {passed}/{total} verificaciones pasaron")
    
    if passed == total:
        print("🎉 ¡TODAS LAS VERIFICACIONES PASARON!")
        sys.exit(0)
    else:
        print("⚠️  Algunas verificaciones fallaron")
        print("\n💡 Consejos:")
        print("   1. Ejecuta 'black src/ tests/' para formatear automáticamente")
        print("   2. Ejecuta 'ruff check src/ tests/ --fix' para corregir errores")
        print("   3. Revisa los errores específicos arriba")
        sys.exit(1)

if __name__ == "__main__":
    main()