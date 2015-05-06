from arbtt_record import ArbttRecord
from nose.tools import raises

class TestCSVInput:

    @raises(ValueError)
    def test_csv_with_less_than_two_fields_raises_exception(self):
        csv_input = "title:foo"
        arbtt_record = ArbttRecord(csv_input)

    @raises(ValueError)
    def test_app_property_with_non_program_tag_raises_exception(self):
        csv_input = "title:foo,00:00:00,45"
        arbtt_record = ArbttRecord(csv_input)

    @raises(ValueError)
    def test_app_duration_without_valid_h_m_s_raises_exception(self):
        csv_input = "Program:foo,00:00:sec,45"
        arbtt_record = ArbttRecord(csv_input)

    def test_application_name_from_valid_csv(self):
        csv_input = "Program:foo,00:00:31,45"
        arbtt_record = ArbttRecord(csv_input)
        assert arbtt_record.application == "foo"

    def test_duration_from_valid_csv(self):
        csv_input = "Program:foo,00:00:31,45"
        arbtt_record = ArbttRecord(csv_input)
        assert arbtt_record.duration == "00:00:31"
    
        
        
