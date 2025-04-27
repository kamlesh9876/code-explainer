# Python Code Explainer

## Overview

The **Python Code Explainer** is a web application built using Flask, which allows users to paste Python code and get a detailed explanation of what the code does. The application features:

- **Syntax highlighting** for Python code.
- **Auto-suggestions** for common Python keywords.
- **Error handling** for invalid code.

## Features

- **Interactive UI**: Clean and modern design.
- **Python Code Parsing**: The app explains Python code by parsing it and returning a readable explanation.
- **Auto-suggestions**: While typing, the input box provides Python keyword suggestions.
- **Loading Indicator**: Displays "Processing..." while the explanation is being fetched.
- **Error Handling**: Alerts the user with a message if something goes wrong.

## Requirements

Before running the application, ensure you have the following dependencies installed:

- Python 3.x
- Flask
- Awesomplete (for autocomplete suggestions)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/python-code-explainer.git
   cd python-code-explainer
