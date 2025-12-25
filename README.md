<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>

<h1>NBA Points Prediction Model</h1>

<p>
    An end-to-end machine learning project that predicts NBA player points per game
    using historical performance data. This repository demonstrates a complete
    analytics workflow: data ingestion, preprocessing, feature engineering,
    model training, and evaluation.
</p>

<div class="highlight">
    <strong>Focus:</strong> Practical data science, clean pipelines, and model interpretability
    using real-world sports data.
</div>

<!-- ===================== -->
<div class="section">
<h2>Project Overview</h2>
<p>
    The goal of this project is to estimate how many points an NBA player will score
    in a given game based on recent performance trends and game-level statistics.
</p>
<ul>
    <li>Collects NBA player game logs using the public NBA statistics API</li>
    <li>Cleans and aggregates multi-season data</li>
    <li>Engineers predictive features from box-score metrics</li>
    <li>Trains and evaluates a regression model</li>
</ul>
<p>
    This project emphasizes clarity, reproducibility, and reasoning over black-box modeling.
</p>
</div>

<!-- ===================== -->
<div class="section">
<h2>Key Features</h2>
<ul>
    <li>Automated NBA data ingestion via <code>nba_api</code></li>
    <li>Feature engineering using historical averages and recent trends</li>
    <li>Linear regression model for interpretability and baseline benchmarking</li>
    <li>Evaluation using Mean Absolute Error (MAE)</li>
    <li>Modular code structure designed for extension</li>
</ul>
</div>

<!-- ===================== -->
<div class="section">
<h2>Tech Stack</h2>
<ul>
    <li><strong>Language:</strong> Python</li>
    <li><strong>Data:</strong> pandas, numpy</li>
    <li><strong>Modeling:</strong> scikit-learn</li>
    <li><strong>Data Source:</strong> Public NBA statistics API</li>
    <li><strong>Version Control:</strong> Git & GitHub</li>
</ul>
</div>

<!-- ===================== -->
<div class="section">
<h2>API Access & Data Considerations</h2>
<p>
    This project uses the public NBA statistics API through the <code>nba_api</code> Python package.
    No authentication or API key is required.
</p>
<ul>
    <li>Requests are unauthenticated and publicly accessible</li>
    <li>Calls are made sequentially to avoid rate limiting</li>
    <li>Fetched data is stored locally to minimize repeated API requests</li>
</ul>
</div>

<!-- ===================== -->
<div class="section">
<h2>Getting Started</h2>

<h3>1. Clone the Repository</h3>
<pre><code>git clone https://github.com/Hani-Mahdi/NBA_Points_Prediction_Model.git
cd NBA_Points_Prediction_Model
</code></pre>

<h3>2. Install Dependencies</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>3. Run the Data Pipeline</h3>
<pre><code>python app/data_ingest.py
python app/preprocess.py
</code></pre>

<h3>4. Train and Evaluate the Model</h3>
<pre><code>python app/train_model.py</code></pre>

<p>
    Model performance metrics are printed to the console and logged for inspection.
</p>
</div>

<!-- ===================== -->
<div class="section">
<h2>Project Structure</h2>
<pre><code>
NBA_Points_Prediction_Model/
├── app/
│   ├── data_ingest.py      # NBA API data collection
│   ├── preprocess.py      # Cleaning & feature engineering
│   ├── train_model.py     # Model training & evaluation
│   └── utils.py           # Shared helper functions
├── data/                  # Cached datasets
├── logs/                  # Model outputs & metrics
├── requirements.txt
└── README.html
</code></pre>
</div>

<!-- ===================== -->
<div class="section">
<h2>Modeling Approach</h2>
<p>
    A linear regression model was selected as a strong baseline due to its:
</p>
<ul>
    <li>Interpretability of feature coefficients</li>
    <li>Low variance and fast training</li>
    <li>Suitability for numeric, continuous targets</li>
</ul>
<p>
    Performance is evaluated using Mean Absolute Error (MAE), which provides an intuitive
    measure of prediction error in points per game.
</p>
</div>

<!-- ===================== -->
<div class="section">
<h2>What I Learned</h2>
<ul>
    <li>Designing data pipelines around real-world APIs</li>
    <li>Feature engineering for sports analytics</li>
    <li>Bias-variance tradeoffs in regression models</li>
    <li>Evaluating model quality beyond raw accuracy</li>
</ul>
</div>

<!-- ===================== -->
<div class="section">
<h2>Future Improvements</h2>
<ul>
    <li>Incorporate advanced models (Random Forests, Gradient Boosting)</li>
    <li>Add opponent-level and defensive matchup features</li>
    <li>Introduce rolling windows and decay-weighted averages</li>
    <li>Build an interactive dashboard (Streamlit or Dash)</li>
</ul>
</div>

<!-- ===================== -->
<div class="section">
<h2>Author</h2>
<p>
    <strong>Hani Mahdi</strong><br>
    Computer Science Student | Sports Analytics & Machine Learning<br>
    GitHub: https://github.com/Hani-Mahdi
</p>
</div>

</body>
</html>
