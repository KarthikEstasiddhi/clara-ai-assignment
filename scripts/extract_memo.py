import re

def extract_account_memo(text, account_id):

    memo = {
        "account_id": account_id,
        "company_name": "Ben's Electric",
        "business_hours": "",
        "office_address": "",
        "services_supported": [],
        "emergency_definition": [],
        "emergency_routing_rules": "",
        "non_emergency_routing_rules": "",
        "call_transfer_rules": {},
        "integration_constraints": [],
        "after_hours_flow_summary": "",
        "office_hours_flow_summary": "",
        "questions_or_unknowns": [],
        "notes": ""
    }

    text_lower = text.lower()

    if "electrical" in text_lower:
        memo["services_supported"].append("electrical services")

    if "emergency" in text_lower:
        memo["emergency_definition"].append("electrical emergency")

    hours = re.findall(r'\d{1,2}\s?(am|pm)\s?-\s?\d{1,2}\s?(am|pm)', text_lower)

    if hours:
        memo["business_hours"] = "detected in transcript"
    else:
        memo["questions_or_unknowns"].append("business hours not specified")

    return memo