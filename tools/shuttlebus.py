import requests
import json
from datetime import datetime

def get_latest_shuttle_location_simple():
    """
    Fetches the shuttle bus location data from SKKU University.

    Returns:
        dict or str: The shuttle bus location information as a dictionary, 
                     or an error message string if an error occurs.
    """
    url = "http://route.hellobus.co.kr:8787/pub/routeView/skku/getSkkuLoc.aspx"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        bus_data = response.json()
        
        if not bus_data:
            return "No data received from the server."

        # Find the latest entry based on 'get_date'
        # The date format is '%Y-%m-%d %p %I:%M:%S' (e.g., "2025-05-22 오전 8:53:44")
        # Need to handle AM/PM correctly. Python's %p handles locale-specific AM/PM.
        # For Korean, "오전" is AM and "오후" is PM.
        # We'll sort and pick the last one, assuming the API might not always return sorted data.
        
        # It seems the user's previous manual edit might have removed the sorting logic.
        # The new request is to "just fetch the latest information", implying the raw data might be enough,
        # or the "latest" is implicitly the last item or requires minimal processing.
        # Given the example, the data is a list of dictionaries.
        # "Latest" usually means the one with the most recent 'get_date'.

        latest_entry = max(bus_data, key=lambda x: datetime.strptime(x['get_date'].replace('오전', 'AM').replace('오후', 'PM'), '%Y-%m-%d %p %I:%M:%S'))
        return latest_entry

    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.ConnectionError as conn_err:
        return f"Connection error occurred: {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        return f"Timeout error occurred: {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        return f"An error occurred during the request: {req_err}"
    except (ValueError, KeyError) as e:
        # ValueError for json decoding issues or strptime issues
        # KeyError if expected keys are missing in the JSON
        return f"Error processing data: {e}. Raw response: {response.text if 'response' in locals() else 'Response object not available'}"

if __name__ == "__main__":
    location_info = get_latest_shuttle_location_simple()
    if isinstance(location_info, dict):
        print("Latest Shuttle Bus Information:")
        # ensure_ascii=False to correctly print Korean characters
        print(json.dumps(location_info, indent=2, ensure_ascii=False))
    else:
        print(f"Error: {location_info}")

