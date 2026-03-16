# Coffee Helper


CLI tool for generating reports from student exam preparation data.

## Available Reports

- `median-coffee` — median coffee spending per student.

## Example Usage

Run the script with one or more CSV files:

```bash
    poetry run python -m coffee_helper.main --files ./samples/math.csv ./samples/physics.csv ./samples/programming.csv --report median-coffee
```

## Example Output

```bash
+-------------------+-----------------+
| student           |   median_coffee |
+===================+=================+
| Иван Кузнецов     |             700 |
+-------------------+-----------------+
| Дмитрий Морозов   |             610 |
+-------------------+-----------------+
| Михаил Павлов     |             590 |
...
```

## Architecture

- Reports are implemented as classes inheriting from BaseReport.
- To add a new report:
    1. Create a new class in coffee_helper/reports/.
    2. Register it in REPORTS dictionary.

## Tests

Run `pytest` in the project root.

Coverage can be checked with `pytest --cov=coffee_helper`.
