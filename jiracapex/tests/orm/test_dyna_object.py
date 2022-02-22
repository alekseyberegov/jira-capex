import pytest, json
from typing import Dict
from datetime import datetime
from sqlalchemy import MetaData, Table
from jiracapex.orm.dyna_object import DynaObject

@pytest.fixture
def dyna_obj():
    return DynaObject('map_ping')

class TestDynaObject:
    def test_table_name(self, dyna_obj: DynaObject) -> None:
        assert dyna_obj.table_name == 'prop_table'

    def test_primary_key(self, dyna_obj: DynaObject) -> None:
        assert dyna_obj.primary_key == 'prop1_id'

    def test_foreign_keys(self, dyna_obj: DynaObject) -> None:
        assert dyna_obj.foreign_keys == ['fkey1_id', 'fkey2_id', 'fkey3_id']

    def test_date_fields(self, dyna_obj: DynaObject) -> None:
        assert dyna_obj.date_fields == ['prop1_dt']

    def test_get_field(self, dyna_obj: DynaObject) -> None:
        assert dyna_obj.get_field('field_prop1_nm') == 'prop1_nm'
        assert dyna_obj.get_field('field_prop1_id') == 'prop1_id'

    def test_to_date(self, dyna_obj: DynaObject) -> None:
        dt: datetime = dyna_obj.to_date('2022-01-31T20:14:44.668Z')
        assert dt.month == 1
        assert dt.year  == 2022
        assert dt.day   == 31
    
    @pytest.mark.parametrize("data", [({'field' : { 'prop1': {'nm': 'jiracapex', 'id': '12345'}}})])
    def test_map_object(self, dyna_obj: DynaObject, data: Dict) -> None:
        out: Dict = dyna_obj.map_object(data)
        assert out['prop1_nm'] == data['field']['prop1']['nm']
        assert out['prop1_id'] == data['field']['prop1']['id']

    def test_make_table(self, dyna_obj: DynaObject) -> None:
        metadata: MetaData = MetaData()
        table: Table = dyna_obj.make_table(metadata)

        assert 'prop1_nm' in table.c
        assert 'prop1_id' in table.c
        assert 'prop1_dt' in table.c
        assert 'fkey1_id' in table.c
        assert 'fkey2_id' in table.c
        assert 'fkey3_id' in table.c
        assert 'prop1_id' in table.primary_key
        
        assert dyna_obj.table_name == table.name
        assert str(table.c.prop1_dt.type) == 'DATE'
        assert str(table.c.prop1_nm.type) == 'VARCHAR(120)'
        assert str(table.c.prop1_id.type) == 'INTEGER'
        assert str(table.c.fkey1_id.type) == 'INTEGER'

