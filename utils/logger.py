import logging
import os

os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    filename='logs/bookkeeper.log',
    filemode='a',
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

logger = logging.getLogger('bookkeeper')
