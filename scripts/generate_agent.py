def generate_agent_spec(memo, version):

    prompt = f"""
You are Clara AI receptionist for {memo['company_name']}.

BUSINESS HOURS FLOW
- greet caller
- ask reason for call
- collect name and phone
- transfer call
- fallback if transfer fails
- close call

AFTER HOURS FLOW
- greet caller
- ask if emergency
- collect name phone address
- transfer call
- fallback if transfer fails
"""

    return {
        "agent_name": memo["company_name"] + " Assistant",
        "voice_style": "professional",
        "version": version,
        "system_prompt": prompt
    }