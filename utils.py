# Utility functions for the AI assistant

import json

def load_config(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config

def save_config(file_path, config):
    with open(file_path, 'w') as file:
        json.dump(config, file, indent=4)

def print_welcome_message():
    print("Welcome to My AI Assistant!")
