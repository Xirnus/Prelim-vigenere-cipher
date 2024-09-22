from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

def home(request):
    return HttpResponse('Hello, World!')

    """
    Encrypts a message using the Vigenère cipher.

    Args:
        msg (str): The message to be encrypted.
        key (str): The encryption key.

    Returns:
        str: The encrypted message.

    The function handles both uppercase and lowercase letters. Non-alphabetic characters
    are not encrypted and are included in the output as-is.

    Example:
        >>> encrypt_vigenere("HELLO", "KEY")
        'RIJVS'
    """

    # generate keystream, that is a repeat of the key until it matches the length of the message
def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

    # encrypt the message using the Vigenère cipher, converts the character to its ASCII code, performs the encryption, and converts the result back to a character.
def encrypt_vigenere(msg, key):
    encrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)
    return "".join(encrypted_text)


    # decrypt the message using the Vigenère cipher, converts the character to its ASCII code, performs the decryption, and converts the result back to a character.
def decrypt_vigenere(msg, key):
    decrypted_text = [] 
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)

# render the index.html template
def index(request):
    return render(request, 'index.html')

# encrypt and decrypt views that take the message and key as query parameters, call the corresponding functions, and return the result as a JSON response.
def encrypt(request):
    msg = request.GET.get('msg', '')
    key = request.GET.get('key', '')
    encrypted_msg = encrypt_vigenere(msg, key)
    return JsonResponse({'encrypted_msg': encrypted_msg})

def decrypt(request):
    msg = request.GET.get('msg', '')
    key = request.GET.get('key', '')
    decrypted_msg = decrypt_vigenere(msg, key)
    return JsonResponse({'decrypted_msg': decrypted_msg})