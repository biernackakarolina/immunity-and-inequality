def read_and_check_quality(filepath, vac_iso_codes):
    """
    - Reads the file skipping first 4 rows
    - Chooses columns for country name and code, and years 2012-2022
    - filters for countris included in vaccinations scope

    Parameters:
        filepath: The input filepath

    Returns:
        pd.DataFrame: Filtred dataframe
    """
    import pandas as pd
    
    #reading the file
    df = pd.read_csv(filepath, skiprows=4)
    
    #choosing applicable columns 
    df = df[['Country Name', 'Country Code', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']]
    
    #filtering for countries included in vac_index df
    df = df[df["Country Code"].isin(vac_iso_codes)]

    return df



def clean_and_merge(df, countries_map, code_column='Country Code'):
    """
    Cleans the dataframe by:
    - Removing rows with at least 4 missing values
    - Interpolating remaining missing values
    - Dropping any rows still containing NaNs
    - Rounding numeric values
    - Merging with countries_map on ISO code
    - Reordering columns to: country, iso3, <year columns>

    Parameters:
        df (pd.DataFrame): The input dataframe
        countries_map (pd.DataFrame): Mapping dataframe with 'iso3' and 'country'
        code_column (str): Column name in df with ISO3 codes to join on (default: 'Country Code')

    Returns:
        pd.DataFrame: Cleaned and reordered dataframe
    """
    import pandas as pd
    
    # Drop rows with at least 4 missing values
    df = df.dropna(thresh=df.shape[1] - 4)

    # Interpolate missing values
    df.iloc[:, 2:] = df.iloc[:, 2:].interpolate(method='linear', axis=1)

    # Drop any remaining NaNs
    df = df.dropna()

    # Round to 2 decimal places
    df = df.round(2)

    # Merge with country mapping
    df = df.merge(countries_map, left_on='Country Code', right_on='iso3', how='left')

    # Reorder columns
    year_cols = [col for col in df.columns if col.startswith('20')]
    df = df[['country', 'iso3'] + year_cols]

    return df
