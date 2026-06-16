import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logger = logging.getLogger(__name__)


def get_shipping_rate(method: str, distance: int) -> float:
    """Trả về chi phí vận chuyển cơ sở"""

    logger.info(
        f"Đang tính phí giao hàng cho phương thức {method} với khoảng cách {distance} km"
    )

    if distance <= 0:
        raise ValueError("Distance must be positive")

    if method == "standard":
        base_rate = 15000
    elif method == "express":
        base_rate = 30000
    elif method == "next_day":
        base_rate = 50000
    else:
        base_rate = 20000

    if distance >= 20:
        base_rate += 10000

    return base_rate


def calculate_final_shipping(
        weight: float,
        distance: int,
        method: str) -> float:

    if weight < 0:
        raise ValueError("Trọng lượng hàng hóa không được âm")

    base_rate = get_shipping_rate(method, distance)

    total_cost = base_rate + (weight * 2000)

    logger.warning(
        f"Kết quả: Tổng phí vận chuyển = {total_cost}"
    )

    return total_cost


if __name__ == "__main__":
    calculate_final_shipping(3.5, 25, "express")
    calculate_final_shipping(2.0, -5, "standard")

# # Smart Shipping System

# ## Mô tả
# Chương trình tính phí vận chuyển dựa trên khoảng cách và phương thức giao hàng.

# ## Chức năng
# - Standard Shipping
# - Express Shipping
# - Next Day Shipping
# - Phụ thu khoảng cách từ 20 km trở lên
# - Logging theo chuẩn INFO
# - Xử lý ngoại lệ bằng ValueError

# ## Công nghệ sử dụng
# - Python 3
# - Visual Studio Code
# - GitHub