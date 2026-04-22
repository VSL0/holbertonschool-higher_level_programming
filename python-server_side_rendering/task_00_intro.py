import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected str, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print(f"Error: Invalid input type for attendees. Expected list of dictionaries, got {type(attendees).__name__}")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, 1):
        invitation = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            invitation = invitation.replace("{" + key + "}", str(value))

        filename = f"output_{i}.txt"
        with open(filename, 'w') as f:
            f.write(invitation)
