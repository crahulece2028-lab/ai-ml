# Week 1 — Foundation Phase: Python, Mathematics & Machine Learning Foundations

Complete solutions for the Week‑1 assignments of the **Skill Set Go EduTech — AI/ML** roadmap,
organized **task-wise** under `week1/`.

```
week1/
├── README.md
├── task1_1_python_fundamentals/     → 1.1 Python Fundamentals Assignment
├── task1_2_data_cleaning_eda/       → 1.2 Data Cleaning & EDA
├── task1_3_math_for_ml/             → 1.3 Math for ML Practice Set
└── task1_4_ml_models/               → 1.4 Two ML Models with Scikit-learn
```

| Task | Topic | Level | Location | Status |
|------|-------|-------|----------|--------|
| 1.1 | Python Fundamentals | Beginner | `task1_1_python_fundamentals/` — 8 solved exercise scripts + test runner | Done |
| 1.2 | Data Cleaning & EDA | Beginner | `task1_2_data_cleaning_eda/titanic_eda.ipynb` + cleaned CSV | Done |
| 1.3 | Math for ML Practice Set | Beginner | `task1_3_math_for_ml/math_for_ml_solutions.ipynb` | Done |
| 1.4 | Two ML Models with Scikit-learn | Intermediate | `task1_4_ml_models/scikit_learn_models.ipynb` | Done |

## 1.1 Python Fundamentals — `task1_1_python_fundamentals/`

Exercises covering variables, loops, functions, OOP, lists, dictionaries, file handling
and exceptions. Every script prints its result and asserts expected answers.

```bash
cd task1_1_python_fundamentals
python run_all.py                            # runs all 8 exercise files
python 01_variables_basics.py                # run a single one
```

## 1.2 Data Cleaning & EDA — `task1_2_data_cleaning_eda/`

Real-world dataset: **Titanic passenger manifest** (`data/raw/titanic.csv`).
The notebook cleans the data (groupwise Age imputation, Cabin→flag, mode/median fills,
duplicate and type checks) and explores it with NumPy, pandas and Matplotlib.

```bash
cd task1_2_data_cleaning_eda
jupyter notebook titanic_eda.ipynb           # or open in any Jupyter UI
```

Output: `data/processed/titanic_clean.csv` (891 rows, 0 missing values).

## 1.3 Math for ML — `task1_3_math_for_ml/`

Worked problems in **statistics, probability, linear algebra, and calculus** as they
appear in ML — each solved by hand (markdown) and verified numerically with NumPy/SciPy:
z-scores, normal tails, Bayes' theorem, expected value, dot products, matrix inverses,
eigenvalues (PCA intuition), gradients and gradient-descent updates.

## 1.4 Two ML Models — `task1_4_ml_models/`

Both tasks share the same pipeline: **load → preprocess → train/test split → train → evaluate**.

- **Regression** — California housing: `LinearRegression` vs `RandomForestRegressor`,
  metrics MAE / RMSE / R², residual analysis. (Final: MAE 0.533 / 0.327, RMSE 0.746 / 0.504, R² 0.576 / 0.806)
- **Classification** — Wisconsin breast cancer: `LogisticRegression` vs
  `RandomForestClassifier`, metrics accuracy / precision / recall / F1 / ROC-AUC /
  confusion matrix. (Final: acc 0.986 / 0.958, F1 0.989 / 0.967, ROC-AUC 0.998 / 0.995)

The final section of the notebook is the **evaluation report** comparing both models
across the two tasks. The California housing dataset downloads once from scikit-learn
and is cached locally afterwards.

## Environment

- Python 3.14, NumPy 2.5, pandas 3.0, matplotlib 3.11, scikit-learn 1.9, SciPy 1.18
- Reproduce with: `pip install numpy pandas matplotlib scikit-learn scipy ipykernel`
- All notebooks are executed (outputs embedded); re-run them to confirm from scratch.