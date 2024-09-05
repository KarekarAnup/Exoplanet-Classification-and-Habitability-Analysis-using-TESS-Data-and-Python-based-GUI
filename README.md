# Exoplanet-Classification-and-Habitability-Analysis-using-TESS-Data-and-Python-based-GUI
This project involves the development of a Python-based GUI application for the analysis of exoplanet data from the TESS mission. The application integrates various astrophysical algorithms to classify stars into stellar types, calculate exoplanet eccentricity, assess habitability based on insolation, and evaluate transit parameters.

### **Project Flow Structure**

1. **Dataset Loading**:  
   The project starts by loading a cleaned TESS dataset into a pandas DataFrame. The data contains various parameters related to stars and their associated exoplanets.

2. **Stellar Classification**:  
   A function `stellar_type` is applied to classify stars into spectral types (O, B, A, F, G, K, M) based on their effective temperature (`st_teff`). This helps in categorizing the stars according to their characteristics.

3. **Eccentricity Calculation**:  
   A custom function `calculate_eccentricity` is implemented to estimate the eccentricity of exoplanets, factoring in their radius and the stellar type they orbit. The eccentricity is added as a new column to the dataset.

4. **Habitability Zone Check**:  
   The function `is_habitable_zone` assesses whether an exoplanet lies in the habitable zone of its host star, based on insolation (`pl_insol`) and stellar type. This classification is crucial for understanding potential life-supporting conditions.

5. **Orbital Period Ratio and Transit Duration**:  
   The code computes two essential parameters:
   - `orbital_period_ratio`: A normalized ratio of an exoplanet's orbital period to reference values based on stellar type.
   - `transit_duration`: The transit duration of the exoplanet, calculated using the stellar radius, planet radius, and orbital period.

6. **Data Analysis by Stellar Type**:  
   The function `analyze_by_stellar_type` analyzes data grouped by stellar types and computes the mean transit depth, habitable planet count, orbital period ratios, and transit durations for each stellar group. This analysis provides insights into trends across different stellar types.

7. **Tkinter GUI**:  
   The graphical user interface (GUI) is built using Tkinter to allow users to:
   - Select a TESS ID from the dataset.
   - View detailed parameters like stellar type, eccentricity, and habitability.
   - Analyze the dataset based on stellar type, showing key statistics.
   - Reset the fields and exit the application.

### **Future Plans**

1. **Integration of Machine Learning Models**:  
   Add machine learning models, such as Convolutional Neural Networks (CNN), for automated classification of exoplanets based on their physical and orbital parameters.

2. **Dynamic Visualization**:  
   Implement real-time visualization of planetary systems, such as star-planet orbits and habitability zones, using libraries like `matplotlib` or `plotly` for better data representation.

3. **Support for Additional Datasets**:  
   Allow users to load datasets from different exoplanetary missions (Kepler, Hubble, etc.) for comparative analysis.

4. **Advanced Habitability Metrics**:  
   Extend habitability analysis by incorporating additional metrics like atmospheric composition and water presence to assess potential biosignatures.

5. **User Input for Custom Analysis**:  
   Enable users to input custom parameters (e.g., stellar temperature, planet radius) to simulate hypothetical exoplanets and determine their characteristics.

6. **Cloud-based Dataset and Analysis**:  
   Enable cloud-based integration for accessing larger datasets and running complex analysis remotely, enhancing the scalability of the project.

7. **Exporting Analysis Results**:  
   Add functionality to export results as CSV, PDF, or graphical reports for further usage or sharing within the scientific community.

8. **Multi-language Support**:  
   Provide translations for the GUI to make the tool accessible to a broader, global audience. 

These enhancements will make the project more robust, user-friendly, and applicable to advanced exoplanetary research.
