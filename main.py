import os
import json
import csv

from classifier import classify_ticket


results = []


for file in os.listdir("tickets"):

    path = os.path.join(
        "tickets",
        file
    )

    with open(path, "r") as f:

        ticket = json.load(f)

        answer = classify_ticket(ticket)

        results.append({
            "ticket_id": ticket["ticket_id"],
            "category": answer["category"],
            "priority": answer["priority"],
            "reason": answer["reason"]
        })


with open(
    "output/results.csv",
    "w",
    newline=""
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "ticket_id",
            "category",
            "priority",
            "reason"
        ]
    )

    writer.writeheader()

    writer.writerows(results)


print("All tickets classified successfully!")