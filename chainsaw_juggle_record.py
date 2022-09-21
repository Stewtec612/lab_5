import sqlite3
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
conn.execute('CREATE TABLE IF NOT EXISTS records(name text, country text, number_of_catches integer)')

#add data to the table
conn.execute('INSERT INTO records VALUES("Jane Mustonen", "Finland", 98)')
conn.execute('INSERT INTO records VALUES("Ian Stewart", "Canada", 94)')
conn.execute('INSERT INTO records VALUES("Aaron Gregg", "Canada", 88)')
conn.execute('INSERT INTO records VALUES("Chad Taylor", "USA", 78)')

#finalize additions
conn.commit()

for row in conn.execute("SELECT * FROM records"):
    print(row)

conn.close()

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


def add_new_record():
    print('todo add new record. What if user wants to add a record that already exists?')


def edit_existing_record():
    print('todo edit existing record. What if user wants to edit record that does not exist?') 


def delete_record():
    try:
        with sqlite3.connect('chainjugglerec.db') as conn:

            for row in conn.execute("SELECT * FROM records"):
                print(row)

            entry_to_delete = input('What is the name of the record holder would you like to delete? ')
        conn.execute('DELETE FROM records WHERE name = ?',(entry_to_delete, ))
    except sqlite3.Error as e:
        print('Error accessing data {e}')
    finally:
        conn.commit()
        conn.close



if __name__ == '__main__':
    main()