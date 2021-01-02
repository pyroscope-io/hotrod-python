.PHONY: docker-hotrod
docker-hotrod:
	docker build . -t pyroscope/hotrod-python:dev
