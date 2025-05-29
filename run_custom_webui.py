#!/usr/bin/env python
"""
Skrypt do uruchamiania Open WebUI z niestandardowymi modyfikacjami
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def setup_custom_theme():
    """Kopiuje niestandardowy motyw do katalogu Open WebUI"""
    custom_theme_path = Path('/workspaces/hai50154-openwebui/custom_theme/custom.css')
    
    if not custom_theme_path.exists():
        print("Błąd: Nie znaleziono niestandardowego motywu.")
        return False
    
    # Znajdź ścieżkę do zainstalowanego pakietu Open WebUI
    try:
        import open_webui
        package_path = Path(open_webui.__file__).parent
        themes_dir = package_path / 'frontend' / 'themes'
        
        if not themes_dir.exists():
            print(f"Błąd: Katalog tematów nie istnieje: {themes_dir}")
            return False
        
        # Kopiuj niestandardowy motyw
        target_path = themes_dir / 'custom.css'
        shutil.copy(custom_theme_path, target_path)
        print(f"Pomyślnie skopiowano niestandardowy motyw do {target_path}")
        
        # Modyfikuj plik index.html, aby dodać klasę custom-theme
        index_html_path = package_path / 'frontend' / 'index.html'
        if index_html_path.exists():
            try:
                with open(index_html_path, 'r') as f:
                    content = f.read()
                
                # Dodaj klasę custom-theme do znacznika body
                if '<body' in content and 'custom-theme' not in content:
                    content = content.replace('<body', '<body class="custom-theme"')
                    
                    # Dodaj link do CSS
                    css_link = '<link rel="stylesheet" href="/themes/custom.css">'
                    if '<head>' in content and css_link not in content:
                        content = content.replace('</head>', f'{css_link}</head>')
                    
                    with open(index_html_path, 'w') as f:
                        f.write(content)
                    print(f"Pomyślnie zaktualizowano {index_html_path} z klasą custom-theme")
            except Exception as e:
                print(f"Błąd podczas modyfikacji index.html: {e}")
        
        return True
    
    except ImportError:
        print("Błąd: Nie można zaimportować pakietu open_webui")
        return False
    except Exception as e:
        print(f"Błąd podczas kopiowania motywu: {e}")
        return False

def setup_environment():
    """Konfiguruje zmienne środowiskowe dla Supabase"""
    # Pobierz DATABASE_URL i ustaw jako SUPABASE_URL
    database_url = os.environ.get('DATABASE_URL')
    if database_url:
        # Konwertuj postgresql:// URL na URL Supabase API
        # Zazwyczaj Supabase URL ma format https://<project-id>.supabase.co
        # Ten krok wymaga dostosowania w zależności od formatu DATABASE_URL
        # Poniższy kod jest przykładowy i może wymagać dostosowania
        if 'pooler.supabase.com' in database_url:
            project_id = database_url.split('@')[1].split('.')[0]
            supabase_url = f"https://{project_id}.supabase.co"
            os.environ['SUPABASE_URL'] = supabase_url
            print(f"Ustawiono SUPABASE_URL: {supabase_url}")
        else:
            print("Ostrzeżenie: Nie można automatycznie określić SUPABASE_URL")
    
    # Sprawdź, czy SUPABASE_KEY jest ustawiony
    supabase_key = os.environ.get('SUPABASE_KEY')
    if not supabase_key:
        print("Ostrzeżenie: SUPABASE_KEY nie jest ustawiony")
        # W rzeczywistym środowisku możesz pobierać klucz z bezpiecznego źródła
        # np. z usługi zarządzania sekretami
    
    return True

def run_open_webui():
    """Uruchamia Open WebUI z własnymi modyfikacjami"""
    command = ["open-webui", "serve"]
    
    # Dodaj dodatkowe argumenty w razie potrzeby
    # command.extend(["--host", "0.0.0.0", "--port", "8080"])
    
    print(f"Uruchamiam Open WebUI: {' '.join(command)}")
    subprocess.run(command)

if __name__ == "__main__":
    print("Konfiguracja niestandardowego interfejsu Open WebUI...")
    
    # Konfiguruj środowisko
    if not setup_environment():
        print("Błąd podczas konfiguracji środowiska")
        sys.exit(1)
    
    # Ustaw niestandardowy motyw
    if not setup_custom_theme():
        print("Ostrzeżenie: Nie można skonfigurować niestandardowego motywu")
        # Kontynuuj mimo to
    
    # Uruchom Open WebUI
    run_open_webui()
