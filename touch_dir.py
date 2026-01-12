import copy
import datetime
import json
import os
import sqlite3
import sys

# config setup
#
#


# config_file = "config.touchdir.json"

# with open(config_file, "r", encoding="utf-8") as f:
#    config_data = json.load(f)


time_now = datetime.datetime.now()
day = time_now.strftime("%m-%d")
args = sys.argv
if args[1].startswith("All IT Support"):
    args[1] = ""
# arg1 = first name
# arg2 = last name
# arg3 = caller number
# get args and pass them into a format string for creating the file
#
#

# CHANGE ME

filename = f"C:/Users/kenneth.howard/Documents/init/Calls/{day} {args[1]} {args[2]} - {args[3]}.md"
# get area code from call args
areacode = args[3][2:5]
# print(sys.argv[1])
# create the file
with open(filename, "w"):
    os.utime(filename, None)
main_write_payload = f"IT Support Call - User Called In - @ {time_now}\n \n__________________\n\n*Auto Generated Call Info:*\n\nTime: {time_now}\nFirst name: {args[1]}\nLast name: {args[2]}\n\n__________________\n\nUser Info:\n - \n\nDescription:\n - user called in \n - \n\nNext Steps:\n - n/a\n\nResolution:\n - n/a\n\nDetails:\n - {args[3]}\n - "
file = open(filename, "a")
file.write(main_write_payload)
# create connection to local DB
# conn = sqlite3.connect("E:/main_facil.db")
# cursor = conn.cursor()
# create querie for the local db with phone, name where the areacode is the key search value
# phone_search = cursor.execute(
#     """
#     SELECT phone, name FROM main_table WHERE SUBSTR(phone, 2, 3) = ?
#     """,
#     (areacode,),
# )
# rows_main = cursor.fetchall()
# # prep the data for printing
# rows_str_main = "\n".join(str(row) for row in rows_main)
# ###
# # get the object ID for the FLD so I can link web links to the payload
# # names = cursor.execute(
# #     """
# #     SELECT name FROM main_table WHERE SUBSTR(phone, 2, 3)
# #     """,
# #     (),
# # )
# # objectid = cursor.execute(
# #     """
# #     SELECT name, id FROM all_groups WHERE name LIKE 'Fld_%_Users' AND cloud = 'Cloud' AND name NOT LIKE '%FolderRedirectionUsers' WHERE name = ?;
# #     """,
# #     (),
# # )

# conn.commit()
# conn.close()

# meta_payload = f"\n___\n## Meta: \n\n```json```"


# file.write(meta_payload)
