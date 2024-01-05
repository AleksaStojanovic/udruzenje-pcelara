from flaskr_carved_rock import create_app
from flaskr_carved_rock.models import *
from flaskr_carved_rock.sqla import sqla

app = create_app()
app.app_context().push()