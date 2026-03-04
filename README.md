# clara-ai-assignment
# Clara AI Automation Pipeline

## Overview
This project builds an automation pipeline that converts demo and onboarding call transcripts into structured AI agent configurations.

## Architecture

Demo Call Transcript
        ↓
Data Extraction
        ↓
Account Memo JSON (v1)
        ↓
Agent Prompt Generator
        ↓
Retell Agent Draft Spec

Onboarding Transcript
        ↓
Update Account Memo
        ↓
Generate v2 Agent Spec
        ↓
Create Changelog

## Outputs

outputs/accounts/account_001/v1/
memo.json
agent_spec.json

outputs/accounts/account_001/v2/
memo.json
agent_spec.json

changelog/account_001_changes.md

## Tech Stack

Python
Kaggle Notebook
JSON-based storage
Rule-based extraction

## How to Run

1. Upload transcripts
2. Run the notebook
3. Outputs will be generated automatically
