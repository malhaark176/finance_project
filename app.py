from logging import exception
from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route("/")
def index():
        return render_template("index.html")

@app.route("/ticker", methods = ["GET","POST"])
def ticker():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method=="POST":
        try:    
            quote = request.form.get("ticker")
            stock = yf.Ticker(quote)
            data = stock.history(period="6mo")
            if 'Empty DataFrame' in str(data):
                raise Exception
        except:
            return render_template("apology.html")
        table = pd.DataFrame(data)
        table["MA10"] = table["Close"].rolling(10).mean()
        table["MA50"] = table["Close"].rolling(50).mean()
        table = table.dropna() 
        table["Buy"]=[1 if table.loc[ei,"MA10"]>table.loc[ei,"MA50"] else 0 for ei in table.index]
        table["Close1"]=table["Close"].shift(-1)
        table["Profit"]=[table.loc[ei,"Close1"]- table.loc[ei,"Close"] if table.loc[ei,"Buy"]==1 else 0 for ei in table.index]
        table['Profit'] = table['Profit'].astype(float)
        table['Wealth']=np.cumsum(table['Profit'])
        amount = table.loc[table.index[-2],"Wealth"]
        table = table.reset_index()
        return render_template("answer.html", quote=quote, img_data=plot(quote,table),img_data_2=plot(quote,table), amount=amount)
            

def plot(quote, table):
    plt.figure(figsize=(10,4))
    plt.subplot(1, 2, 1)
    plt.plot(table["Date"], table["Profit"])
    plt.xlabel('Date')
    plt.ylabel('Profit ($)')
    plt.axhline(y=0,color="red")
    plt.gcf().autofmt_xdate()
    plt.xticks(rotation=45)
    plt.title("Profit")
    plt.subplot(1, 2, 2)
    plt.plot(table["Date"], table["Wealth"])
    plt.xlabel('Date')
    plt.ylabel('Wealth ($)')
    plt.axhline(y=0,color="red")
    plt.gcf().autofmt_xdate()
    plt.xticks(rotation=45)
    plt.title("Wealth")
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_data = base64.b64encode(buf.getvalue()).decode('utf-8')
    return img_data





   












        
 

    

        
