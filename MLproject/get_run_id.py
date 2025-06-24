import mlflow
import json
from mlflow.tracking import MlflowClient
import os

client = MlflowClient()
experiments = client.search_experiments()
experiment_id = None

for exp in experiments:
    if exp.name == "Resume Classifier":
        experiment_id = exp.experiment_id
        break

if experiment_id is None:
    print("Experiment not found.")
    exit(1)

runs = client.search_runs(experiment_ids=[experiment_id],
                          filter_string="attributes.status = 'FINISHED'",
                          order_by=["start_time DESC"],
                          max_results=1)

if not runs:
    print("No finished runs found.")
    exit(1)

run_id = runs[0].info.run_id
print(f"MLFLOW_RUN_ID={run_id}")

# also write to GitHub env
with open(os.environ["GITHUB_ENV"], "a") as f:
    f.write(f"MLFLOW_RUN_ID={run_id}\n")