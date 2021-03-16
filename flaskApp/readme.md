db.create_all()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\javacloudmc597\.virtualenvs\vmdemo-sKQ0gMMj\lib\site-packages\flask_sqlalchemy\__init__.py", line 1039, in create_all
    self._execute_for_all_tables(app, bind, 'create_all')
  File "C:\Users\javacloudmc597\.virtualenvs\vmdemo-sKQ0gMMj\lib\site-packages\flask_sqlalchemy\__init__.py", line 1031, in _execute_for_all_tables
    op(bind=self.get_engine(app, bind), **extra)
  File "C:\Users\javacloudmc597\.virtualenvs\vmdemo-sKQ0gMMj\lib\site-packages\flask_sqlalchemy\__init__.py", line 962,
in get_engine
    return connector.get_engine()
  File "C:\Users\javacloudmc597\.virtualenvs\vmdemo-sKQ0gMMj\lib\site-packages\flask_sqlalchemy\__init__.py", line 555,
in get_engine
    options = self.get_options(sa_url, echo)
  File "C:\Users\javacloudmc597\.virtualenvs\vmdemo-sKQ0gMMj\lib\site-packages\flask_sqlalchemy\__init__.py", line 570,
in get_options
    self._sa.apply_driver_hacks(self._app, sa_url, options)
  File "C:\Users\javacloudmc597\.virtualenvs\vmdemo-sKQ0gMMj\lib\site-packages\flask_sqlalchemy\__init__.py", line 914,
in apply_driver_hacks
    sa_url.database = os.path.join(app.root_path, sa_url.database)
AttributeError: can't set attribute
