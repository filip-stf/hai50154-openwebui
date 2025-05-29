import os
from pydantic import BaseModel, Field
from typing import List, Optional
import requests
from supabase import create_client, Client

class SupabaseTool:
    def __init__(self):
        # Inicjalizacja połączenia z Supabase
        self.supabase_url = os.environ.get("SUPABASE_URL")
        self.supabase_key = os.environ.get("SUPABASE_KEY")
        self.client = None
        
        if self.supabase_url and self.supabase_key:
            try:
                self.client = create_client(self.supabase_url, self.supabase_key)
            except Exception as e:
                print(f"Błąd podczas inicjalizacji klienta Supabase: {e}")
    
    def get_data_from_table(self, table_name: str = Field(..., description="Nazwa tabeli w Supabase")) -> str:
        """
        Pobierz dane z określonej tabeli w Supabase.
        """
        if not self.client:
            return "Błąd: Brak poprawnej konfiguracji klienta Supabase"
        
        try:
            response = self.client.table(table_name).select("*").execute()
            return f"Dane z tabeli {table_name}: {response.data}"
        except Exception as e:
            return f"Błąd podczas pobierania danych z tabeli {table_name}: {e}"
    
    def insert_into_table(
        self, 
        table_name: str = Field(..., description="Nazwa tabeli w Supabase"),
        data: dict = Field(..., description="Dane do zapisania w formacie JSON")
    ) -> str:
        """
        Wstaw nowe dane do określonej tabeli w Supabase.
        """
        if not self.client:
            return "Błąd: Brak poprawnej konfiguracji klienta Supabase"
        
        try:
            response = self.client.table(table_name).insert(data).execute()
            return f"Dane zostały pomyślnie dodane do tabeli {table_name}: {response.data}"
        except Exception as e:
            return f"Błąd podczas dodawania danych do tabeli {table_name}: {e}"
    
    def update_in_table(
        self, 
        table_name: str = Field(..., description="Nazwa tabeli w Supabase"),
        id_value: str = Field(..., description="Wartość ID rekordu do aktualizacji"),
        data: dict = Field(..., description="Dane do aktualizacji w formacie JSON")
    ) -> str:
        """
        Aktualizuj dane w określonej tabeli w Supabase.
        """
        if not self.client:
            return "Błąd: Brak poprawnej konfiguracji klienta Supabase"
        
        try:
            response = self.client.table(table_name).update(data).eq("id", id_value).execute()
            return f"Dane zostały pomyślnie zaktualizowane w tabeli {table_name}: {response.data}"
        except Exception as e:
            return f"Błąd podczas aktualizacji danych w tabeli {table_name}: {e}"
