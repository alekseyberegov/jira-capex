import pytest, datetime
from typing import Dict, List
from datetime import datetime
from sqlalchemy import MetaData, Table, create_engine, inspect, select, text
from jiracapex.orm.dyna_object import DynaObject

@pytest.fixture(scope="function")
def dyna_obj():
    return DynaObject('map_ping')

@pytest.fixture
def engine():
    return create_engine('sqlite:///:memory:', echo = True)

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
    
    @pytest.mark.parametrize("data", [({'field' : { 'prop1': {'nm': 'jiracapex', 'id': 12345}}})])
    def test_cast(self, dyna_obj: DynaObject, data: Dict) -> None:
        out: Dict = dyna_obj.cast(data)
        assert out['prop1_nm'] == data['field']['prop1']['nm']
        assert out['prop1_id'] == data['field']['prop1']['id']

    def test_storage(self, dyna_obj: DynaObject) -> None:
        metadata: MetaData = MetaData()
        table: Table = dyna_obj.storage(metadata)

        assert 'prop1_nm' in table.c
        assert 'prop1_id' in table.c
        assert 'prop1_dt' in table.c
        assert 'fkey1_id' in table.c
        assert 'fkey2_id' in table.c
        assert 'fkey3_id' in table.c
        assert 'prop1_id' in table.primary_key

        assert dyna_obj.table_name == table.name
        assert str(table.c.prop1_dt.type) == 'DATE'
        assert str(table.c.prop1_nm.type) == 'VARCHAR(250)'
        assert str(table.c.prop1_id.type) == 'INTEGER'
        assert str(table.c.fkey1_id.type) == 'INTEGER'

    def test_create_table(self, dyna_obj: DynaObject, engine) -> None:
        table: Table = dyna_obj.bind(engine).create_table()
        inspector = inspect(engine)
        assert inspector.has_table(table.name)

    @pytest.mark.parametrize("data", [({'field' : { 'prop1': {'nm': 'jiracapex', 'id': 12345, 'dt': '2022-02-27T22:44:00.000Z' }}})])
    def test_insert(self, dyna_obj: DynaObject, engine, data: Dict) -> None:
        dyna_obj.bind(engine).create_table()
        dyna_obj.insert(data)

        rows = None
        with engine.connect() as conn:
            rows = conn.execute(select(dyna_obj.table)).all()
        
        assert len(rows) == 1
        assert rows[0]['prop1_nm'] == data['field']['prop1']['nm']
        assert rows[0]['prop1_id'] == data['field']['prop1']['id']

    def test_get_ids(self, dyna_obj: DynaObject, engine) -> None:
        with engine.connect() as conn:
            tran = conn.begin()
            conn.execute(text("CREATE TABLE prop_table (prop1_id int, prop1_nm varchar(10))"))
            conn.execute(text("INSERT INTO  prop_table (prop1_id, prop1_nm) VALUES (:prop1_id, :prop1_nm)"),
                [
                    {"prop1_id": 10, "prop1_nm": "text 1"}, 
                    {"prop1_id": 20, "prop1_nm": "text 2"},
                    {"prop1_id": 30, "prop1_nm": "text 3"}
                ]
            )
            tran.commit()

        dyna_obj.bind(engine).create_table()
        ids = {}
        for id in dyna_obj.get_values('prop1_id'):
            ids[str(id)] = id

        assert ids['10'] == 10
        assert ids['20'] == 20
        assert ids['30'] == 30



    @pytest.mark.parametrize("data", [({'field' : { 'prop1': {}}})])
    def test_flush(self, dyna_obj: DynaObject, engine, data: Dict) -> None:
        dyna_obj.bind(engine).create_table()
        ids = [i for i in range(10, 110, 10)]
        nms = [f"item {i}" for i in ids]
        for i in ids:
            data['field']['prop1']['id'] = i
            data['field']['prop1']['nm'] = f"item {i}"
            data['field']['prop1']['dt'] = datetime.now().isoformat() + 'Z'
            dyna_obj.add(data)
        dyna_obj.flush()

        rows = None
        with engine.connect() as conn:
            rows = conn.execute(select(dyna_obj.table)).all()

        assert len(rows) == 10
        for r in rows:
            assert r['prop1_id'] in ids
            assert r['prop1_nm'] in nms

    def test_nodes(self, dyna_obj: DynaObject) -> None:
        nodes: List = dyna_obj.nodes()

        assert 'prop1' in nodes
        assert 'prop2' in nodes
        assert 'prop3' in nodes