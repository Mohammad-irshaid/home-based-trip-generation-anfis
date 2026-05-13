# 🚗 Modeling Home-Based Trip Generation using ANFIS

## Overview

This repository implements **Adaptive Neuro‑Fuzzy Inference System (ANFIS)** models for **home‑based trip generation** – a core component of the four‑step travel demand forecasting process. The work is based on a case study in **Salfit City, Palestine**, using a dataset of 256 households (and 53 additional households for validation). The socio‑economic variables used as inputs include household size, employment, education, vehicle ownership, income, and dwelling type (see Table 1 in the associated paper).

The implementation follows the methodology described in our peer‑reviewed paper:  

> **Irshaid, M., & Abu‑Eisheh, S.** (2023). *Application of Adaptive Neuro-Fuzzy Inference System in Modelling Home-Based Trip Generation*. Ain Shams Engineering Journal (Q1), 14(11), 102523. 
[DOI: 10.1016/j.asej.2023.102523]
> 
> (Available in this repository as `Application of ANFIS in Modelling Home-Based Trip Generation.pdf`)

### Why ANFIS for trip generation?
Traditional **Multiple Linear Regression (MLR)** is widely used for its simplicity, but trip‑making behaviour involves non‑linearities, uncertainty, and interdependencies that MLR cannot fully capture. ANFIS combines the learning capability of neural networks with the interpretability of fuzzy logic, making it particularly suitable for modelling complex, ambiguous systems.

### Key findings from the paper
- **Four model types** were developed: total household trips (HBALL), work trips (HBW), education trips (HBE), and other trips (HBO).
- **ANFIS outperformed MLR** for the more complex models (HBALL and HBO):
  - HBALL: RMSE reduced by **13.0%**, R² increased from 65.8% to **74.2%**.
  - HBO: RMSE reduced by **8.6%**, R² increased from 80.7% to **83.9%**.
- For the simpler models (HBW and HBE), both approaches performed similarly – MLR already achieved R² > 90%.
- The optimal ANFIS architectures used **Gaussian membership functions**, a **hybrid learning algorithm** (least‑squares + backpropagation), and early stopping to avoid overfitting.

### What this repository (paper) contains
- Python implementation of the ANFIS models described in the paper.
- Scripts to replicate the training, validation, and comparison with MLR.
- The dataset (anonymised household travel survey from Salfit City).
- Visualisation for membership functions, training convergence, and error analysis.

This repository serves as a reproducible, open‑source reference for researchers and practitioners exploring hybrid AI in transport modelling.

---

## Abstract

**Keywords:** Home‑based trip generation · Travel demand modelling · Multiple linear regression · Adaptive neuro‑fuzzy inference system

This study investigates the feasibility of using the **Adaptive Neuro‑Fuzzy Inference System (ANFIS)** and **Multiple Linear Regression (MLR)** for modelling home‑based trip generation in Salfit City, Palestine. The research compares the performance of these two methods and provides insights into their efficiency for different trip purposes. The methodology involves developing separate trip generation models for various purposes, including total daily household trips (HBALL), home‑based work (HBW), home‑based education (HBE), and other home‑based trips (HBO). Objective evaluation metrics like **Root Mean Squared Error (RMSE)**, **Mean Absolute Error (MAE)**, and **R‑squared** are used to assess model effectiveness.

Results indicate that ANFIS performs well for modelling HBALL and HBO trips, which exhibit more complex behaviour with wider data ranges and higher average daily trip counts. Compared to MLR, ANFIS shows improved accuracy and closer predictions – for HBALL trips, ANFIS achieved an RMSE of 1.4880 while MLR resulted in 1.7112 (a reduction of 13.04%). However, for HBW and HBE trip purposes, where behaviour is less complicated, MLR appears sufficient. The R‑squared values obtained with MLR are high (e.g., 96.63% for HBE, 90.36% for HBW), and results between the two approaches are closely comparable.

In conclusion, **ANFIS shows promise for modelling systems with complex behaviour**, while MLR remains a suitable option for less complicated scenarios. The study emphasises the importance of exploring different modelling techniques in transportation research to identify the most appropriate approach for specific cases.
