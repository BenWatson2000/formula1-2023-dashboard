
import mysql.connector


def view_teams(cursor):
    query = "SELECT * FROM F1Teams"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def init_teams(cursor,mydb):
    query = """INSERT INTO F1Teams (teamid, teamname, constructorchampionshippoints, constructorsstanding) 
               VALUES (1, 'Mercedes', 0, 0),
                      (2, 'RedBull', 0, 0),
                      (3, 'Ferrari', 0, 0),
                      (4, 'Aston Martin', 0, 0),
                      (5, 'Mclaren', 0, 0),
                      (6, 'Haas', 0, 0),
                      (7, 'Williams', 0, 0),
                      (8, 'Alfa Romeo', 0, 0),
                     (9, 'Alpha Tauri', 0, 0),
                     (10, 'Alpine', 0, 0);"""
    
    cursor.execute(query)

    # Commit the changes to the database
    mydb.commit()


def init_drivers(cursor,mydb):
    query = """INSERT INTO F1Drivers (driverid, teamid, drivername, driverchampionshippoints, driversstanding) 
                VALUES 
                (1, 1, 'George Russell', 0, 0),
                (2, 1, 'Lewis Hamilton', 0, 0),
                (3, 2, 'Max Verstappen', 0, 0),
                (4, 2, 'Sergio Perez', 0, 0),
                (5, 3, 'Charles Leclerc', 0, 0),
                (6, 3, 'Carlos Sainz', 0, 0),
                (7, 10, 'Esteban Ocon', 0, 0),
                (8, 10, 'Pierre Gasly', 0, 0),
                (9, 5, 'Lando Norris', 0, 0),
                (10, 5, 'Oscar Piastri', 0, 0),
                (11, 8, 'Valtteri Bottas', 0, 0),
                (12, 8, 'Zhou Guanyu', 0, 0),
                (13, 4, 'Lance Stroll', 0, 0),
                (14, 4, 'Fernando Alonso', 0, 0),
                (15, 6, 'Kevin Magnussen', 0, 0),
                (16, 6, 'Nico Hulkenberg', 0, 0),
                (17, 9, 'Yuki Tsunoda', 0, 0),
                (18, 9, 'Nyck de Vries', 0, 0),
                (19, 7, 'Alex Albon', 0, 0),
                (20, 7, 'Logan Sargeant', 0, 0);"""
    
    cursor.execute(query)

    # Commit the changes to the database
    mydb.commit()


def set_all_zero(cursor,mydb):
    query = """UPDATE F1Drivers
                SET driverchampionshippoints = CASE
                WHEN drivername = 'Lewis Hamilton' THEN 347
                WHEN drivername = 'George Russell' THEN 0
                WHEN drivername = 'Max Verstappen' THEN 286
                WHEN drivername = 'Sergio Perez' THEN 190
                WHEN drivername = 'Charles Leclerc' THEN 158
                WHEN drivername = 'Carlos Sainz' THEN 155
                WHEN drivername = 'Pierre Gasly' THEN 110
                WHEN drivername = 'Esteban Ocon' THEN 74
                WHEN drivername = 'Nyck de Vries' THEN 0
                WHEN drivername = 'Yuki Tsunoda' THEN 32
                WHEN drivername = 'Lando Norris' THEN 160
                WHEN drivername = 'Oscar Piastri' THEN 0
                WHEN drivername = 'Fernando Alonso' THEN 74
                WHEN drivername = 'Lance Stroll' THEN 34
                WHEN drivername = 'Valtteri Bottas' THEN 122
                WHEN drivername = 'Zhou Guanyu' THEN 0
                WHEN drivername = 'Alex Albon' THEN 0
                WHEN drivername = 'Logan Sargeant' THEN 0
                WHEN drivername = 'Kevin Magnussen' THEN 0
                WHEN drivername = 'Nico Hulkenberg' THEN 0
                END
                WHERE drivername IN ('Lewis Hamilton', 'George Russell', 'Max Verstappen', 'Sergio Perez', 'Charles Leclerc', 'Carlos Sainz', 'Pierre Gasly', 'Esteban Ocon', 'Nyck de Vries', 'Yuki Tsunoda', 'Lando Norris', 'Oscar Piastri', 'Fernando Alonso', 'Lance Stroll', 'Valtteri Bottas', 'Zhou Guanyu', 'Alex Albon', 'Logan Sargeant', 'Kevin Magnussen', 'Nico Hulkenberg');
                """
    
    cursor.execute(query)

    # Commit the changes to the database
    mydb.commit()

def change_points(cursor,mydb):
    query = """UPDATE F1Drivers
                SET driverchampionshippoints = CASE
                WHEN drivername = 'Lewis Hamilton' THEN 347
                WHEN drivername = 'George Russell' THEN 10
                WHEN drivername = 'Max Verstappen' THEN 286
                WHEN drivername = 'Sergio Perez' THEN 190
                WHEN drivername = 'Charles Leclerc' THEN 158
                WHEN drivername = 'Carlos Sainz' THEN 155
                WHEN drivername = 'Pierre Gasly' THEN 110
                WHEN drivername = 'Esteban Ocon' THEN 74
                WHEN drivername = 'Nyck de Vries' THEN 10
                WHEN drivername = 'Yuki Tsunoda' THEN 32
                WHEN drivername = 'Lando Norris' THEN 160
                WHEN drivername = 'Oscar Piastri' THEN 10
                WHEN drivername = 'Fernando Alonso' THEN 74
                WHEN drivername = 'Lance Stroll' THEN 34
                WHEN drivername = 'Valtteri Bottas' THEN 122
                WHEN drivername = 'Zhou Guanyu' THEN 10
                WHEN drivername = 'Alex Albon' THEN 10
                WHEN drivername = 'Logan Sargeant' THEN 10
                WHEN drivername = 'Kevin Magnussen' THEN 10
                WHEN drivername = 'Nico Hulkenberg' THEN 10
                END
                WHERE drivername IN ('Lewis Hamilton', 'George Russell', 'Max Verstappen', 'Sergio Perez', 'Charles Leclerc', 'Carlos Sainz', 'Pierre Gasly', 'Esteban Ocon', 'Nyck de Vries', 'Yuki Tsunoda', 'Lando Norris', 'Oscar Piastri', 'Fernando Alonso', 'Lance Stroll', 'Valtteri Bottas', 'Zhou Guanyu', 'Alex Albon', 'Logan Sargeant', 'Kevin Magnussen', 'Nico Hulkenberg');
                """
    
    cursor.execute(query)

    # Commit the changes to the database
    mydb.commit()

db_hostname = input("Enter your database hostname: ")
db_password = input("Enter your database password: ")

# Establish a connection to the MySQL database
mydb = mysql.connector.connect(
  host=db_hostname,
  user="admin",
  password=db_password,
  database="F1-Schema"
)

# Create a cursor object to interact with the database
cursor = mydb.cursor()


# init_teams(cursor,mydb)

change_points(cursor,mydb)

# view_teams(cursor)

# Close the connection to the database
mydb.close()