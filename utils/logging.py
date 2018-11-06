import logging

logger = logging.getLogger('rabbit-cloudwatch')
logger.setLevel(logging.INFO)

fh = logging.FileHandler('rabbit-cloudwatch.log')
sh = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(sh)
