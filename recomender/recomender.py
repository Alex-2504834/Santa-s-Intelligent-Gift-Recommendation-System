import sqlite3

def recomendGift(childID:str, intrests:list, wishlist:list):
    con = sqlite3.connect("./DB/childrensData.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM wishlist WHERE child_id=?", (childID))

    return cur.fetchall()