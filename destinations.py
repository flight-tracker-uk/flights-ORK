"""Cork Airport (ORK) destinations — April 2026."""

DESTINATIONS = {
    "ORK": {
        "name": "Cork",
        "routes": {
            # UK
            "BHX": "Birmingham",
            "BRS": "Bristol",
            "EDI": "Edinburgh",
            "GLA": "Glasgow",
            "LGW": "London Gatwick",
            "LPL": "Liverpool",
            "MAN": "Manchester",
            # Spain (Mainland)
            "AGP": "Malaga",
            "ALC": "Alicante",
            "BCN": "Barcelona",
            "BIO": "Bilbao",
            "GRO": "Girona",
            "REU": "Reus",
            "SCQ": "Santiago de Compostela",
            "SVQ": "Seville",
            "VLC": "Valencia",
            # Balearic Islands
            "PMI": "Palma de Mallorca",
            # Canary Islands
            "ACE": "Lanzarote",
            "FUE": "Fuerteventura",
            "LPA": "Gran Canaria",
            "TFS": "Tenerife South",
            # Italy
            "AHO": "Alghero",
            "BGY": "Milan Bergamo",
            "PSA": "Pisa",
            "VCE": "Venice Marco Polo",
            # France
            "BOD": "Bordeaux",
            "CCF": "Carcassonne",
            "CDG": "Paris Charles de Gaulle",
            "LRH": "La Rochelle",
            "NCE": "Nice",
            # Portugal
            "FAO": "Faro",
            # Germany
            "MUC": "Munich",
            # Greece
            "RHO": "Rhodes",
            # Turkey
            "ADB": "Izmir",
            # Czech Republic
            "PRG": "Prague",
            # Netherlands
            "AMS": "Amsterdam",
            # Belgium
            "BRU": "Brussels",
            # Croatia
            "ZAD": "Zadar",
            # Switzerland
            "ZRH": "Zurich",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
