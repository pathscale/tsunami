# BUILD:  docker build -t rapidjson_wrapper-debian .
# RUN:    docker run -it -v "$PWD"/../..:/rapidjson_wrapper rapidjson_wrapper-debian

FROM debian:jessie

RUN apt-get update && apt-get install -y g++ cmake doxygen valgrind

ENTRYPOINT ["/bin/bash"]
