from convert.convert_sumerian import *


def test_sumerian_cardinal():
    cardinal_tests = [
        ("1(u) 2(asz)", Cardinal, 12),
        ("2(asz)", Cardinal, 2),
        ("1(asz)", Cardinal, 1),
        ("3(u) 2(disz) 5(disz) gin2 2(disz) sze", Cardinal, 32.08351851851852),
        (
            "3(disz) 1/3(disz) 9(disz) 2/3(disz) gin2 4(disz) igi-4(disz)-gal2 sze",
            Cardinal,
            3.494837962962963,
        ),
        ("1(disz) 1(u) gin2", Cardinal, 1.1666666666666667),
        ("1(disz) 1(u) 1(disz) gin2", Cardinal, 1.1833333333333333),
        (
            "1(disz) 1/2(disz) 1/4(disz) 1(disz) 1/2(disz) 1/4(disz) gin2",
            Cardinal,
            1.7791666666666668,
        ),
        ("igi-6(disz)-gal2 sze", Cardinal, 1 / 64800),
    ]
    for test, system, expected in cardinal_tests:
        assert np.isclose(convert(test, system)[0]["value"], expected)


def test_sumerian_length():
    length_tests = [
        ("1(gesz2) 2(u) 1(disz) 1/2(disz) ninda", Length, 163),
    ]
    for test, system, expected in length_tests:
        assert np.isclose(convert(test, system)[0]["value"], expected)


def test_sumerian_surface():
    surface_tests = [
        (
            "1(szargal){gal} 7(szar2) 1(bur'u) 4(bur3) 2(esze3) 5(iku) 1/2(iku) 1/4(iku) GAN2",
            Surface,
            435778500.0,
        ),
    ]
    for test, system, expected in surface_tests:
        assert np.isclose(convert(test, system)[0]["value"], expected)


def test_sumerian_volume():
    volume_tests = [
        (
            "1(u) 5/6(disz) sar 2(disz) 2/3(disz) gin2 2(u) sze",
            Volume,
            652.7777777777777777,
        ),
        ("1(bur3)", Volume, 108000),
        ("1(esze3)", Volume, 36000),
        ("1(bur3) 2(esze3)", Volume, 180000),
        ("1(bur3) 2(esze3) 1(iku) 1/4(iku) iku", Volume, 187500),
        ("1(bur3) 1(esze3) 1(u) 1(disz) sar 1(disz) sze", Volume, 144660.00555555554),
        ("1(bur3) 1(esze3) 1(iku) iku 1(u) 1(disz) sar", Volume, 150660),
    ]
    for test, system, expected in volume_tests:
        assert np.isclose(convert(test, system)[0]["value"], expected)


def test_sumerian_drycapacity():
    drycapacity_tests = [
        (
            "1(gesz2) 2(u) 1(asz) 2(barig) 3(ban2) 2(disz) 1/2(disz) sila3 sze gur",
            DryCapacity,
            24452.5,
        ),
    ]
    for test, system, expected in drycapacity_tests:
        assert np.isclose(convert(test, system)[0]["value"], expected)


def test_sumerian_brick():
    brick_tests = [
        ("6(disz) 1/3(disz) sar 7(disz) gin2", Brick, 4644),
        ("2(gesz2) 2(u) 2(disz) sar 1(u) 2(disz) gin2", Brick, 102384),
    ]
    for test, system, expected in brick_tests:
        assert np.isclose(convert(test, system)[0]["value"], expected)
