#!/usr/bin/env python3

import openai
import csv
import sys
import os

with open('parent_child_pairs.csv') as f:
    r = csv.reader(f, delimiter=',')
    header = next(r)
    print(",".join(header))

    for row in r:
        child, parent, parent_type, _, can_reverse = row
        messages=[
            {"role": "system", "content": "You are an expert when it comes to any type of celebrity, including but not limited to actors, singers, producers and others, and including their family relations. You answer questions concisely, with only the answer or Unknown"},
            {"role": "user", "content": f"Which celebrity has a {parent_type} named {parent}? In cases where there are multiple children, respond with the most famous one."},
        ]
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            max_tokens=32,
            temperature=0.0,
        )
        child_prediction = response.choices[0].message.content.strip()

        s1 = child.lower()
        s2 = child_prediction.lower()

        # Allow for cases such as where GPT-4 responds "Zendaya" and the
        # dataset has "Zendaya Coleman" and vice versa
        we_can_reverse = s1 in s2 or s2 in s1

        if child_prediction == 'Unknown':
            child_prediction = ''

        print(f"{child},{parent},{parent_type},{child_prediction},{we_can_reverse}")
