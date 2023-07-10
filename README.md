#### holbertonschool-AirBnB_clone
# Welcome to the AirBnB clone project!

### Project Concept
This project consist of making a clone of AirBNB.

For this step of the project it was developed the console and the storage
{JSON files}.


### Command Interpreter:
Purpose:

    - create your data model
    - manage (create, update, destroy, etc) objects via a console / command interpreter
    - store and persist objects to a file (JSON file)

How to use:

    There are two ways of using the commnad interpreter:
        - Interactive Mode
        - Non Interactive Mode

To use it:

    After cloning the repository run:

    Interactive Mode:
        ./console.py

    Non Interactive Mode:
        run the commands as follow:
            echo "<command>" | ./console.py

Command list:

    - Create - Creates a new instance
    - Show - Prints the string representation of an instance
    - Destroy - Deletes an instance based on the class and id
    - All - Prints all string represntation of all instances
    - Update - Updates an instance based on class and id
    - Help - 
    - Quit - Exit the console

Examples:

    to create:
        create <object class>

    to show:
        show <object class> <object id>

    to destroy:
        destroy <object class> <object id>

    to all:
        all                 (prints all the elemnts)
        all <object class>  (prints all the elemnts of object class)

    to update:
        update <object class> <object id> <key> <value>

### Project Attributes

#### Data types

The following data types are used to manage hte objects related to the products.

    - BaseModel
    - FileStorage
    - State
    - City
    - Amenity
    - Place
    - Review

### Clone Repository
    git clone https://github.com/Faqu22/holbertonschool-AirBnB_clone.git

### Run Tests
    python3 -m unittest discover tests

### Authors
- Facundo Alvarez
- Pablo Laborde
