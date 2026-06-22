class product:
    def __init__(self,id ,name  ,import_price  ,quantity ,storage_fee):
        self.id = id # id
        self.name = name # tên
        self.import_price = import_price #giá nhập 
        self.quantity = quantity #Số lượng tồn kho
        self.storage_fee = storage_fee #Chi phí lưu kho phát sinh
        self.total_value = 0 #tổng số lượng
        self.stock_status = "" #số lượng tồn kho
    def calculate_total_value(self):
        self.total_value = self.import_price * self.quantity + self.storage_fee
    def classify_stock_status(self):
        if self.total_value < 9000000:
            print("Thấp (An toàn)")
        elif self.total_value < 15000000:
            print("Trung bình")
        elif self.total_value < 30000000:
            print("Cao (Cần chú ý)")
        else:
            print("Rất cao (Rủi ro ứ đọng vốn)")
class ProductManager:
    def __init__(self):
        