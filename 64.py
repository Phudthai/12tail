import subprocess
import time
import pyautogui

pyautogui.FAILSAFE = False

def switch_to_12tails():
    # กด Alt+Tab เพื่อย้าย Tab ไปที่โปรแกรม 11.5tails
    pyautogui.hotkey('alt', 'tab')

def create_autogun():
    # กดปุ่ม w เป็นเวลา 1 วินาที
    print("กำลังกดปุ่ม 1...")
    pyautogui.keyDown('1')
    time.sleep(2.5)
    pyautogui.keyUp('1')

def press_q():
    print("กำลังกดปุ่ม q...")
    pyautogui.keyDown('q')
    time.sleep(1.5)
    pyautogui.keyUp('q')

def press_qw_camp():
    print("กำลังกดปุ่ม q...")
    pyautogui.keyDown('q')
    time.sleep(0.4)
    pyautogui.keyDown('w')
    time.sleep(3)
    pyautogui.click(1139, 736)
    pyautogui.keyUp('w')
    pyautogui.keyUp('q')

def press_sq():
    print("กำลังกดปุ่ม q...")
    pyautogui.keyDown('s')
    pyautogui.keyDown('q')
    time.sleep(0.5)
    pyautogui.keyUp('s')
    pyautogui.keyUp('q')


def press_e():
    print("กำลังกดปุ่ม e...")
    pyautogui.keyDown('e')
    time.sleep(1.5)
    pyautogui.keyUp('e')

def press_e_config():
    print("กำลังกดปุ่ม e...")
    pyautogui.keyDown('e')
    time.sleep(0.7)
    pyautogui.keyUp('e')

def press_w():
    print("กำลังกดปุ่ม w...")
    pyautogui.keyDown('w')
    time.sleep(1.5)
    pyautogui.keyUp('w')

def press_wconfig():
    print("กำลังกดปุ่ม w...")
    pyautogui.keyDown('w')
    time.sleep(1.75)
    pyautogui.keyUp('w')

def press_s():
    print("กำลังกดปุ่ม s...")
    pyautogui.keyDown('s')
    time.sleep(1.3)
    pyautogui.keyUp('s')

def create_robot():
    print("กำลังกดปุ่ม 2...")
    pyautogui.keyDown('2')
    time.sleep(4.5)
    pyautogui.keyUp('2')

def press_reload():
    print("กำลังกดปุ่ม 8...")
    pyautogui.keyDown('8')
    time.sleep(0.2)
    pyautogui.keyUp('8')

def press_sync():
    print("กำลังกดปุ่ม 7...")
    pyautogui.keyDown('7')
    time.sleep(0.2)
    pyautogui.keyUp('7')

def press_6():
    print("กำลังกดปุ่ม6...")
    pyautogui.keyDown('6')
    time.sleep(1)
    pyautogui.keyUp('6')

def press_5():
    print("กำลังกดปุ่ม 5...")
    pyautogui.keyDown('5')
    time.sleep(0.5)
    pyautogui.keyUp('5')

def press_c():
    print("กำลังกดปุ่ม z...")
    pyautogui.keyDown('z')
    time.sleep(2.7)
    pyautogui.keyUp('z')

def press_c_camp():
    print("กำลังกดปุ่ม c...")
    pyautogui.keyDown('c')
    time.sleep(1.5)
    pyautogui.keyUp('c')

def press_0():
    print("กำลังกดปุ่ม 0...")
    pyautogui.keyDown('0')
    time.sleep(0.7)
    pyautogui.keyUp('0')

def press_space():
    print("กำลังกดปุ่ม Spacebar...")
    pyautogui.keyDown('space')
    time.sleep(0.2)  # กด Spacebar เป็นเวลา 2 วินาที
    pyautogui.keyUp('space')


def check_mission_camp():
    image_path = "image/mission_camp.png"  # รูปภาพที่ต้องการคลิก
    target_position = pyautogui.locateCenterOnScreen(image_path)

    if target_position is not None:
        # คลิกที่ตำแหน่ง
        pyautogui.click(target_position)
    else:
        print("ไม่พบรูปภาพที่ต้องการคลิก")
        
class ImageNotFoundException(pyautogui.ImageNotFoundException):
    pass

def create_turret():
    image_path = "image/turret.png"  # รูปภาพที่ต้องการคลิก
    target_region = (1011, 1000, 86, 79)  # บริเวณที่ต้องการค้นหา
    while True:
        try:
            target_position = pyautogui.locateCenterOnScreen(image_path, region=target_region, grayscale=True, confidence=0.7)
            break
        except pyautogui.ImageNotFoundException:
            print("ไม่พบรูปภาพที่ต้องการคลิก")
            time.sleep(0.3)
            pyautogui.dragTo(96, 963, 0.2)

    if target_position is not None:
        # คลิกที่ตำแหน่ง
        print("พบปืน")
        pyautogui.click(target_position)
        
    else:
        # เรียกใช้ข้อยกเว้น ImageNotFoundException เมื่อไม่พบรูปภาพ
        raise ImageNotFoundException("ไม่พบรูปภาพที่ต้องการคลิก")

def end():
    image_path = "image/end.png"  # รูปภาพที่ต้องการคลิก
    target_region = (484, 182, 396, 109)  # บริเวณที่ต้องการค้นหา
    while True:
        try:
            target_position = pyautogui.locateCenterOnScreen(image_path, region=target_region, grayscale=True, confidence=0.7)
            break
        except pyautogui.ImageNotFoundException:
            print("ไม่พบรูปภาพที่ต้องการคลิก")
            time.sleep(0.5)

    if target_position is not None:
        print("พบปืน")
    else:
        # เรียกใช้ข้อยกเว้น ImageNotFoundException เมื่อไม่พบรูปภาพ
        raise ImageNotFoundException("ไม่พบรูปภาพที่ต้องการคลิก")

