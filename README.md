# Clara AI Automation Pipeline

## Overview

This project implements an automation pipeline that converts demo and onboarding call transcripts into structured configurations for an AI voice agent.

The system simulates how Clara Answers converts real-world customer conversations into operational rules and AI agent prompts.

---

## Architecture

Demo Call Transcript
↓
Information Extraction
↓
Account Memo JSON (v1)
↓
Agent Prompt Generator
↓
Retell Agent Draft Spec (v1)

Onboarding Transcript
↓
Configuration Update
↓
Account Memo JSON (v2)
↓
Updated Agent Spec (v2)
↓
Changelog Generation

---

## Pipeline Components

### Pipeline A – Demo Call

Input: Demo call transcript

Output:

* Account Memo JSON (v1)
* Retell Agent Draft Spec (v1)

### Pipeline B – Onboarding Call

Input: Onboarding transcript

Output:

* Updated Account Memo JSON (v2)
* Updated Retell Agent Spec
* Changelog describing changes

---

## Folder Structure

outputs/accounts/account_001/v1/

* memo.json
* agent_spec.json

outputs/accounts/account_001/v2/

* memo.json
* agent_spec.json

changelog/account_001_changes.md

---

## Tech Stack

Python
Local file storage (JSON)
Rule-based extraction pipeline

---

## How to Run

1. Place transcripts inside:

   * data/demo_calls
   * data/onboarding_calls

2. Run the pipeline:

python run_pipeline.py

3. Outputs will be generated automatically in the outputs folder.

## Retell Setup

1. Create a free Retell account at https://retellai.com
2. Navigate to the Retell dashboard and create a new agent.
3. Copy the generated **Agent Draft Spec JSON** from:

outputs/accounts/<account_id>/v1/agent_spec.json

or

outputs/accounts/<account_id>/v2/agent_spec.json

4. In the Retell UI:

   * Paste the system prompt
   * Configure business hours variables
   * Configure call transfer rules

Because the free tier may not allow API-based agent creation, this project outputs a **Retell-compatible Agent Spec JSON** that can be manually imported into the Retell UI.

---

## Automation Setup

This project uses a lightweight Python-based pipeline instead of external orchestration tools.

To run the pipeline locally:

python run_pipeline.py

The script performs:

1. Transcript ingestion
2. Account Memo extraction
3. Agent Spec generation
4. Versioned output storage
5. Changelog generation

Outputs are automatically stored in the `outputs/accounts` directory.

---

## LLM Usage

This implementation follows the **zero-cost constraint** required by the assignment.

No external LLM APIs were used.

Instead, the system uses **rule-based extraction and prompt templating** implemented in Python scripts.

This ensures the pipeline remains fully reproducible without paid services.

---

## Data Privacy

All transcripts and recordings used in this project are treated as confidential.


Only structured outputs are included in the repository. Raw recordings are not published.
