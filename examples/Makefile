
# ifeq ($(shell uname),Darwin)
# SED_ARGS = -i ''
# else
# SED_ARGS = -i
# endif

.PHONY: generate-protobuf
generate-protobuf:
	rm -rf msgs/python/*
	rm -rf msgs/cpp/*
	mkdir -p msgs/cpp
	mkdir -p msgs/python
	protoc --python_out=pyi_out:msgs/python --cpp_out=msgs/cpp --proto_path=proto proto/*.proto

# protoc --python_out=pyi_out:py --proto_path=proto --cpp_out=cpp proto/*.proto
# --proto_path proto/*.proto
# --mypy_out=gen/proto
# mv foxglove-schemas-protobuf/foxglove_schemas_protobuf/foxglove/* foxglove-schemas-protobuf/foxglove_schemas_protobuf
# rmdir foxglove-schemas-protobuf/foxglove_schemas_protobuf/foxglove
# sed -E $(SED_ARGS) 's/from foxglove import/from . import/g' foxglove-schemas-protobuf/foxglove_schemas_protobuf/*_pb2.py
# sed -E $(SED_ARGS) 's/import foxglove\.(.+)$$/from . import \1 as foxglove_\1/g' foxglove-schemas-protobuf/foxglove_schemas_protobuf/*_pb2.pyi
# sed -E $(SED_ARGS) 's/foxglove\./foxglove_/g' foxglove-schemas-protobuf/foxglove_schemas_protobuf/*_pb2.pyi

# .PHONY: build
# build: pipenv generate-flatbuffer generate-protobuf
#     pipenv run python -m build foxglove-schemas-protobuf

.PHONY: clean
clean:
	rm -rf dist
	rm -rf msgs
	find . -name "build" -type d -exec rm -rf {} +
	find . -name "dist" -type d -exec rm -rf {} +
	find . -name "*.egg-info" -type d -exec rm -rf {} +
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name "*_pb2*" -delete
	find . -name "*.mcap" -delete