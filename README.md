![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Research](https://img.shields.io/badge/Type-Research_Project-orange)
![Journal](https://img.shields.io/badge/Journal-Q1-success)

# 🚗 Modeling Home-Based Trip Generation Using ANFIS

A research-oriented implementation of the Adaptive Neuro-Fuzzy Inference System (ANFIS) for modeling home-based trip generation - a core component of the four‑step travel demand forecasting process. This repository reproduces and extends the methodology presented in our peer‑reviewed paper: 

> **Irshaid, M., & Abu‑Eisheh, S.** (2023). *Application of Adaptive Neuro-Fuzzy Inference System in Modelling Home-Based Trip Generation*. Ain Shams Engineering Journal (Q1), 14(11), 102523. 
[DOI: 10.1016/j.asej.2023.102523]

## Abstract

**Keywords:** Home‑based trip generation · Travel demand modelling · Multiple linear regression · Adaptive neuro‑fuzzy inference system

This study investigates the feasibility of using the **Adaptive Neuro‑Fuzzy Inference System (ANFIS)** and **Multiple Linear Regression (MLR)** for modelling home‑based trip generation in Salfit City, Palestine. The research compares the performance of these two methods and provides insights into their efficiency for different trip purposes. The methodology involves developing separate trip generation models for various purposes, including total daily household trips (HBALL), home‑based work (HBW), home‑based education (HBE), and other home‑based trips (HBO). Objective evaluation metrics like **Root Mean Squared Error (RMSE)**, **Mean Absolute Error (MAE)**, and **R‑squared** are used to assess model effectiveness.

Results indicate that ANFIS performs well for modelling HBALL and HBO trips, which exhibit more complex behaviour with wider data ranges and higher average daily trip counts. Compared to MLR, ANFIS shows improved accuracy and closer predictions – for HBALL trips, ANFIS achieved an RMSE of 1.4880 while MLR resulted in 1.7112 (a reduction of 13.04%). However, for HBW and HBE trip purposes, where behaviour is less complicated, MLR appears sufficient. The R‑squared values obtained with MLR are high (e.g., 96.63% for HBE, 90.36% for HBW), and results between the two approaches are closely comparable.

In conclusion, **ANFIS shows promise for modelling systems with complex behaviour**, while MLR remains a suitable option for less complicated scenarios. The study emphasises the importance of exploring different modelling techniques in transportation research to identify the most appropriate approach for specific cases.

---


## Overview
This repository presents the implementation of Multiple Linear Regression (MLR) and Adaptive Neuro-Fuzzy Inference System (ANFIS) models for estimating home-based trip generation in Salfit City, Palestine. The study evaluates the capability of ANFIS to model complex nonlinear travel behavior compared with conventional regression approaches commonly used in the four-step travel demand forecasting process.

## Research Motivation

Trip generation is the first step in the traditional four-step transportation planning framework and plays a critical role in travel demand forecasting.

Conventional Multiple Linear Regression (MLR) models are widely used due to their simplicity and interpretability. However, travel behavior often involves:
- nonlinear relationships
- uncertainty
- vague decision-making patterns
- interdependent socioeconomic factors

These characteristics can limit the predictive performance of traditional regression approaches.

ANFIS combines:
- Artificial Neural Networks (ANN)
- Fuzzy Inference Systems (FIS)

into a hybrid framework capable of learning complex nonlinear relationships while handling uncertainty and imprecise data.

This research investigates whether ANFIS can improve the modeling accuracy of home-based trip generation compared with traditional regression methods.

## Methodology

The study follows the workflow below:

```text
Household Survey Data
        ↓
Data Preprocessing
        ↓
Feature Selection
        ↓
Train/Test Split
        ↓
MLR Model Development
ANFIS Model Development
        ↓
Model Training & Optimization
        ↓
Performance Evaluation
(RMSE, MAE, R²)
        ↓
Model Comparison & Validation
```

**ANFIS Methodology**
The implemented ANFIS architecture is a **first‑order Sugeno fuzzy model** with the following layers:

1. **Fuzzification** – Gaussian membership functions for each input.
2. **Rule firing strength** – Product t‑norm.
3. **Normalisation** – Normalised firing strengths.
4. **Defuzzification** – Linear output functions (consequents).
5. **Overall output** – Weighted sum of rule outputs.

Training uses a **hybrid learning algorithm**:
- **Forward pass:** Least‑squares estimate (LSE) for consequent parameters.
- **Backward pass:** Gradient descent (backpropagation) for premise (membership) parameters.


## Modeling Approaches

### Multiple Linear Regression (MLR)

The regression models were developed using:
- backward stepwise regression
- ordinary least squares estimation
- statistical significance testing
- multicollinearity diagnostics

### Adaptive Neuro-Fuzzy Inference System (ANFIS)

The ANFIS models use:
- Takagi–Sugeno fuzzy inference system
- Gaussian membership functions
- hybrid learning algorithm
- gradient descent + least squares optimization

The models were trained and validated using separate datasets to avoid overfitting.

## Key findings from the paper
- **Four model types** were developed: total household trips (HBALL), work trips (HBW), education trips (HBE), and other trips (HBO).
- **ANFIS outperformed MLR** for the more complex models (HBALL and HBO):
  - HBALL: RMSE reduced by **13.0%**, R² increased from 65.8% to **74.2%**.
  - HBO: RMSE reduced by **8.6%**, R² increased from 80.7% to **83.9%**.
- For the simpler models (HBW and HBE), both approaches performed similarly – MLR already achieved R² > 90%.
- The optimal ANFIS architectures used **Gaussian membership functions**, a **hybrid learning algorithm** (least‑squares + backpropagation), and early stopping to avoid overfitting.


## Repository Structure

```text
home-based-trip-generation-anfis/
│
├── code/
│   ├── preprocessing.py
│   ├── metrics.py
│   ├── mlr_model.py
│   ├── anfis_model.py
│   ├── train_mlr.py
│   ├── train_anfis.py
│   ├── evaluate_models.py
│   └── run_pipeline.py
│
├── data/
│   ├── features_target_description.md
│   └── salfit_trip_data.csv
│
├── figures/
│   ├── anfis_developing_training_flowchart.png
│   ├── equivalent_anfis_architecture.png
│   ├── equivalent_anfis_architecture_HBALL.png
│   └── initial_final_input_mfs_HBALL.png
│
├── notebooks/
│   ├── HBALL_Model.ipynb
│   ├── HBW_Model.ipynb
│   ├── HBE_Model.ipynb
│   └── HBO_Model.ipynb
│
├── paper/
│   └── Application of adaptive neuro-fuzzy inference system in modelling home-based trip generation.pdf
│
├── results/
│   ├── anfis_result.md
│   ├── mlr_results.md
│   ├── model_comparison.md
│   └── models_validation.md
│
├── LICENSE
├── README.md
└── requirements.txt
```

---
  
## Reproducing Results

1. Install dependencies
2. Load data and run preprocessing
3. Train MLR model
4. Train ANFIS model
5. Compare metrics


## Citation

If you use this repository in your research, please cite:

```bibtex
@article{irshaid2023anfis,
  title={Application of adaptive neuro-fuzzy inference system in modelling home-based trip generation},
  author={Irshaid, Mohammad and Abu-Eisheh, Sameer},
  journal={Ain Shams Engineering Journal},
  volume={14},
  pages={102523},
  year={2023},
  publisher={Elsevier}
}
```

---

## Future Work

Potential extensions of this research include:

- comparison with deep learning approaches
- integration with GIS-based accessibility measures
- activity-based travel demand modeling
- transferability analysis across cities
- explainable AI techniques for transportation models
- SHAP-based feature importance analysis
- integration with mode choice models
- development of web-based prediction tools

---

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

### Acknowledgements

The authors acknowledge the contribution of the household survey participants and transportation planning researchers whose work supported this study.
