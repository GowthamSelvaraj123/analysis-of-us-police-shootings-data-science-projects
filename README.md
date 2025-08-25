<body>
  <div class="container py-4 py-lg-5">
    <header class="hero shadow-soft mb-4">
      <div class="d-flex align-items-center gap-3 flex-wrap">
        <div class="flex-grow-1">
          <h1 class="mb-2">US Police Fatalities + Census Data Analysis</h1>
          <p class="mb-0 text-secondary">
            A data analysis & visualization project exploring fatal police shootings (The Washington Post) alongside US census socio-economic indicators.
          </p>
        </div>
        <div class="text-nowrap">
          <span class="badge badge-soft rounded-pill me-2">Flask</span>
          <span class="badge badge-soft rounded-pill me-2">Pandas</span>
          <span class="badge badge-soft rounded-pill me-2">Matplotlib</span>
          <span class="badge badge-soft rounded-pill">Seaborn</span>
        </div>
      </div>
    </header>
      <div class="col-lg-8">
        <section id="overview" class="section mb-4">
          <h2>1) Project Overview</h2>
          <div class="callout">
            <p class="mb-2">
              This project analyzes US fatal police shootings (from <em>The Washington Post</em> database since Jan 1, 2015) in conjunction with socio-economic indicators from US census data: poverty rate, median household income, high school completion, and racial demographics. It aims to identify patterns and relationships across locations.
            </p>
            <p class="mb-0">
              Output includes data cleaning/merging, descriptive stats, EDA charts (bar, pie, scatter), and a Flask dashboard with an integrated journal.
            </p>
          </div>
        </section>
        <section id="dataset-list" class="section mb-4">
          <h2>2) Datasets</h2>
          <ul class="list-files">
            <li><code>data/raw/deaths_by_police_us.csv</code> — Fatal police shootings</li>
            <li><code>data/raw/median_household_income_2015.csv</code> — Income</li>
            <li><code>data/raw/pct_people_below_poverty_level.csv</code> — Poverty rate</li>
            <li><code>data/raw/pct_over_25_completed_high_school.csv</code> — High school completion</li>
            <li><code>data/raw/share_of_race_by_city.csv</code> — Racial demographics</li>
          </ul>
        </section>
        <section id="structure" class="section mb-4">
          <h2>3) Folder Structure</h2>
<pre><code>.
├─ app.py
├─ templates/
│   └─ index.html
├─ static/
│   └─ charts/              # generated charts (PNG)
├─ data/
│   ├─ raw/                 # original CSVs (see above)
│   └─ processed/
│       └─ merged_dataset.csv (exported)
├─ screenshot/
│   └─ dashboard_sample.png
└─ README.html (this file)
</code></pre>
        </section>
        <section id="setup" class="section mb-4">
          <h2>4) Setup & Run</h2>
          <ol>
            <li>Install Python 3.10+ and create a virtual environment (recommended).</li>
            <li>Install dependencies:</li>
          </ol>
<pre><code>pip install pandas matplotlib seaborn flask
</code></pre>
          <ol start="3">
            <li>Place CSVs under <code>data/raw/</code>.</li>
            <li>Run the Flask app:</li>
          </ol>
<pre><code>python app.py
# Open http://127.0.0.1:5000
</code></pre>
        </section>
        <section id="algorithm" class="section mb-4">
          <h2>5) Step-by-Step Algorithm</h2>
          <h5 class="mt-3">English (Concise)</h5>
          <ol>
            <li>Project setup & libraries installation.</li>
            <li>Load datasets with <code>pandas.read_csv</code>; store DataFrames in a dictionary.</li>
            <li>Preliminary exploration: shape, columns, NaNs, duplicates, head/tail, <code>.describe()</code>.</li>
            <li>Data cleaning: standardize column names, handle missing values, remove duplicates, fix dtypes.</li>
            <li>Merge: identify common keys (e.g., <code>state</code>, <code>city</code>); merge shootings with census datasets.</li>
            <li>EDA: bar (by state), pie/bar (by race), scatter (poverty/income/education vs shootings).</li>
            <li>Insights & reporting; note limitations (observational only, missing data).</li>
            <li>Dashboard (Flask): tables, charts, journal; optional filters.</li>
            <li>Reflection/Journal: approach, challenges, learning, improvements.</li>
            <li>Deliverables: merged CSV, charts, Flask app, journal.</li>
          </ol>
        <section id="eda" class="section mb-4">
          <h2>6) Visualizations (EDA)</h2>
          <ul>
            <li><strong>Shootings per State</strong> — bar chart (counts).</li>
            <li><strong>Shootings per Race</strong> — pie or bar chart.</li>
            <li><strong>Correlations</strong> — scatter plots:
              <ul>
                <li>Poverty rate vs shootings</li>
                <li>Median income vs shootings</li>
                <li>High school completion vs shootings</li>
              </ul>
            </li>
          </ul>
          <p class="mb-1"><em>Generated PNGs are saved under</em> <code>static/charts/</code>.</p>
