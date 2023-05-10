import csv
import requests

# valid access token get it from spotify
access_token="-"
# open the CSV file
with open('NSEI.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        var = "./MusicChart/regional-in-daily-"
        date = row[0]
        var = var+date+".csv"
        if(date=="Date"):
            continue
        with open(var, 'r') as csv_file:
            print("secure")
            sub_reader = csv.reader(csv_file)
            # loop over each row in the file
            for row in sub_reader:
                # get the track id
                track_id = row[1]
                track_id=track_id[14:]
                print(track_id)
                # make a request to check if the audio features have been calculated
                url = f"https://api.spotify.com/v1/audio-features/{track_id}"
                headers = {"Authorization": f"Bearer {access_token}"}
                response = requests.get(url, headers=headers)
                # check if the response contains the 'valence' key
                if 'valence' in response.json():
                    # make an API request to get the track audio features
                    data = response.json()
                    # get the valence and liveness values
                    valence = data['valence']
                    print(valence)
                    # add the valence and liveness values to the row
                    row.append(valence)
                    output_file_name=date+"_music_info.csv"
                    with open(output_file_name, 'a') as out_file:
                        writer = csv.writer(out_file)
                        writer.writerow(row)
