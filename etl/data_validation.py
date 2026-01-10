"""
Data Validation Script
=======================
This script demonstrates data quality checks - a key Data Engineering responsibility.

Data Engineers ensure data quality by:
- Validating data types
- Checking for missing values
- Detecting duplicates
- Identifying outliers
- Validating business rules
- Monitoring data quality metrics

Author: Data Engineering Example
Date: 2026-01-10
"""

import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')


class DataValidator:
    """Data quality validation framework."""
    
    def __init__(self, df, dataset_name="Dataset"):
        self.df = df
        self.dataset_name = dataset_name
        self.validation_results = {
            'dataset': dataset_name,
            'timestamp': datetime.now().isoformat(),
            'total_checks': 0,
            'passed_checks': 0,
            'failed_checks': 0,
            'warnings': [],
            'errors': []
        }
    
    def validate_completeness(self):
        """Check for missing values and data completeness."""
        print("=" * 60)
        print("1. COMPLETENESS CHECK")
        print("=" * 60)
        
        missing_counts = self.df.isnull().sum()
        missing_pct = (missing_counts / len(self.df) * 100).round(2)
        
        print(f"Dataset shape: {self.df.shape}")
        print(f"\nMissing values per column:")
        
        for col in self.df.columns:
            count = missing_counts[col]
            pct = missing_pct[col]
            status = "✓ PASS" if pct < 5 else "✗ FAIL"
            print(f"  {col}: {count} ({pct}%) - {status}")
            
            self.validation_results['total_checks'] += 1
            if pct < 5:
                self.validation_results['passed_checks'] += 1
            else:
                self.validation_results['failed_checks'] += 1
                self.validation_results['errors'].append(
                    f"{col} has {pct}% missing values (threshold: 5%)"
                )
        
        print("\n")
    
    def validate_uniqueness(self, key_columns):
        """Check for duplicate records."""
        print("=" * 60)
        print("2. UNIQUENESS CHECK")
        print("=" * 60)
        
        duplicate_count = self.df.duplicated(subset=key_columns).sum()
        duplicate_pct = (duplicate_count / len(self.df) * 100).round(2)
        
        print(f"Key columns: {key_columns}")
        print(f"Duplicate records: {duplicate_count} ({duplicate_pct}%)")
        
        self.validation_results['total_checks'] += 1
        if duplicate_count == 0:
            print("✓ PASS - No duplicates found")
            self.validation_results['passed_checks'] += 1
        else:
            print("✗ FAIL - Duplicates detected")
            self.validation_results['failed_checks'] += 1
            self.validation_results['errors'].append(
                f"{duplicate_count} duplicate records found"
            )
        
        print("\n")
    
    def validate_data_types(self, expected_types):
        """Validate data types match expectations."""
        print("=" * 60)
        print("3. DATA TYPE CHECK")
        print("=" * 60)
        
        print("Expected vs Actual data types:")
        
        for col, expected_type in expected_types.items():
            if col in self.df.columns:
                actual_type = str(self.df[col].dtype)
                match = expected_type in actual_type
                status = "✓ PASS" if match else "✗ FAIL"
                print(f"  {col}: Expected={expected_type}, Actual={actual_type} - {status}")
                
                self.validation_results['total_checks'] += 1
                if match:
                    self.validation_results['passed_checks'] += 1
                else:
                    self.validation_results['failed_checks'] += 1
                    self.validation_results['errors'].append(
                        f"{col} has incorrect type: {actual_type} (expected: {expected_type})"
                    )
        
        print("\n")
    
    def validate_ranges(self, range_rules):
        """Validate numeric columns are within expected ranges."""
        print("=" * 60)
        print("4. RANGE VALIDATION")
        print("=" * 60)
        
        for col, (min_val, max_val) in range_rules.items():
            if col in self.df.columns:
                out_of_range = ((self.df[col] < min_val) | (self.df[col] > max_val)).sum()
                out_of_range_pct = (out_of_range / len(self.df) * 100).round(2)
                status = "✓ PASS" if out_of_range == 0 else "✗ FAIL"
                
                print(f"  {col}: Range=[{min_val}, {max_val}]")
                print(f"    Out of range: {out_of_range} ({out_of_range_pct}%) - {status}")
                
                self.validation_results['total_checks'] += 1
                if out_of_range == 0:
                    self.validation_results['passed_checks'] += 1
                else:
                    self.validation_results['failed_checks'] += 1
                    self.validation_results['warnings'].append(
                        f"{col} has {out_of_range} values outside range [{min_val}, {max_val}]"
                    )
        
        print("\n")
    
    def validate_categorical(self, categorical_rules):
        """Validate categorical columns have expected values."""
        print("=" * 60)
        print("5. CATEGORICAL VALIDATION")
        print("=" * 60)
        
        for col, valid_values in categorical_rules.items():
            if col in self.df.columns:
                invalid = ~self.df[col].isin(valid_values)
                invalid_count = invalid.sum()
                invalid_pct = (invalid_count / len(self.df) * 100).round(2)
                status = "✓ PASS" if invalid_count == 0 else "✗ FAIL"
                
                print(f"  {col}: Valid values={valid_values}")
                print(f"    Invalid values: {invalid_count} ({invalid_pct}%) - {status}")
                
                if invalid_count > 0:
                    print(f"    Unique invalid values: {self.df[invalid][col].unique()}")
                
                self.validation_results['total_checks'] += 1
                if invalid_count == 0:
                    self.validation_results['passed_checks'] += 1
                else:
                    self.validation_results['failed_checks'] += 1
                    self.validation_results['errors'].append(
                        f"{col} has {invalid_count} invalid categorical values"
                    )
        
        print("\n")
    
    def validate_consistency(self):
        """Check for logical consistency in data."""
        print("=" * 60)
        print("6. CONSISTENCY CHECK")
        print("=" * 60)
        
        # Example: check if all numeric columns that should be positive are positive
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols:
            if 'amount' in col.lower() or 'price' in col.lower():
                negative_count = (self.df[col] < 0).sum()
                status = "✓ PASS" if negative_count == 0 else "⚠ WARNING"
                print(f"  {col}: Negative values={negative_count} - {status}")
                
                if negative_count > 0:
                    self.validation_results['warnings'].append(
                        f"{col} has {negative_count} negative values"
                    )
        
        print("\n")
    
    def generate_report(self):
        """Generate validation summary report."""
        print("=" * 60)
        print("VALIDATION SUMMARY")
        print("=" * 60)
        
        total = self.validation_results['total_checks']
        passed = self.validation_results['passed_checks']
        failed = self.validation_results['failed_checks']
        success_rate = (passed / total * 100) if total > 0 else 0
        
        print(f"Dataset: {self.validation_results['dataset']}")
        print(f"Timestamp: {self.validation_results['timestamp']}")
        print(f"\nTotal checks: {total}")
        print(f"Passed: {passed} ({success_rate:.1f}%)")
        print(f"Failed: {failed}")
        print(f"Warnings: {len(self.validation_results['warnings'])}")
        
        if self.validation_results['errors']:
            print(f"\n❌ ERRORS ({len(self.validation_results['errors'])}):")
            for i, error in enumerate(self.validation_results['errors'], 1):
                print(f"  {i}. {error}")
        
        if self.validation_results['warnings']:
            print(f"\n⚠️  WARNINGS ({len(self.validation_results['warnings'])}):")
            for i, warning in enumerate(self.validation_results['warnings'], 1):
                print(f"  {i}. {warning}")
        
        if failed == 0:
            print(f"\n✅ ALL VALIDATIONS PASSED!")
        else:
            print(f"\n⚠️  VALIDATION FAILED - {failed} checks did not pass")
        
        print("=" * 60 + "\n")
        
        return self.validation_results


