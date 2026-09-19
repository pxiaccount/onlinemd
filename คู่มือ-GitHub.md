---
title: คู่มือ GitHub — เผยแพร่โน้ตขึ้นเว็บ
aliases:
  - GitHub Guide
tags:
  - guide/github
created: 2026-09-19
---

# คู่มือ GitHub — เผยแพร่โน้ตขึ้นเว็บ

> [!abstract] สรุปในหนึ่งบรรทัด
> โน้ตทุกไฟล์ใน vault นี้จะกลายเป็น**เว็บไซต์อ่านฟรี**ที่เปิดจากมือถือ/คอมเครื่องไหนก็ได้ ผ่าน GitHub Pages โดยแค่ push ครั้งแรก หลังจากนั้นเว็บจะอัปเดตเองทุกครั้งที่มีโน้ตใหม่

## 🖼 ภาพประกอบ

<svg width="400" height="230" viewBox="0 0 400 230" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrowFlow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#333"/>
    </marker>
  </defs>
  <!-- กล่อง 1: Freebuff -->
  <rect x="15" y="70" width="100" height="60" rx="10" fill="#4dabf7" fill-opacity="0.3" stroke="#1971c2" stroke-width="2"/>
  <text x="65" y="95" font-size="13" font-weight="bold" fill="#333" text-anchor="middle">Freebuff</text>
  <text x="65" y="113" font-size="11" fill="#333" text-anchor="middle">สร้าง .md</text>
  <!-- กล่อง 2: GitHub -->
  <rect x="150" y="70" width="100" height="60" rx="10" fill="#ffd43b" fill-opacity="0.35" stroke="#f59f00" stroke-width="2"/>
  <text x="200" y="95" font-size="13" font-weight="bold" fill="#333" text-anchor="middle">GitHub</text>
  <text x="200" y="113" font-size="11" fill="#333" text-anchor="middle">เก็บ vault</text>
  <!-- กล่อง 3: Actions -->
  <rect x="285" y="70" width="100" height="60" rx="10" fill="#69db7c" fill-opacity="0.35" stroke="#2f9e44" stroke-width="2"/>
  <text x="335" y="95" font-size="13" font-weight="bold" fill="#333" text-anchor="middle">GitHub Pages</text>
  <text x="335" y="113" font-size="11" fill="#333" text-anchor="middle">เว็บอ่านโน้ต</text>
  <!-- ลูกศร -->
  <line x1="115" y1="100" x2="148" y2="100" stroke="#333" stroke-width="2" marker-end="url(#arrowFlow)"/>
  <line x1="250" y1="100" x2="283" y2="100" stroke="#333" stroke-width="2" marker-end="url(#arrowFlow)"/>
  <!-- คำอธิบาย -->
  <text x="200" y="165" font-size="12" fill="#333" text-anchor="middle">push เมื่อไร เว็บอัปเดตเองใน ~1 นาที</text>
  <text x="200" y="185" font-size="12" fill="#868e96" text-anchor="middle">เปิดได้จากมือถือ แท็บเล็ต คอมทุกเครื่อง</text>
</svg>

## 📋 ขั้นตอนครั้งแรก (ทำครั้งเดียว)

### 1. สมัคร GitHub (ฟรี)

- เปิด https://github.com → กด **Sign up** → ตั้งชื่อผู้ใช้ (username) และรหัสผ่าน
- ยืนยันอีเมล

### 2. สร้าง repository (คลังไฟล์)

- ล็อกอินแล้วกดปุ่ม **+** มุมขวาบน → **New repository**
- ตั้งชื่อ เช่น `study-vault` (ตัวพิมพ์เล็ก ไม่มีเว้นวรรค)
- เลือก **Public** (จำเป็น เพื่อให้ GitHub Pages ฟรีทำงาน)
- กด **Create repository** — อย่าติ๊กสร้าง README เพราะ vault มีไฟล์อยู่แล้ว

### 3. Push vault ขึ้น GitHub

บอกผมใน Freebuff ว่า **"push vault ขึ้น GitHub repo <ชื่อ-user>/<ชื่อ-repo>"** — ผมจะรันคำสั่งให้ครบ โดยเบื้องหลังคือ:

```bash
git init
git add .gitignore ดัชนี.md *.md เคมี/ แผนการเรียน/ quartz/ .github/
git commit -m "เริ่มต้น vault โน้ตการเรียนรู้"
git remote add origin https://github.com/<user>/<repo>.git
git branch -M main
git push -u origin main
```

