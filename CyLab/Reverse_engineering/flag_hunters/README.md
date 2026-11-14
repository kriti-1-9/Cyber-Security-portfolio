# Flag Hunters

## Challenge Overview
The program reads a flag from `flag.txt` and embeds it inside a hidden section (`secret_intro`) of a song-like script.

The execution starts at `[VERSE1]`, so the secret intro is normally never printed.

The program implements a custom interpreter that processes special commands:

- `REFRAIN`
- `RETURN X`
- `END`

User input is accepted during the `CROWD` section.

---

## Vulnerability

Inside the `reader()` function:

```python
elif re.match(r"CROWD.*", line):
    crowd = input('Crowd: ')
    song_lines[lip] = 'Crowd: ' + crowd
    lip += 1
```
The user input is directly inserted into `song_lines` without validation.

Later, each line is split using:
```python
for line in song_lines[lip].split(';'):
```
This means we can inject additional commands using `;`.

## Exploitation
If we provide this as input:
```
;RETURN 0
```
It gets split into:
- (empty)
- RETURN 0
The interpreter processes:
```python
lip = 0
```
This redirects execution to the beginning of the script, where `secret_intro` (containing the flag) is located.

As a result, the flag is printed.

## Payload
```
;RETURN 0
```

## Why This Works
This is a control flow injection vulnerability caused by:
- Unsanitized user input
- Custom DSL interpreter
- Support for `;` command chaining
- Direct instruction pointer manipulation via `RETURN`

## Concepts Learned
- Custom interpreter exploitation
- Control flow manipulation
- Command injection in DSL environments
- Logic vulnerability analysis