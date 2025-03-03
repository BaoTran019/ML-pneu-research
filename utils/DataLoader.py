import pandas as pd
from sklearn.model_selection import train_test_split
import os

def Read_Excel_Data(filename):
    
    """
    Đọc file Excel từ thư mục "data" trong thư mục gốc của dự án.

    Parameters:
        filename (str): Tên file (ví dụ: "File_10000_final.xlsx")

    Returns:
        df (DataFrame): Dữ liệu đã đọc
    """
    # Lấy thư mục gốc của dự án (thư mục cha của `notebooks` và `utils`)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Tạo đường dẫn đầy đủ đến file trong "data"
    file_path = os.path.join(project_root, "data", filename)

    # Kiểm tra file có tồn tại không
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ Không tìm thấy file: {file_path}")

    # print(f"📂 Đọc dữ liệu từ: {file_path}")
    df = pd.read_excel(file_path)
    df = df.drop(columns=["text", "advanced_text", "BioLORD emb"], errors='ignore')  
    df.info()


    # Tạo nhãn kết hợp từ hai cột pneu và cold
    df['label_combined'] = df[['pneu', 'cold']].astype(str).agg('-'.join, axis=1)

    # Kiểm tra số lượng mẫu mỗi nhóm nhãn
    print(df['label_combined'].value_counts())

    # Chia train/test với stratify theo nhãn mới
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df['label_combined'])

    # Xóa cột label_combined không cần thiết sau khi chia
    train_df = train_df.drop(columns=['label_combined'])
    test_df = test_df.drop(columns=['label_combined'])

    # Kiểm tra lại số lượng mẫu sau khi chia
    print(train_df[['pneu', 'cold']].value_counts())
    print(test_df[['pneu', 'cold']].value_counts())

    target = targets = ["pneu", "cold"]  # Danh sách các nhãn cần chạy

    return df