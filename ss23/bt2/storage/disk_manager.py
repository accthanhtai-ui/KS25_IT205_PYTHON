import math

def calculate_disk_blocks(size_bytes, block_size=4096):
    return math.ceil(size_bytes / block_size)


def calculate_aspect_ratio(width, height):
    """
    Tính tỷ lệ khung hình (Aspect Ratio)
    """
    if height == 0:
        return None
    gcd = math.gcd(width, height)
    return f"{width//gcd}:{height//gcd}"