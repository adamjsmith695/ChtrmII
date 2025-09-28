NOTE: MUST INSTALL `pygetwindow` using 'pip install pygetwindow' in command prompt before running chtrmII.py.

# ChtrmII – Retro Console Python Chatroom

A **custom-built console-based chatroom** designed entirely from scratch in Python, demonstrating **real-time communication, encryption, and moderation**. This project showcases a lightweight, functional messaging platform with a focus on **security, user experience, and modular code design**.

## Overview

ChtrmII simulates a retro-style console chatroom with multiple interactive windows. It implements **custom user authentication** linked to device MAC addresses, a **bespoke encryption system** for all sensitive information, and a **sophisticated profanity filter**. The project explores **file-based message logging**, multi-process input/output handling, and interactive command management, reflecting a strong understanding of Python, system I/O, and security practices.

## Features

- **Custom User Authentication:**  
  Secure account creation and login tied to device identifiers, with username and password validation and sanitisation.
- **Bespoke Encryption System:**  
  All sensitive data is encrypted using a custom cipher and shuffle/unscramble method, ensuring stored credentials and messages are secure.
- **Real-Time Multi-Window Communication:**  
  Separate input and output windows managed via Python subprocesses for smooth concurrent message sending and receiving.
- **File-Based Logging:**  
  Maintains a running log of all messages (`chtLog.txt`) and supports commands like `/clearlog` to manage chat history.
- **Profanity Filtering:**  
  Advanced censorship system detects letter substitutions, repeated characters, and variations to filter inappropriate content dynamically.
- **Interactive Commands:**  
  Includes `/help`, `/date`, `/quit`, and more for user guidance and chatroom management.
- **Lightweight and Modular Design:**  
  Structured for maintainability, readability, and future enhancements.

## Installation

1. Clone the repository
2. pip install pygetwindow in Command Prompt
3. Ensure the following files are present in the project directory:
   - chtrmII.py (launcher)
   - chtrmin.py (input console)
   - chtrmout.py (output console)
   - encryption.py (custom encryption module)
   - censor.py (profanity filter)
   - _db__.txt (encrypted user database)
   - certificate.txt (encryption key certificate)
   - chtLog.txt (chat log)
4. Run the launcher `chtrmII.py`.

## Usage

- Follow the prompts to **create an account** or **login**.  
- The system opens separate **input** and **output windows** for sending and viewing messages.  
- Use the commands:  
  - `/help` for guidance  
  - `/date` to view the date  
  - `/quit` to exit safely  
- Messages are automatically logged in `chtLog.txt`.

## Technical Highlights

- Implemented **custom encryption and decryption** using **mathematical ciphering** and **key-based shuffling**.  
- Managed **multi-process console I/O** to simulate a **real-time chat experience**.  
- Developed **dynamic input sanitisation and censorship** to handle **text variations** and **symbol substitutions**.  
- Designed the system to be **device-aware** via **MAC address tracking** for account uniqueness.  

**ChtrmII** demonstrates a **professional-level Python project** combining **security**, **user interface design**, and **system-level programming**, ideal for showcasing **coding proficiency** and **systems thinking**.
