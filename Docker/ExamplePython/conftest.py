## Read more about it https://docker-py.readthedocs.io/en/7.1.0/containers.html
import pytest
import docker
import time

NETWORK = "testing_network"

SPACEFLIGHT_TAG = "test_spaceflights"
SPACEFLIGHTS_INNER_PORT = 8001

POSTGRES_TAG = "postgres:13.14"
POSTGRES_INNER_PORT = 5432

container_list = []


@pytest.fixture(scope="session")
def run_spaceflights():
    """
    Build and run spaceflights docker container
    Cleanup all of them after fixture is used
    """
    client = docker.from_env()
    client.images.build(path=".", dockerfile="Dockerfile",
                        tag=SPACEFLIGHT_TAG, rm=True, nocache=True)

    def _start_container():
        container_ports = {f'{SPACEFLIGHTS_INNER_PORT}/tcp': 8010}
        spaceflights_container = client.containers.run(
            SPACEFLIGHT_TAG, name="spaceflights_test",
            detach=True, ports=container_ports) # maybe add network=NETWORK
        container_list.append(spaceflights_container)

        # Wait for the container to be ready
        time.sleep(5)  # This is a simple wait, adjust if needed
        return spaceflights_container

    yield _start_container

    for container in container_list:
        if container.id == SPACEFLIGHT_TAG:
            try:
                container.kill()
            except Exception as e:
                print(f"Error stopping container {container.id}: {e}")
            try:
                container.remove()
            except Exception as e:
                print(f"Error removing container {container.id}: {e}")


@pytest.fixture(scope="session")
def run_postgres():
    client = docker.from_env()
    # have a way to run init containers for migrations


@pytest.fixture(scope="session")
def run_minio():
    client = docker.from_env()


@pytest.fixture(scope="session")
def run_java_app():
    ...


def teardown():
    for container in container_list:
        try:
            container.kill()
        except Exception as e:
            print(f"Error stopping container {container.id}: {e}")
        try:
            container.remove()
        except Exception as e:
            print(f"Error removing container {container.id}: {e}")












# import os
# from pathlib import Path
# from unittest import mock
#
# import pytest
# from app.main import kedro_service
#
# # from app.main import kedro_service
# from fastapi.testclient import TestClient
# from testcontainers.core.container import DockerContainer
# from testcontainers.postgres import PostgresContainer
#
#
# @pytest.fixture(scope="session")
# def build_spacetype_image():
#     # Define the path and Dockerfile location
#     path_to_directory = str(Path(os.getcwd()).parent)
#     dockerfile_path = (
#         "./tests/spacetypes-test-service/spacetypes-test-service" ".Dockerfile"
#     )
#     image_tag = "my_custom_image:latest"
#     docker_container = DockerContainer(image=image_tag).with_bind_ports(80, 0)
#     # Override the credential store configuration
#     docker_container.get_docker_client().client.api.creds_store = None
#     try:
#         image, _ = docker_container.get_docker_client().client.images.build(
#             path=path_to_directory, dockerfile=dockerfile_path, tag=image_tag, rm=True
#         )
#     except Exception as e:
#         print(f"Error during Docker image build: {e}")
#         raise
#
#
# @pytest.fixture(scope="session")
# def spacetypes_service():
#     # Define the path and Dockerfile location
#     path_to_directory = str(Path(os.getcwd()).parent)
#     dockerfile_path = (
#         "./tests/spacetypes-test-service/spacetypes-test-service." "Dockerfile"
#     )
#     image_tag = "my_custom_image:latest"
#     docker_container = DockerContainer(image=image_tag).with_bind_ports(80, 80)
#     # Override the credential store configuration
#     docker_container.get_docker_client().client.api.creds_store = None
#     try:
#         image, _ = docker_container.get_docker_client().client.images.build(
#             path=path_to_directory, dockerfile=dockerfile_path, tag=image_tag, rm=True
#         )
#     except Exception as e:
#         print(f"Error during Docker image build: {e}")
#         raise
#     with docker_container as spacetypes:
#         spacetypes.start()
#         yield spacetypes
#         spacetypes.stop()
#
#
# # @pytest.fixture(scope='session') #all tests will automatically request them autouse
# # def postgres_container(request):
# #     with PostgresContainer(
# #         image="postgres:13.14",
# #         username="postgres",
# #         password="postgres",
# #         dbname="service"
# #     ) as postgres:
# #         postgres.start()
# #         yield postgres
# #         postgres.stop()
#
#
# postgres = PostgresContainer("postgres:13.14")
#
#
# @pytest.fixture(autouse=True)
# def setup(request, monkeypatch):
#     postgres.start()
#
#     def remove_container():
#         postgres.stop()
#
#     request.addfinalizer(remove_container)
#
#     with mock.patch.dict(os.environ, clear=True):
#         envvars = {
#             "DB_DIALECT": "postgresql",
#             "DB_DRIVER": "psycopg2",
#             "DB_USERNAME": postgres.username,
#             "DB_PASSWORD": postgres.password,
#             "DB_HOST": postgres.get_container_host_ip(),
#             "DB_PORT": postgres.get_exposed_port(5432),
#             "DB_DATABASE": postgres.dbname,
#             "POD_NAMESPACE": None,
#         }
#         postgres.get_connection_url()
#         for k, v in envvars.items():
#             monkeypatch.setenv(k, v)
#         yield
#
#
# @pytest.fixture(scope="module")
# def client():
#     with TestClient(kedro_service) as c:
#         yield c
#
#
# # @pytest.fixture(autouse=True, scope="session")
# # def patch_json_loads(monkeypatch):
# #     def custom_side_effect(arg):
# #         print(arg)
# #         if arg == '{{ cookiecutter.service_metadata.source.maintainers | tojson }}':
# #             return [{"name": "bobo", "email": "bobo@gmail.com"}]
# #         else:
# #             import json
# #             return json.loads(arg)
# #
# #     monkeypatch.setattr("json.loads", custom_side_effect)
# #
#
# # @pytest.fixture(scope='session')
# # def db_engine(postgres_container):
# #     engine = create_engine(
# #         url=postgres_container.get_connection_url(),
# #     )
# #     for _ in range(30):
# #         try:
# #             connection = engine.connect()
# #             connection.close()
# #             break
# #         except Exception as e:
# #             print("Waiting for PostgreSQL to be ready...")
# #             time.sleep(2)
# #     else:
# #         raise Exception("PostgreSQL service not ready in time")
# #
# #
# #
# #     yield engine
#
#
# # @pytest.fixture(scope='session')
# # def get_db(db_engine) -> Generator[Session, Any, None]:
# #     SessionLocal = sessionmaker(bind=db_engine)
# #     db = SessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()
# # @pytest.fixture(scope='function')
# # def client():
# #     with TestClient(kedro_service) as client:
# #         yield client
