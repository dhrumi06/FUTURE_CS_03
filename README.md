# FUTURE_CS_03

# 🔒 Secure File Sharing System

This project is a secure file sharing web application built with Python Flask and AES encryption.  
It allows users to upload files, which are then encrypted on the server, and later download them securely with automatic decryption.



# 📌 Project Objective

It simulates real-world secure file transfer for environments where data privacy is critical — such as healthcare, legal, or corporate sectors.

# Intern Details

**Name:** Dhrumi Sonani

**Role:** CyberSecurity

**Program:** Future Interns - Cybersecurity Internship

**Task:** Secure File Sharing System (Task 3)



**Key Features:**
- 📁 Upload files through a simple web portal.
- 🔐 AES encryption (CBC mode) for all files at rest.
- ✅ Decryption on download — files are only stored encrypted.
- 🔑 Basic key management using a static secret key.
- 📄 Simple frontend with HTML/CSS.



## ⚙️ **Tools & Technologies**

- **Backend:** Python 3, Flask
- **Encryption:** PyCryptodome (AES)
- **Frontend:** HTML, CSS
  


# 🗂️ **Project Structure**


secure_file_sharing/
│
├── run.py
├── requirements.txt
├── uploads_encrypted/
│
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── encryption.py
│ ├── config.py
│ ├── templates/
│ │ └── index.html
│ └── static/
│ └── style.css



1️⃣ **How to Run Locally**

git clone https://github.com/YOUR-USERNAME/secure-file-sharing.git
cd secure-file-sharing

2️⃣ Create a virtual environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the Flask server
python run.py

5️⃣ Open in browser
http://127.0.0.1:5000/



# 🔑 How It Works
Upload: Users upload a file → the app reads it in bytes → encrypts it with AES → stores only the encrypted .enc version.

Download: User clicks download → the app reads the .enc → decrypts it in memory → sends the original file back.\



# 📈 Future Enhancements
🔐 Use environment variables for the secret key.

🔑 Add key rotation and user-based key management.

🧑‍💻 Implement user authentication.

📜 Add file integrity checks (e.g., hashing).

📁 Add file size limits and type restrictions.

