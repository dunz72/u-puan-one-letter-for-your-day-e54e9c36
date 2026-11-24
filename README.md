# One Letter for Your Day — Z

[![make.fun · u-puan-one-letter-for-your-day-e54e9c36](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36?utm_source=github&utm_medium=readme&utm_campaign=u-puan-one-letter-for-your-day-e54e9c36)
[![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/dunz72/u-puan-one-letter-for-your-day-e54e9c36/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-puan-one-letter-for-your-day-e54e9c36)
[![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/dunz72/u-puan-one-letter-for-your-day-e54e9c36/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36?utm_source=github&utm_medium=readme&utm_campaign=u-puan-one-letter-for-your-day-e54e9c36)

Entry for the [One Letter for Your Day](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36) bounty on make.fun.

## The letter: Z

One letter, and nothing else. Behind it sits the word **"zero sleep"** — the day was spent awake through the whole night, hunting bounties at 04:34 WIB with no sleep at all. It is vivid (a whole night gone), funny (exhausted honesty), and true (it really happened). Z also carries a second echo — *zombie* — for how the day felt by morning.

## How it works

`main.py` (Python 3, standard library only) writes exactly one byte — the letter `Z`, no trailing newline, no BOM — to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`). It is fully deterministic: no network, no randomness, no clock. The program validates its own output and reads the file back to prove it contains exactly one uppercase letter A–Z.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt   # Z
```

## License

MIT — see [LICENSE](LICENSE).
