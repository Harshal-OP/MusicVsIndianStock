import webbrowser as wb  
import csv
import time
import os
import keyboard

#open the csv file
with open('NSEI.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        date = row[0]
        print(date)
        url = 'https://charts.spotify.com/charts/view/regional-in-daily/'+ date
        print('secure')
        wb.open_new(url)
        keyboard.wait('esc')
        
        os.system("taskkill /im firefox.exe /f")
        


