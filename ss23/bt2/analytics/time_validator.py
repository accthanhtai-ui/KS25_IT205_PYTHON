from datetime import datetime, timedelta

def parse_and_validate_date(date_str):
    """
    Validate ngày upload + chống crash format sai
    """
    try:
        return datetime.strptime(date_str, "%Y-%m-%d"), True
    except ValueError:
        return None, False


def classify_upload_time(upload_date):
    """
    Phân loại video cũ / mới (30 ngày)
    """
    now = datetime(2026, 6, 16)  
    diff = now - upload_date

    if diff.days > 30:
        return "OLD"
    return "NEW"