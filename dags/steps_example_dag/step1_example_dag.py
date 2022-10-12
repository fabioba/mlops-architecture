"""
This module includes the logic of the first step

Date: Oct, 2022
Author: Fabio Barbazza
"""
import logging 

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


def run_feat_eng():
    """
        This method is responsible for running feature engineering
    """
    try:


        logger.info('run_feat_eng starting')

    except Exception as err:
        logger.exception(err)
        raise err


def run_feat_enrich():
    """
        This method is responsible for running feature enrichment
    """
    try:


        logger.info('run_feat_enrich starting')

    except Exception as err:
        logger.exception(err)
        raise err



def run_workflow_step1():
    """
        This method is responsible for running the sequence of methods of the step1
    """
    try:

        logger.info('run_workflow_step1 starting')

        run_feat_eng()

        run_feat_enrich()

        logger.info('run_workflow_step1 finish')

    except Exception as err:
        logger.exception(err)
        raise err