import sqlite3

# ========== 1. 初始化数据库 ==========
def init_db():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            status TEXT,
            tracking TEXT,
            date TEXT
        )
    """)
    
    cursor.execute("SELECT COUNT(*) FROM orders")
    if cursor.fetchone()[0] == 0:
        orders = [
            ("ORD001", "已发货", "SF123456", "2026-06-10"),
            ("ORD002", "处理中", None, "2026-06-12"),
            ("ORD003", "已送达", "YT987654", "2026-06-05")
        ]
        cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?)", orders)
        conn.commit()
    
    conn.close()
    print("✅ 数据库初始化完成")

# ========== 2. 查询订单 ==========
def get_order_status(order_id: str) -> str:
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.execute("SELECT status, date FROM orders WHERE order_id = ?", (order_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        status, date = row
        return f"订单{order_id}状态：{status}，下单日期：{date}"
    return f"未找到订单{order_id}"

# # ========== 3. 测试 ==========
# if __name__ == "__main__":
#     init_db()
#     for oid in ["ORD001", "ORD002", "ORD999"]:
#         print(get_order_status(oid))