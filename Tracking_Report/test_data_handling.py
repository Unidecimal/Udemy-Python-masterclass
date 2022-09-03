import datetime
import unittest
import data_handling


class TestReport(unittest.TestCase):

    def setUp(self):
        self.test_list = [[datetime.datetime(2019, 3, 1, 9, 0),
                           '/contact.html', '12345'],
                          [datetime.datetime(2019, 3, 1, 9, 0),
                           '/contact.html', '12346'],
                          [datetime.datetime(2019, 3, 1, 10, 0),
                           '/contact.html', '12345'],
                          [datetime.datetime(2019, 3, 1, 10, 30),
                           '/home.html   ', '12347'],
                          [datetime.datetime(2019, 3, 1, 11, 0),
                           '/contact.html', '12347'],
                          [datetime.datetime(2019, 3, 2, 11, 0),
                           '/contact.html', '12348'],
                          [datetime.datetime(2019, 3, 2, 12, 0),
                           '/home.html   ', '12348'],
                          [datetime.datetime(2019, 3, 3, 13, 0),
                           '/home.html   ', '12349'],
                          ]

    def test_create_date(self):
        result = data_handling.create_date("2019-03-01 09:00:00UTC")
        self.assertIsInstance(result, datetime.datetime)
        result = data_handling.create_date("2019-04-04 10:00:00UTC")
        self.assertEqual(result, datetime.datetime(2019, 4, 4, 10, 0))
        result = data_handling.create_date("1970-01-01 00:00:00UTC")
        self.assertEqual(result, datetime.datetime(1970, 1, 1, 0, 0))
        result = data_handling.create_date("2036-03-06 23:59:59UTC")
        self.assertEqual(result, datetime.datetime(2036, 3, 6, 23, 59, 59))

    def test_is_date_time_in_range(self):
        result = data_handling.is_date_time_in_range("2019-03-01 09:00:00 - 2019-03-02 11:59:59",
                                                     datetime.datetime(2019, 3, 1, 20, 0, 0))
        self.assertTrue(result)
        result = data_handling.is_date_time_in_range("2019-03-01 09:00:00 - 2019-03-02 11:59:59",
                                                     datetime.datetime(2010, 1, 1, 11, 0, 0))
        self.assertFalse(result)
        result = data_handling.is_date_time_in_range("2020-06-01 00:00:01 - 2022-01-02 11:59:59",
                                                     datetime.datetime(2020, 6, 1, 0, 0, 1))
        self.assertTrue(result)
        result = data_handling.is_date_time_in_range("2020-03-01 09:00:00 - 2023-03-02 11:59:59",
                                                     datetime.datetime(2023, 3, 2, 12, 0, 0))
        self.assertFalse(result)

    def test_create_report(self):
        test_dict = {'/contact.html': (5, {'12345': 2, '12346': 1, '12347': 1, '12348': 1}),
                     '/home.html   ': (1, {'12347': 1})
                     }

        result = data_handling.create_report(self.test_list, "2019-03-01 09:00:00 - 2019-03-02 11:59:59")
        self.assertIsInstance(result, dict)
        result = data_handling.create_report(self.test_list, "2019-03-01 09:00:00 - 2019-03-02 11:59:59")
        self.assertEqual(result, test_dict)

    def test_read_log_file(self):
        file_path = "test_log.txt"

        result = data_handling.read_log_file(file_path)
        self.assertIsInstance(result, list)

        result = data_handling.read_log_file(file_path)
        self.assertEqual(result, self.test_list)

    def test_print_report(self):
        test_data = {'/home.html   ': (1, {'12347': 1}),
                     '/contact.html': (5, {'12346': 1, '12345': 2, '12347': 1, '12348': 1})}
        result = data_handling.print_report(test_data)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
