#!/usr/bin/env python3

# # stdlib imports
# import pathlib
# import typing as T
#
# # 3rd party imports
# import docker
# from loguru import logger
# import pytest
# import rich.color
#
# # 1st party imports
# from jumpstart.constants import Paths
# from jumpstart.core import Component
#
# if T.TYPE_CHECKING:
#     # 3rd party imports
#     import docker.models.images
#
# # TODO auto-build images?
#
# docker_client = docker.from_env()
# docker_imgs = docker_client.images.list(name="jumpstart")
# component_dirs = [d for d in Paths.INDEX_DIR.iterdir() if d.is_dir() and (d / "metadata.json").is_file()]
#
# # @pytest.mark.parametrize('fixture_name, fixture_value', [('fixture1', 'val1'), ('fixture2', 'val2')])
# # def test_dynamic_fixtures(request, fixture_name, fixture_value):
# #     assert fixture_value == request.getfixturevalue(fixture_name)
# #
#
# #     argnames="filtering_test_case",
# #     argvalues=common_machine_tool_test_cases + filter_machine_tools_only_test_cases,
# #     ids=lambda x: str(x),
# # )
#
#
# @pytest.mark.parametrize("component_dir", component_dirs, ids=lambda d: d.name)
# @pytest.mark.parametrize("docker_img", docker_imgs, ids=lambda img: img.attrs["RepoTags"][0])
# def test_abc(
#     docker_img: docker.models.images.Image,
#     component_dir: pathlib.Path,
# ) -> None:
#     print("OHO")
#
#     # TODO generate to output dir?
#
#     # Mount dir to docker
#
#     # status -> no
#
#     # Upstream version
#
#     # Install , status -> yes
#
#     # local version
#
#     # match?
#
#     # remove, status -> no
#     print(docker_imgs)
#
#
# # >>> client.containers.run("ubuntu:latest", "echo hello world")
#
# # @pytest.fixture(scope="module")
# # def docker_client():
# #     return docker.from_env()
# #
# # @pytest.fixture(scope="module")
# # def docker_imgs(docker_client)->T.List[docker.models.images.Image]:
# #     return docker_client.images.list(name="jumpstart")
# #
# #
# # @pytest.fixture(scope="module")
# # def component_dirs()->T.List[pathlib.Path]:
# #     return [d for d in Paths.INDEX_DIR.iterdir() if d.is_dir() and (d/'metadata.json').is_file()]
