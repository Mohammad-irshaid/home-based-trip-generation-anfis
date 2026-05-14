# 🚗 Modeling Home-Based Trip Generation Modeling Using ANFIS

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Research](https://img.shields.io/badge/Type-Research_Code-orange)
![Journal](https://img.shields.io/badge/Publication-Q1-success)

---

## 📌 Overview

This repository provides a **research-grade implementation** of:

- Multiple Linear Regression (MLR)
- Adaptive Neuro-Fuzzy Inference System (ANFIS)

for modeling **home-based trip generation** as part of the classical **four-step travel demand modeling framework**.

The work reproduces and extends findings from the peer-reviewed publication:

> Irshaid, M., & Abu-Eisheh, S. (2023).  
> *Application of Adaptive Neuro-Fuzzy Inference System in Modelling Home-Based Trip Generation*.  
> Ain Shams Engineering Journal, 14(11), 102523.  
> https://doi.org/10.1016/j.asej.2023.102523

---

## 🎯 Key Idea

Trip generation is traditionally modeled using linear statistical methods. However, real-world travel behavior is:

- nonlinear  
- uncertain  
- influenced by interacting socioeconomic factors  

This repository investigates whether **ANFIS can better capture behavioral complexity** compared to classical regression models.

---

## 🧠 Models Implemented

### 1. Multiple Linear Regression (MLR)
- Ordinary Least Squares (OLS)
- Stepwise feature selection
- Statistical significance testing
- Multicollinearity diagnostics

### 2. Adaptive Neuro-Fuzzy Inference System (ANFIS)
- Takagi–Sugeno fuzzy inference system
- Gaussian membership functions
- Hybrid learning:
  - Least Squares Estimation (forward pass)
  - Gradient Descent (backward pass)

---

## 📊 Study Cases

Four trip production categories are modeled:

| Code | Description |
|------|-------------|
| HBALL | Total household trips |
| HBW   | Home-based work trips |
| HBE   | Home-based education trips |
| HBO   | Home-based other trips |

---

## 🧾 Dataset

- **Location:** Salfit City, Palestine  
- **Source:** Household travel survey  
- **Sample size:**
  - 256 households (training/calibration)
  - 53 households (validation)

### Input Features

Socioeconomic variables include:
- Household size  
- Employment status  
- Education status  
- Vehicle ownership  
- Income level  
- Household structure  

---

## ⚙️ Methodology Pipeline

```
Raw Survey Data
      ↓
Data Cleaning & Preprocessing
      ↓
Feature Engineering
      ↓
Train / Test Split
      ↓
MLR Model Training
ANFIS Model Training
      ↓
Prediction & Evaluation
      ↓
Model Comparison
```

---

## 📈 Performance Summary

| Model | Method | RMSE | R² |
|------|--------|------|------|
| HBALL | MLR   | 1.7112 | 65.85% |
|      | ANFIS | 1.4880 | 74.18% |
| HBW   | MLR   | 0.5932 | 90.36% |
|       | ANFIS | 0.5465 | 92.74% |
| HBE   | MLR   | 0.4035 | 96.63% |
|       | ANFIS | 0.4020 | 96.66% |
| HBO   | MLR   | 1.5778 | 80.65% |
|       | ANFIS | 1.4419 | 83.94% |

---

## 🔍 Key Findings

- ANFIS significantly improves prediction for:
  - HBALL (complex aggregated behavior)
  - HBO (heterogeneous trip purpose)

- MLR performs competitively for:
  - HBW
  - HBE

- Insight:
  > Nonlinear AI models are most beneficial when behavioral complexity increases.

---

## 🧪 Repository Structure

```
home-based-trip-generation-anfis/
│
├── code/                 # Core implementation
│   ├── preprocessing.py
│   ├── mlr_model.py
│   ├── anfis_model.py
│   ├── train_mlr.py
│   ├── train_anfis.py
│   ├── evaluate_models.py
│   └── run_pipeline.py
│
├── data/                 # Dataset + metadata
│   ├── salfit_trip_data.csv
│   └── feature_description.md
│
├── figures/              # Paper figures & diagrams
│
├── notebooks/           # Exploratory & experimental analysis
│
├── results/             # Outputs & evaluation logs
│
├── paper/               # Published article
│
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

```bash
git clone https://github.com/Mohammad-irshaid/home-based-trip-generation-anfis.git
cd home-based-trip-generation-anfis

python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

pip install -r requirements.txt
```

---

## ▶️ Usage

### Run Full Pipeline
```bash
python code/run_pipeline.py
```

### Train Models
```bash
python code/train_mlr.py
python code/train_anfis.py
```

### Evaluate Models
```bash
python code/evaluate_models.py
```

---

## 📌 Reproducibility

To reproduce the published results:

1. Load dataset from `/data`
2. Run preprocessing pipeline
3. Train MLR and ANFIS models
4. Evaluate using RMSE, MAE, R²
5. Compare outputs with paper results

---

## ⚠️ Limitations

- Single-city case study (Salfit)
- Limited sample size
- No cross-city validation
- Static socioeconomic features only

---

## 🔭 Future Work

- Deep learning comparison (DNN, LSTM)
- GIS-based accessibility integration
- Transferability across cities
- Explainable AI (SHAP / LIME)
- Mode choice integration
- Activity-based modeling extension

---

## 📄 Citation

If you use this work, please cite:

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

## 🙏 Acknowledgements

- Department of Civil Engineering, An-Najah National University  
- Field survey participants in Salfit City  
- Transportation planning research community  

---

## 📜 License

This project is licensed under the MIT License.
