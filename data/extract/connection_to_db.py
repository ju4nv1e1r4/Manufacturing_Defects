# %%
# importando bibliotecas e etc
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker
import pandas as pd
from config import DBconfig

# %%
# evento de conexão
username = DBconfig.USERNAME
password = DBconfig.PASSWORD
hostname = DBconfig.HOSTNAME
database = DBconfig.DATABASE

conn = f'postgresql+psycopg2://{username}:{password}@{hostname}/{database}'

# %%
# evento de teste de conexão
engine = create_engine(conn)
try:
    with engine.connect() as connection:
        print('O banco de dados está conectado.')
except Exception as Error:
    print('Algo deu errado com sua conexão.', Error)

# %%
# evento de teste com query e salvando arquivo em csv
try:
    metadata = MetaData()
    tb = 'manufacturing_defects'
    table_name = Table(tb, metadata, autoload_with=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    stmt = select(table_name)
    res = session.execute(stmt)

    
    df = pd.DataFrame(res.fetchall(), columns=res.keys())

    
    csv = 'manufacturing_defects_data.csv'
    df.to_csv(csv, index=False)
    
    session.close()
    print(f'Query executada com sucesso. Dados salvos em {csv}')

except Exception as QueryError:
    print('Query não pode ser executada. Seguem os detalhes do erro:', QueryError)


# %%
session.close()