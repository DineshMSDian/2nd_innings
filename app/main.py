from db.connection import get_connection
print("Here's my 2nd inning! truly for me.")

conn = get_connection()
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS players(
            player_id INT PRIMARY KEY,
            name VARCHAR(255),
            batting_style VARCHAR(100),
            bowling_style VARCHAR(100),
            country VARCHAR(255),
            is_active BOOL,
            created_at TIMESTAMPTZ);
""")

cur.execute("""INSERT INTO players (player_id, name, batting_style, bowling_style, country, is_active) VALUES
            (001, 'MS Dhoni', 'Right Hand Batsemen', NULL, 'India', FALSE),
            (002, 'Rohit Sharma', 'Right Hand Batsemen', 'Right Arm Off Spin', 'India', TRUE),
            (003, 'Virat Kohli', 'Right Hand Batsemen', NULL, 'India', TRUE);
""")

conn.commit()
cur.close()
conn.close()
