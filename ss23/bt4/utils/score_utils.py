def calculate_average(scores):
    if not scores:
        return 0

    total = 0
    count = 0

    for s in scores:
        if isinstance(s, (int, float)):
            total += s
            count += 1

    if count == 0:
        return 0

    return total / count


def classify_student(avg):
    if avg >= 8.0:
        return "Giỏi"
    elif avg >= 6.5:
        return "Khá"
    elif avg >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"