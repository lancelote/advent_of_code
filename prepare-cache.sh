docker run --rm \
  -v /Users/Pavel.Karateev/git/advent_of_code/:/data/project/ \
  -v /Users/Pavel.Karateev/.qodana/advent-of-code/cache/:/data/cache/ \
  --entrypoint=bash \
  jetbrains/qodana:2021.2-eap -c '
python3 -m venv /data/cache/venv
source /data/cache/venv/bin/activate
pip3 install -r /data/project/requirements-dev.txt
'
