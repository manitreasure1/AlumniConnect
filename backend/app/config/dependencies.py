
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_compress import Compress
from flask_caching import Cache


cache =Cache()
compress = Compress()
cors = CORS()
db = SQLAlchemy()
bcrypt  = Bcrypt()
migrate = Migrate()
jwt_manager = JWTManager()