> [!warning] สิ่งที่จะไม่ถูก push (ตาม .gitignore)
> - โฟลเดอร์ระบบ `.obsidian/`, `.freebuff/`, `.firecrawl/`
> - ไฟล์ PDF โจทย์ (ใหญ่เกินและเป็นของบุคคลอื่น)

### 4. เปิด GitHub Pages (กดไม่กี่ครั้ง — ต้องทำบนเว็บเอง)

1. เปิดหน้า repo บน github.com → แท็บ **Settings**
2. เมนูซ้าย → **Pages**
3. หัวข้อ **Build and deployment** → Source เลือก **GitHub Actions**
4. กด Save — เสร็จ!

> [!tip] ลิงก์เว็บของคุณคือ
> `https://<ชื่อ-user>.github.io/<ชื่อ-repo>` — เปิดครั้งแรกอาจรอ build 1–2 นาที

### 5. แก้ baseUrl ให้ตรงลิงก์จริง

หลังรู้ชื่อ user/repo แล้ว บอกผมได้เลย ผมจะแก้ `quartz/quartz.config.yaml` บรรทัด `baseUrl: example.github.io` เป็น `<user>.github.io/<repo>` ให้ (จำเป็นเพื่อให้ระบบค้นหา/ลิงก์ในเว็บทำงานถูกต้อง)

## 🔄 การใช้งานหลังตั้งค่าเสร็จ

| สิ่งที่อยากทำ | วิธีทำ |
|---|---|
| เพิ่มโน้ตใหม่ | บอกผมใน Freebuff → ผมสร้าง .md ให้ → บอก "push ขึ้นเว็บ" |
| แก้โน้ตเก่า | บอกผมว่าแก้อะไร → ผมแก้ → push |
| อ่านโน้ตจากมือถือ | เปิดลิงก์เว็บได้ทันที ไม่ต้องติดตั้งอะไร |
| ค้นหาโน้ตบนเว็บ | ใช้ช่องค้นหาซ้ายบนของเว็บ (Quartz มี full-text search) |
| อัปเดตเองเมื่อไร | หลัง push รอ ~1 นาที (ดูสถานะที่แท็บ Actions ของ repo) |

## ⚠️ ข้อควรระวัง

> [!warning] สิ่งที่ต้องรู้ก่อนเผยแพร่
> 1. **เว็บนี้สาธารณะ** — ทุกโน้ตที่ push ขึ้นไป ใครก็มีลิงก์แล้วอ่านได้ ถ้ามีโน้ตส่วนตัว บอกชื่อไฟล์ผมเพื่อเพิ่มใน `.gitignore` และ `ignorePatterns` ก่อน push
> 2. **AGENTS.md ไม่ถูกเผยแพร่** — ตั้ง ignore ไว้แล้ว เพราะเป็นคู่มือของ AI ไม่ใช่โน้ตเรียน
> 3. **ห้าม push ข้อมูลส่วนตัวที่อ่อนไหว** (เลขบัตร รหัสผ่าน ฯลฯ) ลง repo สาธารณะเด็ดขาด
> 4. **การแก้ไขบนเว็บอ่านไม่ได้** — เว็บเป็น read-only การแก้ทำผ่านผม (เดสก์ท็อป) เมื่อ Freebuff เว็บเวอร์ชันรองรับวันหน้า จะเชื่อม repo เดียวกันนี้ได้ทันที

## 🎴 การ์ดทบทวน #flashcards

ลิงก์เว็บของ vault บน GitHub Pages มีรูปแบบอย่างไร?::https://\<user\>.github.io/\<repo\>

ต้องตั้ง Source ของ GitHub Pages เป็นอะไร?::GitHub Actions (ใน Settings → Pages)

หลัง push โน้ตใหม่ เว็บอัปเดตในกี่นาที?::ประมาณ 1 นาที (ดูสถานะที่แท็บ Actions)

ไฟล์ชนิดใดไม่ถูก push ขึ้น repo?::ไฟล์ระบบ (.obsidian, .freebuff) และ PDF — ตาม .gitignore

## 🔗 หัวข้อที่เกี่ยวข้อง

- [[ดัชนี]] — หน้าแรกของเว็บ
- [[AGENTS]] — มาตรฐานการเขียนโน้ต (ไม่ถูกเผยแพร่บนเว็บ)
