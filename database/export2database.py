from sqlalchemy import create_engine
from settings import database_engine_url
from settings import csv_source_folder
from settings import lottery_names
import pandas as pd
import os

engine = create_engine(database_engine_url)

for name in lottery_names:
  df = pd.read_csv(os.path.join(csv_source_folder, '%s.csv' % name))
  df.to_sql(name, engine, if_exists='replace')
  print name, df.shape
