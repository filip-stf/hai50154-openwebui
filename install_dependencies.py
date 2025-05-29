#!/usr/bin/env python
"""
Skrypt do instalacji wymaganych zależności dla niestandardowego interfejsu Open WebUI
"""

import subprocess
import sys

def install_dependencies():
    """Instaluje wymagane zależności"""
    dependencies = [
        "supabase",  # Klient Python dla Supabase
        "python-dotenv",  # Do ładowania zmiennych środowiskowych z pliku .env
        "requests",  # Do wykonywania żądań HTTP
        "open-webui"  # Open WebUI
    ]
    
    print(f"Instalowanie zależności: {', '.join(dependencies)}")
    
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade"] + dependencies, check=True)
        print("Pomyślnie zainstalowano wszystkie zależności.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Błąd podczas instalacji zależności: {e}")
        return False

if __name__ == "__main__":
    if not install_dependencies():
        sys.exit(1)
