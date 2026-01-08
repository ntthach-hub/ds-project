from sqlalchemy import create_engine, text

def run_transfrom():
    engine = create_engine(
        "postgresql+psycopg2://postgres:%4005012005@localhost:5432/hr_data"
    )

    sql_files = [
        "sql/create_schema.sql",
        "sql/transform_raw_to_staging.sql",
        "sql/analytics.sql"
    ]

    with engine.connect() as conn:
        for file in sql_files:
            print(f"Running {file}")
            with open(file, "r", encoding="utf-8") as f:
                conn.execute(text(f.read()))
            conn.commit()

    print("Pipeline finished")
