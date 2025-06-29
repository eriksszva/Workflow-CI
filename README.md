# Workflow CI for Resume Classifier (MLflow Project)

This directory contains the full **MLflow-based machine learning project** for the **Resume Screening Classifier for Data Scientist Applications** project, including all files necessary for model training, reproducibility, and automated deployment through **GitHub Actions CI/CD**.

## 📂 Directory Structure Overview

```bash
├── .github/
│   └── workflows/
│       └── main.yaml                 # GitHub Actions workflow: automates training mlflow project
📁 MLproject/
│
├── cleaned_data/
│   └── resume_data_cleaned.csv      # Preprocessed dataset used for training
│
├── utils/
│   └── SentenceTransformers.py      # Embedding logic using pre-trained SentenceTransformer
│
├── conda.yaml                       # Conda environment file for MLflow runs
├── drive-link.txt                   # Reference to Google Drive folder for experiment outputs
├── MLproject                        # MLflow project specification (entry point config)
├── modelling.py                     # Main script for training and evaluating the classifier
├── requirements.txt                 # Additional pip-based Python dependencies
└── upload_to_drive.py               # Script to automatically upload outputs to Google Drive
```

## Purpose

This MLproject is built to:

* Train a **binary classifier** that predicts whether a resume is relevant for a Data Scientist role.
* Use **SentenceTransformer embeddings** to capture semantic meaning of resume content.
* Ensure reproducibility through MLflow and a version-controlled conda environment.
* Automate testing and output management via GitHub Actions.

## CI/CD with GitHub Actions

The CI/CD workflow located at:

```
.github/workflows/main.yaml
```

is responsible for:

* Validating code and dependencies upon each push or pull request
* Automatically running the training pipeline (`modelling.py`)
* Uploading artifacts (e.g., trained model, metrics, logs) to external storage such as Google Drive
* Ensuring all outputs are reproducible and tracked via MLflow

## How It Works

1. On push to `main` or a PR:

   * The workflow sets up the conda environment.
   * Runs the `MLproject` with MLflow using the specified entry point.
   * Saves results to `mlruns/` directory.

2. On success:

   * Outputs are uploaded using `upload_to_drive.py` (based on access to Drive folder).
   * The model can be registered or deployed depending on the next pipeline stage.

## Requirements

To run this project manually:

```bash
conda env create -f conda.yaml
mlflow run .
```

To install requirements separately:

```bash
pip install -r requirements.txt
```

## Notes

* Make sure to configure proper Drive access tokens or service account credentials if using Google Drive automation.
* The `SentenceTransformers.py` module assumes a pre-trained model like `all-MiniLM-L6-v2` is available or downloaded during the run.
* CI/CD workflows assume MLflow is already installed and available in the runner environment.
