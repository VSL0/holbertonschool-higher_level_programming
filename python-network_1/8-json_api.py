#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]

    payload = {'q': q}
    try:
        r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
        json_data = r.json()
        if json_data == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
    except ValueError:
        print("Not a valid JSON")
