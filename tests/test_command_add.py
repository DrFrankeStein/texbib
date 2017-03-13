def test_adding_file(commands, tmpdir):
    path = tmpdir.join('test.bib')
    with path.open('w') as testfile:
        testfile.write("""@book{foo,
            author = "Mr. Mister",
            year = 1999,
            title = "The title"
        }""")
    commands['add']([path])
    assert 'foo' in commands.run.active.db.keys()


def test_skip_non_existing(commands, tmpdir, capsys):
    commands['add']([tmpdir.join('foo.bib')])
    _, err = capsys.readouterr()
    assert 'FileNotFound' in err


def test_empty_list(commands):
    commands['add']([])