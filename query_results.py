import sqlite3

DB_PATH = "automation-testing/test_results.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("=" * 45)
print("      BÁO CÁO KẾT QUẢ KIỂM THỬ")
print("=" * 45)

# Tổng quan Pass/Fail
cursor.execute("""
    SELECT status, COUNT(*) as total, ROUND(AVG(duration), 2) as avg_time
    FROM test_results
    GROUP BY status
""")
rows = cursor.fetchall()
for row in rows:
    print(f"  {row[0]}: {row[1]} tests | Thời gian TB: {row[2]}s")

print()

# Pass rate
cursor.execute("SELECT COUNT(*) FROM test_results")
total = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM test_results WHERE status = 'PASS'")
passed = cursor.fetchone()[0]
print(f"  Pass Rate: {round(passed/total*100, 1)}%  ({passed}/{total} tests)")

print()
print("-" * 45)

# Top 3 test chậm nhất
cursor.execute("""
    SELECT test_name, status, duration
    FROM test_results
    ORDER BY duration DESC
    LIMIT 3
""")
print("  TOP 3 TEST CHẠY CHẬM NHẤT:")
for i, row in enumerate(cursor.fetchall(), 1):
    print(f"  {i}. {row[0]} | {row[1]} | {row[2]}s")

print("=" * 45)
conn.close()