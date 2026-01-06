"""
Titanic Survival Prediction Project
====================================
Predicting passenger survival on the Titanic using machine learning.

Author: Data Science Learner
Date: 2026-01-06
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')


def create_sample_titanic_data():
    """
    Create a sample Titanic dataset for demonstration purposes.
    In a real scenario, you would load this from a CSV file.
    """
    np.random.seed(42)
    
    n_samples = 200
    
    # Generate sample data
    data = {
        'PassengerId': range(1, n_samples + 1),
        'Pclass': np.random.choice([1, 2, 3], n_samples, p=[0.25, 0.25, 0.5]),
        'Sex': np.random.choice(['male', 'female'], n_samples, p=[0.65, 0.35]),
        'Age': np.random.normal(30, 15, n_samples).clip(0.5, 80),
        'SibSp': np.random.choice([0, 1, 2, 3, 4], n_samples, p=[0.6, 0.2, 0.1, 0.07, 0.03]),
        'Parch': np.random.choice([0, 1, 2, 3], n_samples, p=[0.7, 0.15, 0.1, 0.05]),
        'Fare': np.random.gamma(2, 15, n_samples),
        'Embarked': np.random.choice(['S', 'C', 'Q'], n_samples, p=[0.7, 0.2, 0.1])
    }
    
    df = pd.DataFrame(data)
    
    # Create survival based on some rules (simplified)
    survival_prob = 0.5
    survival_prob += (df['Sex'] == 'female') * 0.3
    survival_prob -= (df['Pclass'] == 3) * 0.2
    survival_prob += (df['Age'] < 18) * 0.15
    survival_prob = survival_prob.clip(0.1, 0.9)
    
    df['Survived'] = (np.random.random(n_samples) < survival_prob).astype(int)
    
    # Add some missing values
    missing_age_indices = np.random.choice(n_samples, size=int(n_samples * 0.2), replace=False)
    df.loc[missing_age_indices, 'Age'] = np.nan
    
    return df


def explore_data(df):
    """Perform exploratory data analysis."""
    print("=" * 60)
    print("TITANIC DATASET OVERVIEW")
    print("=" * 60)
    print(f"\nDataset shape: {df.shape}")
    print(f"\nFirst few rows:\n{df.head()}")
    print(f"\nData types:\n{df.dtypes}")
    print(f"\nMissing values:\n{df.isnull().sum()}")
    print(f"\nSurvival rate: {df['Survived'].mean():.2%}")
    print(f"\nSurvival by Sex:\n{df.groupby('Sex')['Survived'].mean()}")
    print(f"\nSurvival by Class:\n{df.groupby('Pclass')['Survived'].mean()}")


def preprocess_data(df):
    """Clean and preprocess the data."""
    print("\n" + "=" * 60)
    print("DATA PREPROCESSING")
    print("=" * 60)
    
    # Create a copy
    df_processed = df.copy()
    
    # Handle missing age values
    df_processed['Age'] = df_processed['Age'].fillna(df_processed['Age'].median())
    
    # Feature engineering: Family size
    df_processed['FamilySize'] = df_processed['SibSp'] + df_processed['Parch'] + 1
    df_processed['IsAlone'] = (df_processed['FamilySize'] == 1).astype(int)
    
    # Encode categorical variables
    le = LabelEncoder()
    df_processed['Sex_encoded'] = le.fit_transform(df_processed['Sex'])
    
    # One-hot encode Embarked
    df_processed = pd.get_dummies(df_processed, columns=['Embarked'], prefix='Embarked')
    
    print("Feature engineering completed:")
    print(f"  - Filled missing Age values with median")
    print(f"  - Created FamilySize feature")
    print(f"  - Created IsAlone feature")
    print(f"  - Encoded Sex variable")
    print(f"  - One-hot encoded Embarked variable")
    
    return df_processed


def prepare_features(df):
    """Prepare features and target for model training."""
    # Select features for modeling
    feature_columns = ['Pclass', 'Sex_encoded', 'Age', 'SibSp', 'Parch', 
                       'Fare', 'FamilySize', 'IsAlone']
    
    # Add Embarked columns if they exist
    embarked_cols = [col for col in df.columns if col.startswith('Embarked_')]
    feature_columns.extend(embarked_cols)
    
    X = df[feature_columns]
    y = df['Survived']
    
    print(f"\nFeatures used for modeling: {feature_columns}")
    print(f"Feature matrix shape: {X.shape}")
    
    return X, y


def train_models(X_train, X_test, y_train, y_test):
    """Train multiple models and compare their performance."""
    
    # Define models
    models = {
        'Logistic Regression': LogisticRegression(max_iter=200, random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, random_state=42),
        'Support Vector Machine': SVC(kernel='rbf', random_state=42)
    }
    
    print("\n" + "=" * 60)
    print("MODEL TRAINING AND EVALUATION")
    print("=" * 60)
    
    results = {}
    
    for name, model in models.items():
        # Train
        model.fit(X_train, y_train)
        
        # Predict
        y_pred = model.predict(X_test)
        
        # Evaluate
        accuracy = accuracy_score(y_test, y_pred)
        cv_scores = cross_val_score(model, X_train, y_train, cv=5)
        
        results[name] = {
            'accuracy': accuracy,
            'cv_mean': cv_scores.mean(),
            'cv_std': cv_scores.std(),
            'model': model,
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
    print(f"\nClassification Report for {best_model_name}:")
    print(classification_report(
        y_test, 
        results[best_model_name]['predictions'],
        target_names=['Not Survived', 'Survived']
    ))
    
    # Confusion matrix
    cm = confusion_matrix(y_test, results[best_model_name]['predictions'])
    print(f"\nConfusion Matrix:")
    print(cm)
    
    return results


def main():
    """Main function to run the entire pipeline."""
    print("\n" + "=" * 60)
    print("TITANIC SURVIVAL PREDICTION PROJECT")
    print("=" * 60)
    
    # Create sample data
    print("\nCreating sample Titanic dataset...")
    df = create_sample_titanic_data()
    
    # Explore data
    explore_data(df)
    
    # Preprocess data
    df_processed = preprocess_data(df)
    
    # Prepare features
    X, y = prepare_features(df_processed)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"\n{'=' * 60}")
    print(f"Training set size: {len(X_train)}")
    print(f"Testing set size: {len(X_test)}")
    print(f"{'=' * 60}")
    
    # Train models
    results = train_models(X_train_scaled, X_test_scaled, y_train, y_test)
    
    print("\n" + "=" * 60)
    print("PROJECT COMPLETED SUCCESSFULLY!")
    print("=" * 60 + "\n")
    
    return results


if __name__ == "__main__":
    main()
