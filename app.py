# fsdg/app.py
import json
import pandas as pd
import random
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'

@app.route('/oneday')
def one_day():
    df_source = pd.read_csv('./one_day_solar.csv', sep=',')
    df = pd.DataFrame(columns=['ts','prod'])
    for h in range(24):
        for m in ['00','15','30','45']:
            s_time = format_time(h,m)
            if s_time in df_source.ts.tolist():
                source_val = df_source.loc[df_source.ts==s_time, 'prod'].tolist()[0]
            else:
                source_val = 0
            df = pd.concat([df, pd.DataFrame([{'ts':s_time,'prod':fake_prod(source_val)}])])
    return(df.to_json(orient='records'))

@app.route('/prod/<time>')
def prod(time=None):
    source_val = 0
    if time:
        df_source = pd.read_csv('./one_day_solar.csv', sep=',')
        if time in df_source.ts.tolist():
            source_val = fake_prod(df_source.loc[df_source.ts==time, 'prod'].tolist()[0])
    return "{{'ts':'{}','prod':{}}}".format(time, source_val)

def fake_prod(val):
    r = random.randrange(100)
    noise = random.randrange(-3,4)
    if r < 5: #5% of missing values
        return None
    elif r > 96: #3% of incoherent values
        return val * noise
    else:
        return val * (1 + noise / 100)



def format_time(h,m):
    if h<10:
        return '0'+str(h)+':'+m
    return str(h)+':'+m

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')