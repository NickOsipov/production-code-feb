build-jupyter:
	docker build -t prod-code:jupyter -f Dockerfile.jupyter .

run-jupyter:
	docker run -v ./notebooks:/app/notebooks -p 8888:8888 --name prod-code-jupyter prod-code:jupyter

stop-jupyter:
	docker stop prod-code-jupyter

build:
	docker build -t prod-code:latest -f Dockerfile .

run:
	docker run --rm -p 5000:5000 --name prod-code prod-code:latest

run-dev:
	docker run \
		--rm \
		-d \
		-e MODE_ENV=dev \
		-v ./config:/app/config \
		-v ./logs:/app/logs \
		-v ./data:/app/data \
		-v ./models:/app/models \
		-v ./src:/app/src \
		-p 5000:5000 \
		--name prod-code-dev \
		prod-code:latest
