# analyzer.py
from datetime import date

today = date.today().isoformat()

html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>本日のスロット分析</title>
</head>
<body>
<h1>{today} の結果</h1>

<h2>🏆 店舗ランキング</h2>
<ol>
  <li>パラッツォ葛西（81）</li>
  <li>○○店（76）</li>
</ol>

<h2>🎰 狙い台TOP3</h2>
<ol>
  <li>北斗 台387</li>
  <li>モンキー 台412</li>
  <li>北斗 台381</li>
</ol>

</body>
</html>
"""

with open("web/index.html", "w", encoding="utf-8") as f:
    f.write(html)
