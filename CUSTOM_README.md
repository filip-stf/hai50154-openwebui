# Niestandardowy interfejs Open WebUI z Supabase

Ten projekt zawiera modyfikacje interfejsu użytkownika Open WebUI oraz integrację z bazą danych Supabase.

## Wymagania

- Zainstalowany Open WebUI
- Konto i projekt Supabase
- Klucz API Supabase
- Środowisko Python 3.10+

## Konfiguracja

1. Skopiuj plik `.env.example` do `.env` i uzupełnij zmienne środowiskowe:
   ```bash
   cp .env.example .env
   ```

2. Edytuj plik `.env` i uzupełnij:
   - `SUPABASE_URL`: URL do twojego projektu Supabase (np. https://your-project-id.supabase.co)
   - `SUPABASE_KEY`: Klucz API Supabase (znajdziesz go w ustawieniach projektu Supabase)
   - `DATABASE_URL`: URL połączenia do bazy danych PostgreSQL w Supabase
   - `PGVECTOR_DB_URL`: Ten sam URL co `DATABASE_URL`
   - `OPENAI_API_KEY`: Twój klucz API OpenAI lub Google Gemini

3. Jeśli używasz Codespaces, skonfiguruj sekrety w ustawieniach GitHub Codespaces.

## Uruchamianie

Aby uruchomić Open WebUI z niestandardowymi modyfikacjami:

```bash
python run_custom_webui.py
```

## Modyfikacje interfejsu użytkownika

Projekt zawiera niestandardowy motyw CSS w katalogu `custom_theme/`. Możesz edytować plik `custom_theme/custom.css`, aby dostosować wygląd interfejsu.

## Narzędzia Supabase

Dodaliśmy narzędzia do integracji z Supabase:

- `get_data_from_supabase(table_name)`: Pobiera dane z określonej tabeli
- `insert_into_supabase(table_name, data)`: Dodaje dane do tabeli
- `update_in_supabase(table_name, id_value, data)`: Aktualizuje dane w tabeli

## Tworzenie własnych modyfikacji

Aby dodać własne modyfikacje interfejsu:

1. Edytuj plik `custom_theme/custom.css`
2. Uruchom `python run_custom_webui.py`, aby zastosować zmiany

Aby rozszerzyć funkcjonalność Supabase:

1. Dodaj nowe metody w pliku `tools/supabase_tool.py`
2. Zaktualizuj plik `tool.py`, aby eksponować nowe metody
