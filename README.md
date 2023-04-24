
# Web Flask

This was a sub-project within AirBnB in which I began working with Flask
and Jinja2. In this project, I began integrating the back-end storage engine
with the web static HTML/CSS pages written earlier.

Files 0 - 6 were introductory tasks familiarizing myself with
using Flask. Files 7 forward involved gradually putting together more and more
complex Jinja templates based on the HBnB HTML pages.

The most complete Flask/Jinja app-template combo in this directory is defined
in Flask module [100-hbnb.py](./100-hbnb.py) and Jinja template
[100-hbnb.html](./100-hbnb.html).

To run the Flask app, execute the following command from the root directory
of the project:

```
~ $ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost
HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.100-hbnb
```

The app can be accessed at `0.0.0.0:5000/hbnb`.

Screenshots:
<p align="center">
  <img src="https://github.com/bdbaraban/AirBnB_clone_v2/blob/master/assets/hbnb_screenshot_0.png"
       alt="HolbertonBnB logo">
</p>

---

<p align="center">
  <img src="https://github.com/bdbaraban/AirBnB_clone_v2/blob/master/assets/hbnb_screenshot_1.png"
       alt="HolbertonBnB logo">
</p>

---

<p align="center">
  <img src="https://github.com/bdbaraban/AirBnB_clone_v2/blob/master/assets/hbnb_screenshot_2.png"
       alt="HolbertonBnB logo">
</p>
=======
# holbertonschool-AirBnB_clone

## The Console

The AirBnB console is a command line interface that allows users to interact with the JSON file-based data storage system for the AirBnB project. It uses the Python module 'cmd' to create the interface and provides a custom prompt of '(hbnb)'. The console implements the ability to quit the program using 'quit' or 'EOF' and provides a 'help' command to display information on available commands.

## How to start the console:

Clone the repository and run the console.py
```
$ git clone https://github.com/------/holbertonschool-AirBnB_clone.git
```

## How to use the console:

|   **Method**   |   **Description**   |
| -------------- | --------------------- |
|[create](./console.py) | Creates object of given class |
|[show](./console.py) | Prints the string representation of an instance based on the class name and id |
|[all](./console.py) | Prints all string representation of all instances based or not on the class name |
|[update](./console.py) | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) |
|[destroy](./console.py)| Deletes an instance based on the class name and id (save the change into the JSON file) |
|[count](./console.py)| Retrieve the number of instances of a class |
|[help](./console.py)| Prints information about specific command |
|[quit/ EOF](./console.py)| Exit the program |

## Examples: 

```
➜  AirBnB_clone git:(feature) ✗ ./console.py
(hbnb) create User
bb4f4b81-7757-460b-9263-743c9ea6fef6
(hbnb) show User bb4f4b81-7757-460b-9263-743c9ea6fef6
[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'created_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492106)}
(hbnb) all User
["[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'created_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492106)}"]
(hbnb) update User bb4f4b81-7757-460b-9263-743c9ea6fef6 name Betty
['User', 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'name', 'Betty']
(hbnb) all User
["[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'name': 'Betty', 'created_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492106)}"]
(hbnb) destroy User bb4f4b81-7757-460b-9263-743c9ea6fef6
(hbnb) all User
[]
(hbnb) show User
** instance id missing **
(hbnb)

```

```
➜  AirBnB_clone git:(feature) ✗ ./console.py
(hbnb) User.create
*** Unknown syntax: User.create
(hbnb) User.create()
e6ee5344-04ef-454d-84e4-ba6fc613f1b4
(hbnb) User.all()
["[User] (e6ee5344-04ef-454d-84e4-ba6fc613f1b4) {'id': 'e6ee5344-04ef-454d-84e4-ba6fc613f1b4', 'updated_at': datetime.datetime(2019, 11, 13, 17, 14, 1, 963404), 'created_at': datetime.datetime(2019, 11, 13, 17, 14, 1, 963373)}"]
(hbnb) User.show()
** instance id missing **
(hbnb) User.show(e6ee5344-04ef-454d-84e4-ba6fc613f1b4)
[User] (e6ee5344-04ef-454d-84e4-ba6fc613f1b4) {'id': 'e6ee5344-04ef-454d-84e4-ba6fc613f1b4', 'updated_at': datetime.datetime(2019, 11, 13, 17, 14, 1, 963404), 'created_at': datetime.datetime(2019, 11, 13, 17, 14, 1, 963373)}
(hbnb) User.update("e6ee5344-04ef-454d-84e4-ba6fc613f1b4", "name", "Betty")
['User', '"e6ee5344-04ef-454d-84e4-ba6fc613f1b4"', '"name"', '"Betty"']
(hbnb) User.all()
['[User] (e6ee5344-04ef-454d-84e4-ba6fc613f1b4) {\'"name"\': \'"Betty"\', \'id\': \'e6ee5344-04ef-454d-84e4-ba6fc613f1b4\', \'updated_at\': datetime.datetime(2019, 11, 13, 17, 14, 1, 963404), \'created_at\': datetime.datetime(2019, 11, 13, 17, 14, 1, 963373)}']
(hbnb) User.destroy(e6ee5344-04ef-454d-84e4-ba6fc613f1b4)
(hbnb) User.all()
[]
(hbnb) quit
➜  AirBnB_clone git:(feature) ✗

```

## Authors:

* Ricardo Corona - @LW068
* Manuel Zambrado - @mnlazs
