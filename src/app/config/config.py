import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        os.environ.get('LLMTR_CNX_USER', 'postgres'),
        os.environ.get('LLMTR_CNX_PASSWORD', 'postgres'),
        os.environ.get('LLMTR_CNX_HOST', '127.0.0.1'),
        os.environ.get('LLMTR_CNX_PORT', '5432'),
        os.environ.get('LLMTR_CNX_DATABASE', 'LLMTR'),
    )
    DEBUG = os.environ.get('LLMTR_DEBUG', False)
    HOST = os.environ.get('LLMTR_HOST', '0.0.0.0')
    PORT = os.environ.get('LLMTR_PORT', 5000)
    MAX_CONTENT_LENGTH = int(os.environ.get('LLMTR_FILE_MAX_SIZE') or 1024 * 1024 * 1024) # 1GB
    REDIS_CLIENT_ADDRESS = os.environ.get('LLMTR_REDIS_CLIENT_ADDRESS', '127.0.0.1:6379')
    REDIS_CLIENT_USERNAME = os.environ.get('LLMTR_REDIS_USERNAME', '')
    REDIS_CLIENT_PASSWORD = os.environ.get('LLMTR_REDIS_PASSWORD', '')