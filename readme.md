# Project Portfolio Prioritization

## Overview

Organizations often need to prioritize projects when financial, human, and operational resources are limited.

This project develops a data-driven decision-support framework for project portfolio prioritization using multicriteria decision analysis and stochastic simulation.

The analysis applies three complementary approaches:

- Analytic Hierarchy Process (AHP)
- AHP-Gaussian
- Monte Carlo simulation

The methods are used to evaluate project priorities, incorporate criterion variability, and assess the uncertainty associated with project scores.

## Objective

The objective of this project is to develop and evaluate a structured approach for prioritizing projects based on multiple evaluation criteria.

The analysis aims to:

- Define the relative importance of project evaluation criteria.
- Rank projects using AHP.
- Incorporate criterion variability through a Gaussian adjustment to the AHP weights.
- Use Monte Carlo simulation to evaluate score uncertainty.
- Compare the rankings produced by the different approaches.
- Identify projects that remain highly ranked across deterministic and simulation-based analyses.

## Dataset

The project uses a dataset containing 4,000 software projects and 51 variables.

Six criteria are selected for the prioritization analysis:

| Criterion | Objective |
|---|---|
| Project Budget | Minimize |
| Estimated Timeline | Minimize |
| Complexity Score | Minimize |
| Previous Delivery Success Rate | Maximize |
| Resource Availability | Maximize |
| Historical Risk Incidents | Minimize |

The dataset is used as the basis for the exploratory analysis, AHP prioritization, Monte Carlo simulation, and AHP-Gaussian analysis.

## Methodology

### 1. Exploratory Data Analysis

The dataset is first analyzed to understand its structure, data quality, distributions, and relationships between the selected evaluation criteria.

The analysis includes:

- Dataset structure and data types
- Missing-value analysis
- Duplicate analysis
- Descriptive statistics
- Criterion distributions
- Correlation analysis

### 2. Analytic Hierarchy Process (AHP)

AHP is used to determine the relative importance of the evaluation criteria through pairwise comparisons.

The resulting criteria weights are then applied to the normalized project data to calculate an overall AHP score for each project.

The consistency of the pairwise comparison matrix is also evaluated using the Consistency Ratio.

### 3. Monte Carlo Simulation

Monte Carlo simulation is used to evaluate the uncertainty associated with project scores.

For each project, criterion values are simulated using an empirical uncertainty model based on the observed variability of the portfolio.

The simulation generates a distribution of possible scores for each project, allowing the analysis to estimate:

- Mean score
- Standard deviation
- Minimum and maximum simulated scores
- 5th percentile
- Median
- 95th percentile

The simulation results are then compared with the deterministic AHP ranking.

### 4. AHP-Gaussian

The AHP-Gaussian analysis extends the conventional AHP weighting process by incorporating the relative variability of each criterion through a Gaussian adjustment.

The adjusted weights combine:

- The relative importance defined by AHP
- The coefficient of variation of each criterion

The resulting weights are applied to the normalized decision matrix to generate an AHP-Gaussian ranking.

The AHP-Gaussian results are compared with both the conventional AHP and Monte Carlo rankings.

## Results

The analyses show a high degree of consistency between the different prioritization approaches.

The Monte Carlo ranking presents a Spearman correlation of approximately 0.996 with the conventional AHP ranking.

The AHP and Monte Carlo rankings also show a high similarity in their overall score patterns, while the Top-20 comparison identifies projects whose prioritization is more sensitive to the treatment of uncertainty.

The AHP-Gaussian analysis provides an additional perspective by incorporating criterion variability directly into the weighting process.

The project therefore demonstrates how deterministic multicriteria analysis and stochastic simulation can be used together to provide complementary information for project portfolio prioritization.

## Technologies
- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## How to Run
Clone the repository and navigate to the project directory.
Install the required dependencies:
pip install -r requirements.txt
Run the notebooks in the following order:
1. 01_data_ingestion.ipynb
2. 02_exploratory_data_analysis.ipynb
3. 03_ahp.ipynb
4. 04_monte_carlo_simulation.ipynb
5. 05_ahp_gaussian.ipynb
The notebooks generate processed datasets that are stored in the data/processed/ directory and reused by subsequent analyses.

## Limitations
The results should be interpreted as decision-support information rather than as an automatic project selection mechanism.
The Monte Carlo uncertainty model is based on assumptions derived from the observed portfolio variability and therefore does not represent a direct forecast of future project outcomes.
The AHP-Gaussian implementation used in this project represents the specific Gaussian adjustment adopted for this analysis. Alternative formulations of AHP-Gaussian may use different approaches to incorporate variability into the weighting process.
Additional business constraints, strategic priorities, resource limitations, dependencies, and managerial judgment should be considered before making final portfolio decisions.

## Roadmap
- Project structure
- Documentation
- Data ingestion
- Exploratory Data Analysis
- Data preprocessing
- AHP implementation
- Monte Carlo simulation
- AHP-Gaussian analysis
- Ranking comparison
- Uncertainty analysis
- Processed results
- Refactor reusable AHP implementation into src/
- Add automated tests
- Add final project visualizations

## Project Structure

```text
project-portfolio-prioritization/
│
├── data/
│   ├── raw/
│   │   └── projects.csv
│   └── processed/
│       ├── ahp_ranking.csv
│       ├── monte_carlo_ranking.csv
│       ├── ahp_monte_carlo_comparison.csv
│       ├── ahp_gaussian_ranking.csv
│       ├── ahp_gaussian_weights.csv
│       └── ahp_gaussian_monte_carlo_comparison.csv
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   ├── 03_ahp.ipynb
│   ├── 04_monte_carlo_simulation.ipynb
│   └── 05_ahp_gaussian.ipynb
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   └── ahp.py
│
├── main.py
├── requirements.txt
└── README.md