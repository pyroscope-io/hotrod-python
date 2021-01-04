.PHONY: docker-login
docker-login:
	aws ecr get-login-password \
    --region us-east-1 \
	| docker login \
    --username AWS \
    --password-stdin 489437247049.dkr.ecr.us-east-1.amazonaws.com

.PHONY: docker
docker: docker-login
	docker build --platform linux/amd64 -t 489437247049.dkr.ecr.us-east-1.amazonaws.com/hotrod-client:dev .
	docker push 489437247049.dkr.ecr.us-east-1.amazonaws.com/hotrod-client:dev

.PHONY: deploy
deploy:
	ssh ec2-user@3.88.237.39 'sh /home/ec2-user/docker-login.sh ; docker-compose down; docker-compose pull; docker-compose up -d'
