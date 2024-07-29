lint:
	python3 -m isort . --profile black
	python3 -m black .
	python3 -m pylint ./django_test --load-plugins=pylint_django
	python3 -m pylint ./objects --load-plugins=pylint_django