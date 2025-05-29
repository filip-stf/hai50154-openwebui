#!/usr/bin/env python
# Skrypt do inicjalizacji klasy Supabase i konfiguracji połączenia

import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Ładowanie zmiennych środowiskowych z pliku .env (jeśli istnieje)
load_dotenv()

def init_supabase():
    # Pobieranie URL i klucza z zmiennych środowiskowych
    supabase_url = os.environ.get("SUPABASE_URL")
    supabase_key = os.environ.get("SUPABASE_KEY")
    
    # Sprawdź, czy zmienne są dostępne
    if not supabase_url or not supabase_key:
        print("Błąd: Brak wymaganych zmiennych środowiskowych SUPABASE_URL lub SUPABASE_KEY")
        return None
    
    # Inicjalizacja klienta Supabase
    try:
        supabase: Client = create_client(supabase_url, supabase_key)
        print("Połączenie z Supabase zostało pomyślnie zainicjalizowane.")
        return supabase
    except Exception as e:
        print(f"Błąd podczas inicjalizacji klienta Supabase: {e}")
        return None

# Przykład użycia:
if __name__ == "__main__":
    # Inicjalizacja klienta Supabase
    supabase_client = init_supabase()
    
    if supabase_client:
        # Przykładowe zapytanie do tabeli
        try:
            response = supabase_client.table("example_table").select("*").execute()
            print("Dane z tabeli:", response.data)
        except Exception as e:
            print(f"Błąd podczas wykonywania zapytania: {e}")
