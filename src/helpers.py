def detect_outliers_iqr(df, column):
    """
    Detects outliers in a specified column of a dataframe using the Interquartile Range (IQR) method.
    
    The function calculates the first (Q1) and third (Q3) quartiles, the IQR (Q3 - Q1), 
    and defines the outlier bounds as 1.5 * IQR below Q1 and 1.5 * IQR above Q3.
    Any value outside these bounds is considered an outlier and is marked as True in the 
    new column created for outliers.
    
    Parameters:
    df (pandas.DataFrame): The dataframe containing the data.
    column (str): The name of the column in the dataframe to check for outliers.
    
    Returns:
    pandas.DataFrame: The original dataframe with an additional column indicating 
                       whether each value is an outlier.
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Create a new column with True/False if it's an outlier
    outlier_col = f"{column}_outlier"
    df[outlier_col] = (df[column] < lower_bound) | (df[column] > upper_bound)

    return df



def plot_region_trends(df, region_name):
    """
    Plots vaccination trends for a given region:
    - One line per subregion
    - One gray line for the region average
    
    Parameters:
    df (DataFrame): Your full dataset with columns: year, region, subregion, vac_index
    region_name (str): Name of the region to plot (must match df['region'])
    """

    region_df = df[df['region'] == region_name]
    
    plt.figure(figsize=(10, 5))
    
    sns.lineplot(data=region_df, x='year', y='vac_index', hue='subregion', estimator='mean', marker='o', 
                 palette="Set2", errorbar=None)
    sns.lineplot(data=region_df, x='year', y='vac_index', estimator='mean', color='grey', linewidth=10, 
                 alpha=0.4, label=f"{region_name} (avg)", errorbar=None)
    
    plt.title(f"Vaccination Index in {region_name} (2012–2022)", fontsize=14)
    plt.ylabel('% of Population Vaccinated')
    plt.xlabel('Year')
    plt.legend(title='Subregion')
    plt.xticks(np.arange(2012, 2023, step=1))
    plt.ylim(60, 100)
    plt.tight_layout()
    plt.show()


def calculate_corr (variable):
    """
    Calculates and prints Pearson correlation coefficient (r) for a given variable and a vaccination score toghether with p-value.
    
    Parameters:
    variable: name of a variable in the avg_df dataframe
    """
    r, p_value = pearsonr(avg_df[variable], avg_df['vac_index'])

    print(f"Pearson r: {r}")
    print(f"P-value: {p_value}")


def add_corr(data, x, y, **kwargs):
    """Creates regression plot with a correlation coefficient and p value displayed on the top left corner"""
    
    #creating regression plot
    sns.regplot(data=data, x=x, y=y, scatter_kws={'alpha': 0.4}, line_kws={"color": "green"})

    # Calculate r and p-value
    r, p = pearsonr(data[x], data[y])

    # Display r and p on the plot
    plt.text(0.05, 0.9, f"r = {r:.2f}\np = {p:.2e}", transform=plt.gca().transAxes)
