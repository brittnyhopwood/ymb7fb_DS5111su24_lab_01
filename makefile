default:
	@echo "Available targets: setup, test, integration"

get_texts:
	@for i in 2147 2148 2149 45484 1064 10031 32037 1063 932 50852; do \
		wget -O book$$i.txt https://www.gutenberg.org/cache/epub/$$i/pg$$i.txt; \
	done

get_raven:
	wget -O raven.txt https://www.gutenberg.org/cache/epub/17192/pg17192.txt

raven_line_count:
	wc -l raven.txt

raven_word_count:
	wc -w raven.txt

raven_counts:
	grep -o '\braven\b' raven.txt | wc -l
	grep -o '\bRaven\b' raven.txt | wc -l
	grep -o 'raven' raven.txt | wc -l

total_lines:
	wc -l book*.txt

total_words:
	wc -w book*.txt

setup:
	python3 -m venv env
	. env/bin/activate; pip install --upgrade pip
	. env/bin/activate; pip install -r requirements.txt

test:
	. env/bin/activate; pytest -m "not integration"

integration:
	. env/bin/activate; pytest -m integration

#updated makefile
.PHONY: test
test:
    pytest --ignore=tests/test_integration.py

.PHONY: test-integration
test-integration:
    pytest -m integration
