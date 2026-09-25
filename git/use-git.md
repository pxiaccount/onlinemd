---
title: การใช้ Git และ GitHub สำหรับผู้เริ่มต้น
aliases:
  - Git
  - การควบคุมเวอร์ชัน
tags:
  - tools/git
  - tools/github
created: 2026-09-25
---

# การใช้ Git และ GitHub สำหรับผู้เริ่มต้น

> [!abstract] สรุปในหนึ่งบรรทัด
> Git เป็นโปรแกรมควบคุมเวอร์ชันที่บันทึกการเปลี่ยนแปลงไฟล์ในโฟลเดอร์ (repository) ได้ ช่วยให้เราสามารถย้อนกลับ ดูประวัติ และทำงานร่วมกันได้ โดย GitHub เป็นเว็บไซต์เก็บ repository บนคลาวด์

> [!tip] เคล็ดลับจำเร็ว
> - `add` = เตรียมไฟล์เข้า "กล่อง"
> - `commit` = ตรวจรวมพร้อมเขียนโน๊ต
> - `push` = ส่งกลับไป GitHub
> - `pull` = ดึงรับจาก GitHub

## 🖼 ภาพประกอบ

### แผนภาพต้นไม้ commit และสาขา (branch)

![แผนภาพต้นไม้ commit และสาขา](git-svg/commit-history.svg)

### สถานะการเปลี่ยนแปลงในงาน (working tree) ← index ← HEAD

![แผนภาพ рабоอันดับของ Git](git-svg/git-staging.svg)

## 🧠 ทำความเข้าใจ

Git ทำงานแบบ 3 ชั้นหลัก:

1. **Working tree** — ไฟล์ของเราตามปกติ
2. **Index (staging area)** — กล่องรอ "จัดเก็บ"
3. **HEAD (last commit)** — เวอร์ชันที่จัดเก็บไว้ล่าสุด

การดำเนินการสำคัญผ่าน `git status` เริ่มจากมองสถานะว่าไฟล์อยู่ในขั้นตอนไหน: **untracked** (ยังไม่ได้เพิ่ม) → **staged** (เพิ่มเข้า index แล้ว) → **committed** (จัดเก็บไปแล้ว) → **pushed** (ไป GitHub แล้ว).

## ✏️ ตัวอย่างการใช้คำสั่งพื้นฐาน

```bash
# เริ่มใช้ Git ในโฟลเดอร์ใหม่
git init

# ลอกสำเนา repository ที่มีอยู่แล้ว
git clone https://github.com/ชื่อผู้ใช้/repository.git

# ตรวจสอบสถานะ
git status

# เตรียมไฟล์เข้า index
git add ไฟล์ที่แก้ไข.md

# ตรวจรวมและเขียนโน๊ต
git commit -m "ข้อความโน๊ตสั้น ๆ อธิบายการเปลี่ยนอะไร"

# ส่งกลับไป GitHub
git push origin main

# ดึงรับจาก GitHub
git pull origin main
```

## ⚠️ ข้อควรระวัง

> [!warning] ข้อผิดพลาดที่พบบ่อย
> 1. ลืม `git add` ก่อน `git commit` → commit จะเพิ่มเฉพาะไฟล์ที่เตรียมไว้เท่านั้น
> 2. `git push` ชนกับ `git pull` โดยไม่รวม (merge) → แก้ไขด้วย `git pull --rebase` แล้ว push ใหม่
> 3. ใส่รหัสผ่านหรือไฟล์ลับใน repository → ลบด้วย `git rm --cached` และเพิ่มใน `.gitignore`
> 4. สับสนว่าสาขาหลักชื่อ `master` หรือ `main` → ตรวจสอบด้วย `git branch`

## 🏋️ แบบฝึกหัด

> [!question]- แบบฝึกหัดที่ 1: ระบบรวมขั้นตอน
> ให้แยกขั้นตอนของ Git จากข้อความนี้ให้ถูกต้อง: "git add" (เตรียม), "git commit" (เขียนโน๊ต), "git push" (ส่งจากเครื่อง), "git pull" (ดึงสู่เครื่อง), "git clone" (ลอกมา), "git init" (เริ่มใหม่)
> > [!success]- เฉลย
> > 1. `git init` — เริ่มใช้ Git ใหม่ในโฟลเดอร์
> > 2. `git clone` — ลอก repository มาที่เครื่อง
> > 3. `git add` — เตรียมไฟล์เข้า index
> > 4. `git commit` — จัดเก็บพร้อมโน๊ต
> > 5. `git push` — ส่งจากเครื่องมายังเซิร์ฟเวอร์
> > 6. `git pull` — ดึงจากเซิร์ฟเวอร์มายังเครื่อง

> [!question]- แบบฝึกหัดที่ 2: อ่านประวัติ
> หลังจาก `git log --oneline` ได้ผลลัพธ์ดังนี้:
> ```
> a1b2c3d เพิ่มโน้ตสุขศึกษา 30 + 2
> 8973fc7 ปรับปรุง SVG ของเซลล์เคมี
> 3f4c963 แก้ไขสมการเลขจากเบ็น
> ```
> สรุปคำสั่งที่ใช้ "นำเวอร์ชันล่าสุดมาที่เครื่อง" ได้ครบถ้วน?
> > [!success]- เฉลย
> > ใช้ `git pull origin main` (หรือ `git pull` สามารถลดรูปได้เมื่อ tracking ตั้งไว้แล้ว)

## 🎴 การ์ดทบทวน #flashcards

Git ย่อมาจาก?
Git: **G**lobal **I**ndex **T**ree

`git add` คืออะไร?
`git add` = เตรียมไฟล์เข้า "index" (staging area)

`git commit` คืออะไร?
`git commit` = ตรวจรวมพร้อมเขียนโน๊ตจัดเก็บเวอร์ชัน

`git push` คืออะไร?
`git push` = ส่ง commits จากเครื่องไป repository อื่น (เช่น GitHub)

`git pull` คืออะไร?
`git pull` = ดึง repository จาก distant มาเทียบกับ local แล้วรวม

`git clone` คืออะไร?
`git clone` = ลอกสำเนา repository มาที่เครื่องใหม่

## 🔗 หัวข้อที่เกี่ยวข้อง

- [[เซลล์กัลวานิก]] — ทักษะ Git ใช้เมื่อแก้ไขโน้ตเคมี
- [[ข้อสอบสุขศึกษา ค่านิยมทางเพศและโรคไม่ติดต่อเรื้อรัง]] — โน้ตที่แก้ไขเพื่อ push (ควรใช้ workflow นี้)
