# Assignment-ODDS 📋

## Usage ✍🏻
---
### Run ผ่าน IDE Online ได้ที่ 👉🏻 https://trinket.io/library/trinkets/891e74fcec

#### เมื่อ Run โปรแกรม ใส่เลขที่มีค่าอยู่ระหว่าง 1 - 20 และจะ Return ผลลัพธ์ออกมาดังนี้
```
output:
Enter a number between 1 - 20:  16
Number is: 16
Function A: Odd1Even6
Function B: DDO1NEVE6
Function C: 6868791786986696
Function D: DDO1NEVE6
Function E: Odd1Even6
Function F: 16
```
## How it work💡
---
### 🤖 Function A  รับ parameter เป็น Int  ทำหน้าที่แปลงจากตัวเลขให้เป็นดังนี้
หลักสิบ : ทำการแยกเลขให้เป็นหลักหน่วย 2 ตัว จากนั้นแปลงให้อยู่ในรูปแบบ "Odd" หรือ "Even" แล้วตามด้วยตัวเลขที่ใส่เข้าไป โดยใช้เกณฑ์เลขคู่หรือเลขคี่ในการแบ่ง และนำเลขอีกตัวมาแปลง
หลักหน่วย : แปลงให้อยู่ในรูปแบบ "Odd" หรือ "Even" แล้วตามด้วยตัวเลขที่ใส่เข้าไป โดยใช้เกณฑ์เลขคู่หรือเลขคี่ในการแบ่ง<br>
```Ex. 1 = 'Odd1' , 2 = 'Even2' , 3 = 'Odd3' , … 12 = 'Odd1Even2'```

### 🤖 Function B รับ parameter เป็น String ทำหน้าที่แปลงผลลัพธ์ที่ได้จาก Function ก่อนหน้าให้เป็นคำศัพท์ตัวพิมพ์ใหญ่แบบย้อนกลับ
```Ex. 'Odd1' = 'DDO1', 'Even2' = 'NEVE2' … 12 = 'DDO1NEVE2'```
### 🤖 Function  รับ parameter เป็น String ทำหน้าที่แปลงผลลัพธ์ที่ได้จาก Function ก่อนหน้าให้เป็นตัวเลข Ascii แต่ตัวเลขยังคงเดิม
```Ex. 'DDO1' = ‘6868791', ‘NEVE2' = '786986692' , … 12 = '6868791786986692'```
### 🤖 Function D รับ parameter เป็น String ทำหน้าที่แปลงผลลัพธ์ที่ได้จาก Function ก่อนหน้าให้อยู่ใน	รูปแบบผลลัพธ์ของ Function B
```Ex. '6868791' = 'DDO1' , '786986692' = 'NEVE2' , …  '6868791786986692' =  'DDO1NEVE2'```
### 🤖 Function E รับ parameter เป็น String ทำหน้าที่แปลงผลลัพธ์ที่ได้จาก Function ก่อนหน้าให้อยู่ในรูปแบบผลลัพธ์ของ Function A'
```Ex. 'DDO1' = 'Odd1' , 'NEVE2' = 'Even2' … 'DDO1NEVE2' = 'Odd1Even2'```
### 🤖 Function F รับ parameter เป็น String ทำหน้าที่แปลงผลลัพธ์ที่ได้จาก Function ก่อนหน้าให้อยู่ในรูปแบบตัวเลขที่รับเข้ามา
```Ex. 'Odd1' = 1, 'Even2’ = 2 , 'Odd3' = 3, … 'Odd1Even2'= 12```
 
