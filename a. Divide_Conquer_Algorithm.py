import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox

# Loading asteroid dataset into a pandas DataFrame
df = pd.read_csv('C:/Users/Anup/! EXO-PLANET Datasets/TESS/cleaned_tess_dataset-main.csv')

# Define a function to classify stars into stellar types based on their effective temperature
def stellar_type(teff):
    if teff > 30000:
        return 'O'
    elif teff > 10000:
        return 'B'
    elif teff > 7500:
        return 'A'
    elif teff > 6000:
        return 'F'
    elif teff > 5200:
        return 'G'
    elif teff > 3700:
        return 'K'
    else:
        return 'M'

# Apply the stellar_type function to create a new column 'stellar_type'
df['stellar_type'] = df['st_teff'].apply(stellar_type)

# Function to calculate eccentricity based on planet radius and stellar type
def calculate_eccentricity(planet_radius, stellar_type):
    if stellar_type in ['O', 'B']:
        return 0.1 + 0.3 * planet_radius
    elif stellar_type in ['A', 'F']:
        return 0.05 + 0.2 * planet_radius
    else:
        return 0.01 + 0.1 * planet_radius

# Apply the calculate_eccentricity function to create a new column 'eccentricity'
df['eccentricity'] = df.apply(lambda row: calculate_eccentricity(row['pl_rade'], row['stellar_type']), axis=1)

# Define a function to check if a planet is in the habitable zone based on stellar type and insolation
def is_habitable_zone(insolation, stellar_type):
    hz_distances = {
        'O': (None, None),  # Not applicable
        'B': (10, 100),
        'A': (5, 20),
        'F': (1.5, 7),
        'G': (0.95, 1.4),
        'K': (0.3, 1.0),
        'M': (0.08, 0.3)
    }
    
    if stellar_type not in hz_distances or hz_distances[stellar_type][0] is None:
        return False
    
    hz_min, hz_max = hz_distances[stellar_type]
    return hz_min <= insolation <= hz_max

# Apply the is_habitable_zone function to create a new column 'is_habitable'
df['is_habitable'] = df.apply(lambda row: is_habitable_zone(row['pl_insol'], row['stellar_type']), axis=1)

# Function to analyze data by stellar type
def analyze_by_stellar_type(stellar_type):
    subset = df[df['stellar_type'] == stellar_type]
    mean_trandep = subset['pl_trandep'].mean()
    std_trandep = subset['pl_trandep'].std()
    habitable_planets = subset[subset['is_habitable'] == True]
    habitable_count = habitable_planets.shape[0]
    total_count = subset.shape[0]
    
    return {
        'stellar_type': stellar_type,
        'mean_trandep': mean_trandep,
        'std_trandep': std_trandep,
        'habitable_count': habitable_count,
        'total_count': total_count,
        'habitable_fraction': habitable_count / total_count if total_count > 0 else 0
    }

# Tkinter GUI
class ExoplanetAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("TESS Exoplanet Analyzer")
        
        # Create drop-down menu for TESS ID selection
        self.tess_id_label = ttk.Label(root, text="Select TESS ID:")
        self.tess_id_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.tess_id_var = tk.StringVar()
        self.tess_id_dropdown = ttk.Combobox(root, textvariable=self.tess_id_var)
        self.tess_id_dropdown['values'] = df['tid'].tolist()
        self.tess_id_dropdown.grid(row=0, column=1, padx=10, pady=10)
        
        self.analyze_button = ttk.Button(root, text="Analyze", command=self.analyze_planet)
        self.analyze_button.grid(row=0, column=2, padx=10, pady=10)
        
        self.results_text = tk.Text(root, height=15, width=50)
        self.results_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        
        self.stellar_type_analysis_button = ttk.Button(root, text="Stellar Type Analysis", command=self.stellar_type_analysis)
        self.stellar_type_analysis_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def analyze_planet(self):
        tess_id = self.tess_id_var.get()
        
        try:
            tess_id = int(tess_id)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please select a valid TESS ID.")
            return
        
        planet_info = df[df['tid'] == tess_id]
        
        if not planet_info.empty:
            planet_info = planet_info.iloc[0]
            result_text = (
                f"Planet with TESS ID {tess_id}:\n"
                f"Stellar Type: {planet_info['stellar_type']}\n"
                f"Eccentricity: {planet_info['eccentricity']:.2f}\n"
                f"Is Habitable: {'Yes' if planet_info['is_habitable'] else 'No'}\n"
                f"Other Parameters:\n{planet_info}"
            )
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, result_text)
        else:
            messagebox.showinfo("Not Found", f"No planet found with TESS ID {tess_id}")

    def stellar_type_analysis(self):
        results = []
        for st_type in df['stellar_type'].unique():
            result = analyze_by_stellar_type(st_type)
            results.append(result)
        
        results_df = pd.DataFrame(results)
        result_text = results_df.to_string(index=False)
        
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, result_text)

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = ExoplanetAnalyzer(root)
    root.mainloop()