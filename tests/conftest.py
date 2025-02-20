"""Conftest provides all shared configurations for testing log anomaly detector."""
import pytest
from anomaly_detector.config import Configuration
import uuid
from enum import Enum
from anomaly_detector.core import DetectorPipeline


class Spec(Enum):
    """Specification for constants used in test cases."""

    CUSTOMER_ID = "#123456"
    LOCAL_FILE = "local"


@pytest.fixture(scope='module')
def cnf_hadoop_2k():
    """Initialize configurations before testing."""
    config = Configuration()
    config.STORAGE_DATASOURCE = "local"
    config.STORAGE_DATASINK = "stdout"
    config.LS_INPUT_PATH = "validation_data/Hadoop_2k.json"
    return config


@pytest.fixture(scope='module')
def cnf_wrong_settings():
    """Initialize configurations before testing."""
    config = Configuration()
    config.STORAGE_DATASOURCE = "local.source"
    config.STORAGE_DATASINK = "local.sink"
    config.LS_INPUT_PATH = "validation_data/orders-500.log"
    config.LS_OUTPUT_PATH = "validation_data/results-oct4.1.txt"
    return config


@pytest.fixture(scope='module')
def cnf_100K_events():
    """Provide default configurations to load yaml instead of env var."""
    config = Configuration()
    config.STORAGE_DATASOURCE = "local"
    config.STORAGE_DATASINK = "stdout"
    config.LS_INPUT_PATH = "validation_data/log_anomaly_detector-100000-events.json"
    return config


@pytest.fixture(scope='module')
def cnf_localdir():
    """Initialize configurations before testing."""
    config = Configuration()
    config.STORAGE_DATASOURCE = "localdir"
    config.STORAGE_DATASINK = "stdout"
    config.LS_INPUT_PATH = "validation_data/test_sample_input"
    return config


@pytest.fixture(scope='module')
def cnf_local_500():
    """Initialize configurations before testing."""
    config = Configuration()
    config.STORAGE_DATASOURCE = "local"
    config.STORAGE_DATASINK = "local"
    config.LS_INPUT_PATH = "validation_data/orders-500.log"
    config.LS_OUTPUT_PATH = "validation_data/results-oct4.1.txt"
    return config


@pytest.fixture(scope='module')
def cnf_hadoop2k_w2v_params(cnf_hadoop_2k):
    """Initialize configurations before testing."""
    cnf_hadoop_2k.W2V_MIN_COUNT = 1
    cnf_hadoop_2k.W2V_ITER = 500
    cnf_hadoop_2k.W2V_COMPUTE_LOSS = "True"
    cnf_hadoop_2k.W2V_SEED = 50
    cnf_hadoop_2k.W2V_WORKERS = 1
    return cnf_hadoop_2k


@pytest.fixture()
def sample_feedback():
    """Provide sample feedback objects for testing factstore."""
    CUSTOMER_ID = "#123456"
    return ({
                'predict_id': str(uuid.uuid4()),
                'message': "222JSJSJJS",
                'anomaly_status': True,
                'customer_id': CUSTOMER_ID
            },
            {
                'predict_id': str(uuid.uuid4()),
                'message': "Testing123",
                'anomaly_status': True,
                'customer_id': CUSTOMER_ID
            },
            {
                'predict_id': str(uuid.uuid4()),
                'message': "PhonyMessage",
                'anomaly_status': False,
                'customer_id': CUSTOMER_ID
            })


@pytest.fixture(scope='function')
def pipeline():
    """Providing pipeline that clears up history of task runs."""
    pipeline = DetectorPipeline()
    yield pipeline
    pipeline.clear()
