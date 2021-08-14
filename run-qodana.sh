docker run --rm -it -p 8080:8080 \
  -v /Users/Pavel.Karateev/git/advent_of_code/:/data/project/ \
  -v /Users/Pavel.Karateev/.qodana/advent-of-code/output/:/data/results/ \
  -v /Users/Pavel.Karateev/.qodana/advent-of-code/cache/:/data/cache/ \
  jetbrains/qodana:2021.2-eap \
  --show-report -profileName Default
