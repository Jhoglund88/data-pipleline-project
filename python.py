python
import csv

def load_data(filepath):


    """Läser in data från en CSV-fil."""
    data = []
    try:
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Gör om temperaturen till ett flyttal
                row['temperature'] = float(row['temperature'])
                data.append(row)
        print(f"✅ Laddade {len(data)} rader från {filepath}")
        return data
    except FileNotFoundError:
        print(f"❌ Filen {filepath} hittades inte!")
        return None

   hej = input("Skriv ditt namn:")

   # ... load_data funktionen här ...

def transform_data(data):
    """Konverterar temperaturen från Celsius till Fahrenheit."""
    if data is None:
        return None
    for row in data:
        celsius = row['temperature']
        fahrenheit = (celsius * 9/5) + 32
        row['temperature_f'] = round(fahrenheit, 1)
    print("✅ Data transformerad (Celsius → Fahrenheit)")
    return data

