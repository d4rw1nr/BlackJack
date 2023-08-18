import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import numpy as np

load_dotenv()

DATABASE = os.getenv('DB_NAME')
USER = os.getenv("DB_USER")
PASSWORD = os.getenv('DB_PASSWORD')
HOST = os.getenv('DB_HOST')
PORT = os.getenv('DB_PORT')

engine = create_engine(f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')

df = pd.read_sql_query("SELECT * FROM main.games;", engine)

print(df.head())

final_balance = np.array(df[['final_balance']])
mean_profit = final_balance.mean()
print(mean_profit)