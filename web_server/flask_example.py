import os
from flask import Flask
from flask import request


APP = Flask(__name__)

class ManageFile(object):
    
    # change FILE_PATH variable according the current OS
    FILE_PATH = "/tmp"
    FILE_LOCATION = os.path.join(FILE_PATH, "flask_file.txt")

    # class method
    def write(self, username=None):
        """Creates a new file"""

        if username:
            # create the file
            with open(ManageFile.FILE_LOCATION, "w") as _file:
                _file.write(username)

                text = "Username ({}) successfully storaged ".format(username)
        else:
            text = "Please set a <username>"

        return text

    # class method
    def read(self):
        """Read a file

        return:
            - the content of the file"""

        file_content = None
        if os.path.isfile(ManageFile.FILE_LOCATION) and os.stat(
            ManageFile.FILE_LOCATION).st_size == 0:
            file_content = "The file is empty, please create a username"
        elif os.path.isfile(ManageFile.FILE_LOCATION):
            with open(ManageFile.FILE_LOCATION, "r") as _file:
                file_content = _file.read()
        else:
            file_content = "Create a username first!"

        return file_content

    # class method
    def delete(self):
        """Delete a username"""

        if os.path.isfile(ManageFile.FILE_LOCATION) and os.stat(
            ManageFile.FILE_LOCATION).st_size == 0:
            text = "The username has already been deleted, please create a new one"
        elif os.path.isfile(ManageFile.FILE_LOCATION):
            with open(ManageFile.FILE_LOCATION, "w") as _file:
                _file.seek(0)
                _file.truncate()
            text = "The username was removed successfully"
        else:
            text = "Create a username first!"

        return text

# flask decorator
@APP.route('/', methods=['GET'])
# function
def hello():
    """Return a sample Hellow World"""

    return "Hello World!"

# flask decorator
@APP.route('/current_username/')
# function
def current_username():

    # instantiate the object
    obj = ManageFile()

    return obj.read()


# flask decorator
@APP.route('/modify_username/<username>')
# function
def modify_username(username):

    # instantiate the object
    obj = ManageFile()

    return obj.write(username)


# flask decorator
@APP.route('/delete_username/')
# function
def delete_username():
    # instantiate the object
    obj = ManageFile()

    return obj.delete()


if __name__ == '__main__':
    APP.run(debug=True, port=5000)
