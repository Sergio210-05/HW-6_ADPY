import unittest
import dictionaries
from parameterized import parameterized


class MyTestCase(unittest.TestCase):

    def test_dictionaries_geo(self):
        self.assertEqual(dictionaries.geo_logs,
                         [
                             {'visit1': ['Москва', 'Россия']},
                             {'visit3': ['Владимир', 'Россия']},
                             {'visit7': ['Тула', 'Россия']},
                             {'visit8': ['Тула', 'Россия']},
                             {'visit9': ['Курск', 'Россия']},
                             {'visit10': ['Архангельск', 'Россия']}
                         ]
                         )

    def test_dictionaries_unique_id(self):
        self.assertEqual(set(dictionaries.unique_id_list), {213, 15, 54, 119, 98, 35})

    def test_dictionaries_site_sales(self):
        self.assertEqual(dictionaries.best_sites, ['yandex'])


if __name__ == '__main__':
    unittest.main()
