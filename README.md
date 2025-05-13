# Immunity & Inequality: Analyzing Vaccination Trends Across the Globe

This project explores global vaccination trends using data from UNICEF, the World Bank, the World Values Survey, and V-Dem. The goal is to understand how socioeconomic, political, and technological factors — such as GDP, health expenditure, internet use, government trust, and polarization — influence vaccination rates across countries.

## Notebooks

### 1. `Data Preparation.ipynb`
This notebook focuses on cleaning, aligning, and merging data from multiple sources. Key steps include:
- Loading raw datasets from UNICEF, World Bank, V-Dem, and WVS.
- Cleaning and harmonizing country names and formats.
- Handling missing data.
- Generating a final merged dataset for analysis and modeling.

Final variables include:
- `country`, `region`, `subregion`, `year`
- `vac_index` – average coverage of key vaccines
- `gdp`, `health_exp`, `child_mort`, `internet_use`, `gov_trust`, `polarization`

  
### 2. `Exploratory Analysis.ipynb`
This notebook explores relationships between vaccination rates and selected predictors. It includes:
- Correlation analysis
- Pairplots and heatmaps
- Visualization with Plotly and Seaborn
- Initial insights into trends by region and year

## Data Sources
- [UNICEF Immunization Data](https://data.unicef.org/topic/child-health/immunization/)
- [World Bank Open Data](https://data.worldbank.org/)
- [World Values Survey](https://www.worldvaluessurvey.org/)
- [V-Dem Dataset](https://www.v-dem.net/)

## Requirements
The analysis uses the following Python libraries:
- `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`, `scipy`

Install all requirements using:
```bash
pip install -r requirements.txt
