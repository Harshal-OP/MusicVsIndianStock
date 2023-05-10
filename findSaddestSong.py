import csv
import pandas as pd

max=0
min=1

with open('./NSEI.csv') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        date = row[0]
        if(date=="Date"):
            continue # skip the header
        var = "./MusicChart_Valence/"+date+"_music_info.csv"
        
        df=pd.read_csv(var)
        p=df.iloc[:,9].max()
        q=df.iloc[:,9].min()
        
        if(p>max):
            max=p
            final_date_max=date
        if(q<min):
            min=q
            final_date_min=date

print(max,final_date_max,min,final_date_min)
