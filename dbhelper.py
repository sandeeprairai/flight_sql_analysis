import  mysql.connector

class DB:
    def __init__(self):
        #connect to the database
        try:
            self.conn=mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='indigo'
            )
            self.mycursor=self.conn.cursor()
            print("Connection established")

        except:
            print("Connection error") 

    def fetch_city_names(self):
        city=[]
        self.mycursor.execute("""
       SELECT DISTINCT(Destination) from indigo.flight
       UNION
       SELECT DISTINCT(Source) fROM indigo.flight

           """)
        data=self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
        return city   
    
    def fetch_all_flights(self,source,destination):

        self.mycursor.execute("""
        SELECT Airline,Route,Dep_Time,Duration,Price from flight
        where Source='{}' and Destination='{}' """ .format(source,destination))
        data=self.mycursor.fetchall()
        return data
    
    def fetch_airline_frequency(self):

        airline=[]
        frequency=[]

        self.mycursor.execute("""
        SELECT Airline,COUNT(*) from flight 
        GROUP BY Airline

      """)
        data=self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])
        return airline,frequency
    
    def busy_airport(self):
        city=[]
        frequency=[]

        self.mycursor.execute("""
      SELECT Source,COUNT(*) FROM (SELECT Source FROM flight
							UNION ALL
							SELECT Destination FROM flight) t
        GROUP BY t.Source
        ORDER BY COUNT(*) DESC
      """)
        data=self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1]) 

        return city,frequency   
    
    def daily_frequency(self):
        date=[]
        frequency=[]
        self.mycursor.execute("""
    SELECT Date_of_Journey,COUNT(*) from flight
    GROUP BY Date_of_Journey
""")
        data=self.mycursor.fetchall()
        for item in data:
            date.append(item[0])
            frequency.append(item[1])
        return date,frequency
        
        
        