#Natalie Warner 
#this program incoorporates SQL and Python and CSV File Management 

import sqlite3
import csv


def create_db_table():
    
    conn = sqlite3.connect("vehicle.db")    
    cursor = conn.cursor()
    sql = "CREATE TABLE VehicleDatabase (vehicletype text, vehiclestatus text, vehiclemake text, vehiclemodel text, vehiclemodelyear int, vehiclecolor text, vehiclefuelsource text, vehiclewheelchairaccessible text, city text, state text, ZIPcode int)"
    cursor.execute(sql)
    cursor.close()

def add_data():
    conn = sqlite3.connect("vehicle.db")
    cursor = conn.cursor()
    
    with open ('vehicle.csv', 'r') as f:
        for line in f:
            L = line.split(",")
            vehicle_type = L[0]
            status = L[1]
            vehicle_make = L[2]
            vehicle_model = L[3]
            vehicle_model_year = L[4]
            vehicle_color = L[5]
            vehicle_fuel_source = L[6]
            wheelchair_accessible = L[7]
            city = L[8]
            state = L[9]
            ZIP_code = L[10]
            sql = "INSERT INTO VehicleDatabase (vehicletype, vehiclestatus, vehiclemake, vehiclemodel, vehiclemodelyear, vehiclecolor, vehiclefuelsource, vehiclewheelchairaccessible, city, state, ZIPcode) VALUES (:vehicletype, :vehiclestatus, :vehiclemake, :vehiclemodel, :vehiclemodelyear, :vehiclecolor, :vehiclefuelsource, :vehiclewheelchairaccessible, :city, :state, :ZIPcode)"
            cursor.execute(sql, {"vehicletype":vehicle_type, "vehiclestatus": status, "vehiclemake":vehicle_make, "vehiclemodel":vehicle_model, "vehiclemodelyear":vehicle_model_year, "vehiclecolor":vehicle_color, "vehiclefuelsource":vehicle_fuel_source, "vehiclewheelchairaccessible":wheelchair_accessible, "city":city, "state": state, "ZIPcode":ZIP_code})
            conn.commit()
    cursor.close()


def average_year():
    conn = sqlite3.connect("vehicle.db")
    cursor = conn.cursor()
    sql1 = "SELECT vehiclemodelyear FROM VehicleDatabase"
    cursor.execute(sql1)
    years = cursor.fetchall()
    for i in years:
        print(i[0])

def vehicle_models():
    conn = sqlite3.connect("vehicle.db")
    cursor = conn.cursor()
    sql2 = "SELECT DISTINCT vehiclemodel FROM VehicleDatabase"
    cursor.execute(sql2)
    vehiclemodel = cursor.fetchall()
    print(vehiclemodel)
    
def citycount():
    conn = sqlite3.connect("vehicle.db")
    cursor = conn.cursor()
    sql3 = "SELECT DISTINCT city FROM VehicleDatabase"
    cursor.execute(sql3)
    city = cursor.fetchall()
    print(city)

def zip_code():
    conn = sqlite3.connect("vehicle.db")
    cursor = conn.cursor()
    sql4 = "SELECT DISTINCT ZIPcode FROM VehicleDatabase"
    cursor.execute(sql4)
    ZIPcode = cursor.fetchall()
    print(ZIPcode)
    
def main():
     create_db_table()
     add_data()
     average_year()
     vehicle_models()
     citycount()
     zip_code()
main()
