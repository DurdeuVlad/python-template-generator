# Python Template Generator

## Introduction

This project is a Python desktop app that lets you generate customized Word documents automatically. Instead of manually editing a template every time you need a new file, you input the variables once and the app handles the rest.

It has a simple front-end where you can fill in your data, pick your template, and set your output path. Behind the scenes, it plugs everything into a .docx file and generates a clean final document.

Built it to save time when dealing with repetitive document creation.

## What It Does

Simple GUI for entering variable values  
Selects template and output file location  
Replaces variables in the .docx template  
Saves a ready-to-use Word document  
Supports saving and loading template settings for reusability

## Requirements

Python 3.x  
tkinter (comes with Python)  
python-docx

## File Structure

- `frontEnd.py`: GUI for input and interaction
- `templateGenerator.py`: handles template logic and document generation
- `template.docx`: sample template with variable fields
- `RaportProiect.docx`: project documentation

## How to Use

### 1. Clone the repo

```bash
git clone https://github.com/DurdeuVlad/python-template-generator.git
cd python-template-generator
```

### 2. Install dependencies

```bash
pip install python-docx
```

### 3. Prepare your template

Put your `.docx` template file into the project folder. It should have variable placeholders.

### 4. Launch the app

```bash
python frontEnd.py
```

### 5. Fill out variables

Fill in all the required fields. Pick your template and choose where you want to save the output.

### 6. Generate

Click "Generate" and the app will create your customized document.
