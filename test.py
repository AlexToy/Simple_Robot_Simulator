import model

m = model.Model

def test_dk_m_same_speed():
    linear_speed, rotation_speed = m.dk(m, 10, 10)
    if linear_speed == 10 and rotation_speed == 0:
        print(" Test dk same speed : OK")
    else:
        print(" Test dk same speed : KO")


def test_dk_m1_null_m2_speed():
    linear_speed, rotation_speed = m.dk(m, 0, 10)
    if linear_speed == 0 and rotation_speed != 0:
        print(" Test dk m1 = 0, m2 = speed : OK")
    else:
        print(" Test dk m1 = 0, m2 = speed : KO")

test_dk_m1_null_m2_speed()
test_dk_m_same_speed()