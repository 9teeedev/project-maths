import numpy as np

def gauss_seidel(A, b, tol=1e-6, max_iter=100):
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)
    x = np.zeros(n)

    # === ตรวจสอบศูนย์บนแนวทแยง แล้วสลับแถวอัตโนมัติ ===
    for i in range(n):
        if A[i, i] == 0:
            for k in range(i+1, n):
                if A[k, i] != 0:
                    A[[i, k]] = A[[k, i]]
                    b[[i, k]] = b[[k, i]]
                    break
            else:
                raise ZeroDivisionError(f"ไม่สามารถทำ Pivot ที่แถว {i+1} ได้ (A[{i},{i}] = 0)")

    print("\n=== เริ่มคำนวณวิธีเกาส์-ไซเดล ===\n")

    for k in range(1, max_iter+1):
        x_old = x.copy()
        for i in range(n):
            sum_ = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x[i+1:])
            x[i] = (b[i] - sum_) / A[i, i]

        if np.max(np.abs(x - x_old)) < tol:
            print(f"\nสิ้นสุดการคำนวณหลัง {k} ครั้ง (ถึงค่าความคลาดเคลื่อนที่กำหนด)\n")
            break

        print(f"รอบที่ {k}: x = {x}")

    print("\nคำตอบประมาณคือ:")
    for i in range(n):
        print(f"x[{i+1}] = {x[i]:.4f}")

    return x


# ===========================
# 🔹 ส่วนรับค่าจากผู้ใช้
# ===========================
print("=== โปรแกรมคำนวณระบบสมการเชิงเส้นด้วยวิธีเกาส์-ไซเดล ===\n")

n = int(input("กรุณาระบุขนาดเมทริกซ์ (n x n): "))

print("\nกรุณาป้อนค่าของเมทริกซ์ A (แต่ละแถวคั่นด้วยช่องว่าง):")
A = np.zeros((n, n))
for i in range(n):
    A[i] = list(map(float, input(f"แถวที่ {i+1}: ").split()))

print("\nกรุณาป้อนค่าของเวกเตอร์ b (คั่นด้วยช่องว่าง):")
b = np.array(list(map(float, input().split())))

tol = float(input("\nกรุณาป้อนค่าความคลาดเคลื่อน (ε): "))

# เรียกใช้ฟังก์ชัน
gauss_seidel(A, b, tol=tol)
