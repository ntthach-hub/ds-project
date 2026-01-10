"""
Simple ETL Pipeline Example
============================
This script demonstrates a basic ETL (Extract, Transform, Load) process.

Data Engineer Role:
- Build automated pipelines like this
- Schedule them to run daily/hourly
- Monitor for failures
- Ensure data quality

Author: Data Engineering Example
Date: 2026-01-10
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os
import json


class SimpleETL:
    """A simple ETL pipeline for processing customer data."""
    
    def __init__(self, source_path, destination_path):
        self.source_path = source_path
        self.destination_path = destination_path
        self.metadata = {
            'pipeline_name': 'Simple ETL',
            'execution_time': None,
            'records_processed': 0,
            'records_loaded': 0,
            'status': 'initialized'
        }
    
    def extract(self):
        """
        Extract: Load data from source
        
        In real scenarios, this could be:
        - Reading from databases
        - Calling APIs
        - Reading from cloud storage (S3, GCS)
        - Streaming from Kafka
        """
        print("=" * 60)
        print("STEP 1: EXTRACT")
        print("=" * 60)
        
        try:
            # For demo, create sample data
            print("Extracting data from source...")
            
            # Simulate customer transaction data
            np.random.seed(42)
            n_records = 1000
            
            data = {
                'customer_id': range(1, n_records + 1),
                'transaction_date': pd.date_range('2024-01-01', periods=n_records, freq='H'),
                'amount': np.random.uniform(10, 500, n_records).round(2),
                'product_category': np.random.choice(['Electronics', 'Clothing', 'Food', 'Books'], n_records),
                'payment_method': np.random.choice(['Credit Card', 'Debit Card', 'Cash', 'PayPal'], n_records),
                'customer_age': np.random.randint(18, 80, n_records),
                'is_member': np.random.choice([True, False], n_records),
                # Add some dirty data
                'email': ['user' + str(i) + '@example.com' if i % 10 != 0 else None 
                         for i in range(n_records)],
                'country': np.random.choice(['US', 'UK', 'CA', 'AU', None], n_records)
            }
            
            df = pd.DataFrame(data)
            
            print(f"✓ Extracted {len(df)} records")
            print(f"✓ Columns: {list(df.columns)}")
            print(f"\nSample of raw data:")
            print(df.head())
            
            self.metadata['records_processed'] = len(df)
            return df
            
        except Exception as e:
            print(f"✗ Error during extraction: {e}")
            self.metadata['status'] = 'failed'
            raise
    
    def transform(self, df):
        """
        Transform: Clean and process the data
        
        Common transformations:
        - Data cleaning (handle nulls, duplicates)
        - Data type conversions
        - Feature engineering
        - Data validation
        - Normalization/standardization
        - Aggregations
        """
        print("\n" + "=" * 60)
        print("STEP 2: TRANSFORM")
        print("=" * 60)
        
        try:
            print("Applying transformations...")
            
            # 1. Handle missing values
            print("\n1. Handling missing values...")
            print(f"   Missing values before: \n{df.isnull().sum()}")
            df['email'] = df['email'].fillna('unknown@example.com')
            df['country'] = df['country'].fillna('Unknown')
            print(f"   ✓ Missing values handled")
            
            # 2. Remove duplicates
            print("\n2. Removing duplicates...")
            initial_count = len(df)
            df = df.drop_duplicates()
            print(f"   ✓ Removed {initial_count - len(df)} duplicates")
            
            # 3. Data type conversions
            print("\n3. Converting data types...")
            df['transaction_date'] = pd.to_datetime(df['transaction_date'])
            df['is_member'] = df['is_member'].astype(int)
            print(f"   ✓ Data types converted")
            
            # 4. Feature engineering
            print("\n4. Engineering new features...")
            df['year'] = df['transaction_date'].dt.year
            df['month'] = df['transaction_date'].dt.month
            df['day_of_week'] = df['transaction_date'].dt.dayofweek
            df['hour'] = df['transaction_date'].dt.hour
            df['amount_category'] = pd.cut(df['amount'], 
                                          bins=[0, 50, 150, 300, 1000],
                                          labels=['Low', 'Medium', 'High', 'Very High'])
            print(f"   ✓ Created 5 new features")
            
            # 5. Data validation
            print("\n5. Validating data...")
            # Remove invalid records
            df = df[df['amount'] > 0]
            df = df[df['customer_age'] >= 18]
            print(f"   ✓ Validation complete, {len(df)} valid records")
            
            # 6. Create summary statistics
            print("\n6. Creating summary statistics...")
            df['total_transactions'] = df.groupby('customer_id')['customer_id'].transform('count')
            df['avg_transaction'] = df.groupby('customer_id')['amount'].transform('mean')
            print(f"   ✓ Summary statistics added")
            
            print(f"\n✓ Transformation complete!")
            print(f"\nSample of transformed data:")
            print(df.head())
            print(f"\nTransformed data shape: {df.shape}")
            
            return df
            
        except Exception as e:
            print(f"✗ Error during transformation: {e}")
            self.metadata['status'] = 'failed'
            raise
    
    def load(self, df):
        """
        Load: Store the processed data
        
        In real scenarios, this could be:
        - Writing to databases (PostgreSQL, MySQL)
        - Writing to data warehouses (Snowflake, BigQuery)
        - Writing to cloud storage (S3, GCS)
        - Writing to data lakes
        """
        print("\n" + "=" * 60)
        print("STEP 3: LOAD")
        print("=" * 60)
        
        try:
            print("Loading data to destination...")
            
            # Create destination directory if it doesn't exist
            os.makedirs(os.path.dirname(self.destination_path), exist_ok=True)
            
            # Save to CSV (in real scenarios, this would be a database)
            df.to_csv(self.destination_path, index=False)
            
            print(f"✓ Loaded {len(df)} records to: {self.destination_path}")
            
            self.metadata['records_loaded'] = len(df)
            self.metadata['status'] = 'success'
            
            # Save metadata
            metadata_path = self.destination_path.replace('.csv', '_metadata.json')
            self.metadata['execution_time'] = datetime.now().isoformat()
            with open(metadata_path, 'w') as f:
                json.dump(self.metadata, f, indent=2)
            print(f"✓ Metadata saved to: {metadata_path}")
            
            return True
            
        except Exception as e:
            print(f"✗ Error during loading: {e}")
            self.metadata['status'] = 'failed'
            raise
    
    def run(self):
        """Execute the complete ETL pipeline."""
        print("\n" + "=" * 60)
        print("STARTING ETL PIPELINE")
        print("=" * 60)
        print(f"Source: {self.source_path}")
        print(f"Destination: {self.destination_path}")
        print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        start_time = datetime.now()
        
        try:
            # Extract
            df = self.extract()
            
            # Transform
            df = self.transform(df)
            
            # Load
            self.load(df)
            
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            
            print("\n" + "=" * 60)
            print("ETL PIPELINE COMPLETED SUCCESSFULLY")
            print("=" * 60)
            print(f"Duration: {duration:.2f} seconds")
            print(f"Records processed: {self.metadata['records_processed']}")
            print(f"Records loaded: {self.metadata['records_loaded']}")
            print(f"Status: {self.metadata['status']}")
            print("=" * 60 + "\n")
            
        except Exception as e:
            print("\n" + "=" * 60)
            print("ETL PIPELINE FAILED")
            print("=" * 60)
            print(f"Error: {e}")
            print("=" * 60 + "\n")
            raise


def main():
    """Main function to run the ETL pipeline."""
    
    # Set paths
    source_path = "source_data"  # In real scenarios, this could be a database connection
    destination_path = "../data/processed/customer_transactions_clean.csv"
    
    # Initialize and run ETL
    etl = SimpleETL(source_path, destination_path)
    etl.run()
    
    print("\n📌 Data Engineering Notes:")
    print("=" * 60)
    print("This ETL pipeline demonstrates core DE responsibilities:")
    print("1. Extracting data from sources")
    print("2. Transforming/cleaning data")
    print("3. Loading data to destinations")
    print("4. Logging and monitoring")
    print("5. Error handling")
    print("\nIn production, Data Engineers would:")
    print("- Schedule this with Airflow/Cron")
    print("- Add more robust error handling")
    print("- Implement data quality checks")
    print("- Add alerting for failures")
    print("- Optimize for large datasets")
    print("- Add data versioning")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
