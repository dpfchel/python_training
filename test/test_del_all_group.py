


def test_all_group(app, db, check_ui):
    app.group.delete_all_group()
    assert len(db.get_group_list()) == 0