<pre><code># Example (matplotlib/seaborn):
# sns.scatterplot(data=df_group, x='poverty_rate', y='shootings'); plt.savefig('static/charts/poverty_vs_shootings.png')
</code></pre>
        </section>
        <section id="insights" class="section mb-4">
          <h2>7) Insights & Limitations</h2>
          <div class="row g-3">
            <div class="col-md-6">
              <div class="callout h-100">
                <h6 class="mb-2">Typical Insights</h6>
                <ul class="mb-0">
                  <li>States with higher counts may align with population size and urbanization.</li>
                  <li>Areas with higher poverty rates often show higher shootings counts.</li>
                  <li>Education and income may show inverse relationships with shootings in some locales.</li>
                </ul>
              </div>
            </div>
            <div class="col-md-6">
              <div class="callout h-100">
                <h6 class="mb-2">Limitations</h6>
                <ul class="mb-0">
                  <li>Observational analysis (no causal inference).</li>
                  <li>Missing/inconsistent city-state keys; potential merge mismatches.</li>
                  <li>Aggregate statistics can hide neighborhood-level variation.</li>
                </ul>
              </div>
            </div>
          </div>
        </section>
        <section id="deliverables" class="section mb-4">
          <h2>8) Deliverables</h2>
          <ul>
            <li><code>data/processed/merged_dataset.csv</code> (exported merged dataset)</li>
            <li>EDA charts under <code>static/charts/</code></li>
            <li>Flask app (<code>app.py</code> + <code>templates/index.html</code>)</li>
            <li>Reflection/journal (in dashboard or a separate doc)</li>
          </ul>
        </section>
        <section id="journal" class="section mb-4">
          <h2>9) Reflection / Journal Prompts</h2>
          <ul>
            <li><strong>Approach:</strong> How did you break down the problem?</li>
            <li><strong>Challenges:</strong> What was hard (e.g., cleaning, merging)?</li>
            <li><strong>Easy parts:</strong> What felt straightforward?</li>
            <li><strong>Learning:</strong> Key insights from the data and process.</li>
            <li><strong>Improvements:</strong> What would you change next time?</li>
          </ul>
          <p class="footer-note mb-0">Tip: Keep your journal concise (200–300 words) and specific—mention exact steps, blockers, and fixes.</p>
        </section>
        <section id="screens" class="section mb-4">
          <h2>10) Screenshots</h2>
          <p>Place screenshots under <code>./screenshot/</code> and reference them in your README or dashboard.</p>
          <div class="row g-3">
            <div class="col-md-6">
              <figure class="m-0">
                <img class="screenshot" src="https://github.com/user-attachments/assets/6373f529-fa91-4f39-aba5-796ed5a01774" alt="Dashboard Sample (placeholder)">
                <figcaption class="mt-2 text-secondary">Dashboard overview (sample)</figcaption>
              </figure>
            </div>
            <div class="col-md-6">
              <figure class="m-0">
                <img class="screenshot" src="https://github.com/user-attachments/assets/5ed31081-8c41-4ee5-8f3b-e361cc12e2e1" alt="Shootings per State (chart placeholder)">
                <figcaption class="mt-2 text-secondary">Shootings per State (chart)</figcaption>
              </figure>
            </div>
          </div>
        </section>
        <section id="attribution" class="section mb-5">
          <h2>11) Attribution & Ethics</h2>
          <div class="callout">
            <p class="mb-2">
              <strong>Data sources:</strong> Fatal police shootings data compiled by <em>The Washington Post</em> (since Jan 1, 2015); socio-economic indicators from US Census datasets. Respect data licenses and terms of use when sharing or publishing results.
            </p>
            <p class="mb-0">
              <strong>Sensitivity & ethics:</strong> This topic is sensitive and politically charged. Analyses here are descriptive and do not imply causation. Interpret with care, consider context, and avoid stigmatizing communities.
            </p>
          </div>
        </section>
        <footer class="footer-note">
          <p class="mb-1">Made with ❤️ using Flask, Pandas, Matplotlib, and Seaborn.</p>
          <p class="mb-0">For questions or improvements, open an issue or add notes to the project journal.</p>
        </footer>
      </div>
    </div>
  </div>
