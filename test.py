import model

m = model.Model()

def test_dk_m_same_speed():
    m.m1.speed = 10.0
    m.m2.speed = 10.0
    linear_speed, rotation_speed = m.dk()
    if linear_speed == 10 and rotation_speed == 0:
        print(" Test dk m1 = 10, test m2 = 10 : OK")
    else:
        print(" Test dk m1 = 10, test m2 = 10 : KO")


def test_dk_m1_null_m2_speed():
    m.m1.speed = 0.0
    m.m2.speed = 10.0
    linear_speed, rotation_speed = m.dk()
    if linear_speed == 0 and rotation_speed != 0:
        print(" Test dk m1 = 0, m2 = 10 : OK")
    else:
        print(" Test dk m1 = 0, m2 = 10 : KO")

test_dk_m1_null_m2_speed()
test_dk_m_same_speed()