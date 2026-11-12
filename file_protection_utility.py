import base64
from pathlib import Path

DATA_FILE = Path("protected_data.txt")


def protect_text():
    text = input("Enter sample text to protect: ")
    key = input("Create a key (remember it): ")

    if not text or not key:
        print("Text and key cannot be empty.")
        return

    text_bytes = text.encode("utf-8")
    key_bytes = key.encode("utf-8")

    protected_bytes = bytes(
        value ^ key_bytes[index % len(key_bytes)]
        for index, value in enumerate(text_bytes)
    )

    encoded_text = base64.b64encode(protected_bytes)
    DATA_FILE.write_bytes(encoded_text)
    print("Demo-protected text saved in protected_data.txt")


def restore_text():
    if not DATA_FILE.exists():
        print("No protected_data.txt found. Protect some text first.")
        return

    key = input("Enter the same key: ")

    if not key:
        print("Key cannot be empty.")
        return

    key_bytes = key.encode("utf-8")
    protected_bytes = base64.b64decode(DATA_FILE.read_bytes())

    restored_bytes = bytes(
        value ^ key_bytes[index % len(key_bytes)]
        for index, value in enumerate(protected_bytes)
    )

    try:
        print("Restored text:", restored_bytes.decode("utf-8"))
    except UnicodeDecodeError:
        print("That key did not restore readable text. Check the key and try again.")


def main():
    while True:
        print("\nFile Protection Utility - Demo")
        print("1. Protect text")
        print("2. Restore text")
        print("3. Exit")

        choice = input("Choose 1, 2, or 3: ").strip()

        if choice == "1":
            protect_text()
        elif choice == "2":
            restore_text()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()