def check_cannon():
    image_path = "image/image.png"  # รูปภาพที่ต้องการคลิก
    target_region = (522, 534, 393, 175)  # บริเวณที่ต้องการค้นหา
    try:
        target_position = pyautogui.locateCenterOnScreen(image_path, region=target_region, grayscale=True, confidence=0.7)
    except pyautogui.ImageNotFoundException:
        raise ImageNotFoundException("ไม่พบรูปภาพที่ต้องการคลิก")

    if target_position is not None:
        # คลิกที่ตำแหน่ง
        print("พบปืน")
        pyautogui.click(target_position)
    else:
        # เรียกใช้ข้อยกเว้น ImageNotFoundException เมื่อไม่พบรูปภาพ
        raise ImageNotFoundException("ไม่พบรูปภาพที่ต้องการคลิก")

def check_hp():
    image_path = "image/hp.png"  # รูปภาพที่ต้องการคลิก
    target_region = (522, 534, 393, 175)  # บริเวณที่ต้องการค้นหา
    while True:
        try:
            target_position = pyautogui.locateCenterOnScreen(image_path, region=target_region, grayscale=True, confidence=0.7)
            # คลิกที่ตำแหน่ง
            print("พบปืน")
            pyautogui.click(target_position)
            time.sleep(0.8)
        except pyautogui.ImageNotFoundException:
            print("ไม่พบรูปภาพที่ต้องการคลิก")
            break
    
    # เมื่อไม่พบรูปภาพหลังจากทดลองหลายครั้ง
    raise ImageNotFoundException("ไม่พบรูปภาพที่ต้องการคลิก")

def check_ring():
    image_path = "image/ring.png"  # รูปภาพที่ต้องการคลิก
    target_region = (522, 534, 393, 175)  # บริเวณที่ต้องการค้นหา
    try:
        target_position = pyautogui.locateCenterOnScreen(image_path, region=target_region, grayscale=True, confidence=0.8)
    except pyautogui.ImageNotFoundException:
        raise ImageNotFoundException("ไม่พบรูปภาพที่ต้องการคลิก")

    if target_position is not None:
        # คลิกที่ตำแหน่ง
        print("พบปืน")
        pyautogui.click(target_position)
    else:
        # เรียกใช้ข้อยกเว้น ImageNotFoundException เมื่อไม่พบรูปภาพ
        raise ImageNotFoundException("ไม่พบรูปภาพที่ต้องการคลิก")

def check_cannon_2():
    image_path = "image/image.png"  # รูปภาพที่ต้องการคลิก
    target_region = (522, 534, 393, 175)  # บริเวณที่ต้องการค้นหา
    try :
        target_position = pyautogui.locateCenterOnScreen(image_path, region=target_region, grayscale=True, confidence=0.7)
    except pyautogui.ImageNotFoundException:
        raise ImageNotFoundException("ไม่พบรูปภาพที่ต้องการคลิก")


    if target_position is not None:
        # คลิกที่ตำแหน่ง
        print("พบปืน")
        pyautogui.click(target_position)
    else:
        # เรียกใช้ข้อยกเว้น ImageNotFoundException เมื่อไม่พบรูปภาพ
        raise ImageNotFoundException("ไม่พบรูปภาพที่ต้องการคลิก")
        
class ColorNotFoundException(Exception):
    pass

def press_f3():
    print("กำลังกดปุ่ม F3...")
    pyautogui.keyDown('f3')
    time.sleep(0.5)
    pyautogui.keyUp('f3')
    time.sleep(1.2)
    pyautogui.click(1802, 883)
        
def main():
    # # print("โปรแกรมจะย้าย Tab ไปที่ 11.5tails และทำการกดปุ่ม w และ a ในเวลาที่กำหนด")
    # print("กด Enter เพื่อเริ่มการทำงาน...")
    # input()

    # # # ย้าย Tab ไปที่ 11.5tails
    # switch_to_12tails()

    # # หน่วงเวลา 5 วินาทีเพื่อให้โปรแกรม 11.5tails เปิดและโหลด
    time.sleep(2)

    try:
       check_ring()
    except ImageNotFoundException as e:
       print(e)

    time.sleep(0.8)

    try:
        check_hp()
    except ImageNotFoundException as e:
        print(e)

    time.sleep(0.8)

    try:
        check_cannon()
    except ImageNotFoundException as e:
        print(e)

    time.sleep(0.8)
    
    pyautogui.click(843, 822)
    print("กลับแคมป์")

    press_f3()

    pyautogui.press

    time.sleep(3)

    press_qw_camp()

    time.sleep(6.5)

    pyautogui.click(1656, 693)

    time.sleep(1.2)

    pyautogui.click(1656, 693)

    time.sleep(16)

    press_sq()

    try:
        create_turret()
    except ImageNotFoundException as e:
        print(e)

    time.sleep(2.5)

    create_robot()

    press_e()

    try:
        create_turret()
    except ImageNotFoundException as e:
        print(e)

    time.sleep(2.5)
    
    press_w()

    try:
        create_turret()
    except ImageNotFoundException as e:
        print(e)

    time.sleep(0.5)

    press_sync()

    time.sleep(0.5)

    press_q()

    time.sleep(2)

    try:
        create_turret()
    except ImageNotFoundException as e:
        print(e)

    time.sleep(2.5)

    press_wconfig()

    press_reload()

    create_autogun()
    time.sleep(0.5)
    press_sync()

    press_e_config()
    
    time.sleep(8)

    press_6()

    press_space()

    press_5()

    press_0()

    print("จบด่านเสร็จสิ้น")

    end()
    
    time.sleep(4)

    main()

if __name__ == "__main__":
    main()

    
