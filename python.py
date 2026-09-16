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
