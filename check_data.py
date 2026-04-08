import asyncio
import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

async def test():
    try:
        conn = await asyncpg.connect(DATABASE_URL)
        print("SUCCESS: Connected to database!")
        
        # Check table
        rows = await conn.fetch("SELECT id, nama, jenis FROM fasilitas_publik LIMIT 5")
        if rows:
            print(f"Found {len(rows)} records in 'fasilitas_publik':")
            for r in rows:
                print(f" - ID: {r['id']}, Nama: {r['nama']}, Jenis: {r['jenis']}")
        else:
            print("Table 'fasilitas_publik' exists but is empty.")
            
        await conn.close()
    except Exception as e:
        print(f"FAILED: {e}")

if __name__ == "__main__":
    asyncio.run(test())
