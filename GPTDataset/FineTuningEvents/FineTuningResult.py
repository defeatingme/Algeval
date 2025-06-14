import re
import json
import matplotlib.pyplot as plt
import datetime

# Extract relevant data
events = []
metrics = []
# Read the uploaded file to inspect its contents
file_path = "GPTDataset/FineTuningEvents/ft_job_1.txt"

with open(file_path, "r", encoding="utf-8") as file:
    file_contents = file.readlines()

# Display a sample of the first few lines to understand the data format
file_contents[:10]

for line in file_contents:
    match = re.search(r"FineTuningJobEvent\(id='(.*?)', created_at=(\d+), level='(.*?)', message='(.*?)', object='fine_tuning.job.event', data=(\{.*?\}), type='(.*?)'\)", line)
    if match:
        event_id, created_at, level, message, data, event_type = match.groups()
        data = json.loads(data.replace("'", '"')) if data != "{}" else {}

        event = {
            "id": event_id,
            "created_at": created_at,
            "level": level,
            "message": message,
            "data": data,
            "type": event_type,
        }

        events.append(event)
        
        if event_type == "metrics" and "step" in data and "train_loss" in data:
            metrics.append((data["step"], data["train_loss"], data.get("train_mean_token_accuracy", None)))

# Sort metrics by step number
metrics.sort(key=lambda x: x[0])

# Extract values for plotting
steps = [m[0] for m in metrics]
train_losses = [m[1] for m in metrics]
token_accuracies = [m[2] for m in metrics if m[2] is not None]

# Plot Training Loss Over Steps
plt.figure(figsize=(10, 5))
plt.plot(steps, train_losses, marker='o', linestyle='-', color='b', label='Training Loss')
plt.xlabel('Training Step')
plt.ylabel('Loss')
plt.title('Training Loss Over Steps')
plt.legend()
plt.grid(True)
plt.show()

# Plot Token Accuracy Over Steps if available
if token_accuracies:
    plt.figure(figsize=(10, 5))
    plt.plot(steps, token_accuracies, marker='s', linestyle='-', color='g', label='Token Accuracy')
    plt.xlabel('Training Step')
    plt.ylabel('Token Accuracy')
    plt.title('Token Accuracy Over Steps')
    plt.legend()
    plt.grid(True)
    plt.show()
