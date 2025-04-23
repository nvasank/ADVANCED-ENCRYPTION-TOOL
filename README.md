# ADVANCED-ENCRYPTION-TOOL
### Tool Description: Advanced Encryption Tool (AES-256)
The Advanced Encryption Tool is a robust, Python-based file security application developed to provide secure encryption and decryption capabilities using the AES-256 (Advanced Encryption Standard) algorithm in CBC (Cipher Block Chaining) mode. This tool is created as part of Task - 4 of the CodTech Internship Program, aimed at enhancing data confidentiality and protection in modern computing environments.

In an age where data breaches and cyber intrusions are rampant, protecting sensitive information has become paramount. Whether it's personal documents, company records, or confidential research, secure file encryption is a non-negotiable security measure. This tool bridges the gap between complex cryptographic principles and user-friendly file security by offering a simple interface backed by robust security practices.

---

### Purpose
The main objective of this tool is to facilitate strong encryption and decryption of files, ensuring that only authorized users with the correct password can access the data. Leveraging AES-256, which is widely regarded as one of the most secure encryption algorithms in use today, the tool guarantees high levels of data confidentiality, integrity, and resistance against brute-force and cryptanalytic attacks.

This tool serves both educational and practical purposes—ideal for students learning cybersecurity principles and professionals seeking a quick encryption utility for sensitive data management.

---

### How It Works
### **Encryption Phase:**

- A user supplies the file and a strong password.

- The system generates a random 16-byte salt and IV (Initialization Vector).

- A PBKDF2 (Password-Based Key Derivation Function 2) function, using SHA-256, transforms the password and salt into a secure 32-byte key.

- The plaintext file content is padded, encrypted using AES-256 in CBC mode, and written to a .enc file.

### **Decryption Phase:**

- The user provides the encrypted file and the same password.

- The tool extracts the original salt and IV from the encrypted blob.

- Using the same PBKDF2 function, the key is regenerated.

- The content is decrypted, unpadded, and written to a .dec file, restoring the original data.

---

### Features
-  AES-256 Encryption: Industry-standard security for highly sensitive information.

-  Password-Based Key Derivation: Ensures even weak passwords are hardened using PBKDF2 with SHA-256.

-  Random Salt & IV: Enhances security by preventing pattern detection in encrypted data.

-  Dual Mode: Supports both file encryption and decryption with automatic filename handling.

-  Lightweight & Standalone: Minimal dependencies (cryptography package), making it portable and efficient.

---

### Technologies Used
Python 3.x

cryptography library for AES and secure key derivation

os, base64 for file handling and encoding
