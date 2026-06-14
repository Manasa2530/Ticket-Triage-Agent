# Ticket Triage Agent

## Team Members
- Vuggina Sri Sai Manasa
- Sennamsetti Eswara Rao
- Pilla Prudhvi Sai Manikanta
- Purri Preethi Sree Varsha

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