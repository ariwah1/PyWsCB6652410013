import os

def createsubjectfile():
    filename = input("กรุณาตั้งชื่อไฟล์ (ภาษาอังกฤษ) โดยต้องมีนามสกุล .txt เท่านั้น: ")
    
    if not filename.endswith(".txt"):
        print("ชื่อ-นามสกุลไฟล์ไม่ถูกต้อง กรุณาป้อนใหม่")
        return
    
    with open(filename, 'w') as file:
        print("ไฟล์ถูกสร้างขึ้นแล้ว")
        
        studentname = input("ชื่อ-สกุลนักเรียน: ")
        midtermscore = float(input("คะแนนสอบกลางภาค: "))
        finalscore = float(input("คะแนนสอบปลายภาค: "))
        homeworkscore = float(input("คะแนนเก็บ: "))
        
        totalscore = midtermscore + finalscore + homeworkscore
        result = "ผ่าน" if totalscore > 50 else "ไม่ผ่าน"
        
        file.write(f"{studentname},{midtermscore},{finalscore},{homeworkscore},{totalscore},{result}\n")
        print("สร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว")

def selectsubjectandappenddata():
    files = [f for f in os.listdir('.') if f.endswith('.txt')]
    
    if not files:
        print("ไม่มีไฟล์ใดๆ อยู่เลย")
        return
    
    print("รายชื่อไฟล์ที่มีอยู่:")
    for file in files:
        print(file)
    
    selectedfile = input("กรุณาเลือกไฟล์ที่ต้องการ: ")
    
    if selectedfile not in files:
        print("คุณพิมพ์ชื่อไฟล์ผิด")
        return
    
    with open(selectedfile, 'a') as file:
        studentname = input("ชื่อ-สกุลนักเรียน: ")
        midtermscore = float(input("คะแนนสอบกลางภาค: "))
        finalscore = float(input("คะแนนสอบปลายภาค: "))
        homeworkscore = float(input("คะแนนเก็บ: "))
        
        totalscore = midtermscore + finalscore + homeworkscore
        result = "ผ่าน" if totalscore > 50 else "ไม่ผ่าน"
        
        file.write(f"{studentname},{midtermscore},{finalscore},{homeworkscore},{totalscore},{result}\n")
        print("เพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว")

def selectsubjectandreaddata():
    files = [f for f in os.listdir('.') if f.endswith('.txt')]
    
    if not files:
        print("ไม่มีไฟล์วิชาใดๆ อยู่เลย")
        return
    
    print("รายชื่อไฟล์ที่มีอยู่:")
    for file in files:
        print(file)
    
    selectedfile = input("กรุณาเลือกไฟล์ที่ต้องการ: ")
    
    if selectedfile not in files:
        print("คุณพิมพ์ชื่อไฟล์ผิด")
        return
    
    with open(selectedfile, 'r') as file:
        content = file.read()
        print(content)

def selectsubjectanddeletefile():
    files = [f for f in os.listdir('.') if f.endswith('.txt')]
    
    if not files:
        print("ไม่มีไฟล์ใดๆ อยู่เลย")
        return
    
    print("รายชื่อไฟล์ที่มีอยู่:")
    for file in files:
        print(file)
    
    selectedfile = input("กรุณาเลือกไฟล์ที่ต้องการลบ: ")
    
    if selectedfile not in files:
        print("คุณพิมพ์ชื่อไฟล์ผิด")
        return
    
    os.remove(selectedfile)
    print("ลบไฟล์เรียบร้อยแล้ว")

while True:
    print("\nเมนู:")
    print("1. สร้างไฟล์วิชาใหม่เพื่อเพิ่มข้อมูล")
    print("2. เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์")
    print("3. เลือกวิชาและอ่านข้อมูลจากไฟล์มาแสดงผล")
    print("4. เลือกวิชาและลบไฟล์")
    print("0. จบการทำงาน")

    choice = input("กรุณาเลือกเมนู (1, 2, 3, 4, 0): ")

    if choice == '1':
        createsubjectfile()
    elif choice == '2':
        selectsubjectandappenddata()
    elif choice == '3':
        selectsubjectandreaddata()
    elif choice == '4':
        selectsubjectanddeletefile()
    elif choice == '0':
        print("จบการทำงาน")
        break
    else:
        print("กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น")
