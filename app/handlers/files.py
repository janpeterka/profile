import os

from werkzeug.utils import secure_filename

from flask import send_from_directory


class FileHandler(object):
    def __init__(self, folder=None):
        DIR_ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../")
        self.folder = os.path.join(DIR_ROOT, "uploads/")
        if folder is not None:
            # TODO: create folder if doesn't exist 
            self.folder = os.path.join(self.folder, folder)

        self.allowed_extension = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}

    def save(self, file):
        file.save(os.path.join(self.folder, secure_filename(file.filename)))
        return secure_filename(file.filename)

    def get_path(self, item):
        if item.filename is None:
            return None
        return os.path.join(self.folder, item.filename)

    def show(self, item):
        return send_from_directory(self.folder, item.filename)