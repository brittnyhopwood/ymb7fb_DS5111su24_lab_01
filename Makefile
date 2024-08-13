default:
	@type Makefile

get_texts:
	@for %%i in (2147 2148 2149	45484 1064 10031 32037 1063 932 50852) do ( \
		wget -O book%%i.txt https://www.gutenberg.org/cache/epub/%%i/pg%%i.txt \
	)

get_raven:
	wget -O raven.txt https://www.gutenberg.org/cache/epub/17192/pg17192.txt

raven_line_count:
	powershell -Command "(Get-Content raven.txt | Measure-Object -Line).Lines"

raven_word_count:
	powershell -Command "(Get-Content raven.txt | Measure-Object -Word).Words"

raven_counts:
	powershell -Command "$$content = Get-Content raven.txt; $$countLower = ($$content | Select-String -Pattern '\braven\b').Count; $$countTitle = ($$content | Select-String -Pattern '\bRaven\b').Count; $$countIgnore = ($$content | Select-String -Pattern 'raven' -AllMatches).Matches.Count; Write-Output 'Lowercase ''raven'': ' + $$countLower; Write-Output 'Title case ''Raven'': ' + $$countTitle; Write-Output 'Case-insensitive ''raven'': ' + $$countIgnore"

total_lines:
	powershell -Command "(Get-Content raven.txt | Measure-Object -Line).Lines"

total_words:
	powershell -Command "(Get-Content book*.txt | Measure-Object -Word).Words"

# New targets
setup:
	python3 -m venv env
	. env/bin/activate; pip install --upgrade pip
	. env/bin/activate; pip install -r requirements.txt

test:
	. env/bin/activate; pytest