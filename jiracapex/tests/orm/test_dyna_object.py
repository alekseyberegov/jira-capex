from jiracapex.orm.dyna_object import DynaObject

class TestDynaObject:
    def test_load_map(self):
        obj = DynaObject('map_ol')
        assert obj.get_field('fields_priority_name') == 'priority_name'