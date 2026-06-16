import os
def safe_create_dir(path):
    os.makedirs(path, exist_ok=True)
def move_file(filename, target_dir):
    """
    Mô phỏng di chuyển file vào thư mục lưu trữ
    """
    safe_create_dir(target_dir)
    target_path = os.path.join(target_dir, filename)
    return target_path