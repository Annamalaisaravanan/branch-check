import pandas as pd
from sklearn.datasets import fetch_california_housing
from branch_check_dbx.common import Task


class ModelDevelopment(Task):
    
    def train_model(self):
             print("Model training executed in Dev environment")


    def launch(self):
          self.train_model()

# if you're using python_wheel_task, you'll need the entrypoint function to be used in setup.py
def entrypoint():  # pragma: no cover
    task = ModelDevelopment()
    task.launch()

# if you're using spark_python_task, you'll need the __main__ block to start the code execution
if __name__ == '__main__':
    entrypoint()
