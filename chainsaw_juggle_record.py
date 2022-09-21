import sqlite3
from urllib import request
"""
This progam uses a database that collects all chainsaw juggling records in 2018
The user is given the option to choose between:
    -displaying all recorded records in database 
    -add a new record to the database
    -modify and update an existing entry in the database
    -Delete an entry in the database
"""
#establish a connection to chainjugglerec.db
conn = sqlite3.connect('chainjugglerec.db')
conn.execute('DROP TABLE records')

#create table for db
conn.execute('CREATE TABLE IF NOT EXISTS records(rowid INTEGER PRIMARY KEY, name text, country text, number_of_catches integer)')

#add data to the table
conn.execute('INSERT INTO records VALUES(NULL, "Jane Mustonen", "Finland", 98)')
conn.execute('INSERT INTO records VALUES(NULL, "Ian Stewart", "Canada", 94)')
conn.execute('INSERT INTO records VALUES(NULL, "Aaron Gregg", "Canada", 88)')
conn.execute('INSERT INTO records VALUES(NULL, "Chad Taylor", "USA", 78)')

#finalize additions
conn.commit()

for row in conn.execute("SELECT * FROM records"):
    print(row)


def main():
    menu_text = """
    1. Display all records
    2. Add new record
    3. Edit existing record
    4. Delete record 
    5. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            add_new_record()
        elif choice == '3':
            edit_existing_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    print('todo display all records')
    for row in conn.execute("SELECT * FROM records"):
        print(row)


def add_new_record():
    print('todo add new record. What if user wants to add a record that already exists?')


def edit_existing_record():
    try:
        with sqlite3.connect('chainjugglerec.db') as conn:
            
            new_name = input('Enter new name: ')
            new_country = input('enter new country: ')
            new_juggle_rec = input('Enter new juggle record: ')
            name_to_change = input('whats the name of the record holder that youd like to change? ')
            conn.execute('UPDATE records SET name = ?, country = ?, number_of_catches = ? WHERE name = ?',(new_name, new_country, new_juggle_rec, name_to_change))
    except sqlite3.Error as e:
        print(f'Cannot edit data, entry with {new_name} does not exists')
    else:
        conn.commit()
        conn.close()
    
    
    

def delete_record():
    print('todo delete existing record. What if user wants to delete record that does not exist?') 


if __name__ == '__main__':
    main()