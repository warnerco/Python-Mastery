import sqlite3

def Creating_Table_and_Database():
    conn = sqlite3.connect("mydb.db")
    cursor = conn.cursor()
    sql = "CREATE TABLE FavoriteMovies (name text, genre text, year int, director text)"
    cursor.execute(sql)
    cursor.close()


def Add_Data():
    conn = sqlite3.connect("mydb.db")
    cursor = conn.cursor()
    while True:
        name = input("Favorite Movie\'s name:" )
        genre = input("Favorite Movie\'s genre:" )
        year = input("Favorite Movies\'s year:" )
        director = input("Favorite Movie\'s director:" )
        sql = "INSERT INTO FavoriteMovies (name, genre, year, director) VALUES (:rname, :rgenre, :ryear, :rdirector)"
        cursor.execute(sql, {'rname': name, 'rgenre': genre, 'ryear': year, 'rdirector': director})
        conn.commit()
        loopcontrol = input ("Add another movie (y/n)?:")
        if loopcontrol == 'n':
            break
    cursor.close()


def Fetch_Data():
    conn = sqlite3.connect("mydb.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM FavoriteMovies" #* means add all 
    results = cursor.execute(sql)
    all_movies = results.fetchall()
    for i in all_movies:
        print(i)

    cursor.close()

def Delete_Data():

    conn = sqlite3.connect("mydb.db")
    cursor = conn.cursor()
    sql = "DELETE FROM FavoriteMovies WHERE name = 'Interstellar'"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    



def Update_Data():
    conn = sqlite3.connect("mydb.db")
    cursor = conn.cursor()
    sql = "UPDATE FavoriteMovies SET name = 'What We Do in the Shadows' WHERE name 'Liar Liar'"
    conn.commit()
    cursor.close()


def main():
    Creating_Table_and_Database()
    Add_Data()
    Delete_Data()
    Update_Data()
    Fetch_Data()

main()