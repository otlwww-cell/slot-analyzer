# ===== ダミーデータ（後でスクレイピングに置き換える） =====

data = {
    "store": "パラッツォ葛西店",
    "max_diff": 6200,
    "machine_avg": 1800,
    "store_avg": 950,
    "win_rate": 0.58,
    "event_day": True
}

# ===== 正規化関数 =====
def normalize(value, min_val, max_val):
    return max(0, min(100, (value - min_val) / (max_val - min_val) * 100))

# ===== 各スコア算出 =====
score_max = normalize(data["max_diff"], 0, 8000)
score_machine = normalize(data["machine_avg"], -1000, 3000)
score_store = normalize(data["store_avg"], -500, 2000)
score_win = data["win_rate"] * 100
score_event = 100 if data["event_day"] else 0

# ===== 総合スコア =====
total_score = (
    0.35 * score_max +
    0.20 * score_machine +
    0.20 * score_store +
    0.15 * score_win +
    0.10 * score_event
)

# ===== HTML出力 =====
html = f"""
<h1>{data['store']} 総合判定</h1>
<p>総合スコア：{round(total_score, 1)}</p>
<ul>
<li>最大差枚スコア：{round(score_max,1)}</li>
<li>機種平均スコア：{round(score_machine,1)}</li>
<li>店平均スコア：{round(score_store,1)}</li>
<li>勝率スコア：{round(score_win,1)}</li>
<li>特定日補正：{score_event}</li>
</ul>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
