import csv, pandas, tabloo

def graph(columns,filename):
    csv = f'data/{filename}.csv'
    df = pandas.read_csv(csv, sep=',', names=columns)
    tabloo.show(df)
