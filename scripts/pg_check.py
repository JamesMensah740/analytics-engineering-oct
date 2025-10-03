# save as scripts/pg_check.py
import os
from sqlalchemy import create_engine, text

# optionally put secrets in .env: PGHOST, PGUSER, PGPASSWORD, PGDATABASE, PGPORT
PGHOST=os.getenv("PGHOST","localhost")
PGUSER=os.getenv("PGUSER","postgres")
PGPASSWORD=os.getenv("PGPASSWORD","james")
PGDATABASE=os.getenv("PGDATABASE","analytics")
PGPORT=os.getenv("PGPORT","5432")

engine = create_engine(f"postgresql+psycopg2://{PGUSER}:{PGPASSWORD}@{PGHOST}:{PGPORT}/{PGDATABASE}")
with engine.connect() as conn:
    print(conn.execute(text("SELECT 'connected_to_postgres'")).scalar())
