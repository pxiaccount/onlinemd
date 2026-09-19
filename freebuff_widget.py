# -*- coding: utf-8 -*-
"""
Freebuff Usage Widget — หน้าต่างจำลองหน้า freebuff.com/account
รัน: python freebuff_widget.py
"""
import tkinter as tk
from tkinter import font as tkfont
import random
import datetime

# ---------- ข้อมูลจำลอง (fallback: ไม่มี API จริง) ----------
DATA = {
    "plan": "Free",
    "used_credits": 13.7,
    "total_credits": 20.0,
    "messages_today": 24,
    "models": [
        ("z-ai/glm-5.3-flash", 8.2),
        ("claude/gpt-class", 3.9),
        ("other/small", 1.6),
    ],
    "reset_date": "2026-10-01",
}

BG = "#101014"
CARD = "#18181f"
FG = "#f2f2f5"
MUTED = "#8b8b96"
ACCENT = "#4dabf7"
GREEN = "#69db7c"
YELLOW = "#ffd43b"
RED = "#ff8787"


def pct(used, total):
    return used / total if total else 0


class FreebuffWidget(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Freebuff Usage")
        self.configure(bg=BG)
        self.minsize(300, 220)
        self.geometry("380x420")

        # ฟอนต์ยืดหยุ่นตามขนาดหน้าต่าง
        self.f_title = tkfont.Font(family="Segoe UI", size=15, weight="bold")
        self.f_h = tkfont.Font(family="Segoe UI", size=10, weight="bold")
        self.f_body = tkfont.Font(family="Segoe UI", size=10)
        self.f_small = tkfont.Font(family="Segoe UI", size=9)

        self.widgets = []
        self.build()
        self.bind("<Configure>", self.on_resize)
        self.refresh_loop()

    # ---------- สร้าง UI ----------
    def build(self):
        for w in self.winfo_children():
            w.destroy()

        outer = tk.Frame(self, bg=BG)
        outer.pack(fill="both", expand=True, padx=14, pady=12)
        self.widgets.append(outer)

        # หัว
        head = tk.Frame(outer, bg=BG)
        head.pack(fill="x")
        tk.Label(head, text="⚡ Freebuff", bg=BG, fg=FG,
                 font=self.f_title).pack(side="left")
        tk.Label(head, text="account", bg=BG, fg=MUTED,
                 font=self.f_body).pack(side="left", padx=(6, 0), pady=(6, 0))
        tk.Label(head, text=f"แผน: {DATA['plan']}", bg=CARD, fg=ACCENT,
                 font=self.f_small, padx=8, pady=3).pack(side="right")

        # การ์ดเครดิต
        card = self.card(outer)
        self.lbl_credits = tk.Label(card, text="", bg=CARD, fg=FG, font=self.f_title)
        self.lbl_credits.pack(anchor="w")
        self.bar = tk.Canvas(card, bg=CARD, height=10, highlightthickness=0)
        self.bar.pack(fill="x", pady=(6, 4))
        self.lbl_reset = tk.Label(card, text="", bg=CARD, fg=MUTED, font=self.f_small)
        self.lbl_reset.pack(anchor="w")

        # การ์ดสถิติ
        card2 = self.card(outer)
        row = tk.Frame(card2, bg=CARD)
        row.pack(fill="x")
        self.lbl_msgs = self.stat(row, "ข้อความวันนี้", "")
        self.lbl_pct = self.stat(row, "ใช้ไปแล้ว", "")

        # การ์ดโมเดล
        card3 = self.card(outer)
        tk.Label(card3, text="การใช้งานตามโมเดล", bg=CARD, fg=MUTED,
                 font=self.f_small).pack(anchor="w")
        self.lbl_models = []
        for name, _ in DATA["models"]:
            l = tk.Label(card3, text="", bg=CARD, fg=FG, font=self.f_small, anchor="w")
            l.pack(anchor="w", pady=(3, 0))
            self.lbl_models.append(l)

        tk.Label(outer, text="จำลองข้อมูล • freebuff.com/account",
                 bg=BG, fg=MUTED, font=self.f_small).pack(side="bottom", anchor="e")

    def card(self, parent):
        c = tk.Frame(parent, bg=CARD, padx=12, pady=10)
        c.pack(fill="x", pady=(10, 0))
        return c

    def stat(self, parent, label, value):
        f = tk.Frame(parent, bg=CARD)
        f.pack(side="left", expand=True)
        tk.Label(f, text=label, bg=CARD, fg=MUTED, font=self.f_small).pack()
        l = tk.Label(f, text=value, bg=CARD, fg=FG, font=self.f_h)
        l.pack()
        return l

    # ---------- วาด progress bar ----------
    def draw_bar(self, ratio):
        self.bar.delete("all")
        w = self.bar.winfo_width() or 1
        h = 10
        self.bar.create_rectangle(0, 0, w, h, fill="#26262e", width=0)
        color = GREEN if ratio < 0.6 else YELLOW if ratio < 0.85 else RED
        self.bar.create_rectangle(0, 0, max(w * ratio, 2), h, fill=color, width=0)

    # ---------- อัปเดตค่า ----------
    def update_data(self):
        used = DATA["used_credits"]
        total = DATA["total_credits"]
        ratio = pct(used, total)
        self.lbl_credits.config(
            text=f"{used:.1f} / {total:.0f} เครดิต")
        self.lbl_reset.config(text=f"รีเซ็ตวันที่ {DATA['reset_date']}")
        self.lbl_msgs.config(text=str(DATA["messages_today"]))
        self.lbl_pct.config(text=f"{ratio*100:.0f}%")
        for l, (name, val) in zip(self.lbl_models, DATA["models"]):
            l.config(text=f"{name} — {val:.1f} เครดิต")
        self.draw_bar(ratio)

    def refresh_loop(self):
        # จำลองข้อมูลขยับเล็กน้อยเหมือน live usage
        if random.random() < 0.15:
            DATA["used_credits"] = min(DATA["total_credits"],
                                       DATA["used_credits"] + 0.1)
            DATA["messages_today"] += 1
        self.update_data()
        self.after(5000, self.refresh_loop)

    # ---------- responsive ----------
    def on_resize(self, event):
        if event.widget is not self:
            return
        w = max(self.winfo_width(), 300)
        scale = w / 380
        self.f_title.config(size=max(12, int(15 * scale)))
        self.f_h.config(size=max(9, int(10 * scale)))
        self.f_body.config(size=max(9, int(10 * scale)))
        self.f_small.config(size=max(8, int(9 * scale)))
        self.update_data()


if __name__ == "__main__":
    FreebuffWidget().mainloop()
