# utils/imports.py

import importlib
import subprocess
import sys

# ===============================
# TỰ ĐỘNG CÀI THƯ VIỆN (nếu thiếu)
# ===============================
def install_if_missing(package_name, import_name=None):
    try:
        importlib.import_module(import_name or package_name)
    except ImportError:
        print(f"🔧 Installing missing package: {package_name} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
    else:
        pass  # Nếu đã có thì không cần in nữa

required_packages = [
    ("numpy",),
    ("pandas",),
    ("matplotlib",),
    ("scikit-learn", "sklearn"),
    ("xgboost",),
    ("pgmpy",),
    ("tensorflow",),
]

for pkg in required_packages:
    install_if_missing(*pkg)

# ===============================
# Sau khi đảm bảo thư viện đã cài
# Mới tiến hành import
# ===============================

# Built-in
import pickle
import random

# Data Handling & Visualization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import (
    precision_score, recall_score, f1_score, accuracy_score,
    roc_curve, auc, precision_recall_curve
)
from sklearn.utils.class_weight import compute_class_weight

# XGBoost
import xgboost as xgb

# Bayesian Networks (pgmpy)
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import BayesianEstimator, MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

# Deep Learning (TensorFlow / Keras)
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.metrics import Precision
