from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

def home(request):
    return HttpResponse('Hello, World!')

def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

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

def index(request):
    return render(request, 'index.html')

def process(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')
        key = request.POST.get('key', '')
        action = request.POST.get('action', '')

        if action == 'encode':
            output_text = encrypt_vigenere(input_text, key)
        elif action == 'decode':
            output_text = decrypt_vigenere(input_text, key)
        else:
            return JsonResponse({'error': 'Invalid action'}, status=400)

        return JsonResponse({'output_text': output_text})
    return JsonResponse({'error': 'Invalid request'}, status=400)