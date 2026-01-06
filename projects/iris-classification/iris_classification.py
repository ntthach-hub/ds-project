"""
Iris Classification Project
============================
A simple machine learning project using the Iris dataset to demonstrate
various classification algorithms.

Author: Data Science Learner
Date: 2026-01-06
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')


def load_and_explore_data():
    """Load the Iris dataset and perform basic exploration."""
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # Create a DataFrame for better visualization
    df = pd.DataFrame(X, columns=iris.feature_names)
    df['target'] = y
    df['species'] = df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    
    print("=" * 60)
    print("IRIS DATASET OVERVIEW")
    print("=" * 60)
    print(f"\nDataset shape: {df.shape}")
    print(f"\nFeatures: {iris.feature_names}")
    print(f"\nTarget classes: {iris.target_names}")
    print(f"\nFirst few rows:\n{df.head()}")
    print(f"\nDataset statistics:\n{df.describe()}")
    print(f"\nClass distribution:\n{df['species'].value_counts()}")
    
    return X, y, iris.target_names


def prepare_data(X, y):
    """Split data into training and testing sets and scale features."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print("\n" + "=" * 60)
    print("DATA PREPARATION")
    print("=" * 60)
    print(f"Training set size: {len(X_train)}")
    print(f"Testing set size: {len(X_test)}")
    
    return X_train_scaled, X_test_scaled, y_train, y_test


def train_and_evaluate_models(X_train, X_test, y_train, y_test, target_names):
    """Train multiple classification models and evaluate their performance."""
    
    # Define models
    models = {
        'Logistic Regression': LogisticRegression(max_iter=200, random_state=42),
        'K-Nearest Neighbors': KNeighborsClassifier(n_neighbors=5),
        'Decision Tree': DecisionTreeClassifier(random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'Support Vector Machine': SVC(kernel='rbf', random_state=42)
    }
    
    print("\n" + "=" * 60)
    print("MODEL TRAINING AND EVALUATION")
    print("=" * 60)
    
    results = {}
    
    for name, model in models.items():
        # Train the model
        model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = model.predict(X_test)
        
        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)
        
        # Cross-validation score
        cv_scores = cross_val_score(model, X_train, y_train, cv=5)
        
        results[name] = {
            'accuracy': accuracy,
            'cv_mean': cv_scores.mean(),
            'cv_std': cv_scores.std(),
            'predictions': y_pred
        }
        
        print(f"\n{name}:")
        print(f"  Test Accuracy: {accuracy:.4f}")
        print(f"  Cross-validation Accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
    
    # Find best model
    best_model_name = max(results, key=lambda x: results[x]['accuracy'])
    print(f"\n{'=' * 60}")
    print(f"Best Model: {best_model_name}")
    print(f"Accuracy: {results[best_model_name]['accuracy']:.4f}")
    print(f"{'=' * 60}")
    
    # Detailed report for best model
    print(f"\nDetailed Classification Report for {best_model_name}:")
    print(classification_report(
        y_test, 
        results[best_model_name]['predictions'],
        target_names=target_names
    ))
    
    return results


def main():
    """Main function to run the entire pipeline."""
    print("\n" + "=" * 60)
    print("IRIS CLASSIFICATION PROJECT")
    print("=" * 60)
    
    # Load and explore data
    X, y, target_names = load_and_explore_data()
    
    # Prepare data
    X_train, X_test, y_train, y_test = prepare_data(X, y)
    
    # Train and evaluate models
    results = train_and_evaluate_models(X_train, X_test, y_train, y_test, target_names)
    
    print("\n" + "=" * 60)
    print("PROJECT COMPLETED SUCCESSFULLY!")
    print("=" * 60 + "\n")
    
    return results


if __name__ == "__main__":
    main()
