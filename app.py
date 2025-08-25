from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)

# Create folder for charts if not exists
os.makedirs("static/charts", exist_ok=True)

# --- Load datasets ---
df_hh_income = pd.read_csv('data/raw/median_household_income_2015.csv', encoding="windows-1252")
df_pct_poverty = pd.read_csv('data/raw/pct_people_below_poverty_level.csv', encoding="windows-1252")
df_pct_completed_hs = pd.read_csv('data/raw/pct_over_25_completed_high_school.csv', encoding="windows-1252")
df_share_race_city = pd.read_csv('data/raw/share_of_race_by_city.csv', encoding="windows-1252")
df_fatalities = pd.read_csv('data/raw/deaths_by_police_us.csv', encoding="windows-1252")

datasets = {
    'Shootings': df_fatalities,
    'Income': df_hh_income,
    'Education': df_pct_completed_hs,
    'Poverty': df_pct_poverty,
    'Race': df_share_race_city
}

# --- Data Cleaning Function ---
def clean_dataset(df):
    df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')
    df = df.drop_duplicates()
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        df[col] = df[col].fillna(df[col].median())
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].fillna('Unknown')
    return df

for key in datasets:
    datasets[key] = clean_dataset(datasets[key])

# --- Merge Census Data ---
def merge_census_data():
    merge_keys = set(df_hh_income.columns) & set(df_pct_poverty.columns) & set(df_pct_completed_hs.columns) & set(df_share_race_city.columns)
    merge_keys = list(merge_keys)
    if not merge_keys:
        print("No common merge keys found!")
        return None, []
    census = df_hh_income.merge(df_pct_poverty, on=merge_keys, how='outer') \
                         .merge(df_pct_completed_hs, on=merge_keys, how='outer') \
                         .merge(df_share_race_city, on=merge_keys, how='outer')
    return census, merge_keys

merged_census, census_keys = merge_census_data()

# --- Merge shootings with census ---
if merged_census is not None:
    merge_keys_final = [key for key in census_keys if key in df_fatalities.columns]
    final_df = df_fatalities.merge(merged_census, on=merge_keys_final, how='left')
    datasets['Merged'] = final_df

    # --- Convert numeric columns to proper float ---
    numeric_cols = ['poverty_rate', 'median_household_income', 'high_school_completion_rate']
    for col in numeric_cols:
        if col in datasets['Merged'].columns:
            datasets['Merged'][col] = datasets['Merged'][col].astype(str).str.replace(',', '').str.replace('[^0-9.]','', regex=True)
            datasets['Merged'][col] = pd.to_numeric(datasets['Merged'][col], errors='coerce')

# --- Step 6: EDA Charts ---
# Bar chart: shootings per state
if 'state' in df_fatalities.columns:
    plt.figure(figsize=(12,6))
    state_counts = df_fatalities['state'].value_counts()
    sns.barplot(x=state_counts.index, y=state_counts.values, palette='Blues_r')
    plt.xticks(rotation=45)
    plt.title('Shootings per State')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig("static/charts/shootings_per_state.png")
    plt.close()

# Pie chart: shootings per race
if 'race' in df_fatalities.columns:
    race_counts = df_fatalities['race'].value_counts()
    plt.figure(figsize=(6,6))
    plt.pie(race_counts, labels=race_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
    plt.title('Shootings per Race')
    plt.savefig("static/charts/shootings_per_race.png")
    plt.close()

# Scatter plots: correlations
correlation_plots = []
if 'Merged' in datasets:
    merged = datasets['Merged']
    # Poverty vs shootings
    if 'poverty_rate' in merged.columns and 'city' in merged.columns:
        df_group = merged.groupby('city')['poverty_rate'].mean().reset_index()
        df_group['shootings'] = merged.groupby('city').size().values
        plt.figure(figsize=(8,6))
        sns.scatterplot(data=df_group, x='poverty_rate', y='shootings')
        plt.title('Poverty Rate vs Shootings per City')
        plt.xlabel('Poverty Rate')
        plt.ylabel('Shootings')
        fname = "static/charts/poverty_vs_shootings.png"
        plt.savefig(fname)
        plt.close()
        correlation_plots.append(('Poverty vs Shootings', fname))

@app.route('/')
def home():
    return render_template('home.html', datasets=datasets, correlation_plots=correlation_plots)

@app.route('/journal')
def journal():
    reflections = {
        'Approach': 'Step by step: load, clean, merge, EDA, visualize.',
        'Challenges': 'Data cleaning and merging were tricky.',
        'Easy parts': 'Visualization using matplotlib/seaborn was straightforward.',
        'Learning': 'High poverty areas tend to have more shootings.',
        'Future improvements': 'Add interactive filters, dashboards, and more correlations.'
    }
    return render_template('journal.html', reflections=reflections)

if __name__ == '__main__':
    app.run(debug=True)
