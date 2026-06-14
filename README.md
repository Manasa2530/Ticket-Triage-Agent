# Ticket Triage Agent

## Overview
An AI-powered Ticket Triage Agent that classifies support tickets using Google Gemini API and assigns priorities.

## Features
- Reads tickets from JSON files
- Uses Gemini AI for classification
- Stores results in SQLite database
- Generates CSV output

## Technologies Used
- Python
- Google Gemini API
- SQLite
- JSON
- CSV

## Setup
1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Add Gemini API key in .env

## Run
python main.py

## Output
Results are generated in output/results.csv