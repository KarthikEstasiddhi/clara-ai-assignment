import os
import json

from scripts.extract_memo import extract_account_memo
from scripts.generate_agent import generate_agent_spec


# -----------------------------
# Configuration
# -----------------------------

account_id = "account_001"

demo_file = "data/demo_calls/bens_electric_demo.txt"
onboard_file = "data/onboarding_calls/bens_electric_onboard.txt"


# -----------------------------
# Create Required Folders
# -----------------------------

os.makedirs("outputs", exist_ok=True)
os.makedirs("outputs/accounts", exist_ok=True)
os.makedirs("changelog", exist_ok=True)

os.makedirs(f"outputs/accounts/{account_id}/v1", exist_ok=True)
os.makedirs(f"outputs/accounts/{account_id}/v2", exist_ok=True)


# -----------------------------
# Load Transcripts
# -----------------------------

with open(demo_file, "r", encoding="utf-8") as f:
    demo_text = f.read()

with open(onboard_file, "r", encoding="utf-8") as f:
    onboarding_text = f.read()


# -----------------------------
# Generate v1 from Demo Call
# -----------------------------

memo_v1 = extract_account_memo(demo_text, account_id)

agent_v1 = generate_agent_spec(memo_v1, "v1")


# Save memo v1
with open(f"outputs/accounts/{account_id}/v1/memo.json", "w", encoding="utf-8") as f:
    json.dump(memo_v1, f, indent=2)


# Save agent spec v1
with open(f"outputs/accounts/{account_id}/v1/agent_spec.json", "w", encoding="utf-8") as f:
    json.dump(agent_v1, f, indent=2)


# -----------------------------
# Generate v2 from Onboarding
# -----------------------------

memo_v2 = extract_account_memo(onboarding_text, account_id)

agent_v2 = generate_agent_spec(memo_v2, "v2")


# Save memo v2
with open(f"outputs/accounts/{account_id}/v2/memo.json", "w", encoding="utf-8") as f:
    json.dump(memo_v2, f, indent=2)


# Save agent spec v2
with open(f"outputs/accounts/{account_id}/v2/agent_spec.json", "w", encoding="utf-8") as f:
    json.dump(agent_v2, f, indent=2)


# -----------------------------
# Generate Changelog
# -----------------------------

changes = []

for key in memo_v2:
    if memo_v1.get(key) != memo_v2.get(key):
        changes.append(f"{key} updated")


changelog_file = f"changelog/{account_id}_changes.md"

with open(changelog_file, "w", encoding="utf-8") as f:
    f.write("# Changes from v1 to v2\n\n")

    if changes:
        for change in changes:
            f.write(f"- {change}\n")
    else:
        f.write("- No major changes detected\n")


# -----------------------------
# Finish
# -----------------------------

print("Pipeline completed successfully!")
print("Outputs saved in outputs/accounts/")
print("Changelog created in changelog/")