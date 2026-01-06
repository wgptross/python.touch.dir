import datetime
import os
import sqlite3
import sys
from datetime import date

time_now = datetime.datetime.now()
args = sys.argv
areacode = args[3][2:5]


def check_dir() -> bool:
    filename_prefix = (
        "C:/Users/gavin.peatross/Notes/obi-notes/WORK/TICKETS/"
        + str(date.today())
        + "/"
    )

    if os.path.exists(filename_prefix):
        print("dir already exists")
        return True
    else:
        print("")
        os.mkdir(filename_prefix)
        return False


def create(filename):
    with open(filename, "w") as file:
        os.utime(filename, None)

        main_write_payload = f"IT Support Call - User Called In - @ {time_now}\n \n__________________\n\n*Auto Generated Call Info:*\n\nTime: {time_now}\nFirst name: {args[1]}\nLast name: {args[2]}\n\n__________________\n\nUser Info:\n - \n\nDescription:\n - user called in \n - \n\nNext Steps:\n - n/a\n\nResolution:\n - n/a\n\nDetails:\n - {args[3]}\n - "
        file.write(main_write_payload)
        conn = sqlite3.connect("E:/main_facil.db")
        cursor = conn.cursor()
        # create querie for the local db with phone, name where the areacode is the key search value
        cursor.execute(
            """
            SELECT phone, name FROM main_table WHERE SUBSTR(phone, 2, 3) = ?
            """,
            (areacode,),
        )
        rows_main = cursor.fetchall()
        # prep the data for printing
        rows_str_main = "\n".join(str(row) for row in rows_main)
        ###
        # get the object ID for the FLD so I can link web links to the payload
        # names = cursor.execute(
        #     """
        #     SELECT name FROM main_table WHERE SUBSTR(phone, 2, 3)
        #     """,
        #     (),
        # )
        # objectid = cursor.execute(
        #     """
        #     SELECT name, id FROM all_groups WHERE name LIKE 'Fld_%_Users' AND cloud = 'Cloud' AND name NOT LIKE '%FolderRedirectionUsers' WHERE name = ?;
        #     """,
        #     (),
        # )

        conn.commit()
        conn.close()

        meta_payload = f"\n___\n## Meta: \n\n```json \n #Potential Facility: (Area Code)\n\n{rows_str_main}\n```"

        file.write(meta_payload)


def main():
    if check_dir():
        filename = f"C:/Users/gavin.peatross/Notes/obi-notes/WORK/TICKETS/{date.today()}/{args[1]} - {args[2]} - {args[3]} - {date.today()}.md"

    else:
        filename = f"C:/Users/gavin.peatross/Notes/obi-notes/WORK/{args[1]} - {args[2]} - {args[3]}.md"

    create(filename)
