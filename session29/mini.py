"""
Dự án: Rikkei Smart Factory IoT Simulator
Tác giả: Thanh Tài
Mô tả: Hệ thống quản lý thiết bị IoT sử dụng các khái niệm OOP (Abstract Class, Inheritance, MRO, Polymorphism, Duck Typing).
"""

from abc import ABC, abstractmethod
import logging

# Sử dụng logging thay cho print thô để bẫy lỗi chuyên nghiệp
logging.basicConfig(level=logging.INFO, format='%(message)s')

# ==========================================
# 1. ABSTRACT BASE CLASS & LỚP CON
# ==========================================
class BaseDevice(ABC):
    factory_name = "Rikkei Smart Factory"
    base_maintenance_cost = 1000000

    def __init__(self, device_code, device_name):
        self.device_code = device_code
        self._device_name = ""
        self.device_name = device_name  # Gọi setter để chuẩn hóa tên
        self.__operating_hours = 0      # Biến private đóng gói nghiêm ngặt

    @property
    def device_name(self):
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        # In hoa và xóa khoảng trắng thừa
        self._device_name = " ".join(value.split()).upper()

    @property
    def operating_hours(self):
        return self.__operating_hours

    def add_hours(self, hours):
        if hours <= 0:
            raise ValueError("ERR-IOT-03")
        self.__operating_hours += hours

    @staticmethod
    def validate_device_code(device_code):
        # Mã phải đúng 10 ký tự và bắt đầu bằng chữ cái
        if len(device_code) == 10 and device_code[0].isalpha():
            return True
        return False

    @classmethod
    def update_maintenance_cost(cls, new_cost):
        cls.base_maintenance_cost = new_cost

    @abstractmethod
    def track_performance(self):
        pass

    @abstractmethod
    def run_diagnostic(self):
        pass

    # Operator Overloading: Nạp chồng toán tử cộng (+)
    def __add__(self, other):
        if not isinstance(other, BaseDevice):
            raise TypeError("ERR-IOT-04")
        return self.operating_hours + other.operating_hours

    # Operator Overloading: Nạp chồng toán tử so sánh (<)
    def __lt__(self, other):
        if not isinstance(other, BaseDevice):
            raise TypeError("ERR-IOT-04")
        return self.operating_hours < other.operating_hours


class ProductionRobot(BaseDevice):
    def __init__(self, device_code, device_name):
        super().__init__(device_code, device_name)
        self.completed_products = 0

    def track_performance(self):
        if self.operating_hours == 0:
            return 0.0
        # Tính OEE đơn giản (sản lượng / giờ)
        return round((self.completed_products / self.operating_hours), 2)

    def run_diagnostic(self):
        if self.completed_products > 10000:
            return f"Nguy hiểm: Vượt ngưỡng sản lượng! (Hiện tại: {self.completed_products} sản phẩm)"
        return "Bình thường"


class ThermalSensor(BaseDevice):
    def __init__(self, device_code, device_name):
        super().__init__(device_code, device_name)
        self.current_temperature = 0.0
        self.safety_threshold = 80.0

    def track_performance(self):
        return self.current_temperature

    def run_diagnostic(self):
        if self.current_temperature > self.safety_threshold:
            return f"Nguy hiểm: Vượt ngưỡng nhiệt! (Nhiệt độ hiện tại: {self.current_temperature} độ C / Ngưỡng an toàn: {self.safety_threshold} độ C)"
        return "Bình thường"


class HybridSmartActuator(ProductionRobot, ThermalSensor):
    # Kế thừa đa luồng: Tự động tuân theo MRO
    def __init__(self, device_code, device_name):
        BaseDevice.__init__(self, device_code, device_name)
        self.completed_products = 0
        self.current_temperature = 0.0
        self.safety_threshold = 80.0

    def track_performance(self):
        # Gọi đa hình, lấy chỉ số của cả Robot và Cảm biến
        return f"OEE: {ProductionRobot.track_performance(self)} | Nhiệt độ: {self.current_temperature}C"

    def run_diagnostic(self):
        diag_rob = ProductionRobot.run_diagnostic(self)
        diag_sen = ThermalSensor.run_diagnostic(self)
        if "Nguy hiểm" in diag_rob or "Nguy hiểm" in diag_sen:
            return f"{diag_sen} | {diag_rob}".strip(" | Bình thường")
        return "Bình thường"

# ==========================================
# 2. DUCK TYPING & HÀM TOÀN CỤC
# ==========================================
class MQTTEngineGateway:
    def process_stream(self, data):
        print("[Hệ thống MQTT Engine]: Đang khởi tạo băng thông kết nối dữ liệu IoT...")
        print("Xác thực cổng ngoại vi bằng Duck Typing thành công!")
        print(data)

