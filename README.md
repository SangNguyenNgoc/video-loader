## Hướng dẫn chạy trang web download video từ YouTube

### Mục lục
1. [Giới thiệu](#giới-thiệu)
2. [Yêu cầu hệ thống](#yêu-cầu-hệ-thống)
3. [Cài đặt và chạy Backend (FastAPI)](#cài-đặt-và-chạy-backend-fastapi)
4. [Cài đặt và chạy Frontend (ReactJS)](#cài-đặt-và-chạy-frontend-reactjs)
5. [Sử dụng](#sử-dụng)
6. [Ghi chú](#ghi-chú)

### Giới thiệu
Đây là dự án trang web cho phép người dùng tải video từ YouTube, sử dụng công nghệ Frontend là ReactJS và Backend là FastAPI.  
Mục tiêu của dự án là cung cấp một giao diện thân thiện và dễ sử dụng để người dùng có thể tải video một cách nhanh chóng và tiện lợi.

### Yêu cầu hệ thống
- **Node.js** và **npm** (dùng cho ReactJS)
- **Python 3.7+** (dùng cho FastAPI)
- **pip** (Python package installer)

### Cài đặt và chạy Backend (FastAPI)

1. **Clone repository từ GitHub:**
    ```bash
    git clone https://github.com/SangNguyenNgoc/video-loader.git
    cd be
    ```

2. **Tạo và kích hoạt môi trường ảo (tùy chọn nhưng được khuyến nghị):**
    ```bash
    python -m venv env
    source env/bin/activate  # Trên Windows dùng: env\Scripts\activate
    ```

3. **Cài đặt các gói cần thiết:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Chạy ứng dụng FastAPI:**
    ```bash
    uvicorn main:app --reload
    ```

    Ứng dụng sẽ chạy ở `http://127.0.0.1:8000`.

### Cài đặt và chạy Frontend (ReactJS)

1. **Chuyển vào thư mục frontend:**
    ```bash
    cd ../fe
    ```

2. **Cài đặt các gói cần thiết:**
    ```bash
    npm install
    ```

3. **Chạy ứng dụng ReactJS:**
    ```bash
    npm start
    ```

    Ứng dụng sẽ chạy ở `http://localhost:3000`.

### Sử dụng

1. **Mở trình duyệt và truy cập vào ứng dụng ReactJS:**
    ```bash
    http://localhost:3000
    ```

2. **Nhập URL của video YouTube bạn muốn tải xuống vào thanh tìm kiếm và nhấn "Start Download".**

3. **Đợi ứng dụng xử lý và cung cấp link tải về cho bạn.**

### Ghi chú

- Đảm bảo rằng bạn đã cài đặt tất cả các yêu cầu hệ thống trước khi bắt đầu.
- Nếu gặp vấn đề về môi trường ảo hoặc các gói cài đặt, hãy kiểm tra lại các bước cài đặt và đảm bảo rằng bạn đang sử dụng đúng phiên bản Python và Node.js.
- Đảm bảo rằng FastAPI và ReactJS đang chạy trên các cổng khác nhau (mặc định là 8000 cho FastAPI và 3000 cho ReactJS).
- Để dừng môi trường ảo, bạn có thể sử dụng lệnh `deactivate` (trên Windows) hoặc `source deactivate` (trên các hệ điều hành Unix-based).

Cảm ơn bạn đã sử dụng ứng dụng của chúng tôi!  
Nếu bạn có bất kỳ câu hỏi hoặc phản hồi nào, vui lòng liên hệ qua nngocsang38@gmail.com.