def main():
    """Run data validation example."""
    
    print("\n" + "=" * 60)
    print("DATA VALIDATION EXAMPLE")
    print("=" * 60 + "\n")
    
    # Create sample data with some quality issues for demonstration
    np.random.seed(42)
    n = 100
    
    # Note: Values intentionally include data quality issues for validation demo
    data = {
        'customer_id': list(range(1, n+1)),
        'age': np.random.randint(15, 90, n).astype(float),  # Range: 15-90 (some < 18 to trigger validation)
        'income': np.random.uniform(-1000, 100000, n),  # Range: -1000 to 100k (negative values to trigger validation)
        'category': np.random.choice(['A', 'B', 'C', 'Invalid'], n),  # Include 'Invalid' to trigger validation
        'score': np.random.uniform(0, 150, n),  # Range: 0-150 (some > 100 to trigger validation)
    }
    
    # Add some missing values (5% of data) at specific indices for demonstration
    for i in [5, 15, 25, 35, 45]:
        data['age'][i] = np.nan
        data['income'][i] = np.nan
    
    # Add a duplicate record for demonstration
    data['customer_id'][95] = data['customer_id'][1]
    
    df = pd.DataFrame(data)
    
    print(f"Sample data created: {df.shape}")
    print(f"\nFirst few rows:")
    print(df.head())
    print("\n")
    
    # Initialize validator
    validator = DataValidator(df, "Customer Data")
    
    # Run validations
    validator.validate_completeness()
    
    validator.validate_uniqueness(['customer_id'])
    
    validator.validate_data_types({
        'customer_id': 'int',
        'age': 'float',
        'income': 'float',
        'category': 'object',
        'score': 'float'
    })
    
    validator.validate_ranges({
        'age': (18, 100),
        'income': (0, 1000000),
        'score': (0, 100)
    })
    
    validator.validate_categorical({
        'category': ['A', 'B', 'C']
    })
    
    validator.validate_consistency()
    
    # Generate report
    results = validator.generate_report()
    
    print("📌 Data Engineering Notes:")
    print("=" * 60)
    print("Data validation is a critical DE responsibility:")
    print("1. Ensure data quality before it reaches Data Scientists")
    print("2. Implement automated quality checks in pipelines")
    print("3. Monitor data quality metrics over time")
    print("4. Alert stakeholders when quality issues occur")
    print("5. Document data quality standards and SLAs")
    print("\nTools for Data Quality:")
    print("- Great Expectations (Python)")
    print("- dbt tests (SQL)")
    print("- Apache Griffin")
    print("- Custom validation frameworks")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
