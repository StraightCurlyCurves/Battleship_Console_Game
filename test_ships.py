import unittest
from ships import Fleet

class TestShips(unittest.TestCase):
    def test_ship_and_fleet(self):
        my_fleet = Fleet()
        my_fleet.ships['carrier_1'].set_alignment('horizontal')
        my_fleet.ships['carrier_1'].set_start_coordinates([2,3])
        my_fleet.ships['destroyer_1'].set_start_coordinates([7,7])
        my_fleet.place_ships()

        spm_fleet = my_fleet.shots_per_minute

        spm_ship = my_fleet.ships['carrier_1'].shots_per_minute

        is_hit, is_destroyed = my_fleet.hit_coordinates([2,2])
        self.assertFalse(is_hit)
        self.assertFalse(is_destroyed)
        self.assertEqual(spm_ship, my_fleet.ships['carrier_1'].shots_per_minute)
        self.assertEqual(spm_fleet, my_fleet.shots_per_minute)

        is_hit, is_destroyed = my_fleet.hit_coordinates([2,3])
        self.assertTrue(is_hit)
        self.assertFalse(is_destroyed)
        self.assertEqual(spm_ship-2, my_fleet.ships['carrier_1'].shots_per_minute)
        self.assertEqual(spm_fleet-2, my_fleet.shots_per_minute)
        self.assertFalse(my_fleet.ships['carrier_1'].destroyed)

        spm_ship = my_fleet.ships['destroyer_1'].shots_per_minute

        is_hit, is_destroyed = my_fleet.hit_coordinates([7,7])
        self.assertTrue(is_hit)
        self.assertFalse(is_destroyed)
        self.assertEqual(spm_ship-2, my_fleet.ships['destroyer_1'].shots_per_minute)
        self.assertEqual(spm_fleet-4, my_fleet.shots_per_minute)
        self.assertFalse(my_fleet.ships['destroyer_1'].destroyed)

        is_hit, is_destroyed = my_fleet.hit_coordinates([7,8])
        self.assertTrue(is_hit)
        self.assertTrue(is_destroyed)
        self.assertEqual(spm_ship-4, my_fleet.ships['destroyer_1'].shots_per_minute)
        self.assertEqual(spm_fleet-6, my_fleet.shots_per_minute)
        self.assertEqual(0, my_fleet.ships['destroyer_1'].shots_per_minute)
        self.assertTrue(my_fleet.ships['destroyer_1'].destroyed)



if __name__ == '__main__':
    unittest.main()


