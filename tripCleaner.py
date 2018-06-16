import pandas as pd

def clean():
    # Name of the CSV file
    file = 'tripHistories/JC-201701-citibike-tripdata.csv'
    folder = 'tripHistories/'

    dates = ['201701', '201702','201703','201704','201705','201706','201707','201708','201709','201710','201711','201712']

    dataFrames = []

    #make the column names consistent and remove null rows
    for x in dates:
        file_name = 'JC-' + x + '-citibike-tripdata.csv'
        #read in the csv file
        df = pd.read_csv(folder + file_name, encoding = "ISO-8859-1")
        #make column names consistent
        df = df.rename(columns={"tripduration":"Trip Duration", "starttime":"Start Time", "stoptime":"Stop Time", "start station id":"Start Station ID", "start station name":"Start Station Name", "start station latitude":"Start Station Latitude", "start station longitude":"Start Station Longitude", "end station id":"End Station ID", "end station name":"End Station Name", "end station latitude":"End Station Latitude", "end station longitude":"End Station Longitude", "bikeid":"Bike ID", "usertype":"User Type", "birth year":"Birth Year", "gender":"Gender"})
        # Drop all rows with missing information
        df = df.dropna(how='any')
        #save the dataframwe as a clean csv file
        df.to_csv(folder + 'clean_' + file_name)


if __name__ == "__main__":
    clean()