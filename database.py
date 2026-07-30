from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://neondb_owner:npg_d6pzvl2QXqwR@ep-autumn-glitter-zaccgyu0-pooler.c-2.eu-west-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)

with engine.connect() as connection:
    print("Connected successfully!")