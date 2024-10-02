

conn = pyeapi.connect(host='10.1.1.1', transport='https',username='cvpadmin',password='arista')
cs_id = uuid.uuid4()
conn.execute([f"configure session {cs_id}",{"cmd":"copy terminal: session-config","input": configlet},"commit"])


# cd docs/
# python generate_modules.py
# python3 -m sphinx -a docs _build
# python3 -m http.server --directory _build 8084