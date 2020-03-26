import model

m = model.Model()

def test_dk_m_same_speed():
    m.m1.speed = 10.0
    m.m2.speed = 10.0
    linear_speed, rotation_speed = m.dk()
    if linear_speed == 10 and rotation_speed == 0:
        print("Test dk m1 = 10, test m2 = 10 : OK")
    else:
        print("Test dk m1 = 10, test m2 = 10 : KO")


def test_dk_m1_null_m2_speed():
    m.m1.speed = 0.0
    m.m2.speed = 10.0
    linear_speed, rotation_speed = m.dk()
    if linear_speed != 0 and rotation_speed < 0:
        print("Test dk m1 = 0, m2 = 10 : OK")
    else:
        print("Test dk m1 = 0, m2 = 10 : KO")


def test_dk_m1_speed_m2_null():
    m.m1.speed = 10.0
    m.m2.speed = 0.0
    linear_speed, rotation_speed = m.dk()
    if linear_speed != 0 and rotation_speed > 0:
        print("Test dk m1 = 10, m2 = 0 : OK")
    else:
        print("Test dk m1 = 10, m2 = 0 : KO")


def test_ik_rot_speed_null():
    m.m1.speed, m.m2.speed = m.ik(10,0)
    if m.m1.speed == 10 and m.m2.speed == 10:
        print("Test ik linear_speed = 10, rotation_speed = 0 : OK")
    else:
        print("Test ik linear_speed = 10, rotation_speed = 0 : KO")


def test_ik_linear_speed_null_1():
    m.m1.speed, m.m2.speed = m.ik(0,10)
    if m.m1.speed > 0 and m.m2.speed < 0:
        print("Test ik linear_speed = 0, rotation_speed = 10 : OK")
    else:
        print("Test ik linear_speed = 0, rotation_speed = 10 : KO")


def test_ik_linear_speed_null_2():
    m.m1.speed, m.m2.speed = m.ik(0,-10)
    if m.m1.speed < 0 and m.m2.speed > 0:
        print("Test ik linear_speed = 0, rotation_speed = -10 : OK")
    else:
        print("Test ik linear_speed = 0, rotation_speed = -10 : KO")

test_dk_m_same_speed()
test_dk_m1_null_m2_speed()
test_dk_m1_speed_m2_null()
test_ik_rot_speed_null()
test_ik_linear_speed_null_1()
test_ik_linear_speed_null_2()