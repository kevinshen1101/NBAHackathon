import pandas as pd

def process_file(file_name):
    with open(file_name) as f:
        file_data = f.read()
    df = file_data.splitlines()
    columns = df.pop(0).split('\t')
    columns = [i.replace('"', ' ').strip() for i in columns]
    data = [i.split('\t') for i in df]
    for i in range(len(data)):
        data[i] = [j.replace('"', ' ').strip() for j in data[i]]
    return pd.DataFrame(data, columns=columns)

if __name__ == "__main__":
    event_cache = process_file("event_codes.txt")
    game_sample = process_file("game_sample.txt")
    play_by_play = process_file("play_by_play.txt")
    print(play_by_play)