class ERPReportGateway:
    def process_stream(self, data):
        print("[Hệ thống ERP]: Đang đồng bộ số liệu vào hệ thống quản trị...")
        print("Xác thực cổng ngoại vi bằng Duck Typing thành công!")
        print(data)

def export_telemetry_data(data_gateway, device_object):
    # Kiểm tra xem object truyền vào có phương thức process_stream hay không
    if not hasattr(data_gateway, 'process_stream') or not callable(getattr(data_gateway, 'process_stream')):
        raise TypeError("ERR-IOT-05")
    
    data = f"Dữ liệu của thiết bị {device_object.device_code} đã được đóng gói và xuất chuỗi luồng thành công."
    data_gateway.process_stream(data)

# ==========================================
# 3. CLI MENU & LOGIC VẬN HÀNH CHÍNH
# ==========================================
def main():
    devices_list = []
    current_device = None

    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ THIẾT BỊ IOT ===")
        print("1. Đăng ký & Khởi tạo thiết bị IoT mới")
        print("2. Xem thông tin thiết bị & Thứ tự kế thừa (MRO)")
        print("3. Check-in giờ vận hành & Cập nhật hiệu suất")
        print("4. Thực thi quy trình tự chẩn đoán kỹ thuật")
        print("5. Cộng gộp thời gian tải & So sánh hao mòn")
        print("6. Xuất dữ liệu vận hành ra Cổng ngoại vi")
        print("7. Thoát chương trình")
        
        try:
            choice = input("Chọn chức năng (1-7): ").strip()
            if choice not in ['1', '2', '3', '4', '5', '6', '7']:
                raise ValueError("ERR-IOT-06")

            # CHỨC NĂNG 1
            if choice == '1':
                print("--- ĐĂNG KÝ THIẾT BỊ IOT MỚI ---")
                print("1. Production Robot (Robot sản xuất lắp ráp)")
                print("2. Thermal Sensor (Cảm biến nhiệt độ)")
                print("3. Hybrid Smart Actuator (Thiết bị truyền động lai)")
                
                type_choice = input("Chọn phân loại thiết bị (1-3): ").strip()
                code = input("Nhập mã thiết bị 10 ký tự: ").strip()
                name = input("Nhập tên thiết bị: ").strip()

                if not BaseDevice.validate_device_code(code):
                    logging.error("[Lỗi] (ERR-IOT-01): Mã thiết bị không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng tiền tố quy định.")
                    continue

                if type_choice == '1':
                    current_device = ProductionRobot(code, name)
                elif type_choice == '2':
                    current_device = ThermalSensor(code, name)
                elif type_choice == '3':
                    current_device = HybridSmartActuator(code, name)
                else:
                    logging.error("[Lỗi] (ERR-IOT-06): Lựa chọn không hợp lệ!")
                    continue
                
                devices_list.append(current_device)
                print(f"[Thành công]: Đăng ký thiết bị thành công!\nTên thiết bị: {current_device.device_name}")

            # CHỨC NĂNG 2
            elif choice == '2':
                if current_device is None:
                    logging.error("[Lỗi] (ERR-IOT-02): Thao tác bị từ chối! Hệ thống chưa có thông tin thiết bị hoạt động.")
                    continue
                
                print("--- THÔNG TIN THIẾT BỊ HIỆN TẠI ---")
                print(f"Loại thiết bị: {current_device.__class__.__name__}")
                print(f"Nhà máy: {current_device.factory_name}")
                print(f"Mã thiết bị: {current_device.device_code}")
                print(f"Tên thiết bị: {current_device.device_name}")
                print(f"Số giờ vận hành: {current_device.operating_hours} giờ")
                
                # Hiển thị MRO
                mro_names = [cls.__name__ for cls in current_device.__class__.__mro__]
                print(f"[Hệ thống MRO]: {' -> '.join(mro_names)}")

            # CHỨC NĂNG 3
            elif choice == '3':
                if current_device is None:
                    logging.error("[Lỗi] (ERR-IOT-02): Thao tác bị từ chối! Hệ thống chưa có thông tin thiết bị hoạt động.")
                    continue
                
                print("--- GHI NHẬN SỐ LIỆU VẬN HÀNH ---")
                try:
                    hours_str = input("Nhập số giờ chạy mới phát sinh: ")
                    if not hours_str.replace('.', '', 1).isdigit() or float(hours_str) <= 0:
                        raise ValueError("ERR-IOT-03")
                    
                    current_device.add_hours(float(hours_str))
                    
                    # Tự động cập nhật thêm thuộc tính tùy loại thiết bị mà không dùng if-else
                    if hasattr(current_device, 'completed_products'):
                        prod_str = input("Nhập số lượng sản phẩm hoàn thành mới bổ sung: ")
                        if not prod_str.isdigit() or int(prod_str) < 0:
                             raise ValueError("ERR-IOT-03")
                        current_device.completed_products += int(prod_str)
                        
                    if hasattr(current_device, 'current_temperature'):
                        temp_str = input("Nhập nhiệt độ hiện tại (độ C): ")
                        # Lọc nhiệt độ có thể âm hoặc dương
                        try:
                            current_device.current_temperature = float(temp_str)
                        except ValueError:
                            raise ValueError("ERR-IOT-03")

                    print("[Thành công]: Đã cập nhật số liệu vận hành.")
                    print(f"Tổng số giờ chạy tích lũy: {current_device.operating_hours} giờ.")
                    print(f"Chỉ số hiệu suất: {current_device.track_performance()}")

                except ValueError as e:
                    if str(e) == "ERR-IOT-03":
                        logging.error("[Lỗi] (ERR-IOT-03): Định dạng dữ liệu sai! Giá trị nhập vào phải là số lớn hơn 0.")
                    else:
                        logging.error(f"Lỗi hệ thống: {e}")

            # CHỨC NĂNG 4
            elif choice == '4':
                if current_device is None:
                    logging.error("[Lỗi] (ERR-IOT-02): Thao tác bị từ chối! Hệ thống chưa có thông tin thiết bị hoạt động.")
                    continue
                
                print("--- QUY TRÌNH TỰ CHẨN ĐOÁN LỖI KỸ THUẬT ---")
                diagnostic_result = current_device.run_diagnostic()
                
                if "Nguy hiểm" in diagnostic_result:
                    print("[Cảnh báo hệ thống]: Thiết bị phát hiện trạng thái bất thường!")
                    print(f"Kết quả chẩn đoán: {diagnostic_result}")
                    print(f"Định mức chi phí bảo trì dự kiến: {current_device.base_maintenance_cost:,} VND")
                else:
                    print("Thiết bị hoạt động ổn định trong ngưỡng an toàn.")

            # CHỨC NĂNG 5
            elif choice == '5':
                if current_device is None or len(devices_list) < 2:
                    print("Cần ít nhất 2 thiết bị trong hệ thống để thực hiện so sánh.")
                    continue
                
                print("--- KIỂM KÊ & SO SÁNH TẢI (OPERATOR OVERLOADING) ---")
                print(f"Thiết bị hiện tại (A): {current_device.device_code} (Số giờ chạy: {current_device.operating_hours} giờ)")
                
                print("Các thiết bị có sẵn để đối chiếu:")
                for i, dev in enumerate(devices_list):
                    if dev != current_device:
                        print(f"{i}. {dev.device_code} - {dev.device_name}")
                        
                target_idx = int(input("Chọn số thứ tự thiết bị (B): "))
                other_device = devices_list[target_idx]
                
                try:
                    is_less = current_device < other_device
                    total_hours = current_device + other_device
                    
                    status = "ÍT HƠN" if is_less else "NHIỀU HƠN HOẶC BẰNG"
                    print(f"[Kết quả So sánh (__lt__)]: Hao mòn của thiết bị A {status} thiết bị B.")
                    print(f"[Kết quả Tổng hợp (__add__)]: Tổng thời gian tải vận hành của cả 2 là: {total_hours} giờ.")
                except TypeError:
                    logging.error("[Lỗi] (ERR-IOT-04): Lỗi kiểu dữ liệu! Không thể thực hiện toán tử với đối tượng ngoài hệ thống.")

            # CHỨC NĂNG 6
            elif choice == '6':
                if current_device is None:
                    logging.error("[Lỗi] (ERR-IOT-02): Thao tác bị từ chối! Hệ thống chưa có thông tin thiết bị hoạt động.")
                    continue
                
                print("--- XUẤT DỮ LIỆU VẬN HÀNH RA CỔNG NGOẠI VI ---")
                print("1. Xuất dữ liệu qua cổng MQTT (Cloud Stream)")
                print("2. Đồng bộ số liệu vào hệ thống quản trị ERP")
                gw_choice = input("Chọn cổng kết nối ngoại vi (1-2): ").strip()
                
                try:
                    if gw_choice == '1':
                        export_telemetry_data(MQTTEngineGateway(), current_device)
                    elif gw_choice == '2':
                        export_telemetry_data(ERPReportGateway(), current_device)
                    else:
                        print("Lựa chọn cổng không hợp lệ.")
                except TypeError:
                    logging.error("[Lỗi] (ERR-IOT-05): Xung đột kiến trúc! Không thể xuất dữ liệu do cấu hình cổng ngoại vi không tương thích.")

            # CHỨC NĂNG 7
            elif choice == '7':
                print("Cảm ơn bạn đã sử dụng hệ thống Quản lý Thiết bị Rikkei Smart Factory IoT Pro!")
                break

        except ValueError as e:
             if str(e) == "ERR-IOT-06":
                 logging.error("[Lỗi] (ERR-IOT-06): Lựa chọn không hợp lệ! Vui lòng nhập đúng số thứ tự chức năng từ 1 đến 7.")

if __name__ == "__main__":
    main()