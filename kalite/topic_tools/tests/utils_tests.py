from mock import patch, MagicMock

import kalite.topic_tools as mod
from kalite.testing.base import KALiteTestCase


DUMMY_STRING = "maize"
TRANS_STRING = "trans"


ugettext_dummy = MagicMock(return_value=DUMMY_STRING)


@patch.object(mod, '_', new=ugettext_dummy)
class SmartTranslateItemDataTests(KALiteTestCase):

    def tearDown(self):
        ugettext_dummy.reset_mock()

    def test_list_of_lists(self):
        test_data = [[TRANS_STRING]]
        expected_data = [[DUMMY_STRING]]

        result = mod.smart_translate_item_data(test_data)
        ugettext_dummy.assert_called_once_with(TRANS_STRING)

        self.assertEqual(result, expected_data)

    def test_simple_content_dict(self):
        # ugettext_method.return_value = DUMMY_STRING
        test_data = {'content': TRANS_STRING}
        expected_data = {'content': DUMMY_STRING}

        result = mod.smart_translate_item_data(test_data)
        ugettext_dummy.assert_called_once_with(TRANS_STRING)

        self.assertEqual(result, expected_data)

    def test_content_in_widgets_field(self):
        test_data = {'widgets': {'content': TRANS_STRING}}
        expected_data = {'widgets': {'content': DUMMY_STRING}}

        result = mod.smart_translate_item_data(test_data)
        ugettext_dummy.assert_called_once_with(TRANS_STRING)

        self.assertEqual(result, expected_data)

    def test_content_inside_radio_field(self):
        test_data = {'radio 1': {'widgets': {'content': TRANS_STRING}}}
        expected_data = {'radio 1': {'widgets': {'content': DUMMY_STRING}}}

        result = mod.smart_translate_item_data(test_data)
        ugettext_dummy.assert_called_once_with(TRANS_STRING)

        self.assertEqual(result, expected_data)

    def test_simple_string(self):
        test_data = TRANS_STRING
        expected_data = DUMMY_STRING

        result = mod.smart_translate_item_data(test_data)
        ugettext_dummy.assert_called_once_with(TRANS_STRING)

        self.assertEqual(result, expected_data)
