"""
API Data Collector
==================
This script demonstrates collecting data from APIs - a common Data Engineering task.

Data Engineers often:
- Collect data from external APIs
- Handle authentication and rate limits
- Implement retry logic
- Store API responses
- Schedule regular data collection

Author: Data Engineering Example
Date: 2026-01-10
"""

import requests
import pandas as pd
import json
import time
from datetime import datetime
import os


class APIDataCollector:
    """Collect data from public APIs."""
    
    def __init__(self, output_dir="../data/raw"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.collected_data = []
    
    def collect_from_public_api(self):
        """
        Collect data from a public API (example: JSONPlaceholder).
        
        In real scenarios, you might collect from:
        - Social media APIs (Twitter, Facebook)
        - Financial data APIs (Alpha Vantage, Yahoo Finance)
        - Weather APIs (OpenWeatherMap)
        - E-commerce APIs (Shopify, Amazon)
        - Internal company APIs
        """
        print("=" * 60)
        print("COLLECTING DATA FROM API")
        print("=" * 60)
        
        # Example: Collect user data from JSONPlaceholder (free fake API)
        base_url = "https://jsonplaceholder.typicode.com"
        
        try:
            # 1. Collect users
            print("\n1. Collecting user data...")
            response = requests.get(f"{base_url}/users", timeout=10)
            
            if response.status_code == 200:
                users = response.json()
                print(f"   ✓ Collected {len(users)} users")
                
                # Convert to DataFrame
                df_users = pd.DataFrame(users)
                print(f"   ✓ Columns: {list(df_users.columns)}")
                
                # Save raw data
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{self.output_dir}/users_{timestamp}.json"
                with open(filename, 'w') as f:
                    json.dump(users, f, indent=2)
                print(f"   ✓ Saved to: {filename}")
                
                return df_users
            else:
                print(f"   ✗ API request failed with status code: {response.status_code}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"   ✗ Error collecting data: {e}")
            return None
        except Exception as e:
            print(f"   ✗ Unexpected error: {e}")
            return None
    
    def collect_with_pagination(self, endpoint, limit=100):
        """
        Demonstrate collecting data with pagination.
        
        Many APIs return data in pages to limit response size.
        Data Engineers must handle pagination to collect all data.
        """
        print("\n" + "=" * 60)
        print("COLLECTING DATA WITH PAGINATION")
        print("=" * 60)
        
        base_url = "https://jsonplaceholder.typicode.com"
        all_data = []
        
        try:
            print(f"\nCollecting posts (limit: {limit})...")
            
            # Simulate pagination (this API doesn't have true pagination)
            response = requests.get(f"{base_url}/posts", timeout=10)
            
            if response.status_code == 200:
                posts = response.json()[:limit]
                all_data.extend(posts)
                print(f"✓ Collected {len(posts)} posts")
                
                df_posts = pd.DataFrame(posts)
                return df_posts
            else:
                print(f"✗ Failed to collect data")
                return None
                
        except Exception as e:
            print(f"✗ Error: {e}")
            return None
    
    def collect_with_rate_limiting(self, endpoints, delay=1):
        """
        Demonstrate collecting data with rate limiting.
        
        Many APIs have rate limits (e.g., 100 requests per minute).
        Data Engineers must respect these limits to avoid being blocked.
        """
        print("\n" + "=" * 60)
        print("COLLECTING DATA WITH RATE LIMITING")
        print("=" * 60)
        
        base_url = "https://jsonplaceholder.typicode.com"
        results = {}
        
        print(f"\nCollecting from {len(endpoints)} endpoints...")
        print(f"Rate limit: 1 request per {delay} second(s)")
        
        for endpoint in endpoints:
            try:
                print(f"\n  Fetching: {endpoint}...")
                response = requests.get(f"{base_url}/{endpoint}", timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    results[endpoint] = data
                    print(f"  ✓ Collected {len(data)} items from {endpoint}")
                else:
                    print(f"  ✗ Failed: {response.status_code}")
                
                # Wait to respect rate limit
                time.sleep(delay)
                
            except Exception as e:
                print(f"  ✗ Error: {e}")
        
        return results
    
    def transform_and_save(self, df, filename):
        """Transform API data and save to CSV."""
        print("\n" + "=" * 60)
        print("TRANSFORMING AND SAVING DATA")
        print("=" * 60)
        
        if df is None or df.empty:
            print("No data to save")
            return
        
        # Basic transformations
        print("\nApplying transformations...")
        
        # Add metadata
        df['collected_at'] = datetime.now().isoformat()
        df['source'] = 'API'
        
        print(f"✓ Added metadata columns")
        print(f"✓ Final shape: {df.shape}")
        
        # Save to CSV
        filepath = f"{self.output_dir}/{filename}"
        df.to_csv(filepath, index=False)
        print(f"✓ Saved to: {filepath}")
        
        print(f"\nSample of saved data:")
        print(df.head())


def main():
    """Run API data collection example."""
    
    print("\n" + "=" * 60)
    print("API DATA COLLECTION EXAMPLE")
    print("=" * 60)
    print("This demonstrates how Data Engineers collect data from APIs")
    print("=" * 60 + "\n")
    
    # Initialize collector
    collector = APIDataCollector()
    
    # Example 1: Basic API collection
    df_users = collector.collect_from_public_api()
    
    if df_users is not None:
        collector.transform_and_save(df_users, "api_users.csv")
    
    # Example 2: Collection with pagination
    df_posts = collector.collect_with_pagination("posts", limit=20)
    
    if df_posts is not None:
        print(f"\n✓ Successfully collected {len(df_posts)} posts with pagination")
    
    # Example 3: Collection with rate limiting
    endpoints = ["users", "posts", "comments"]
    results = collector.collect_with_rate_limiting(endpoints, delay=0.5)
    
    print("\n" + "=" * 60)
    print("COLLECTION SUMMARY")
    print("=" * 60)
    print(f"Endpoints collected: {len(results)}")
    for endpoint, data in results.items():
        print(f"  {endpoint}: {len(data)} items")
    print("=" * 60 + "\n")
    
    print("📌 Data Engineering Notes:")
    print("=" * 60)
    print("API data collection is a core DE skill:")
    print("\n1. Handle Authentication:")
    print("   - API keys, OAuth tokens")
    print("   - Secure credential management")
    print("\n2. Implement Error Handling:")
    print("   - Retry logic for failed requests")
    print("   - Handle timeouts and network errors")
    print("\n3. Respect Rate Limits:")
    print("   - Implement delays between requests")
    print("   - Use exponential backoff")
    print("\n4. Schedule Regular Collection:")
    print("   - Use Airflow, Cron, or cloud schedulers")
    print("   - Ensure data freshness")
    print("\n5. Monitor Collection:")
    print("   - Track success/failure rates")
    print("   - Alert on failures")
    print("   - Monitor API changes")
    print("\nReal-world API Sources:")
    print("- Twitter API (social media data)")
    print("- Stripe API (payment data)")
    print("- Google Analytics API (web analytics)")
    print("- Weather APIs (weather data)")
    print("- Stock market APIs (financial data)")
    print("=" * 60 + "\n")
    
    print("⚠️  Note: This example uses a public test API.")
    print("In production, you would:")
    print("- Use authentication")
    print("- Store credentials securely (environment variables)")
    print("- Implement comprehensive error handling")
    print("- Add logging and monitoring")
    print("- Schedule automated collection")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
