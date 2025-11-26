import pandas as pd
import matplotlib.pyplot as plt
import os

base = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base, "../data/sample_contact_data.csv")

df = pd.read_csv(csv_path)
df['description'] = df['description'].str.lower()

issue_counts = df['issue_type'].value_counts().reset_index()
issue_counts.columns = ['issue_type', 'count']
print("\nIssue frequency:")
print(issue_counts.to_string(index=False))

esc = df.groupby('issue_type')['escalated'].mean().reset_index()
esc.columns = ['issue_type','escalation_rate']
print("\nEscalation rate by issue:")
print(esc.to_string(index=False))

rt = df.groupby('region')['resolution_time_min'].mean().reset_index()
rt.columns = ['region','avg_resolution_time_min']
print("\nAvg resolution time by region:")
print(rt.to_string(index=False))

output_dir = os.path.join(base, "../outputs")
os.makedirs(output_dir, exist_ok=True)

issue_counts.to_csv(os.path.join(output_dir,'output_issue_counts.csv'),index=False)
esc.to_csv(os.path.join(output_dir,'output_escalation_rate.csv'),index=False)
rt.to_csv(os.path.join(output_dir,'output_region_rt.csv'),index=False)

plt.figure(figsize=(6,4))
plt.bar(issue_counts['issue_type'], issue_counts['count'])
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(output_dir,'issue_counts.png'), dpi=150)

print("\nOutputs saved in /outputs")
