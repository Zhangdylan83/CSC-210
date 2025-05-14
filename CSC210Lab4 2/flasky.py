import click
from flask.cli import with_appcontext
import os
import sys
import unittest
import coverage

from app.app import create_app, db, User

app = create_app()

cov = coverage.coverage(branch=True, omit=['test/*'])

@app.cli.command()
@click.option('--coverage', is_flag=True, help='Run tests under code coverage.')
def test(coverage):
    """Run the unit tests with or without coverage."""
    if coverage:
        cov.start()

    tests = unittest.TestLoader().discover('test')
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if coverage:
        cov.stop()  
        cov.save()  
        print('Coverage Summary:')
        cov.report()  
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        cov.html_report(directory=covdir) 
        print(f'HTML report: file://{covdir}/index.html')
        cov.erase()  

    if not result.wasSuccessful():
        sys.exit(1)

if __name__ == '__main__':
    app.run(debug=True)