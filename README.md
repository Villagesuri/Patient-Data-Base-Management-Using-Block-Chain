# 🏥 **Blockchain-Based Patient Data Management System**

A simple blockchain implementation in Python designed to **securely store patient medical records** using cryptographic hashing and Proof-of-Work. This project demonstrates how blockchain can be applied to healthcare for tamper-proof and verifiable data storage.

---

# 📄 **Description**

This project implements a basic blockchain used to manage and store patient information securely. Each patient’s details—such as ID, name, age, and diagnosis—are added as data and stored inside mined blocks. The system uses SHA-256 hashing and a Proof-of-Work algorithm to maintain data integrity.

The blockchain includes:

* Creation of the **genesis block**
* Addition of new patient records
* **Mining** new blocks by solving PoW puzzles
* Validation of the blockchain to ensure no tampering
* Secure block linking through cryptographic hashing

This project serves as a foundational example of using blockchain technology in digital healthcare systems.

---

# 🛠 **Technologies Used**

* **Python 3.x**
* **hashlib** – for SHA-256 hashing
* **json** – to format block data
* **time** – to generate timestamps

---

# 🏗 **Project Structure**

```
├── blockchain.py        # Main file containing Blockchain class
├── README.md            # Project documentation
└── requirements.txt     # (Optional) Dependencies list
```

Key components inside `blockchain.py`:

* `Blockchain` class
* `create_block()`
* `add_patient_data()`
* `proof_of_work()`
* `valid_proof()`
* `hash()`
* `is_chain_valid()`

---

# ⚙️ **How It Works**

### 🔹 1. **Genesis Block Creation**

The blockchain starts with a predefined “genesis block” having an arbitrary proof and previous hash.

### 🔹 2. **Adding Patient Records**

Each time patient details (ID, name, age, diagnosis) are added, they are stored temporarily until a block is mined.

### 🔹 3. **Mining a Block**

A Proof-of-Work algorithm attempts different values until a hash starting with **"0000"** is found.

### 🔹 4. **Hash Linking**

Every block contains the hash of the previous block, ensuring a secure chain.

### 🔹 5. **Chain Validation**

The system checks:

* If each block's hash matches the previous block
* If all proofs are valid

---

# 📌 **Example Output**

```
Adding patient data...
New Block Mined: {
    "index": 2,
    "timestamp": 1733039400.1234,
    "data": [
        {
            "patient_id": "P001",
            "name": "Surya",
            "age": 30,
            "diagnosis": "Fever"
        },
        {
            "patient_id": "P002",
            "name": "Suresh",
            "age": 40,
            "diagnosis": "Common cold"
        }
    ],
    "proof": 52983,
    "previous_hash": "0000afc9b34f8..."
}
Is Blockchain valid? True
```

---

# ▶️ **How to Run the Program**

### **1️⃣ Clone the Repository**

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### **2️⃣ Run the Python Script**

Make sure Python 3 is installed.

```
python blockchain.py
```

### **3️⃣ View Output**

The program will:

* Add sample patient records
* Mine a new block
* Display the full blockchain
* Validate the chain

---

