import requests
import json
import re

def european_countries_and_capitals():
    url = "https://de.wikipedia.org/w/api.php"
    parameter = {
        "action": "parse",
        "page": "Liste der Hauptstädte Europas",
        "format": "json",
        "prop": "wikitext",
    }
    try:
        # API-Anfrage senden
        api_response = requests.get(url, params=parameter)
        api_response.raise_for_status()  # Fehler bei HTTP-Problemen auslösen
        json_data = api_response.json()

        wikitext = json_data["parse"]["wikitext"]["*"]
        countries_capitals = {}
        table_pattern = r'\|-\n\|(?:.*?)\'\'\'\[\[(.*?)(?:\|.*?)?\]\]\'\'\'(?:.*?\n.*?){3}\| \{\{(.*?)(?:\|.*?)?\}\}'
        matches = re.findall(table_pattern, wikitext, re.DOTALL)
        country_codes = {
            'NLD': 'Niederlande',
            'AND': 'Andorra',
            'GRC': 'Griechenland',
            'SRB': 'Serbien',
            'DEU': 'Deutschland',
            'CHE': 'Schweiz',
            'SVK': 'Slowakei',
            'BEL': 'Belgien',
            'HUN': 'Ungarn',
            'ROU': 'Rumänien',
            'MDA': 'Moldawien',
            'SMR': 'San Marino',
            'IRL': 'Irland',
            'FIN': 'Finnland',
            'UKR': 'Ukraine',
            'DNK': 'Dänemark',
            'PRT': 'Portugal',
            'SVN': 'Slowenien',
            'GBR': 'Vereinigtes Königreich',
            'LUX': 'Luxemburg',
            'ESP': 'Spanien',
            'BLR': 'Belarus',
            'MCO': 'Monaco',
            'RUS': 'Russland',
            'CYP': 'Zypern',
            'NOR': 'Norwegen',
            'FRA': 'Frankreich',
            'MNE': 'Montenegro',
            'CZE': 'Tschechien',
            'ISL': 'Island',
            'LVA': 'Lettland',
            'ITA': 'Italien',
            'BIH': 'Bosnien und Herzegowina',
            'MKD': 'Nordmazedonien',
            'BGR': 'Bulgarien',
            'SWE': 'Schweden',
            'EST': 'Estland',
            'ALB': 'Albanien',
            'LIE': 'Liechtenstein',
            'MLT': 'Malta',
            'VAT': 'Vatikanstadt',
            'LTU': 'Litauen',
            'POL': 'Polen',
            'AUT': 'Österreich',
            'HRV': 'Kroatien'
        }

        for capital, code in matches:
            capital_cleaned = re.sub(r'\s*\(.*?\)|\s*kurz:.*', '', capital)
            if code in country_codes:
                countries_capitals[country_codes[code]] = capital_cleaned

        return countries_capitals

    except requests.exceptions.RequestException as e:
        print(f"API Request Error: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON Decoding Error: {e}")
        return None
    except KeyError as e:
        print(f"Key Error in JSON data: {e}")
        return None

