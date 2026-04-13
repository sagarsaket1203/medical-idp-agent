import mlflow

class ExperimentTracker:
    def __init__(self, experiment_name):
        self.experiment_name = experiment_name
        mlflow.set_experiment(self.experiment_name)

    def log_step(self, step_name, step_details):
        mlflow.log_param('step_name', step_name)
        mlflow.log_param('step_details', step_details)
        mlflow.log_artifact('step.log') # Placeholder for further logging

    def log_extraction(self, extraction_name, extraction_details):
        mlflow.log_param('extraction_name', extraction_name)
        mlflow.log_param('extraction_details', extraction_details)
        mlflow.log_artifact('extraction.log') # Placeholder for further logging

    def log_synthesis(self, synthesis_name, synthesis_details):
        mlflow.log_param('synthesis_name', synthesis_name)
        mlflow.log_param('synthesis_details', synthesis_details)
        mlflow.log_artifact('synthesis.log') # Placeholder for further logging

    def end_experiment(self, status):
        mlflow.set_tag("status", status)

# Example usage:
# tracker = ExperimentTracker('My Experiment')
# tracker.log_step('Step 1', 'Details about step 1')
# tracker.log_extraction('Extraction 1', 'Details about extraction 1')
# tracker.log_synthesis('Synthesis 1', 'Details about synthesis 1')
# tracker.end_experiment('completed')