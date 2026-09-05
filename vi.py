import json
with open("dict.json", "r", encoding="utf-8") as vi:
    data = json.load(vi)


while True:
    ch = input("điền từ hoặc câu (q để thoát): ").strip().lower()
    if ch == 'q':
        exit()

    found = False

    for word in data["vi"]:
            if word["name"].lower() == ch:
                print(f"\nTừ: {word["name"]}")
                print(f"Cách đọc: {word["pronu"]}")
                print(f"nghĩa: {word["meaning"]}")
                print(f"ví dụ: {word["example"]}\n")
                found = True
                break

    if not found:
        print("không tìm thấy từ. Nếu là từ mới vui lòng thêm vào từ điển")