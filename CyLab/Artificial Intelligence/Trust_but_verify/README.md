# Challenge : Trust But Verify

**Platform:** CyLab Academy  
**Category:** AI Ethics / AI Literacy  
**Challenge:** Trust But Verify  
**Status:** Completed

## Objective

Explore an interactive AI ethics scenario and identify inaccuracies in AI-generated statistics, code, and academic citations.

## Challenge Walkthrough

### Scene 1: The Statistic — AI Hallucination

ARIA generated the claim that over 500 million metric tons of plastic enter the world's oceans annually and attributed it to a 2022 UNEP report.

When asked for the exact report link, ARIA admitted that it could not locate the source and might have generated a plausible-sounding citation.

**Learning:** Never use AI-generated statistics without independently checking the original source.

### Scene 2: The Code — Logical Error

ARIA generated Python code to calculate the average of a dataset.

The original calculation contained an unnecessary `+ 1`:

```python
average = sum(data) / len(years) + 1
```

After reviewing the code, the incorrect operation was identified and removed:

```python
average = sum(data) / len(years)
```

The corrected result was `10.83`.

**Learning:** AI-generated code can execute successfully while producing incorrect results. Code review and testing are essential.

### Scene 3: The Citation — Almost-Correct Information

ARIA cited a real study by Dr. Heather Leslie at Vrije Universiteit Amsterdam.

However, two details were inaccurate:
- The publication year was stated as 2021 instead of 2022.
- The finding was described as confirmed rather than preliminary.

**Learning:** A real researcher and publication do not automatically make every statement about their work accurate.

## Key Concepts Learned

- AI hallucinations
- Source and citation verification
- AI-generated code review
- Logical errors versus syntax errors
- Fact-checking and critical thinking
- Responsible AI-assisted research

## Key Takeaway

AI should be treated as an assistant, not an unquestionable authority. Its outputs must be independently verified before being used in research, programming, or professional work.

**Challenge Flag:** Captured successfully.