# Vigenere Cipher Web Application
## This web application allows users to encrypt and decrypt messages using the Vigenere Cipher. It provides a user-friendly interface with text areas for plaintext, key, and ciphertext input, as well as buttons to switch between encoding and decoding modes.

### Authors: James Edward L. Verceles & Richard Joseph Dela Cruz
### Date: Start of Project: September 20, 2024, Last Modification: September 22, 2024
### Version: v1.0.0
### Purpose: A method of encrypting alphabetic text by using a series of interwoven Caesar ciphers based on the letters of a keyword. Though the 'chiffre indéchiffrable' is easy to understand and implement, for three centuries it resisted all attempts to break it.


## System Requirements 

### Hardware:
    
#### CPU: 1 core (2.0+ GHz)
#### RAM: 512 MB to 1 GB (preferably 1 GB)
#### Storage: 5-10 GB SSD (for Django, static files, and database)
#### Network: At least 100 Mbps connection for small-scale traffic

### Software:

#### Operating System: Ubuntu 20.04+ (or other Linux distros), Windows, or macOS

### Browsers:
    
#### A modern browser like Chrome, Firefox, Safari, or Edge to properly render the Tailwind CSS styles and handle the JavaScript.

## Functional Description: 

#### Input: Expected Data Formats and Sources
    
1. Plaintext Input:
    - Format: String
    - Source: User input via the "Plaintext" textarea.

2. Key Input:
    - Format: String (alphanumeric characters)
    - Source: User input via the "Key" textarea.

3. Ciphertext Input (for decoding):
    - Format: String
    - Source: User input via the "Ciphertext" textarea.

#### Output: Generated Data, Formats, and Destinations

1. Encrypted Data:
    - Format: String (ciphertext)
    - Destination: Displayed in the "Ciphertext" textarea after a successful encryption AJAX call to the Django backend.

2. Decrypted Data:
    - Format: String (plaintext)
    - Destination: Displayed in the "Plaintext" textarea after a successful decryption AJAX call to the Django backend.

3.  AJAX Requests:
    - Encryption Endpoint: POST /encrypt/
        - Input Data: JSON object with keys: msg (plaintext) and key.
        - Response Format: JSON object containing the encrypted message.
    - Decryption Endpoint: POST /decrypt/
        - Input Data: JSON object with keys: msg (ciphertext) and key.
        - Response Format: JSON object containing the decrypted message.

#### Processing Steps

1. Generate Key:
    - Function: generate_key(msg, key)
    - Input:
        - msg: String (the message to be encrypted or decrypted)
        - key: String (the encryption key)
    - Process: Extends the key to match the length of the message by repeating it.
    - Output: String (the generated key)

2. Encrypt Message:
    - Function: encrypt_vigenere(msg, key)
    - Input:
        - msg: String (plaintext to encrypt)
        - key: String (encryption key)
    - Process:
        - Generates the key using generate_key().
        - Iterates over each character in the message, converting it to its ASCII code, performing encryption using the Vigenère formula, and converting it back to a character.
    - Output: String (encrypted message)

3. Decrypt Message:
    - Function: decrypt_vigenere(msg, key)
    - Input:
        - msg: String (ciphertext to decrypt)
        - key: String (encryption key)
    - Process:
        - Generates the key using generate_key().
        - Iterates over each character in the message, converting it to its ASCII code, performing decryption using the Vigenère formula, and converting it back to a character.
    - Output: String (decrypted message)

#### Django Views for Encryption and Decryption
 
4. Encryption View:
    - Function: encrypt(request)
    - Input: Query parameters from the request:
        - msg: The plaintext to encrypt (String)
        - key: The encryption key (String)
    - Process:
        - Calls encrypt_vigenere() with the message and key.
        - Returns a JSON response with the encrypted message.
    - Output: JSON object containing {'encrypted_msg': encrypted_message}

5. Decryption View:
    - Function: decrypt(request)
    - Input: Query parameters from the request:
        - msg: The ciphertext to decrypt (String)
        - key: The encryption key (String)
    - Process:
        - Calls decrypt_vigenere() with the message and key.
        - Returns a JSON response with the decrypted message.
    - Output: JSON object containing {'decrypted_msg': decrypted_message

## Security Considerations

1. Vulnerability Assessment: Identification of Potential Security Risks   
    - Input Validation:   
        - Risk of injection attacks (e.g., JavaScript injection) through unsanitized user input.   
    - Data Leakage:   
        - Sensitive data (e.g., plaintext) could be exposed through inadequate protection or logging.   
    - Denial of Service (DoS):   
        - The application could be vulnerable to DoS attacks if not properly managed, especially with heavy computations.   

2. Mitigation Strategies: Measures to Address Identified Vulnerabilities
    - Input Validation:   
        - Sanitize and validate all user inputs to ensure they conform to expected formats (e.g., only allow alphanumeric characters for keys).   
    - Data Leakage:   
        - Implement secure logging practices and avoid logging sensitive information. Use HTTPS to encrypt data in transit.   
    - Denial of Service (DoS):   
        - Limit request rates (rate limiting) and implement timeout mechanisms for long-running processes.   
   
4. Testing: Procedures for Verifying Security Measures   
 
    - Static Code Analysis:   
        - Use tools to analyze the source code for vulnerabilities and coding standards (e.g., Bandit for Python).    
    - Dynamic Application Security Testing (DAST):    
        - Perform automated testing of the running application to identify security vulnerabilities, such as SQL injection and XSS.   
    - Penetration Testing:   
        - Conduct manual testing to simulate attacks and evaluate the security posture of the application.    

## Usage Instructions

### Installation: Steps to Set Up the Program Environment

#### Prerequisites:
- Ensure you have Python (3.7 or higher) installed on your system.
- Install pip (Python package installer), which usually comes with Python.

#### Create a Virtual Environment:
- Open a terminal and navigate to your project directory.
- Create a virtual environment to isolate dependencies.

        python -m venv (virtual environment name)

Activate the virtual environment:

#### On Windows:

    venv\Scripts\activate

#### On macOS/Linux:

    source venv/bin/activate

#### Install Django and Dependencies:

    pip install django
    python -m pip install django-tailwind
    Node js https://nodejs.org/en

#### Starting the webserver

    cd mywebsite

#### MUST BE IN 2 SEPERATE TERMINALS

#### To start tailwind
    python manage.py tailwind start

#### To start Django server
    python manage.py runserver


## Error Handling

Error Codes: The cipher does not receive any error as it does not process other characters apart from a string.
Recovery Procedures: No recovery procedures are needed.

## Maintenance Log

Date: September 20, 2024      
Author: James Edward L. Verceles   
Changes: Start of Project.      

Date: September 20, 2024      
Author: James Edward L. Verceles   
Changes: Changed Website Apperance      
- changed text box, background color, added a logo      
 

Date: September 21, 2024     
Author: James Edward L. Verceles    
Changes: Revamp the website     
- changed the bar at the top, changed the input text areas, added key text area and footer      

Date: September 21, 2024      
Author: James Edward L. Verceles   
Changes: Finished main functions     
- Added the way the website send data to django backend and vice versa,
- added index.html docs
- made the plaintext and ciphertext swap places when decode or encode button is clicked       
 
Date: September 22, 2024      
Author: James Edward L. Verceles   
Changes: Small Changes     
- small changes to author name and documentation txt       

Date: September 22, 2024       
Author: James Edward L. Verceles   
Changes: Finishing Touches    
- Removed unnecessary code
- Changed docs
- added docs to codes 
