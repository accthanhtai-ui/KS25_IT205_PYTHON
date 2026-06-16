import random
import string

def generate_assignment_code():
    code = "PY-" + "".join(
        random.choices(string.ascii_uppercase + string.digits, k=4)
    )

    print("--- SINH MÃ BÀI TẬP ---")
    print(f"Mã bài tập của bạn là: {code}")