class File:
    def __init__(self, file_name, methods):
        self.file_obj = open(file_name, methods)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


with File('example.txt', 'a') as fil:
    fil.write('Out some text here')



