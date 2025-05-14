from flask import render_template

def init_app(app):
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        app.logger.error('Server Error: %s', (error))
        return render_template('500.html'), 500

    @app.errorhandler(Exception)
    def handle_exception(error):
        # Pass the error to the template
        app.logger.error('Unhandled Exception: %s', (error))
        return render_template('error_generic.html', error=error), getattr(error, 'code', 500)