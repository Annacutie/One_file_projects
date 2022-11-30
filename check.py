import sqlalchemy as db

try:
    engine = db.create_engine(f'postgres://Iwvgrfftisdgpl:b25a1fab15a23692e5028aee968628b1b3888cb3256d215dd67dbc6')
    print('Success')
except:
    print('I fail')