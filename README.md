# A/B Testing

This project contains analysis of 2 A/B tests. One of them focuses on fast food marketing campaign and the other one on game design experiment.

## Marketing Campaign A/B Test

A fast-food chain plans to add a new item to its menu and is testing three possible marketing campaigns. The goal is to evaluate A/B testing results and decide which marketing strategy works the best.

### Key Findings:
- Promotions 1 and 3 are statistically better than Promotion 2
- Promotion 1 has the highest overall average sales of 58.10 thousands while Promotion 3 is following with 55.40 thousands.
- While Promotion 1 and 3 are not statistically different according to Tukey's HSD, Mann-Whitney U-test shows a significant difference.
- For market size segmentation:
  - In small markets Promotion 1 performs better by 0.7 thousands than Promotion 3 in sales on averag (though not statistically significant)
  - In medium markets Promotion 1 performs better by 1.8 thousands than Promotion 3 in sales on averag (Statistically significant)
  - In large markets: Promotion 3 performs better by 2 thousands than Promotion 1 in sales on average (though not statistically significant)
- Recommendation: Use Promotion 1 in small and medium markets, and Promotion 3 in large markets. Use either if using different promotions incur high cost

## Game Design A/B Test

This test evaluates whether moving the first in-game gate from level 30 (control) to level 40 (experiment) affects user engagement and retention. Players were randomly assigned to either version upon installation.

### Key Findings:
- Only retention after 7 days showed statistical significance after Benjamini-Hochberg correction
- The direction of the effect was opposite to expected - fewer users came back after 7 days in the experiment group
- No significant difference in retention after 1 day and average game rounds played
- There may be issues with the randomization process as the split between control and experiment groups was not statistically random thus might induce bias. This might be a simptom of sample rate missmatch and I would recommend to check the process in how randomization is done using more data. Although, the p-value of such a split happening is not too low to discredit all of the analysis.
- Recommendation: Stay with the control version (gate at level 30) as the experiment version showed negative impact on 7-day retention.

# Installation
Below is the process to install this project on your local machine. However, there is **game_design.html** and **marketing_campaign.html** files in the root of the project that can be used to view the analysis without installing the project. Just download the files and open them in your browser.

This analysis is structured to be easily continued by another developer, with dependency management handled via the Poetry library. It follows consistent coding standards, enforced using Ruff for linting. To further ease distribution, this project is packaged for ease of use.

Note, I put functions inside notebooks for easier access to logic behind the analysis.

After placing yourself in your desired directory, run this command in your terminal to copy this repo.
```bash
git clone https://github.com/justsvykas/AB_testing_projects
```
Go to project directory.
```bash
cd AB_testing_projects
```
install package
```bash
poetry install
```

# Usage

To run the notebook for analysis:
```bash
cd src/game_design/
# or
cd src/marketing_campaign
```

To run the notebook for game design analysis:
```bash
code main.ipynb
```
Run the notebook cells sequentially or review the precomputed outputs. Notice when running the notebook code will query and store data in data/ directory with.

To run the streamlit dashboard:
```bash
streamlit run src/dashboard.py
```

# Dependencies

- Python 3.12
- poetry

For managing Python versions consider using [pyenv](https://github.com/pyenv/pyenv).
For using poetry take a look at [poetry installation](https://python-poetry.org/docs/#installation).

# Structure

```bash
.
├── .gitignore                    # Specifies files to ignore in Git version control
├── README.md                     # Project documentation
├── pyproject.toml                # Python project configuration (Poetry)
├── ruff.toml                     # Formatter and linter configuration (Ruff)
├── game_design.html              # HTML file for viewing game design analysis without installation
├── marketing_campaign.html       # HTML file for viewing marketing campaign analysis without installation
├── src                           # Source code directory
    ├── dashboard.py              # Streamlit dashboard for marketing campaign visualization
    ├── marketing_campaign/       # Marketing campaign analysis
    │   ├── __init__.py           # Marks directory as a package
    │   ├── main.ipynb            # Main analysis notebook for marketing campaign
    │   └── data/                 # Data directory
    └── game_design/              # Game design analysis
        ├── __init__.py           # Marks directory as a package
        ├── main.ipynb            # Main analysis notebook for game design
        └── data/                 # Data directory
```
