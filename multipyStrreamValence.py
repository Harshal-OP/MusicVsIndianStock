import csv
import pandas as pd
import time 
with open('./NSEI.csv') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        date = row[0]
        if(date=="Date"):
            continue # skip the header
        var = "./MusicChart_Valence/"+date+"_music_info.csv"

        #read each file
        df = pd.read_csv(var,header=None)
        print("done")
        df[''] = df.iloc[:, 8]* df.iloc[:, 9]    
        #Save the new csv file
        new_file=date+"result.csv"
        df.to_csv(new_file) 
