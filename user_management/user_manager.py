import os

def add_user(username):
    os.system(f"sudo useradd {username}")
    print(f"👤 Utilisateur {username} ajouté.")

def delete_user(username):
    os.system(f"sudo userdel {username}")
    print(f"❌ Utilisateur {username} supprimé.")

def list_users():
    os.system("cut -d: -f1 /etc/passwd")

if __name__ == "__main__":
    print("1. Ajouter un utilisateur\n2. Supprimer un utilisateur\n3. Lister les utilisateurs")
    choice = input("Choisissez une option : ")
    if choice == "1":
        username = input("Entrez le nom d'utilisateur : ")
        add_user(username)
    elif choice == "2":
        username = input("Entrez le nom d'utilisateur : ")
        delete_user(username)
    elif choice == "3":
        list_users()
    else:
        print("Option invalide.")
