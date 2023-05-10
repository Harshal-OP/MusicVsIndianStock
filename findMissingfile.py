import csv
import os
import time
count=0
with open('./Music Analysis/NSEI.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        var = "./MusicChart_Valence/"
        date = row[0]
        var = date+"_music_info.csv"
        folder_path = './MusicChart_Valence'
        csv_file_name = var
        # Search for the csv file in the given folder path
        if csv_file_name in os.listdir(folder_path):
            continue

        else:
            count+=1

            print("File Not Found",var)
    print(count)