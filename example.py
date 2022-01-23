from argument_tasks import Interface
from example_data import methods

SOURCE_YML_FILE = open("example_data/tasks.yml", "r")

Interface(SOURCE_YML_FILE, methods).run()
