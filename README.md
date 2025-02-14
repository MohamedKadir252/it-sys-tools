# it-sys-tools

# 🖥️ IT System Tools - Python Scripts  

This repository contains **Python scripts for Linux system automation**, covering **system monitoring and user management**. These scripts are designed to help automate common system administration tasks, making them useful for IT professionals and students learning Linux infrastructure.  

## 📂 Repository Structure  
```
it-sys-tools/  
│── README.md  <- Project overview  
│── monitoring/  
│   ├── system_monitor.py  <- Monitors CPU, RAM, and Disk usage  
│── user_management/  
│   ├── user_manager.py  <- Adds, deletes, and lists Linux users  
```

## 🚀 Available Scripts  

### **📌 System Monitoring**  
**File:** `monitoring/system_monitor.py`  
🔹 Uses `psutil` to monitor **CPU, RAM, and Disk usage** in real-time.  
🔹 Can be extended to **log system metrics** or **trigger alerts** when usage is too high.  

### **📌 Linux User Management**  
**File:** `user_management/user_manager.py`  
🔹 Allows adding, deleting, and listing users in a Linux system.  
🔹 Uses `os.system()` to interact with Linux commands like `useradd`, `userdel`, and `cut`.  
🔹 Can be expanded with **role-based permissions** and **SSH key management**.  

## 📥 How to Use  
Clone the repository and run a script:  
```bash  
git clone https://github.com/MohamedKadir252/it-sys-tools.git  
cd it-sys-tools/monitoring  
python system_monitor.py  
```

For the user management script, **run with sudo**:  
```bash  
cd ../user_management  
sudo python user_manager.py  
```

## 🤝 Contributions  
Feel free to contribute by adding new automation scripts or improving existing implementations.  

## 📜 License  
This project is licensed under the MIT License.  


